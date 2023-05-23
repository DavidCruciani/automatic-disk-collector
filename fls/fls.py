import subprocess
import io
from utils.utils import disk_name, get_start_offset

def run(disk_path, out_path):
    start_offset = get_start_offset(disk_path)

    # List all files
    fls = subprocess.Popen(["fls", "-r", "-p", "-o", str(start_offset), disk_path], stdout=subprocess.PIPE)
    with open(f"{out_path}/{disk_name(disk_path)}.fls", "w") as write_file:
        write_file.write(fls.stdout.read().decode())

    # Bodyfile for mactime
    bodyfile = subprocess.Popen(["fls", "-r", "-p", "-m", "/", "-o", str(start_offset), disk_path], stdout=subprocess.PIPE)
    with open(f"{out_path}/bodyfile.txt", "w") as write_file:
        write_file.write(bodyfile.stdout.read().decode())