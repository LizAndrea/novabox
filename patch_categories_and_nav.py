import re

html_file = '/opt/proyectos/ventaProductos/novabox/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Nav background
html = html.replace('bg-bone-white/90', 'bg-white/90')

categories = [
    ("all", "Todo"),
    ("Audio", "Audio"),
    ("Computación", "Computación"),
    ("Seguridad", "Seguridad"),
    ("Decoración", "Decoración"),
    ("Hogar", "Hogar"),
    ("Fiestas", "Fiestas"),
    ("Tecnología", "Tecnología"),
    ("Bebés", "Bebés"),
    ("Cuidado Personal", "Cuidado"),
    ("Iluminación", "Iluminación"),
    ("Electrónica", "Electrónica"),
    ("Electrohogar", "Electrohogar")
]

buttons_html = ""
for i, (cat_val, cat_label) in enumerate(categories):
    active_class = "active " if i == 0 else ""
    buttons_html += f"""
                <button class="brand-chip {active_class}flex flex-col items-center gap-3 group snap-start min-w-[80px]" data-brand="{cat_val}">
                    <div class="w-16 h-16 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat00.webp" class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md" alt="{cat_label}" />
                    </div>
                    <span class="text-sm font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300">{cat_label}</span>
                </button>"""

brands_section = f"""    <!-- BRANDS -->
    <section id="brands" class="bg-white py-14 text-center">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 relative group/slider">
            <h2 class="text-3xl md:text-[2.5rem] font-bold text-gray-900 mb-10 tracking-tight">
                Nosotros lo categorizamos - Tú eliges
            </h2>
            
            <button id="scrollLeft" class="absolute left-0 top-1/2 translate-y-4 bg-white/90 p-3 rounded-full shadow-md z-10 opacity-0 group-hover/slider:opacity-100 transition hover:scale-110 border border-gray-100 text-gray-600">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
            </button>
            
            <div class="flex justify-start gap-8 md:gap-12 overflow-x-auto scroll-hide pb-6 pt-2 snap-x px-4" id="brandChips">
{buttons_html}
            </div>
            
            <button id="scrollRight" class="absolute right-0 top-1/2 translate-y-4 bg-white/90 p-3 rounded-full shadow-md z-10 opacity-0 group-hover/slider:opacity-100 transition hover:scale-110 border border-gray-100 text-gray-600">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </button>
        </div>
    </section>"""

# Replace the old brands section
new_html = re.sub(r'<!-- BRANDS -->.*?</section>', brands_section, html, flags=re.DOTALL)
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_html)
