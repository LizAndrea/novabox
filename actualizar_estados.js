const fs = require('fs');

// === CONFIGURACIÓN ===
// Asegúrate de que las rutas apunten a los archivos correctos en tu NUEVO proyecto
const RUTA_DATA_JS = './js/data.js'; 
const RUTA_ESTADOS_JSON = './estados_extraidos.json'; 

try {
  // 1. Leer el archivo JSON con los estados
  const estadosRaw = fs.readFileSync(RUTA_ESTADOS_JSON, 'utf8');
  const estados = JSON.parse(estadosRaw);

  // 2. Leer tu nuevo archivo data.js y extraer su contenido
  let dataJsContent = fs.readFileSync(RUTA_DATA_JS, 'utf8');
  
  // Hacemos un "truco" para extraer el array de productos y poder leerlo en JS
  let contenidoArray = dataJsContent.replace(/const\s+PRODUCTS\s*=\s*/, '').replace(/;?\s*$/, '');
  
  // Guardamos los comentarios iniciales del archivo original (opcional, para no perderlos)
  const comentariosMatch = dataJsContent.match(/^(\/\*\*[\s\S]*?\*\/)/);
  const comentarios = comentariosMatch ? comentariosMatch[1] : '';

  // 3. Convertimos el string a un arreglo real de JavaScript
  const productos = Function('return ' + contenidoArray)();
  
  // 4. Actualizamos el estado de cada producto si existe en nuestro JSON
  let contadorActualizados = 0;
  productos.forEach(producto => {
    if (estados[producto.id]) {
      producto.estado = estados[producto.id];
      contadorActualizados++;
    } else {
      // Si no estaba vendido en el original, nos aseguramos que quede disponible
      producto.estado = ""; 
    }
  });

  // 5. Volvemos a armar el contenido del archivo data.js
  const nuevoContenido = `${comentarios}\nconst PRODUCTS = ${JSON.stringify(productos, null, 2)};\n`;

  // 6. Sobrescribimos el data.js con la nueva información
  fs.writeFileSync(RUTA_DATA_JS, nuevoContenido);
  console.log(`✅ ¡Éxito! Se actualizaron los estados de ${contadorActualizados} productos en el nuevo data.js.`);
  
} catch (error) {
  console.error("❌ Hubo un error al actualizar:", error.message);
}
