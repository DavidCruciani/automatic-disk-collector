import os
import argparse
import importlib.util
import sys
from utils.utils import unmount_disk


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--disk_path", help="Path to the image of the disk", required=True)
parser.add_argument("-o", "--out_path", help="Path to store results", required=True)
args = parser.parse_args()

if not os.path.isdir(args.out_path):
    os.mkdir(args.out_path)


try:
    with open("ignored_modules", "r") as read_file:
        ignored_modules = read_file.readlines()
except:
    ignored_modules = []

for i in range(0, len(ignored_modules)):
    ignored_modules[i] = ignored_modules[i].rstrip()


mnt_pts = os.path.join(os.getcwd(), "mnt_pts")


if os.path.isfile(args.disk_path):
    modules_path = os.path.join(os.getcwd(), "modules")
    for module in os.listdir(modules_path):
        full_module_path = os.path.join(modules_path, module)
        if os.path.isdir(full_module_path) and not module in ignored_modules:
            print(module)
            spec = importlib.util.spec_from_file_location(module, os.path.join(full_module_path, module + ".py"))
            foo = importlib.util.module_from_spec(spec)
            sys.modules[module] = foo
            spec.loader.exec_module(foo)
            try:
                foo.run(args.disk_path, args.out_path, mnt_pts=mnt_pts)
            except:
                continue
else:
    print("[-] Image of the disk not found")

unmount_disk(mnt_pts)