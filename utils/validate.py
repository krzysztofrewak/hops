import json
import json5
import glob
import os
from jsonschema import Draft202012Validator, ValidationError

SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "..", "hops.json")
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def load_schema():
    with open(SCHEMA_PATH, "r") as f:
        return json.load(f)

def validate_file(path, validator):
    try:
        with open(path, "r") as f:
            data = json5.load(f)

        validator.validate(data)
        print(f"[OK] {os.path.basename(path)}")
    except ValidationError as e:
        print(f"[ERROR] {os.path.basename(path)}")
        print("   →", e.message)
    except Exception as e:
        print(f"[FAIL] {os.path.basename(path)}")
        print("   →", str(e))

def main():
    schema = load_schema()
    validator = Draft202012Validator(schema)

    files = glob.glob(os.path.join(DATA_DIR, "*.json5"))
    if not files:
        print("No files in ./data/*.json5")
        return

    for file in files:
        validate_file(file, validator)

if __name__ == "__main__":
    main()
