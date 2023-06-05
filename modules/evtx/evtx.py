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

    # modules_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "modules")
    # for module in os.listdir(modules_path):
    #     full_module_path = os.path.join(modules_path, module)
    #     if os.path.isdir(full_module_path) and not module in ignored_modules:
    #         print(module)
    #         spec = importlib.util.spec_from_file_location(module, os.path.join(full_module_path, module + ".py"))
    #         foo = importlib.util.module_from_spec(spec)
    #         sys.modules[module] = foo
    #         spec.loader.exec_module(foo)
    #         foo.run(disk_path, out_path)

