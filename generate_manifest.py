import os
import yaml

ICON_DIR = "icons"
OUTPUT_FILE = "metadata/manifest.yaml"

manifest = {}

for brand in os.listdir(ICON_DIR):
    brand_path = os.path.join(ICON_DIR, brand)
    if not os.path.isdir(brand_path):
        continue

    manifest[brand] = {}

    for flavor in os.listdir(brand_path):
        flavor_path = os.path.join(brand_path, flavor)
        if not os.path.isdir(flavor_path):
            continue

        icons = []
        for file in os.listdir(flavor_path):
            if file.endswith(".svg"):
                icon_name = os.path.splitext(file)[0]
                icons.append({"name": icon_name})

        if icons:
            manifest[brand][flavor] = icons

# Make sure metadata folder exists
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

with open(OUTPUT_FILE, "w") as f:
    yaml.dump(manifest, f, sort_keys=False)

print(f"✅ manifest.yaml generated at {OUTPUT_FILE}")
