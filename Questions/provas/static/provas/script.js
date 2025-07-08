document.addEventListener('DOMContentLoaded', function () {
    const enviarRespostasBtn = document.getElementById('enviar-respostas');
    const marcarRespostasBtn = document.getElementById('marcar-respostas');
    enviarRespostasBtn.addEventListener('click', validarRespostas);
    marcarRespostasBtn.addEventListener('click', validarRespostas);

    function validarRespostas() {
        let perguntasCorretas = 0;
        const totalPerguntas = document.querySelectorAll('.pergunta').length;
        const perguntas = document.querySelectorAll('.pergunta');

        perguntas.forEach(pergunta => {
            const checkboxes = pergunta.querySelectorAll('input[type="checkbox"]');
            let acertos = 0;
            let totalCorretas = 0;

            checkboxes.forEach(cb => {
                if (cb.checked && cb.getAttribute('data-correta')) acertos++;
                if (cb.getAttribute('data-correta')) totalCorretas++;
            });

            if (acertos === totalCorretas) perguntasCorretas++; // Conta só se todas corretas foram marcadas
        });

        alert(`Você acertou ${perguntasCorretas} de ${totalPerguntas} perguntas`);
    }

    const perguntas = document.querySelectorAll('.pergunta');
    let perguntaAtual = 0;

    // Função para mostrar a pergunta atual
    function mostrarPerguntaAtual() {
        perguntas.forEach((pergunta, index) => {
            if (index === perguntaAtual) {
                pergunta.style.display = 'block';
            } else {
                pergunta.style.display = 'none';
            }
        });

        // Habilitar ou desabilitar o botão "Pergunta Anterior" com base na pergunta atual
        const perguntaAnteriorBtn = document.getElementById('pergunta-anterior');
        perguntaAnteriorBtn.disabled = perguntaAtual === 0; // Desabilita o botão na primeira pergunta
    }

    // Mostrar a primeira pergunta ao carregar a página
    mostrarPerguntaAtual();

    // Ouvinte de evento para o botão "Próxima Pergunta"
    const proximaPerguntaBtn = document.getElementById('proxima-pergunta');
    proximaPerguntaBtn.addEventListener('click', () => {
        perguntaAtual = (perguntaAtual + 1) % perguntas.length;
        mostrarPerguntaAtual();
    });

    // Ouvinte de evento para o botão "Pergunta Anterior"
    const perguntaAnteriorBtn = document.getElementById('pergunta-anterior');
    perguntaAnteriorBtn.addEventListener('click', () => {
        if (perguntaAtual > 0) {
            perguntaAtual--;
        }
        mostrarPerguntaAtual();
    });

    function marcarRespostas() {
        document.querySelectorAll('.pergunta').forEach(function (pergunta) {
            pergunta.querySelectorAll('.resposta').forEach(function (resposta) {
                var checkbox = resposta.querySelector('input[type="checkbox"]');
                var respostaLabel = resposta.querySelector('.resposta-label');

                resposta.classList.remove('resposta-correta', 'resposta-incorreta');

                if (checkbox.getAttribute('data-correta') === 'true') {
                    resposta.classList.add('resposta-correta');
                } else {
                    resposta.classList.add('resposta-incorreta');
                }
            });
        });
    }

    btnMarcarRespostas.addEventListener('click', function () {
        marcarRespostas();
    });

    // UPDATE PAGINA AO CLICAR NA IMAGEM DO ALIEN
    const futureImage = document.getElementById('future');
    futureImage.addEventListener('click', () => {
        updatePageFuture();
    });

    function updatePageFuture() {
        window.location.reload();
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