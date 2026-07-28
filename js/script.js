// script.js

// Assumes `PRODUCTS` is loaded from data.js
let activeBrand = 'all';
let searchQuery = '';

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
      <div data-action="view" data-id="${p.id}" class="cursor-pointer flex flex-col w-full group bg-[#f5f5f7] rounded-3xl overflow-hidden shadow-[0_8px_30px_rgba(0,0,0,0.08)] hover:shadow-[0_20px_40px_rgba(0,0,0,0.15)] hover:-translate-y-2 hover:bg-white transition-all duration-300">
        
        <!-- Image Container -->
        <div class="w-full h-[260px] flex items-center justify-center p-6 relative">
          <img src="${imgUrl}" class="max-w-full max-h-full object-contain transition-transform duration-500 group-hover:scale-105 drop-shadow-xl" alt="${p.name}" />
        </div>

        <!-- Content Area (Inside Card) -->
        <div class="flex flex-col items-start text-left w-full px-6 pb-6">
          <h3 class="font-semibold text-[1.4rem] text-black leading-snug w-full tracking-tight truncate">${p.name}</h3>
          <p class="text-[1rem] text-gray-700 mt-1 w-full tracking-wide truncate">${p.brand || 'Accesorio'}</p>
          
          <!-- Color variants (Aesthetic Apple Style) -->
          <div class="flex gap-2 mt-4">
            <div class="w-5 h-5 rounded-full bg-black shadow-sm"></div>
            <div class="w-5 h-5 rounded-full bg-gray-300 shadow-sm"></div>
            <div class="w-5 h-5 rounded-full bg-[#f97316] ring-2 ring-offset-2 ring-[#f97316] shadow-sm"></div>
          </div>
        </div>
      </div>`;
    }).join('');

    html += `
    <div class="category-section relative group/cat">
      <div class="flex items-center justify-center mb-10 relative textContainer MH-mg w-full text-center">
        <div class="textContent a0QQm yXpte w-full">
          <div class="desktopText csCim hidden md:block w-full">
            <h2 class="text-center w-full"><span>${cat}</span></h2>
          </div>
          <div class="mobileText TPiEz md:hidden w-full">
            <h2 class="text-center w-full"><span>${cat}</span></h2>
          </div>
        </div>
      </div>
      
      <div class="relative w-full">
        <div id="${catId}" class="grid grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-3 sm:gap-4 md:gap-6 pb-8 pt-4 px-2 md:px-0">
          ${cardsHtml}
        </div>
      </div>
    </div>`;
  });

  container.innerHTML = html;
}

function openDetail(id) {
  const p = PRODUCTS.find(x => x.id === id);
  if (!p) return;

  const defaultImg = "https://via.placeholder.com/300x400?text=No+Image";
  const imgUrl = p.image ? p.image : defaultImg;

  document.getElementById('detailContent').innerHTML = `
    <div class="flex flex-col md:flex-row h-full">
      <!-- Left side: Image -->
      <div class="md:w-1/2 relative bg-bone-white p-8 flex items-center justify-center min-h-[300px]">
        <img src="${imgUrl}" class="max-h-96 w-auto object-contain rounded-xl shadow-2xl transition-transform hover:scale-105 duration-500" alt="${p.name}" />
        <div class="absolute top-6 left-6 z-10 drop-shadow-md">
          ${conditionBadge(p.category || 'Producto')}
        </div>
      </div>
      
      <!-- Right side: Content -->
      <div class="md:w-1/2 p-8 md:p-10 flex flex-col h-full bg-gradient-to-br from-bone-white to-slate-900">
        <div class="flex items-center gap-2 mb-3">
          <span class="text-sm text-mauve-brown font-medium uppercase tracking-wider">${p.brand}</span>
        </div>
        
        <h2 class="text-3xl md:text-4xl font-extrabold text-deep-coffee mb-2 leading-tight">${p.name}</h2>
        
        <div class="grid grid-cols-2 gap-4 mb-6 text-sm mt-4">
          <div class="bg-ice-grey p-3 rounded-xl border border-slate-700">
            <div class="text-mauve-brown mb-1">Color</div>
            <div class="font-bold text-deep-coffee">${p.color || '-'}</div>
          </div>
          <div class="bg-ice-grey p-3 rounded-xl border border-slate-700">
            <div class="text-mauve-brown mb-1">Energía</div>
            <div class="font-bold text-deep-coffee">${p.energy || '-'}</div>
          </div>
        </div>
        
        <!-- Large Text Area for description -->
        <div class="text-deep-coffee text-sm leading-relaxed mb-8 bg-ice-grey p-5 rounded-xl border border-slate-700 max-h-[200px] overflow-y-auto shadow-inner">
          <p><strong>Características:</strong> ${p.desc}</p>
          ${p.instructions ? `<p class="mt-2"><strong>Instrucciones:</strong> ${p.instructions}</p>` : ''}
          ${p.warnings ? `<p class="mt-2"><strong>Cuidados:</strong> ${p.warnings}</p>` : ''}
        </div>

        <!-- Price and Order Button -->
        <div class="mt-auto pt-4 border-t border-slate-700 flex items-center justify-between gap-6">
          <div class="flex items-end gap-3">
            <div class="text-4xl font-extrabold text-deep-coffee drop-shadow-lg leading-none">${p.price}Bs.</div>
            ${p.original_price > p.price ? `<div class="text-lg text-mauve-brown line-through mb-1">${p.original_price}Bs.</div>` : ''}
          </div>
          <button id="btnModalOrder" data-id="${p.id}" class="flex-1 bg-sage-olive hover:bg-dark-olive text-bone-white font-bold py-4 rounded-xl transition-all shadow-lg flex items-center justify-center gap-2 group">
            Pedir
            <span class="group-hover:translate-x-1 transition-transform">→</span>
          </button>
        </div>
      </div>
    </div>`;

  document.getElementById('detailModal').classList.remove('hidden');
  document.getElementById('detailModal').classList.add('flex');
}

function closeDetail() {
  document.getElementById('detailModal').classList.add('hidden');
  document.getElementById('detailModal').classList.remove('flex');
}

function sendToWhatsApp(id) {
  const p = PRODUCTS.find(x => x.id === id);
  if (!p) return;
  const phoneNumber = "77777777";
  const message = `Hola NovaBox! Quiero hacer un pedido de: ${p.name} por ${p.price}Bs.`;
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

// Brand chips
document.querySelectorAll('.brand-chip').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.brand-chip').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    activeBrand = btn.dataset.brand;
    renderPhones();
  });
});

// Listen for Search Input
const searchInput = document.getElementById('searchInput');
if (searchInput) {
  searchInput.addEventListener('input', (e) => {
    searchQuery = e.target.value;
    
    // Optionally reset brand to 'all' when searching globally
    if(searchQuery.trim() !== '') {
      activeBrand = 'all';
      document.querySelectorAll('.brand-chip').forEach(b => b.classList.remove('active'));
      const allBtn = document.querySelector('.brand-chip[data-brand="all"]');
      if(allBtn) allBtn.classList.add('active');
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
    window.open('https://wa.me/77777777', '_blank');
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
