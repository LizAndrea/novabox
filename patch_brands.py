import re

html_file = '/opt/proyectos/ventaProductos/novabox/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

replacement = """            <div class="flex justify-start gap-8 md:gap-12 overflow-x-auto scroll-hide pb-6 pt-2 snap-x px-4"
                id="brandChips">

                <button class="brand-chip active flex flex-col items-center gap-3 group snap-start min-w-[80px]"
                    data-brand="all">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat00.webp"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Todo" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300">Todo</span>
                </button>
                <button class="brand-chip flex flex-col items-center gap-3 group snap-start min-w-[80px]"
                    data-brand="Decoración / Regalos">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat00.webp"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Decoración" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 text-center">Decoración<br/>/ Regalos</span>
                </button>
                <button class="brand-chip flex flex-col items-center gap-3 group snap-start min-w-[80px]"
                    data-brand="Seguridad / Domótica">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat01.avif"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Seguridad" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 text-center">Seguridad<br/>/ Domótica</span>
                </button>
                <button class="brand-chip flex flex-col items-center gap-3 group snap-start min-w-[80px]"
                    data-brand="Hogar">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat00.webp"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Hogar" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 text-center">Hogar</span>
                </button>
                <button class="brand-chip flex flex-col items-center gap-3 group snap-start min-w-[80px]"
                    data-brand="Audio">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat02.avif"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Audio" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 text-center">Audio</span>
                </button>
                <button class="brand-chip flex flex-col items-center gap-3 group snap-start min-w-[80px]"
                    data-brand="Tecnología">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat00.webp"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Tecnología" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 text-center">Tecnología</span>
                </button>
                <button class="brand-chip flex flex-col items-center gap-3 group snap-start min-w-[80px]"
                    data-brand="Cuidado Personal">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat00.webp"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Cuidado Personal" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 text-center">Cuidado<br/>Personal</span>
                </button>
                <button class="brand-chip flex flex-col items-center gap-3 group snap-start min-w-[80px]"
                    data-brand="Iluminación Exterior">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat00.webp"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Iluminación Exterior" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 text-center">Iluminación<br/>Exterior</span>
                </button>
            </div>"""

html = re.sub(r'<div class="flex justify-start gap-8 md:gap-12 overflow-x-auto scroll-hide pb-6 pt-2 snap-x px-4"\s+id="brandChips">.*?</div>', replacement, html, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
