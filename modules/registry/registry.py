import os
import shutil
from utils.utils import mount_point, unmount_disk

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
            try:
                registry_out_path_user = os.path.join(registry_out_path, user)
                if not os.path.isdir(registry_out_path_user):
                    os.mkdir(registry_out_path_user)
                shutil.copy2(f"{loc_user_path}/NTUSER.DAT", registry_out_path_user)
            except:
                continue

