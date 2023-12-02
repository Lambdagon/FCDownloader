import os
from tkinter import messagebox
import traceback
import downloads
import setup
from gettext import gettext as _
import vars

# Button functions
def install():
    try:
        #sanity_check()
        setup.setup_binaries()
        setup.setup_path(False)
        endpath = vars.INSTALL_PATH + '/fc'
        # After this line, we have two possible paths: installing, or updating/repairing
        if os.path.exists(vars.INSTALL_PATH + '/fc/gameinfo.txt'):
            messagebox.showwarning("FCDownloader", "The mod is already present in your computer.\nTo update, press the 'Update' button.")
        else:
            downloads.clone(endpath)
    except Exception as ex:
        if ex is not SystemExit:
            traceback.print_exc()
            messagebox.showerror("FCDownloader Exception Error", "An exception error has occured.\nNormally the full traceback call will appear mainly on the console.\nSwitch to the debug app (fcdownloader_debug.exe) to see the exception error.")

def update():
    try:
        #sanity_check()
        setup.setup_binaries()
        setup.setup_path(False)
        endpath = vars.INSTALL_PATH + '/fc'
        # After this line, we have two possible paths: installing, or updating/repairing
        if os.path.exists(vars.INSTALL_PATH + '/fc/gameinfo.txt'):
            downloads.pull(endpath)
        else:
            messagebox.showwarning("FCDownloader", "The mod isn't installed. To install, press the 'Install' button.")
    except Exception as ex:
        if ex is not SystemExit:
            traceback.print_exc()
            messagebox.showerror("FCDownloader Exception Error", "An exception error has occured.\nNormally the full traceback call will appear mainly on the console.\nSwitch to the debug app (fcdownloader_debug.exe) to see the exception error.")

"""
def exceptiontest():
    try:
        print(adasd)
        assert(dsauj)
    except Exception as ex:
        messagebox.showerror(_(title="FCDownloader Exception Error", message="An exception error has occured:\n%s") % traceback.print_exc)
"""