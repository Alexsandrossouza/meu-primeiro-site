// ==========================================
// 1. BOTÃO VERDE (SAIBA MAIS / OFERTAS)
// ==========================================
// APAGUE ESTE BLOCO TODO:
// No seu arquivo static/script.js:
const botaoVerde = document.querySelector('.btn-ofertas'); // Usamos .btn-ofertas para não dar conflito!

if (botaoVerde) {
    botaoVerde.addEventListener('click', () => {
        alert('Aproveite! Xbox 360 com 20% de desconto e frete grátis hoje!');
    });
}

// ==========================================
// 2. BOTÃO AZUL (CURIOSO)
// ==========================================
const botaoAzul = document.querySelector('.btn-azul');
if (botaoAzul) {
    botaoAzul.addEventListener('click', () => {
        alert('Fique por dentro das novidades, e não perca nenhuma oferta! 😉');
    });  
}

// ==========================================
// 3. BOTÃO COMPRAR AGORA (NOVA PÁGINA)
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
    const botaoComprar = document.querySelector('.btn-comprar');

    if (botaoComprar) {
        botaoComprar.addEventListener('click', () => {
            window.open('https://www.mercadolivre.com.br', '_blank');
        });
    }
}); // <--- FECHA O IF DO BOTAO COMPRAR AQUI!

