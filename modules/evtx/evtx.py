import os
import sys
import shutil
import pathlib
import importlib
from utils.utils import mount_point, load_modules

def run(disk_path, out_path, mnt_pts):
    mount_point(disk_path, mnt_pts)

    evtx_out_path = f"{out_path}/evtx"
    if not os.path.isdir(evtx_out_path):
        os.mkdir(evtx_out_path)

    # evtx_path = f"{mnt_pts}/Windows/System32/winevt/Logs"
    evtx_path = os.path.join(mnt_pts, "Windows", "System32", "winevt", "Logs")

    for evtx_file in os.listdir(evtx_path):
        full_evtx_file = os.path.join(evtx_path, evtx_file)
        if os.path.isfile(full_evtx_file):
            shutil.copy2(full_evtx_file, evtx_out_path)


    try:
        with open("ignored_modules", "r") as read_file:
            ignored_modules = read_file.readlines()
    except:
        ignored_modules = []

    for i in range(0, len(ignored_modules)):
        ignored_modules[i] = ignored_modules[i].rstrip()


    load_modules(current_folder=pathlib.Path(__file__).parent.resolve(), ignored_modules=ignored_modules, disk_path=disk_path, out_path=out_path)
