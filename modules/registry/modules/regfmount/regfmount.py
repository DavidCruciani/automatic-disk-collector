import os
import shutil
import pathlib
import subprocess


def run(disk_path, out_path):
    current_folder = pathlib.Path(__file__).parent.resolve()
    mnt_reg = os.path.join(current_folder, "mnt_reg")
    if not os.path.isdir(mnt_reg):
        os.mkdir(mnt_reg)

    
    ##########
    # System #
    ##########
    request = ["regfmount", f"{out_path}/registry/SYSTEM", mnt_reg]
    p = subprocess.Popen(request)
    p.wait()

    computer_name = os.path.join(mnt_reg, "ControlSet001", "Control", "ComputerName", "ComputerName", "(values)", "ComputerName")
    language = os.path.join(mnt_reg, "ControlSet001", "Control", "Nls", "Language", "(values)", "InstallLanguageFallback")
    if os.path.isfile(computer_name):
        try:
            shutil.copy2(computer_name, f"{out_path}/registry")
            shutil.copy2(language, f"{out_path}/registry")
        except:
            pass

    request = ["umount", mnt_reg]
    p = subprocess.Popen(request)
    p.wait()



    ############
    # Software #
    ############
    request = ["regfmount", f"{out_path}/registry/SOFTWARE", mnt_reg]
    p = subprocess.Popen(request)
    p.wait()

    product_name = os.path.join(mnt_reg, "Microsoft", "Windows NT", "CurrentVersion", "(values)", "ProductName")
    build_lab_ex = os.path.join(mnt_reg, "Microsoft", "Windows NT", "CurrentVersion", "(values)", "BuildLabEx")
    if os.path.isfile(product_name):
        try:
            shutil.copy2(product_name, f"{out_path}/registry")
            shutil.copy2(build_lab_ex, f"{out_path}/registry")
        except:
            pass

    request = ["umount", mnt_reg]
    p = subprocess.Popen(request)
    p.wait()