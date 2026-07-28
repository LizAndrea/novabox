import os
import re

base_path = '/opt/proyectos/ventaProductos/novabox/assets/images/productos/oficial'
data_file = '/opt/proyectos/ventaProductos/novabox/js/data.js'

folders = os.listdir(base_path)
folders.sort()

# Map folder ID to the first image found in the folder
id_to_image = {}
for f in folders:
    folder_path = os.path.join(base_path, f)
    if os.path.isdir(folder_path):
        m = re.match(r'^(\d+)', f)
        if m:
            pid = str(int(m.group(1))) # e.g. "01" -> "1"
            images = [img for img in os.listdir(folder_path) if img.endswith(('.jpg', '.png', '.jpeg', '.webp'))]
            if images:
                images.sort()
                rel_path = f"assets/images/productos/oficial/{f}/{images[0]}"
                id_to_image[pid] = rel_path

print(f"Found images for IDs: {id_to_image.keys()}")

# Read data.js and update it
with open(data_file, 'r', encoding='utf-8') as file:
    content = file.read()

# Replace image paths in JS
for pid, img_path in id_to_image.items():
    # Looking for:
    # "id": "PID",
    # ...
    # "image": "..."
    # We can use regex to replace it
    pattern = r'("id":\s*"' + pid + r'".*?"image":\s*")[^"]*(")'
    content = re.sub(pattern, r'\g<1>' + img_path + r'\g<2>', content, flags=re.DOTALL)

with open(data_file, 'w', encoding='utf-8') as file:
    file.write(content)

print("Updated data.js")
