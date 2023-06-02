import os
import pathlib
import subprocess

def run(disk_path, out_path):
    hayabusa_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "hayabusa/hayabusa")
    request = [hayabusa_path, "json-timeline", "-d", f"{out_path}/evtx", "-o", f"{out_path}/hayabusa_timeline.json"]
    p = subprocess.Popen(request)
    p.wait()