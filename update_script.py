import csv
import json

csv_path = '/opt/proyectos/ventaProductos/novabox/assets/BD/PlantillaInventario.csv'
json_path = '/opt/proyectos/ventaProductos/novabox/js/categories.json'

categories = set()
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cat = row['Categoría'].strip()
        if cat:
            categories.add(cat)

# Convert to list and sort
cat_list = sorted(list(categories))

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(cat_list, f, ensure_ascii=False, indent=2)

print("categories.json generated successfully!")
