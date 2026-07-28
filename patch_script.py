import re

js_file = '/opt/proyectos/ventaProductos/novabox/js/script.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace renderPhones function
new_render_phones = """function renderPhones() {
  const container = document.getElementById('listingsContainer');
  const noRes = document.getElementById('noResults');
  
  // 1. Filter products based on activeBrand
  let filtered = PRODUCTS.filter(p => {
    if (activeBrand !== 'all') {
      if (!p.category || !p.category.includes(activeBrand)) return false;
    }
    if (searchQuery) {
      const q = searchQuery.toLowerCase();
      if (!p.name.toLowerCase().includes(q) && !p.brand.toLowerCase().includes(q)) return false;
    }
    return true;
  });

  if (filtered.length === 0) { 
    container.innerHTML = ''; 
    noRes.classList.remove('hidden'); 
    return; 
  }
  noRes.classList.add('hidden');

  // 2. Group by category
  const grouped = {};
  filtered.forEach(p => {
    const cat = p.category || 'Varios';
    if (!grouped[cat]) grouped[cat] = [];
    grouped[cat].push(p);
  });

  // 3. Render HTML
  let html = '';
  Object.keys(grouped).forEach((cat, index) => {
    const products = grouped[cat];
    const catId = `carousel-${index}`;
    
    let cardsHtml = products.map(p => {
      const defaultImg = "https://via.placeholder.com/300x400?text=No+Image";
      const imgUrl = p.image ? p.image : defaultImg;
      return `
      <div data-action="view" data-id="${p.id}" class="snap-start flex-shrink-0 cursor-pointer rounded-3xl shadow-[0_2px_12px_rgba(0,0,0,0.04)] hover:shadow-xl bg-white p-6 flex flex-col w-[280px] h-[360px] group transition-all duration-300">
        <!-- Image Container -->
        <div class="w-full h-[65%] flex items-center justify-center mb-4 overflow-hidden bg-white rounded-2xl relative">
          <img src="${imgUrl}" class="max-w-full max-h-full object-contain transition-transform duration-500 group-hover:scale-[1.03]" alt="${p.name}" />
        </div>

        <!-- Content Area -->
        <div class="mt-auto flex flex-col items-start text-left w-full px-1">
          <h3 class="font-bold text-[1.2rem] text-black leading-snug w-full tracking-tight" style="display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; white-space: normal;">${p.name}</h3>
          <p class="text-[0.95rem] font-medium text-gray-500 mt-1 w-full tracking-wide">${p.brand || 'Accesorio'}</p>
        </div>
      </div>`;
    }).join('');

    html += `
    <div class="category-section relative group/cat">
      <div class="flex items-center justify-center mb-8 relative">
        <h2 class="text-[2.2rem] md:text-[2.8rem] font-bold text-black tracking-tight text-center z-10 bg-[#f5f5f7] px-4">${cat} que te encantará</h2>
      </div>
      
      <div class="relative w-full">
        <!-- Scroll Buttons -->
        <button onclick="document.getElementById('${catId}').scrollBy({left: -350, behavior: 'smooth'})" class="absolute left-[-20px] top-1/2 -translate-y-1/2 bg-white/95 p-3 rounded-full shadow-[0_4px_12px_rgba(0,0,0,0.1)] z-10 opacity-0 group-hover/cat:opacity-100 transition-all hover:scale-110 border border-gray-100 text-black">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"></path></svg>
        </button>
        
        <div id="${catId}" class="flex justify-start gap-6 overflow-x-auto scroll-hide pb-8 pt-4 snap-x px-2">
          ${cardsHtml}
        </div>
        
        <button onclick="document.getElementById('${catId}').scrollBy({left: 350, behavior: 'smooth'})" class="absolute right-[-20px] top-1/2 -translate-y-1/2 bg-white/95 p-3 rounded-full shadow-[0_4px_12px_rgba(0,0,0,0.1)] z-10 opacity-0 group-hover/cat:opacity-100 transition-all hover:scale-110 border border-gray-100 text-black">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"></path></svg>
        </button>
      </div>
    </div>`;
  });

  container.innerHTML = html;
}"""

# Replace function
js = re.sub(r'function renderPhones\(\) \{.*?(?=\nfunction openDetail)', new_render_phones + '\n', js, flags=re.DOTALL)

# Fix event delegation to target correct container
js = js.replace("document.getElementById('phoneGrid').addEventListener", "document.getElementById('listingsContainer').addEventListener")

# Remove conditionFilter, priceFilter, sortFilter listeners
js = re.sub(r'document\.getElementById\(\'(condition|price|sort)Filter\'\)\.addEventListener\([^}]+\}\);', '', js)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js)
