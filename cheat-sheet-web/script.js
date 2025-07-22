document.addEventListener('DOMContentLoaded', (event) => {
    // Activa el resaltado de sintaxis en todos los bloques de código
    document.querySelectorAll('pre code.python').forEach((block) => {
        hljs.highlightElement(block);
    });

    // No se añaden efectos de JS adicionales para mantener un diseño limpio
    // y compatible con la impresión.
});
