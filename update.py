import json
import csv
import re

def main():
    with open('./js/data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'const PRODUCTS = (\[.*?\]);', content, re.DOTALL)
    if not match:
        print("Could not find PRODUCTS array")
        return
    
    products_json = match.group(1)
    
    # Try parsing
    try:
        products = json.loads(products_json)
    except Exception as e:
        print("Error parsing JSON:", e)
        return

    # Create map
    prod_map = {p['id']: p for p in products}

    # Read CSV
    with open('./assets/BD/catalogoActualizado.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pid = str(row.get('ID', '')).strip()
            if not pid:
                continue
            
            # Extract fields
            name = row.get('Nombre del Producto', '').strip()
            price_str = row.get('Precio Oficial', '').strip()
            min_price_str = row.get('Precio mínimo', '').strip()
            cat = row.get('Categoría', '').strip()
            brand = row.get('Modelo / Marca', '').strip()
            color = row.get('Color', '').strip()
            carac = row.get('Características', '').strip()
            desc = row.get('Detalle extendido', '').strip()

            price = int(price_str) if price_str.isdigit() else 0
            min_price = int(min_price_str) if min_price_str.isdigit() else 0

            # Formatting desc nicely
            # Let's replace actual newlines with \n for JSON
            desc = desc.replace('\r\n', '\n').replace('\r', '\n')

            if pid in prod_map:
                prod = prod_map[pid]
                # Update basic info from CSV just in case
                prod['name'] = name
                if price: prod['price'] = price
                if min_price: prod['min_price'] = min_price
                if cat: prod['category'] = cat
                if brand: prod['brand'] = brand
                if color: prod['color'] = color
                
                # Update features/desc
                if carac: prod['features'] = carac
                if desc: prod['description'] = desc
            else:
                # New product
                prod = {
                    "id": pid,
                    "name": name,
                    "price": price,
                    "min_price": min_price,
                    "category": cat,
                    "brand": brand,
                    "color": color,
                    "features": carac,
                    "power": "N/A",
                    "instructions": "N/A",
                    "warnings": "N/A",
                    "fun_fact": "N/A",
                    "image": f"assets/images/productos/oficial/ataud01/{pid}.jpg",
                    "estado": "",
                    "description": desc
                }
                products.append(prod)
    
    # Write back
    new_json = json.dumps(products, indent=2, ensure_ascii=False)
    new_content = content[:match.start()] + f"const PRODUCTS = {new_json};\n"
    
    with open('./js/data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated data.js. Total products: {len(products)}")

if __name__ == '__main__':
    main()
