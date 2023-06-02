import subprocess
from utils.utils import disk_name

def run(disk_path, out_path, mnt_pts):
    mactime = subprocess.Popen(["mactime", "-b", f"{out_path}/bodyfile.txt"], stdout=subprocess.PIPE)

    with open(f"{out_path}/{disk_name(disk_path)}.mactime", "w") as write_file:
        write_file.write(mactime.stdout.read().decode())