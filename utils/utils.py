import subprocess
import io
import os

def disk_name(disk_path):
    return disk_path.split('/')[-1].split('.')[0]

def get_start_offset(disk_path):
    mmls = subprocess.Popen(["mmls", disk_path], stdout=subprocess.PIPE)
    cut = subprocess.Popen(["cut", "-c43-55"], stdout=subprocess.PIPE, stdin=mmls.stdout)
    output = cut.stdout.read()

    with io.StringIO() as f:
        f.write(output.decode().rstrip())
        f.seek(0)

        max = 0
        cp_max = 0
        cp = 0
        for line in f.readlines():
            try:
                if int(line) > max:
                    max = int(line)
                    cp_max = cp
            except:
                pass
            cp += 1

    mmls = subprocess.Popen(["mmls", disk_path], stdout=subprocess.PIPE)
    cut_start_offset = subprocess.Popen(["cut", "-c17-26"], stdout=subprocess.PIPE, stdin=mmls.stdout)
    output = cut_start_offset.stdout.read()

    with io.StringIO() as f:
        f.write(output.decode().rstrip())
        f.seek(0)

        return int(f.readlines()[cp_max].rstrip())
    
def mount_point(disk_path):
    if not os.path.isdir("mnt_pts"):
        os.mkdir("mnt_pts")
        
    if not os.path.ismount("mnt_pts"):
        start_offset = get_start_offset(disk_path)
        req = f"mount -o loop,ro,noexec,noload,offset=$((512*{start_offset})) {disk_path} mnt_pts"
        subprocess.Popen(req, stdout=subprocess.PIPE, shell=True)