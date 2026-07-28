import re

html_file = '/opt/proyectos/ventaProductos/novabox/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

replacement = """    <!-- PROOF BAR -->
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
    </section>"""

# Using regex to find from <!-- HOW IT WORKS --> or <!-- PROOF BAR --> to its closing </section>
# First let's check what's there
html = re.sub(r'<!-- (HOW IT WORKS|PROOF BAR) -->.*?</section>', replacement, html, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
