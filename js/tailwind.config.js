/**
 * Configuración de Tailwind CSS.
 * Extiende la paleta de colores nativa con los colores corporativos "Dark Tech" de NovaBox.
 * NOTA: Aunque las variables conservan nombres de tonos tierra (ej. deep-coffee),
 * sus valores (hex) han sido modificados para un estilo tecnológico moderno y oscuro (Dark Mode).
 */
tailwind.config = {
    theme: {
        extend: {
            colors: {
                'deep-coffee': '#f8fafc',
                'bone-white': '#0f172a',
                'mauve-brown': '#94a3b8',
                'sage-olive': '#00f0ff',
                'dark-olive': '#0284c7',
                'ice-grey': '#1e293b',
                'sandy-yellow': '#3b82f6',
                'soft-terracotta': '#8b5cf6',
            }
        }
    }
};
