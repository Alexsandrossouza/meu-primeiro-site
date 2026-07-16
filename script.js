// ==========================================
// 1. BOTÃO VERDE (SAIBA MAIS / OFERTAS)
// ==========================================
const botaoVerde = document.querySelector('.btn-verde');
if (botaoVerde) {
    botaoVerde.addEventListener('click', () => {
        alert('Olá, Bem vindo a nossa página, logo com conteúdo novos! 🎉');
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
// Selecionamos o botão de comprar pela classe dele (.btn-comprar)
const botaoComprar = document.querySelector('.btn-comprar');

if (botaoComprar) 
    botaoComprar.addEventListener('click', () => {
        // OPÇÃO A: Abrir o link em uma NOVA ABA (Mais recomendado para sites de vendas)
        window.open('https://www.mercadolivre.com.br/xbox-360-fat-super-elite-call-of-duty-rgh/up/MLBU3666157348?pdp_filters=item_id%3AMLB6017296060&matt_tool=38524122#origin=share&sid=share&wid=MLB6017296060&action=copy', '_blank');
        
        // OPÇÃO B: Se preferir abrir na MESMA ABA, apague a linha de cima e use esta:
        // window.location.href = 'https://www.xbox.com';
    });
const botaoVerde = document.querySelector('.btn-verde');

if (botaoVerde) {
    botaoVerde.addEventListener('click', () => {
        // Substitua o link abaixo pelo link direto que você copiou do RomsFun!
        window.open('https://sto1.romsforever.co/0:/Xbox-360-Digital/Need%20for%20Speed%20-%20Most%20Wanted%20-%20A%20Criterion%20Game%20-%20Strike%20Pack%20(World)%20(DLC).zip?token=c3xZcFthXAVOQyAgUX5VMw4ATkN1dV1%2BAzYMB05AInEPfgBjDh1FFnlwW3dYY1pS', '_blank');
    });


}
