import csv
import json
import os
import re

csv_path = '/opt/proyectos/ventaProductos/novabox/assets/BD/PlantillaInventario .csv'
images_dir = '/opt/proyectos/ventaProductos/novabox/assets/images/productos/oficial'
output_path = '/opt/proyectos/ventaProductos/novabox/js/data.js'
categories_path = '/opt/proyectos/ventaProductos/novabox/js/categories.json'

products = []
categories = set()

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        product_id = row['ID'].strip()
        
        # Find folder starting with "ID -" or "ID " or "0ID"
        folder_match = None
        if os.path.exists(images_dir):
            for folder in os.listdir(images_dir):
                if folder.startswith(product_id + " -") or folder.startswith(product_id.zfill(2) + " -"):
                    folder_match = folder
                    break
                    
        image_path = ""
        if folder_match:
            folder_full = os.path.join(images_dir, folder_match)
            if os.path.isdir(folder_full):
                # find first image
                for file in sorted(os.listdir(folder_full)):
                    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.avif')):
                        image_path = f"assets/images/productos/oficial/{folder_match}/{file}"
                        break
        
        products.append({
            "id": product_id,
            "name": row['Nombre del Producto'].strip(),
            "price": float(row['Precio Publicación (Bs.)'].strip()) if row['Precio Publicación (Bs.)'].strip() else 0,
            "min_price": float(row['Precio Mínimo (Bs.)'].strip()) if row['Precio Mínimo (Bs.)'].strip() else 0,
            "category": row['Categoría'].strip(),
            "brand": row['Modelo'].strip(),
            "color": row['Color'].strip(),
            "features": row['Características'].strip(),
            "power": row['Fuente de Energía'].strip(),
            "instructions": row['Instrucciones de Uso'].strip(),
            "warnings": row['Cuidados y Advertencias'].strip(),
            "fun_fact": row['Datos Curiosos'].strip(),
            "image": image_path
        })
        
        if row['Categoría'].strip():
            categories.add(row['Categoría'].strip())

js_content = f"const PRODUCTS = {json.dumps(products, indent=2, ensure_ascii=False)};\n"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

cat_list = sorted(list(categories))

color_map = {
    "Audio": "#3b82f6",
    "Cuidado Personal": "#ec4899",
    "Decoración / Regalos": "#f59e0b",
    "Hogar": "#10b981",
    "Seguridad / Domótica": "#6366f1",
    "Tecnología": "#8b5cf6",
}
fallback_colors = ["#ef4444", "#14b8a6", "#f97316", "#84cc16", "#06b6d4"]
fallback_idx = 0

cat_obj_list = []
for i, name in enumerate(cat_list):
    if name in color_map:
        color = color_map[name]
    else:
        color = fallback_colors[fallback_idx % len(fallback_colors)]
        fallback_idx += 1
        
    cat_obj_list.append({
        "id": f"CAT-{str(i+1).zfill(3)}",
        "name": name,
        "color": color
    })

with open(categories_path, 'w', encoding='utf-8') as f:
    json.dump(cat_obj_list, f, ensure_ascii=False, indent=2)

print("data.js and categories.json generated successfully!")
