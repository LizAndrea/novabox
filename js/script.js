// script.js

// Assumes `PRODUCTS` is loaded from data.js
let activeBrand = 'all';
let searchQuery = '';
let CATEGORIES_DATA = null;

function conditionBadge(c) {
  return `<span class="bg-ice-grey text-white text-xs font-bold px-3 py-1 rounded-full">${c}</span>`;
}

function renderPhones() {
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

  // 3. Render HTML
  let cardsHtml = filtered.map(p => {
    const defaultImg = "https://via.placeholder.com/300x400?text=No+Image";
    const imgUrl = p.image ? p.image : defaultImg;

    // Look up category color
    let catColor = '#3b82f6'; // fallback
    if (CATEGORIES_DATA && p.category) {
      const cData = CATEGORIES_DATA.find(c => c.name === p.category);
      if (cData && cData.color) catColor = cData.color;
    }
    const catName = p.category || 'Varios';

    return `
    <div data-action="view" data-id="${p.id}" class="cursor-pointer flex flex-col w-full group bg-white rounded-xl md:rounded-2xl overflow-hidden shadow-[0_4px_15px_rgba(0,0,0,0.03)] border border-gray-100 hover:bg-[#fafaf9] hover:shadow-[0_12px_35px_rgba(0,0,0,0.1)] hover:-translate-y-1.5 transition-all duration-300">
      
      <!-- Image Container -->
      <div class="w-full h-[140px] md:h-[260px] flex items-center justify-center p-3 md:p-6 relative">
        <img src="${imgUrl}" class="max-w-full max-h-full object-contain transition-transform duration-500 group-hover:scale-105" alt="${p.name}" />
      </div>

      <!-- Content Area (Inside Card) -->
      <div class="flex flex-col items-start text-left w-full h-full px-3 pb-3 md:px-6 md:pb-6 flex-1">
        <h3 class="font-semibold text-[0.95rem] md:text-[1.4rem] text-black leading-snug w-full tracking-tight truncate">${p.name}</h3>
        <p class="text-[0.75rem] md:text-[1rem] text-gray-700 mt-0.5 md:mt-1 w-full tracking-wide truncate">${p.brand || 'Accesorio'}</p>
        
        <!-- Category Badge -->
        <div class="mt-2" style="color: ${catColor};">
          <span class="inline-block px-2 py-0.5 text-[0.65rem] md:text-xs font-bold uppercase tracking-wider rounded-full border border-current" style="background-color: ${catColor}1A;">
            ${catName}
          </span>
        </div>
        
        <!-- Bottom Row: Color variants & Pedir Button -->
        <div class="flex items-center justify-between w-full mt-auto pt-4 md:pt-6">
          <div class="flex gap-1.5 md:gap-2">
            <div class="w-3 h-3 md:w-4 md:h-4 rounded-full bg-black shadow-sm"></div>
            <div class="w-3 h-3 md:w-4 md:h-4 rounded-full bg-gray-300 shadow-sm"></div>
            <div class="w-3 h-3 md:w-4 md:h-4 rounded-full bg-[#f97316] ring-2 ring-offset-2 ring-[#f97316] shadow-sm"></div>
          </div>
          
          <button class="text-[0.75rem] md:text-sm font-bold text-white bg-slate-900 hover:bg-sage-olive px-3 py-1.5 md:px-4 md:py-2 rounded-full transition-colors flex items-center gap-1 group/btn shadow-md">
            Pedir 
            <span class="group-hover/btn:translate-x-1 transition-transform">→</span>
          </button>
        </div>
      </div>
    </div>`;
  }).join('');

  let html = `
  <div class="category-section relative group/cat py-2 md:py-8 md:px-6">
    <div class="flex items-center justify-start md:justify-center mb-0 md:mb-4 relative textContainer MH-mg w-full text-left md:text-center px-1 md:px-0">
      <div class="textContent a0QQm yXpte w-full">
        <div class="desktopText csCim hidden md:block w-full">
          <h2 class="text-center w-full text-5xl font-bold text-gray-800 tracking-tight">Productos disponibles</h2>
        </div>
        <div class="mobileText TPiEz md:hidden w-full">
          <h2 class="text-left w-full text-xl font-bold text-gray-800 tracking-tight px-1">Productos disponibles</h2>
        </div>
      </div>
    </div>
    
    <div class="relative w-full">
      <div id="grid-all" class="grid grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-2 sm:gap-4 md:gap-6 pb-4 md:pb-8 pt-2 md:pt-4 px-0 md:px-0">
        ${cardsHtml}
      </div>
    </div>
  </div>`;

  container.innerHTML = html;
}

function openDetail(id) {
  const p = PRODUCTS.find(x => x.id == id);
  if (!p) return;

  const defaultImg = "https://via.placeholder.com/300x400?text=No+Image";
  const imgUrl = p.image ? p.image : defaultImg;

  document.getElementById('detailContent').innerHTML = `
    <div class="flex flex-col md:flex-row h-full">
      <!-- Left side: Image -->
      <div class="md:w-1/2 relative bg-white p-4 md:p-8 flex items-center justify-center min-h-[220px] md:min-h-[300px]">
        <img src="${imgUrl}" class="max-h-64 md:max-h-96 w-auto object-contain rounded-xl shadow-xl md:shadow-2xl transition-transform hover:scale-105 duration-500" alt="${p.name}" />
        <div class="absolute top-4 left-4 md:top-6 md:left-6 z-10 drop-shadow-md">
          ${conditionBadge(p.category || 'Producto')}
        </div>
      </div>
      
      <!-- Right side: Content -->
      <div class="md:w-1/2 p-5 md:p-10 flex flex-col h-full bg-gradient-to-br from-bone-white to-slate-900">
        <div class="flex items-center gap-2 mb-1 md:mb-3">
          <span class="text-xs md:text-sm text-mauve-brown font-medium uppercase tracking-wider">${p.brand}</span>
        </div>
        
        <h2 class="text-2xl md:text-4xl font-extrabold text-deep-coffee mb-1 md:mb-2 leading-tight">${p.name}</h2>
        
        <div class="grid grid-cols-2 gap-2 md:gap-4 mb-4 md:mb-6 text-xs md:text-sm mt-2 md:mt-4">
          <div class="bg-ice-grey p-2 md:p-3 rounded-lg md:rounded-xl border border-slate-700">
            <div class="text-mauve-brown mb-0.5 md:mb-1">Color</div>
            <div class="font-bold text-deep-coffee">${p.color || '-'}</div>
          </div>
          <div class="bg-ice-grey p-2 md:p-3 rounded-lg md:rounded-xl border border-slate-700">
            <div class="text-mauve-brown mb-0.5 md:mb-1">Energía</div>
            <div class="font-bold text-deep-coffee">${p.power || '-'}</div>
          </div>
        </div>
        
        <!-- Large Text Area for description -->
        <div class="text-deep-coffee text-xs md:text-sm leading-relaxed mb-4 md:mb-6 bg-ice-grey p-3 md:p-5 rounded-lg md:rounded-xl border border-slate-700 max-h-[160px] md:max-h-[200px] overflow-y-auto shadow-inner">
          <p><strong>Características:</strong> ${p.features || 'No especificado'}</p>
          ${p.instructions ? `<p class="mt-2"><strong>Instrucciones:</strong> ${p.instructions}</p>` : ''}
          ${p.warnings ? `<p class="mt-2 text-red-600"><strong>⚠️ Cuidados:</strong> ${p.warnings}</p>` : ''}
        </div>

        ${p.fun_fact ? `
        <div class="mb-4 md:mb-6 bg-amber-50 border-l-4 border-amber-400 p-3 md:p-4 rounded-r-lg md:rounded-r-xl">
          <p class="text-[0.65rem] md:text-xs text-amber-800 font-bold uppercase tracking-wider mb-0.5 md:mb-1">💡 ¿Sabías que?</p>
          <p class="text-xs md:text-sm text-amber-900">${p.fun_fact}</p>
        </div>
        ` : ''}

        <!-- Trust Signals (Amazon Style) -->
        <div class="flex items-center gap-3 md:gap-4 text-[0.65rem] md:text-xs font-medium text-slate-500 mb-4 md:mb-6 px-1">
           <div class="flex items-center gap-1"><svg class="w-3.5 h-3.5 md:w-4 md:h-4 text-sage-olive" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Compra Segura</div>
           <div class="flex items-center gap-1"><svg class="w-3.5 h-3.5 md:w-4 md:h-4 text-sage-olive" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> Atención Rápida</div>
        </div>

        <!-- Price and Order Button -->
        <div class="mt-auto pt-3 md:pt-4 border-t border-slate-700 flex items-center justify-between gap-4 md:gap-6 sticky bottom-0 bg-bone-white md:bg-transparent p-3 md:p-0 -mx-5 -mb-5 md:mx-0 md:mb-0 z-20 shadow-[0_-10px_15px_-3px_rgba(0,0,0,0.1)] md:shadow-none">
          <div class="flex items-end gap-2 md:gap-3">
            <div class="text-3xl md:text-4xl font-extrabold text-deep-coffee drop-shadow-lg leading-none">${p.price}Bs.</div>
            ${p.original_price > p.price ? `<div class="text-sm md:text-lg text-mauve-brown line-through mb-1">${p.original_price}Bs.</div>` : ''}
          </div>
          <button id="btnModalOrder" data-id="${p.id}" class="flex-1 bg-sage-olive hover:bg-dark-olive text-bone-white font-bold py-3.5 md:py-4 rounded-xl transition-all shadow-lg flex items-center justify-center gap-2 group">
            Pedir
            <span class="group-hover:translate-x-1 transition-transform">→</span>
          </button>
        </div>
      </div>
    </div>`;

  document.getElementById('detailModal').classList.remove('hidden');
  document.getElementById('detailModal').classList.add('flex');
  history.pushState({ modal: 'detail', id: id }, '', `#producto-${id}`);
}

function closeDetail() {
  document.getElementById('detailModal').classList.add('hidden');
  document.getElementById('detailModal').classList.remove('flex');
  if (window.location.hash.startsWith('#producto-')) {
    history.replaceState(null, '', window.location.pathname);
  }
}

window.addEventListener('popstate', (e) => {
  if (document.getElementById('detailModal').classList.contains('flex')) {
    closeDetail();
  }
});

function sendToWhatsApp(id) {
  const p = PRODUCTS.find(x => x.id == id);
  if (!p) return;
  const phoneNumber = "61198607";
  const message = `Hola NovaBox! 👋\n\nMe interesa el producto *${p.name}* (ID: ${p.id}).\nPrecio: *${p.price} Bs.*\n\n¿Tienen disponibilidad?`;
  const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(message)}`;
  window.open(whatsappUrl, '_blank');
}

function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.remove('hidden');
  setTimeout(() => t.classList.add('hidden'), 2500);
}

function scrollToListings() {
  const q = document.getElementById('heroSearch').value;
  searchQuery = q;
  renderPhones();
  document.getElementById('listings').scrollIntoView({ behavior: 'smooth' });
}

// Scroll controls for categories
const btnScrollLeft = document.getElementById('scrollLeft');
const btnScrollRight = document.getElementById('scrollRight');
const brandChipsContainer = document.getElementById('brandChips');

if (btnScrollLeft && brandChipsContainer) {
  btnScrollLeft.addEventListener('click', () => {
    brandChipsContainer.scrollBy({ left: -250, behavior: 'smooth' });
  });
}
if (btnScrollRight && brandChipsContainer) {
  btnScrollRight.addEventListener('click', () => {
    brandChipsContainer.scrollBy({ left: 250, behavior: 'smooth' });
  });
}

// Load dynamic categories
async function loadCategories() {
  try {
    const response = await fetch('js/categories.json');
    if (response.ok) {
      const categories = await response.json();
      const container = document.getElementById('brandChips');
      const footerContainer = document.getElementById('footerCategories');

      CATEGORIES_DATA = categories;
      renderPhones();

      if (container) {
        categories.forEach(cat => {
          // Top Brand Chips
          const btn = document.createElement('button');
          btn.className = 'brand-chip flex flex-col items-center gap-2 md:gap-3 group snap-start flex-shrink-0 min-w-[70px] md:min-w-[100px]';
          btn.dataset.brand = cat.name;
          btn.dataset.catId = cat.id;
          btn.innerHTML = `
            <div class="w-14 h-14 md:w-20 md:h-20 flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-[.active]:scale-110">
                <img src="assets/images/pagina/categorias/${cat.iconImage || (cat.id + '.png')}" class="max-w-full max-h-full object-contain filter drop-shadow-sm group-[.active]:drop-shadow-md" alt="${cat.name}" />
            </div>
            <span class="text-sm md:text-base font-medium text-gray-500 group-hover:text-gray-900 group-hover:scale-110 group-[.active]:text-gray-900 group-[.active]:font-bold group-[.active]:scale-110 transition-all duration-300 whitespace-nowrap text-center">${cat.name}</span>
          `;
          container.appendChild(btn);
          // Footer Banners
          if (footerContainer) {
            const footerBtn = document.createElement('div');
            footerBtn.className = 'snap-center flex-shrink-0 w-[85%] md:w-full h-full cursor-pointer relative group rounded-3xl md:rounded-none overflow-hidden shadow-2xl md:shadow-none';
            footerBtn.innerHTML = `
              <img src="assets/images/pagina/categorias/${cat.id}.png" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="${cat.name}" />
              <div class="absolute inset-0 bg-black/40 group-hover:bg-black/20 transition-colors duration-500"></div>
              <div class="absolute inset-0 flex flex-col items-center justify-center p-8 text-center">
                <h3 class="text-white font-extrabold text-4xl md:text-6xl drop-shadow-2xl tracking-widest uppercase scale-95 group-hover:scale-100 transition-transform duration-500">${cat.name}</h3>
                ${cat.detail ? `<p class="mt-3 text-white/90 text-sm md:text-lg font-medium drop-shadow-md tracking-wide max-w-2xl">${cat.detail}</p>` : ''}
              </div>
            `;
            footerBtn.addEventListener('click', () => {
              // Same functionality as BRANDS section
              document.querySelectorAll('.brand-chip').forEach(b => b.classList.remove('active'));
              const topChip = document.querySelector(`.brand-chip[data-brand="${cat.name}"]`);
              if (topChip) {
                topChip.classList.add('active');
                topChip.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
              }
              activeBrand = cat.name;
              renderPhones();
              document.getElementById('listings').scrollIntoView({ behavior: 'smooth' });
            });
            footerContainer.appendChild(footerBtn);
          }
        });
      }
    }
  } catch (err) {
    console.error('Error loading categories:', err);
  }

  // Attach click events to top chips
  document.querySelectorAll('.brand-chip').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.brand-chip').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeBrand = btn.dataset.brand;
      renderPhones();
    });
  });
}

// Footer Carousel Scroll Controls
const footerScrollLeft = document.getElementById('footerScrollLeft');
const footerScrollRight = document.getElementById('footerScrollRight');
const footerContainer = document.getElementById('footerCategories');

if (footerScrollLeft && footerScrollRight && footerContainer) {
  footerScrollLeft.addEventListener('click', () => {
    footerContainer.scrollBy({ left: -footerContainer.clientWidth, behavior: 'smooth' });
  });
  footerScrollRight.addEventListener('click', () => {
    footerContainer.scrollBy({ left: footerContainer.clientWidth, behavior: 'smooth' });
  });
}

loadCategories();

// Listen for Search Input
const searchInput = document.getElementById('searchInput');
if (searchInput) {
  searchInput.addEventListener('input', (e) => {
    searchQuery = e.target.value;

    // Optionally reset brand to 'all' when searching globally
    if (searchQuery.trim() !== '') {
      activeBrand = 'all';
      document.querySelectorAll('.brand-chip').forEach(b => b.classList.remove('active'));
      const allBtn = document.querySelector('.brand-chip[data-brand="all"]');
      if (allBtn) allBtn.classList.add('active');
    }

    renderPhones();
  });
}

// Hero search enter key
const heroSearch = document.getElementById('heroSearch');
if (heroSearch) {
  heroSearch.addEventListener('keydown', e => {
    if (e.key === 'Enter') scrollToListings();
  });
}

// Search Hero
const btnSearchHero = document.getElementById('btnSearchHero');
if (btnSearchHero) {
  btnSearchHero.addEventListener('click', scrollToListings);
}

// Global Order Button
const btnContactWhatsApp = document.getElementById('btnContactWhatsApp');
if (btnContactWhatsApp) {
  btnContactWhatsApp.addEventListener('click', () => {
    // Just open normal whatsapp if not a specific product
    window.open('https://wa.me/61198607', '_blank');
  });
}

// Close Detail Modal
const btnCloseDetail = document.getElementById('btnCloseDetail');
if (btnCloseDetail) {
  btnCloseDetail.addEventListener('click', closeDetail);
}

// Event Delegation for Phone Grid (Ver / Pedir)
document.getElementById('listingsContainer').addEventListener('click', (e) => {
  const btn = e.target.closest('[data-action]');
  if (!btn) return;
  const action = btn.dataset.action;
  const id = Number(btn.dataset.id);

  if (action === 'view') {
    openDetail(id);
  } else if (action === 'order') {
    sendToWhatsApp(id);
  }
});

// Event Delegation for Detail Modal Order Button
document.getElementById('detailContent').addEventListener('click', (e) => {
  if (e.target.id === 'btnModalOrder') {
    sendToWhatsApp(Number(e.target.dataset.id));
    closeDetail();
  }
});

renderPhones();
