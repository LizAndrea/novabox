import re

html_file = '/opt/proyectos/ventaProductos/novabox/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the BRANDS section
brands_replacement = """            <div class="flex flex-nowrap justify-start gap-8 md:gap-12 overflow-x-auto scroll-hide pb-6 pt-2 snap-x px-4"
                id="brandChips">

                <button class="brand-chip active flex flex-col items-center gap-3 group snap-start flex-shrink-0 min-w-[100px]"
                    data-brand="all">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat00.webp"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Todo" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 whitespace-nowrap">Todo</span>
                </button>
                <button class="brand-chip flex flex-col items-center gap-3 group snap-start flex-shrink-0 min-w-[100px]"
                    data-brand="Decoración / Regalos">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat00.webp"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Decoración" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 whitespace-nowrap text-center">Decoración / Regalos</span>
                </button>
                <button class="brand-chip flex flex-col items-center gap-3 group snap-start flex-shrink-0 min-w-[100px]"
                    data-brand="Seguridad / Domótica">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat01.avif"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Seguridad" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 whitespace-nowrap text-center">Seguridad / Domótica</span>
                </button>
                <button class="brand-chip flex flex-col items-center gap-3 group snap-start flex-shrink-0 min-w-[100px]"
                    data-brand="Hogar">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat00.webp"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Hogar" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 whitespace-nowrap text-center">Hogar</span>
                </button>
                <button class="brand-chip flex flex-col items-center gap-3 group snap-start flex-shrink-0 min-w-[100px]"
                    data-brand="Audio">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat02.avif"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Audio" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 whitespace-nowrap text-center">Audio</span>
                </button>
                <button class="brand-chip flex flex-col items-center gap-3 group snap-start flex-shrink-0 min-w-[100px]"
                    data-brand="Tecnología">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat00.webp"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Tecnología" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 whitespace-nowrap text-center">Tecnología</span>
                </button>
                <button class="brand-chip flex flex-col items-center gap-3 group snap-start flex-shrink-0 min-w-[100px]"
                    data-brand="Cuidado Personal">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat00.webp"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Cuidado Personal" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 whitespace-nowrap text-center">Cuidado Personal</span>
                </button>
                <button class="brand-chip flex flex-col items-center gap-3 group snap-start flex-shrink-0 min-w-[100px]"
                    data-brand="Iluminación Exterior">
                    <div
                        class="w-20 h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                        <img src="assets/images/pagina/cat00.webp"
                            class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md"
                            alt="Iluminación Exterior" />
                    </div>
                    <span
                        class="text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 whitespace-nowrap text-center">Iluminación Exterior</span>
                </button>
            </div>"""

html = re.sub(r'<div class="flex justify-start gap-8 md:gap-12 overflow-x-auto scroll-hide pb-6 pt-2 snap-x px-4"\s+id="brandChips">.*?(?=<button id="scrollRight")', brands_replacement + '\n\n            ', html, flags=re.DOTALL)

# 2. Fix the catastrophic paste from <!-- HOW IT WORKS -->
# Find the first <!-- HOW IT WORKS --> and delete EVERYTHING after it
idx = html.find('<!-- HOW IT WORKS -->')
if idx != -1:
    html = html[:idx]
    
    # Append the correct bottom half
    bottom_half = """<!-- PROOF BAR -->
    <section id="how" class="bg-[#f5f5f7] relative overflow-hidden border-t border-gray-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 py-20 relative z-10">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Item 1 -->
                <div class="bg-white rounded-3xl p-8 flex flex-col items-center text-center shadow-[0_4px_16px_rgba(0,0,0,0.04)] border border-gray-100 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
                    <div class="text-4xl mb-4">📍</div>
                    <h4 class="font-bold text-[1.15rem] text-black leading-snug tracking-tight">Entregas Presenciales</h4>
                    <p class="text-[0.9rem] font-medium text-gray-600 mt-2 tracking-wide">(Prado / Colón / Cine Center)</p>
                </div>
                <!-- Item 2 -->
                <div class="bg-white rounded-3xl p-8 flex flex-col items-center text-center shadow-[0_4px_16px_rgba(0,0,0,0.04)] border border-gray-100 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
                    <div class="text-4xl mb-4">⚡</div>
                    <h4 class="font-bold text-[1.15rem] text-black leading-snug tracking-tight">Pagos por QR</h4>
                    <p class="text-[0.9rem] font-medium text-gray-600 mt-2 tracking-wide">o Efectivo Contra Entrega</p>
                </div>
                <!-- Item 3 -->
                <div class="bg-white rounded-3xl p-8 flex flex-col items-center text-center shadow-[0_4px_16px_rgba(0,0,0,0.04)] border border-gray-100 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
                    <div class="text-4xl mb-4">🛡️</div>
                    <h4 class="font-bold text-[1.15rem] text-black leading-snug tracking-tight">Productos Probados</h4>
                    <p class="text-[0.9rem] font-medium text-gray-600 mt-2 tracking-wide">y Garantizados</p>
                </div>
                <!-- Item 4 -->
                <div class="bg-white rounded-3xl p-8 flex flex-col items-center text-center shadow-[0_4px_16px_rgba(0,0,0,0.04)] border border-gray-100 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
                    <div class="text-4xl mb-4">💬</div>
                    <h4 class="font-bold text-[1.15rem] text-black leading-snug tracking-tight">Atención Inmediata</h4>
                    <p class="text-[0.9rem] font-medium text-gray-600 mt-2 tracking-wide">por WhatsApp</p>
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="bg-deep-coffee text-ice-grey">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 py-14 grid md:grid-cols-4 gap-10">
            <div>
                <div class="flex items-center gap-2 mb-4">
                    <div>
                        <img src="assets/images/pagina/logo.png" alt="Logo NovaBox"
                            class="h-10 w-auto rounded-md object-contain" />
                    </div>
                    <span class="text-xl font-bold text-white">NovaBox</span>
                </div>
                <p class="text-sm text-mauve-brown/70 mb-5">Equipa tu vida con los mejores gadgets y accesorios tecnológicos.</p>
            </div>
            <div>
                <h4 class="text-white font-semibold mb-3">Marketplace</h4>
                <ul class="space-y-2 text-sm">
                    <li><a href="#" class="hover:text-white">Productos</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-semibold mb-3">Company</h4>
                <ul class="space-y-2 text-sm">
                    <li><a href="#" class="hover:text-white">Sobre Nosotros</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-semibold mb-3">Suporte</h4>
                <ul class="space-y-2 text-sm">
                    <li><a href="#" class="hover:text-white">Contacto</a></li>
                </ul>
            </div>
        </div>
        <div class="border-t border-mauve-brown/30">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 py-6 flex flex-col md:flex-row justify-between items-center text-sm text-mauve-brown">
                <p>© 2026 NovaBox. Todos los derechos reservados.</p>
            </div>
        </div>
    </footer>

    <!-- PHONE DETAIL MODAL -->
    <div id="detailModal" class="fixed inset-0 z-50 hidden modal-bg items-center justify-center p-4">
        <div class="bg-bone-white rounded-[24px] max-w-4xl w-full max-h-[90vh] overflow-y-auto slide-up border border-slate-700 shadow-2xl relative">
            <div class="absolute top-4 right-4 z-50">
                <button id="btnCloseDetail" class="p-2 bg-black/20 hover:bg-black/40 text-white rounded-full backdrop-blur-sm transition">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>
            <div id="detailContent" class="w-full text-white"></div>
        </div>
    </div>

    <!-- TOAST -->
    <div id="toast" class="fixed bottom-6 left-1/2 -translate-x-1/2 bg-deep-coffee text-white px-5 py-3 rounded-xl shadow-lg hidden z-50 text-sm font-medium"></div>

    <script src="js/data.js"></script>
    <script src="js/script.js"></script>
</body>
</html>"""
    html += bottom_half

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
