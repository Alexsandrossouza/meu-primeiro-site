document.addEventListener('DOMContentLoaded', function() {
    const campoBusca = document.getElementById('campoBusca');
    const cardsJogos = document.querySelectorAll('.card-jogo');
    const mensagemNaoEncontrado = document.getElementById('mensagemNaoEncontrado');

    // Executa a função toda vez que o usuário digitar uma letra
    campoBusca.addEventListener('input', function() {
        const termoBusca = campoBusca.value.toLowerCase().trim();
        let encontrouQualquerJogo = false;

        cardsJogos.forEach(function(card) {
            // Pega o título do jogo dentro do h3 do card
            const tituloJogo = card.querySelector('.card-info h3').textContent.toLowerCase();

            // Se o título conter o que foi digitado, mostra o card. Senão, esconde.
            if (tituloJogo.includes(termoBusca)) {
                card.style.display = 'flex'; // Mantém o formato original do card
                encontrouQualquerJogo = true;
            } else {
                card.style.display = 'none'; // Esconde o card
            }
        });

        // Controle da mensagem de "Não encontrado"
        if (encontrouQualquerJogo) {
            mensagemNaoEncontrado.style.display = 'none';
        } else {
            mensagemNaoEncontrado.style.display = 'block';
        }
    });
});
