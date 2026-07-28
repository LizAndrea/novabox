# NovaBox - Electrónica y Tecnología

Bienvenido al repositorio de **NovaBox**, una moderna y rápida *landing page* (catálogo web) diseñada para la venta directa de productos físicos y digitales. El proyecto destaca por su estética "Dark Tech / Cyberpunk", orientada al nicho de la tecnología, y un flujo de compra sumamente ágil e integrado con WhatsApp.

## 🚀 Características Principales

- **Catálogo Dinámico:** Los productos se cargan dinámicamente mediante Vanilla JavaScript desde un archivo de datos local (`data.js`), facilitando el mantenimiento y actualización del inventario sin necesidad de bases de datos complejas.
- **Búsqueda y Filtros en Tiempo Real:** 
  - Barra de búsqueda interactiva por nombre de producto o marca.
  - Filtros rápidos por categorías representados por "chips" visuales con iconos.
- **Visualización Detallada (Modal):** Al hacer clic en un producto, se abre una ventana modal rica en información que muestra características, instrucciones, disponibilidad de colores e incluso datos curiosos (fun facts), sin abandonar la página principal.
- **Flujo de Venta Ágil (WhatsApp):** Cada producto tiene un botón de "Pedir" que redirige a los usuarios directamente al chat de WhatsApp del comercio para concretar la venta de forma personalizada.
- **Optimizada para SEO:**
  - Etiquetas `alt` descriptivas y automáticas en las imágenes de los productos para mejorar el indexado.
  - Metadatos dinámicos: El `<title>` y `<meta name="description">` se actualizan automáticamente cuando se abre la vista de detalle de un producto específico.
- **Gestión de Estados Vacíos:** Si una búsqueda no arroja resultados, se presenta un panel amigable que permite resetear la búsqueda ("Ver todos los productos") o consultar atención al cliente personalizada vía WhatsApp.
- **Diseño Moderno y Responsivo:** Construida con Tailwind CSS, adaptándose impecablemente desde dispositivos móviles hasta grandes pantallas de escritorio, con una estética de modo oscuro (Dark Mode).

## 🛠️ Tecnologías Utilizadas

- **HTML5:** Estructura semántica del contenido.
- **CSS (Tailwind CSS):** Utilizado a través del CDN para un desarrollo rápido y escalable de la interfaz de usuario.
- **Vanilla JavaScript:** Control de estado, renderizado dinámico, enrutamiento ligero (PushState) y manejo de la lógica de negocio, sin dependencias de frameworks externos pesados.

## 📂 Estructura del Proyecto

```text
novabox/
├── index.html              # Estructura principal y plantilla del sitio
├── css/
│   └── styles.css          # Reglas CSS personalizadas y ajustes menores
├── js/
│   ├── script.js           # Lógica de renderizado, modales, búsqueda y eventos
│   ├── data.js             # Base de datos local (Lista de objetos JSON con el inventario)
│   └── tailwind.config.js  # Configuración del tema y colores personalizados (Dark Tech)
├── lineaGrafica/
│   └── colores.md          # Documentación de la paleta de colores del proyecto
└── assets/                 # Imágenes, iconos, logos y banners
```

## ⚙️ Cómo gestionar el Inventario

Todos los productos se gestionan desde el archivo `js/data.js`. Para agregar un producto nuevo, simplemente añade un objeto al arreglo `PRODUCTS`:

```javascript
{
  "id": "1",
  "name": "Nombre del Producto",
  "price": 120.0,
  "min_price": 90.0,       // Se mostrará este precio base si está definido
  "category": "Gadgets",
  "brand": "Marca",
  "color": "Negro",
  "features": "Características principales del producto...",
  "instructions": "Instrucciones de uso básico.",
  "image": "assets/images/productos/ruta_a_la_imagen.jpg"
}
```

## 💻 Despliegue y Ejecución

Dado que es un proyecto Front-end estático puro (HTML, CSS, JS):
1. **Ejecución Local:** Solo necesitas abrir el archivo `index.html` en cualquier navegador web. Para evitar posibles restricciones de políticas de CORS por recursos locales (dependiendo del navegador), se recomienda usar una extensión como *Live Server* en VS Code.
2. **Despliegue a Producción:** Los archivos pueden ser alojados en cualquier servidor estático estándar como GitHub Pages, Vercel, Netlify o un hosting tradicional mediante FTP. No se requiere Node.js ni procesos de build complejos.
