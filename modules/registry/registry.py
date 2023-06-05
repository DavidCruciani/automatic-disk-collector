import os
import shutil
import pathlib
from utils.utils import mount_point, load_modules

def run(disk_path, out_path, mnt_pts):
    mount_point(disk_path, mnt_pts)

    registry_out_path = f"{out_path}/registry"
    if not os.path.isdir(registry_out_path):
        os.mkdir(registry_out_path)

    # registry_path = "mnt_pts/Windows/System32/config"
    registry_path = os.path.join(mnt_pts, "Windows", "System32", "config")


    shutil.copy2(f"{registry_path}/SAM", registry_out_path)
    shutil.copy2(f"{registry_path}/SYSTEM", registry_out_path)
    shutil.copy2(f"{registry_path}/SOFTWARE", registry_out_path)
    shutil.copy2(f"{registry_path}/SECURITY", registry_out_path)
    shutil.copy2(f"{registry_path}/DEFAULT", registry_out_path)

    # user_path = "mnt_pts/Users"
    user_path = os.path.join(mnt_pts, "Users")
    for user in os.listdir(user_path):
        loc_user_path = os.path.join(user_path, user)
        if os.path.isdir(loc_user_path):
            if os.path.isfile(f"{loc_user_path}/NTUSER.DAT"):
                try:
                    registry_out_path_user = os.path.join(registry_out_path, user)
                    if not os.path.isdir(registry_out_path_user):
                        os.mkdir(registry_out_path_user)
                    shutil.copy2(f"{loc_user_path}/NTUSER.DAT", registry_out_path_user)
                except Exception as e:
                    continue

    try:
        with open("ignored_modules", "r") as read_file:
            ignored_modules = read_file.readlines()
    except:
        ignored_modules = []

    for i in range(0, len(ignored_modules)):
        ignored_modules[i] = ignored_modules[i].rstrip()

    load_modules(current_folder=pathlib.Path(__file__).parent.resolve(), ignored_modules=ignored_modules, disk_path=disk_path, out_path=out_path)