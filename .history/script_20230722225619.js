/* script.js */
let micAberto = false;
let timeoutId;

function toggleMicrofone() {
    if (micAberto) {
        fecharMicrofone();
    } else {
        abrirMicrofone();
    }
}

function abrirMicrofone() {
    micAberto = true;
    document.getElementById('abrir_microfone_button').innerText = 'Fechar Microfone';

    fetch('/abrir_microfone_callback', { method: 'POST' })
    .then(response => response.text())
    .then(data => {
        document.getElementById("texto_falado").innerText = "Texto falado: " + data;
        clearTimeout(timeoutId); // Reseta o temporizador se uma resposta válida for recebida.
        timeoutId = setTimeout(fecharMicrofone, 120000); // 120000 ms = 2 minutos.
    })
    .catch(error => {
        console.log(error);
        clearTimeout(timeoutId); // Reseta o temporizador em caso de erro.
        timeoutId = setTimeout(fecharMicrofone, 120000); // 120000 ms = 2 minutos.
    });
}

function fecharMicrofone() {
    micAberto = false;
    document.getElementById('abrir_microfone_button').innerText = 'Abrir Microfone';

    // Adicione aqui a lógica para parar o reconhecimento de fala (se necessário).
}
