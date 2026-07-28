import re

html_file = '/opt/proyectos/ventaProductos/novabox/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Google Font Inter to head
if 'fonts.googleapis.com' not in html:
    font_link = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">\n    <script'
    html = html.replace('<script', font_link, 1)

# 2. Change font family in body
html = html.replace('class="bg-[#f5f5f7] text-gray-900"', 'class="bg-[#f5f5f7] text-gray-900" style="font-family: \'Inter\', sans-serif;"')

# 3. Replace Listings section
listings_replacement = """    <!-- LISTINGS -->
    <section id="listings" class="max-w-[90rem] mx-auto px-4 sm:px-6 pb-16">
        <div id="listingsContainer" class="flex flex-col gap-16 mt-8"></div>
        <div id="noResults" class="hidden text-center py-16 text-gray-500 font-medium text-lg">
            No se encontraron productos
        </div>
    </section>"""

html = re.sub(r'<!-- LISTINGS -->.*?</section>', listings_replacement, html, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
