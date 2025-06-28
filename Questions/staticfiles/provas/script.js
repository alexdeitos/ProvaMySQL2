document.addEventListener('DOMContentLoaded', function () {
    const perguntas = document.querySelectorAll('.pergunta');
    let perguntaAtual = 0;
    function mostrarPergunta(indice) {
        perguntas.forEach((pergunta, index) => {
            if (index === indice) {
                pergunta.style.display = 'block';
            } else {
                pergunta.style.display = 'none';
            }
        });
    }
    function mostrarPerguntaAtual() {
        mostrarPergunta(perguntaAtual);
    }
    mostrarPerguntaAtual();
    const proximaPerguntaBtn = document.getElementById('proxima-pergunta');
    proximaPerguntaBtn.addEventListener('click', () => {
        perguntaAtual = (perguntaAtual + 1) % perguntas.length;
        mostrarPerguntaAtual();
    });
    const perguntaAnteriorBtn = document.getElementById('pergunta-anterior');
    perguntaAnteriorBtn.addEventListener('click', () => {
        perguntaAtual = (perguntaAtual - 1 + perguntas.length) % perguntas.length;
        mostrarPerguntaAtual();
    });

    document.getElementById('enviar-respostas').addEventListener('click', function() {
        marcarRespostas();
    });

    document.getElementById('limpar-respostas').addEventListener('click', function() {
        limparRespostas();
    });

    function marcarRespostas() {
        // Loop sobre todas as perguntas
        document.querySelectorAll('.pergunta').forEach(function(pergunta) {
            // Loop sobre todas as respostas da pergunta
            pergunta.querySelectorAll('.resposta').forEach(function(resposta) {
                var checkbox = resposta.querySelector('input[type="checkbox"]');
                var respostaLabel = resposta.querySelector('.resposta-label');

                // Remover classes anteriores
                resposta.classList.remove('resposta-correta', 'resposta-incorreta');

                // Verifica se a resposta está correta
                if (checkbox.checked) {
                    if (checkbox.getAttribute('data-correta') === 'true') {
                        resposta.classList.add('resposta-correta');
                    } else {
                        resposta.classList.add('resposta-incorreta');
                    }
                }
            });
        });
    }

    function limparRespostas() {
        // Desmarcar todos os checkboxes
        document.querySelectorAll('#formulario-respostas input[type="checkbox"]').forEach(function(checkbox) {
            checkbox.checked = false;
        });

        // Remover classes de cor
        document.querySelectorAll('.resposta').forEach(function(resposta) {
            resposta.classList.remove('resposta-correta', 'resposta-incorreta');
        });
    }

    document.addEventListener('DOMContentLoaded', function() {
        const futureImage = document.getElementById('future');
    
        if (futureImage) {
            futureImage.addEventListener('click', function() {
                window.location.reload(); // Recarrega a página quando a imagem é clicada
            });
        }
    });
});