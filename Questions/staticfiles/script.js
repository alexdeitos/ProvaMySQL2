document.addEventListener('DOMContentLoaded', function () {
    const enviarRespostasBtn = document.getElementById('enviar-respostas');
    enviarRespostasBtn.addEventListener('click', validarRespostas);

    function validarRespostas() {
        perguntasNaoRespondidas = 0;
        perguntasCorretas = 0;
        perguntasIncorretas = 0;

        const totalPerguntas = document.querySelectorAll('.pergunta').length;
        const respostasMarcadas = document.querySelectorAll('input[type="checkbox"]:checked');

        respostasMarcadas.forEach(resposta => {
            const perguntaId = resposta.name;
            const respostaLabel = document.getElementById(`resposta-label-${perguntaId}-${resposta.value}`);

            if (resposta.getAttribute('data-correta')) {
                respostaLabel.style.color = 'blue'; // Marca a resposta como correta (azul)
                perguntasCorretas++;
            } else {
                respostaLabel.style.color = 'red'; // Marca a resposta como incorreta (vermelha)
                perguntasIncorretas++;
                const respostasDaPergunta = document.querySelectorAll(`input[name="${perguntaId}"]`);
                respostasDaPergunta.forEach(respostaCorreta => {
                    if (respostaCorreta.getAttribute('data-correta')) {
                        const respostaCorretaLabel = document.getElementById(`resposta-label-${perguntaId}-${respostaCorreta.value}`);
                        respostaCorretaLabel.style.color = 'blue'; // Marca a resposta correta como azul
                    }
                });
            }
        });

        perguntasNaoRespondidas = totalPerguntas - respostasMarcadas.length;
        const mensagem = `Você respondeu corretamente ${perguntasCorretas} pergunta(s).\n`
            + `Você respondeu incorretamente ${perguntasIncorretas} pergunta(s).\n`
            + `Você não respondeu ${perguntasNaoRespondidas} pergunta(s).`;
        alert(mensagem);

        // Marca as respostas corretas após o usuário ter visto o alerta
        marcarRespostasCorretas();
    }

    const btnMarcarRespostas = document.getElementById('marcar-respostas');

    btnMarcarRespostas.addEventListener('click', function () {
        marcarRespostas(); // Chama a função para marcar as respostas
    });

    function marcarRespostas() {
        // Loop sobre todas as perguntas
        document.querySelectorAll('.pergunta').forEach(function (pergunta) {
            // Loop sobre todas as respostas da pergunta
            pergunta.querySelectorAll('.resposta').forEach(function (resposta) {
                var checkbox = resposta.querySelector('input[type="checkbox"]');
                var respostaLabel = resposta.querySelector('.resposta-label');

                // Remover classes anteriores
                resposta.classList.remove('resposta-correta', 'resposta-incorreta');

                // Verifica se a resposta está correta

                if (checkbox.getAttribute('data-correta') === 'true') {
                    resposta.classList.add('resposta-correta');
                } else {
                    resposta.classList.add('resposta-incorreta');
                }

            });
        });
    }
    // UPDATE PAGINA AO CLICAR NA IMAGEM DO ALIEN
    const futureImage = document.getElementById('future');
    futureImage.addEventListener('click', () => {
        updatePageFuture(); // Chamando a função para validar as respostas
    });

    function updatePageFuture() {
        window.location.reload(); // Recarrega a página quando a imagem é clicada
    }

    const limparRespostasBtn = document.getElementById('limpar-respostas');
    const limparRespostasBtn1 = document.getElementById('limpar-respostas1');
    limparRespostasBtn.addEventListener('click', limparRespostas);
    limparRespostasBtn1.addEventListener('click', limparRespostas);

    function limparRespostas() {
        const respostas = document.querySelectorAll('.resposta');
        respostas.forEach(resposta => {
            resposta.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
                checkbox.checked = false;
            });
            resposta.classList.remove('resposta-correta', 'resposta-incorreta');
            const respostaLabel = resposta.querySelector('.resposta-label');
            respostaLabel.style.color = '';
        });
    }
});