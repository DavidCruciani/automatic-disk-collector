import os
import argparse
import configparser


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


if os.path.isfile(args.disk_path):
    for module in os.listdir(os.getcwd()):
        if os.path.isdir(module) and not module in ignored_modules:
            print(module)
            test_mod = __import__(module)
            test_mod.run(args.disk_path, args.out_path)
else:
    print("[-] Image of the disk not found")

