import os
import subprocess
from utils.utils import mount_point

def run(disk_path, out_path):
    mount_point(disk_path)
