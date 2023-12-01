import os
from tkinter import messagebox
import downloads
import setup
import vars

# Button functions
def install(endpath):
    #sanity_check()
    setup.setup_binaries()
    setup.setup_path(False)
    endpath = vars.INSTALL_PATH + '/fc'
    # After this line, we have two possible paths: installing, or updating/repairing
    if os.path.exists(vars.INSTALL_PATH + '/fc/gameinfo.txt'):
        messagebox.OK("The mod is already present in your computer. To update, press the 'Update' button.", "FCDownloader")
    else:
        downloads.clone(endpath)
        

def update(endpath):
    #sanity_check()
    setup.setup_binaries()
    setup.setup_path(False)
    endpath = vars.INSTALL_PATH + '/fc'
    # After this line, we have two possible paths: installing, or updating/repairing
    if os.path.exists(vars.INSTALL_PATH + '/fc/gameinfo.txt'):
        downloads.pull(endpath)
    else:
        messagebox.OK("The mod isn't installed. To install, press the 'Install' button.")