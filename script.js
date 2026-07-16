// 1. Procuramos o botão verde no HTML usando a classe dele
const botaoVerde = document.querySelector('.btn-verde');

// 2. Dizemos ao botão para "ouvir" quando alguém clicar nele
botaoVerde.addEventListener('click', () => {
    // 3. O que vai acontecer quando clicar: mostrar um alerta na tela!
    alert('Olá, Bem vindo a nossa página, logo com conteúdo novos! 🎉');

// 4. Procurando o botão azul no HTML usando a classe dele
const botaoAzul = document.querySelector('.btn-azul');

// 5. Dizemos ao botão azul para "ouvir" quando alguém clicar nele
botaoAzul.addEventListener('click', () => {
    // 6. O que vai acontecer quando clicar: mostrar um alerta na tela!
    alert('Agora deixe de ser curiosso e para de apertar tudo que vc ver kkkkkkkk');
});