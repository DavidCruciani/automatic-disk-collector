import os
import json
from prefetch_parser import prefetch_parser

def run(disk_path, out_path):
    list_prefetch = dict()
    prefetch_out_path = os.path.join(out_path, "prefetch")
    for prefetch_file in os.listdir(prefetch_out_path):
        full_path_prefetch_file = os.path.join(prefetch_out_path, prefetch_file)
        try:
            list_prefetch[prefetch_file] = prefetch_parser.prefetch2json(full_path_prefetch_file)
        except:
            pass

    with open(f"{out_path}/prefetch_parse.json", "w") as write_json:
        json.dump(list_prefetch, write_json, indent=2)

