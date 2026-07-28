import re

with open('/opt/proyectos/ventaProductos/novabox/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace texts
replacements = {
    "Sabores Biobío — Descubre Sabores Locales": "NovaBox — Electrónica y Tecnología",
    "Sabores Biobío": "NovaBox",
    "SABORES\n                    BIO BIO": "NOVA\n                    BOX",
    "Descubre Sabores": "Descubre el Futuro",
    "100% puros 100% naturales": "Innovación y Diseño",
    "Cocoa intensa": "Tecnología pura",
    "Consumir productos amazónicos ayuda a conservar el bosque.": "Equipa tu vida con los mejores gadgets y accesorios tecnológicos.",
    "El mejor lugar para encontrar productos artesanales, orgánicos y sabor inigualable.": "El mejor lugar para encontrar productos electrónicos de alta calidad y diseño inigualable.",
    "Buscar mermeladas, pan de masa madre, café...": "Buscar parlantes, audífonos, accesorios...",
    "100% Orgánico": "100% Garantizado",
    "Envíos locales": "Envíos a todo el país",
    "Productos verificados": "Productos originales",
    "Ferias Artesanal": "Marcas Globales",
    "Calidad": "Soporte",
    "Oro marron": "Audio y Sonido",
    "mas sabor, menos calorias": "Computación y Periféricos",
    "Frescor amazonico": "Seguridad y Domótica",
    "Aceites alma amazonica": "Decoración y Hogar",
    "Sabores Biobio": "NovaBox",
    "Todo Tipo": "Todos los Estados",
    "Orgánico": "Nuevo",
    "Artesanal": "Destacado",
    "Tradicional": "Oferta",
    "Ferias Artesanales": "Distribuidores",
    "Ayuda a Pedidos": "Soporte Técnico"
}

for old, new in replacements.items():
    html = html.replace(old, new)

# Fix background for nav (make it dark)
html = html.replace("bg-white/90 backdrop-blur-lg border-b border-ice-grey", "bg-bone-white/90 backdrop-blur-lg border-b border-ice-grey")

with open('/opt/proyectos/ventaProductos/novabox/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
