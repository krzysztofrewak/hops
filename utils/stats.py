import json5
import glob
import os
from collections import Counter

DATA_DIR = "./data"

def load_files():
    files = glob.glob(os.path.join(DATA_DIR, "*.json5"))
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            try:
                yield json5.load(f)
            except Exception as e:
                print(f"[ERROR] Failed to read {file}: {e}")

def count_stats():
    hops = 0
    countries = Counter()
    descriptors = Counter()
    aromas = Counter()

    for data in load_files():
        hops += 1

        if "country" in data:
            countries[data["country"]] += 1

        for d in data.get("descriptors", []):
            descriptors[d] += 1

        for desc in data.get("aromaDescription", []):
            aromas[desc] += 1

    return hops, countries, descriptors, aromas

def print_top(counter, title, limit=30):
    print("\n====", title, "====")
    for item, count in counter.most_common(limit):
        print(f"{item:30} {count}")

def main():
    hops, countries, descriptors, aromas = count_stats()

    print(hops, "Hops")
    print_top(countries, "Countries")
    print_top(descriptors, "Descriptors")
    print_top(aromas, "Aromas")

if __name__ == "__main__":
    main()
