from pathlib import Path
import json
import os
import sys
from dataclasses import dataclass
import xml.etree.ElementTree as ET
import csv

@dataclass
class Config:
    resourcePath: str

@dataclass
class Result:
    locale: str
    key: str

def load_config(path="config.json") -> Config:
    print(f"Loading config file from {path}")
    if not os.path.exists(path):
        print("Config file not found!")
        sys.exit(1)

    try:
        with open(path, "r") as f:
            config = json.loads(f.read())
    except json.JSONDecodeError:
        print("Config file is not valid JSON!")
        sys.exit(1)

    resourcePath = config.get("resourcePath")
    if resourcePath is None:
        print("'resourcePath' is missing in the config file!")
        sys.exit(1)

    if not os.path.exists(resourcePath):
        print(f"{resourcePath} does not exist!")
        sys.exit(1)
    
    return Config(resourcePath)

def extract_keys_from_file(xml_file_path: str):
    print(f"Extracting keys from {xml_file_path}")
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    return {
        elem.attrib["name"]
        for elem in root.findall("string")
        if "name" in elem.attrib
    }

def write_to_csv(path: str, task: str, result: set):
    path_obj = Path(path)
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    with open(str(path), mode="w", newline="", encoding="utf-8") as f:
        print(f"Writing {task} to {path}")
        writer = csv.writer(f)
        writer.writerow([task])
        for key in result:
            writer.writerow([key])


config: Config = load_config()

res_path = Path(config.resourcePath)
origin_path = Path(res_path).joinpath("values", "strings.xml")
xml_paths = list(res_path.rglob("values*/strings.xml"))

base_keys = extract_keys_from_file(str(origin_path))
for locale_path in xml_paths:
    locale_dir = next(part for part in locale_path.parts if part.startswith("values"))
    if locale_dir != "values":
        locale_keys = extract_keys_from_file(str(locale_path))
        missing_keys = base_keys - locale_keys
        extra_keys = locale_keys - base_keys

        write_to_csv(f"output/{locale_dir}_missing_keys.csv", "Missing Keys", missing_keys)
        write_to_csv(f"output/{locale_dir}_extra_keys.csv", "Extra Keys", extra_keys)