import re

with open('/opt/proyectos/ventaProductos/novabox/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add <script src="js/data.js"></script> before <script src="js/script.js"></script>
if 'src="js/data.js"' not in html:
    html = html.replace('<script src="js/script.js"></script>', '<script src="js/data.js"></script>\n    <script src="js/script.js"></script>')

# Update background color of the detail modal just in case
html = html.replace('bg-[#1A332C]', 'bg-bone-white')

with open('/opt/proyectos/ventaProductos/novabox/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
