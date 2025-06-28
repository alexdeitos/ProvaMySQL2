document.addEventListener('DOMContentLoaded', function () {
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
});

