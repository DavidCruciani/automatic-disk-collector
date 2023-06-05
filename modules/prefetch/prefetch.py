import os
import shutil
import pathlib
from utils.utils import mount_point, load_modules

def run(disk_path, out_path, mnt_pts):
    mount_point(disk_path, mnt_pts)

    prefetch_out_path = f"{out_path}/prefetch"
    if not os.path.isdir(prefetch_out_path):
        os.mkdir(prefetch_out_path)

    prefetch_path = os.path.join(mnt_pts, "Windows", "Prefetch")

    for prefetch_file in os.listdir(prefetch_path):
        full_prefetch_file = os.path.join(prefetch_path, prefetch_file)
        if os.path.isfile(full_prefetch_file) and prefetch_file.endswith(".pf"):
            shutil.copy2(full_prefetch_file, prefetch_out_path)

    try:
        with open("ignored_modules", "r") as read_file:
            ignored_modules = read_file.readlines()
    except:
        ignored_modules = []

    for i in range(0, len(ignored_modules)):
        ignored_modules[i] = ignored_modules[i].rstrip()


    load_modules(current_folder=pathlib.Path(__file__).parent.resolve(), ignored_modules=ignored_modules, disk_path=disk_path, out_path=out_path)
