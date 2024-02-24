import json
import os

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
json_file_path = os.path.join(desktop_path, 'sample-data.json')

with open(json_file_path, 'r') as file:
    data = json.load(file)
if "imdata" in data:
    imdata = data["imdata"]
    for item in imdata:
        if "l1PhysIf" in item:
            l1_phys_if = item["l1PhysIf"]
            if "attributes" in l1_phys_if:
                attributes = l1_phys_if["attributes"]
                if "dn" in attributes:
                    print(attributes["dn"])
                    print(attributes["speed"])
                    print(attributes["mtu"])


            