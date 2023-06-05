import subprocess
import io
import os
import sys
import importlib

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
    
def mount_point(disk_path, mnt_pts):
    if not os.path.isdir(mnt_pts):
        os.mkdir(mnt_pts)
        
    if not os.path.ismount(mnt_pts):
        start_offset = get_start_offset(disk_path)
        req = f"mount -o loop,ro,noexec,noload,offset=$((512*{start_offset})) {disk_path} {mnt_pts}"
        p = subprocess.Popen(req, stdout=subprocess.PIPE, shell=True)
        p.wait()

def unmount_disk(mnt_pts):
    if os.path.ismount(mnt_pts):
        req = ["umount", mnt_pts]
        p = subprocess.Popen(req, stdout=subprocess.PIPE)
        p.wait()

def load_modules(current_folder, ignored_modules, disk_path, out_path):
    modules_path = os.path.join(current_folder, "modules")
    for module in os.listdir(modules_path):
        full_module_path = os.path.join(modules_path, module)
        if os.path.isdir(full_module_path) and not module in ignored_modules:
            print(module)
            spec = importlib.util.spec_from_file_location(module, os.path.join(full_module_path, module + ".py"))
            foo = importlib.util.module_from_spec(spec)
            sys.modules[module] = foo
            spec.loader.exec_module(foo)
            foo.run(disk_path, out_path)