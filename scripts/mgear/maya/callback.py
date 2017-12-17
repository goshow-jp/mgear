# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
# =============================================================================
import functools
import traceback
from collections import OrderedDict

from maya.api import OpenMaya
from maya import cmds

if False:
    # For type annotation
    from typing import Dict, List, Tuple, Pattern, Callable, Any, Text  # NOQA

# =============================================================================


__CALLBACK_ENTRIES__ = OrderedDict()  # type: Dict[Text, Dict[Text, Any]]
# __CALLBACK_ENTRIES__ = OrderedDict([
#     ("auto_set_project", {
#            "prefkey": "EnableAutoSetProject",
#            "default": 1,
#            "annotation": "auto set project when"
#     }),
# ])


# =============================================================================
def getEntries():
    # type: () -> Dict[Text, Dict[Text, Any]]
    global __CALLBACK_ENTRIES__
    return __CALLBACK_ENTRIES__


def getEntry(key):
    # type: (Text) -> Dict[Text, Any]
    global __CALLBACK_ENTRIES__
    return __CALLBACK_ENTRIES__.get(key)


def getEntryForFunc(func):
    # type: (Callable) -> Dict[Text, Any]
    global __CALLBACK_ENTRIES__
    return __CALLBACK_ENTRIES__.get(getKeyName(func))


def getKeys():
    # type: () -> List[Text]
    global __CALLBACK_ENTRIES__
    return list(__CALLBACK_ENTRIES__.keys())


def getKeyName(func):
    # type: (Callable) -> Text
    key = "{}_{}_{}".format(func.__module__, func.__name__, id(func))
    key = key.replace(".", "_")
    key = key.replace("-", "_")
    return key


def add(register_func, when, cb_func, default=True, prefkey=None, label=None):
    # type: (Callable, int, Callable, bool, Text, Text) -> int
    """Add callback.

    see [OpenMaya.MSceneMessage Class Reference](http://help.autodesk.com/view/MAYAUL/2017/ENU//?guid=__py_ref_class_open_maya_1_1_m_scene_message_html)
    for more detail.

    Args:
        register_func:  may [
            addCallback
            addCheckCallback
            addCheckFileCallback
            addCheckReferenceCallback
            addConnectionFailedCallback
            addReferenceCallback
            addStringArrayCallback
        ]
        when: may [
            kAfterCreateReference = 45
            kAfterExport = 11
            kAfterFileRead = 8
            kAfterImport = 4
            ...
            <snip>
        ]
        cb_func: The callback for invoked.
        default: Default value of callback enable.
        prefkey: The key name of entry in userPrefs.
        label: The label to display in the maya menu.

    Returns:
        int: Identifier used for removing the callback.

    Example:
        >>> import maya.api.OpenMaya as om
        >>> cb_func = lambda client_data: print("callback fired")
        >>> isinstance(add(om.MSceneMessage.addCallback, om.MSceneMessage.kBeforeNew, cb_func), int)
        True

    """
    # from . import menu
    from ctypes import pythonapi, py_object, c_void_p
    global __CALLBACK_ENTRIES__

    # decorate callback function with `executeIfOptionEnable`
    cb_id = register_func(when,  cb_func)

    if "PyCObject" in str(type(cb_id)):
        # Get the actual data (This is beyond my knowledge but it works!)
        pythonapi.PyCObject_AsVoidPtr.restype = c_void_p
        pythonapi.PyCObject_AsVoidPtr.argtypes = [py_object]
        cb_id = pythonapi.PyCObject_AsVoidPtr(cb_id)

    keyname = getKeyName(cb_func)
    print("add: " + keyname)

    if not prefkey:
        prefkey = "CBMAN_{}".format(keyname)

    __CALLBACK_ENTRIES__[keyname] = {
        "prefkey": prefkey,
        "id": cb_id,
        # "cb": cb_id_wrapper,
        "default": 1 if default else 0,
        "label": label or keyname
    }
    setDefault(cb_func)

    # menu.reconstruct_menu()

    return cb_id


def remove(func):
    # type: (Callable) -> None
    """Remove the callback."""

    key = getKeyName(func)
    print("key: " + key)
    print(__CALLBACK_ENTRIES__.keys())
    __CALLBACK_ENTRIES__.pop(key)


# =============================================================================
def isEnable(key):
    # type: (Text) -> bool
    global __CALLBACK_ENTRIES__

    if key not in getKeys():
        print("!!! ERROR: {} is not defined in callback __CALLBACK_ENTRIES__. !!!!".format(key))
        return False

    option_key_name = getEntry(key).get("prefkey")
    return cmds.optionVar(q=option_key_name)


def getDefault(func):
    # type: (Callable) -> Tuple[Text, Text]

    key = getEntryForFunc(func).get("prefkey")
    val = getEntryForFunc(func).get("default")

    return key, val


def setDefault(func):
    # type: (Callable) -> None
    # TODO: skip if environment variable "ENABLE_SET_DEFAULT_OPTION_VAR or somekinda" is not set.
    global __CALLBACK_ENTRIES__

    try:
        key, val = getDefault(func)
        cmds.optionVar(intValue=(key, val))

    except AttributeError:
        print("!!!! ERROR: __CALLBACK_ENTRIES__ entry is not found for {}. !!!!".format(func.__name__))


def executeIfOptionEnable(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        global __CALLBACK_ENTRIES__

        try:
            if isEnable(getKeyName(f)):
                return f(*args, **kwargs)

            else:
                try:
                    key = getEntryForFunc(f).get("prefkey")
                    print("optionVar {} is set False, {} skipped.".format(key, f.__name__))

                except AttributeError:
                    print("__CALLBACK_ENTRIES__ entry is not found for {}.".format(f.__name__))

        except Exception:
            traceback.print_exc()

    return decorated


class MCallbackIdWrapper(object):
    '''Wrapper class to handle cleaning up of MCallbackIds.

    from registered MMessage.

    '''

    def __init__(self, callbackId):
        # super(MCallbackIdWrapper, self).__init__()
        self.callbackId = callbackId

    def __del__(self):
        print("MCallbackIdWrapper.__del__")
        OpenMaya.MMessage.removeCallback(self.callbackId)

    def __repr__(self):
        return "MCallbackIdWrapper(%r)" % self.callbackId
