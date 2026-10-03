import json
import re
import os

def main():
    img_dir = './assets/images/productos'
    files = os.listdir(img_dir)
    
    img_map = {}
    for f in files:
        if f.startswith('NOV-'):
            # e.g., NOV-001.jpg -> 1
            name, ext = os.path.splitext(f)
            num_str = name.split('-')[1]
            try:
                num = int(num_str)
                img_map[num] = f"assets/images/productos/{f}"
            except ValueError:
                pass

    with open('./js/data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'const PRODUCTS = (\[.*?\]);', content, re.DOTALL)
    if not match:
        print("Could not find PRODUCTS array")
        return
    
    products_json = match.group(1)
    
    try:
        products = json.loads(products_json)
    except Exception as e:
        print("Error parsing JSON:", e)
        return

    missing_ids = []
    
    for p in products:
        pid = int(p['id'])
        if pid in img_map:
            p['image'] = img_map[pid]
        else:
            p['image'] = f"assets/images/productos/NOV-{pid:03d}.jpg"
            missing_ids.append(pid)
            
    new_json = json.dumps(products, indent=2, ensure_ascii=False)
    new_content = content[:match.start()] + f"const PRODUCTS = {new_json};\n"
    
    with open('./js/data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    if missing_ids:
        print("FALTAN_IMAGENES=" + ",".join(map(str, missing_ids)))
    else:
        print("NO_FALTAN_IMAGENES")

if __name__ == '__main__':
    main()
