document.addEventListener("DOMContentLoaded", () => {
    const faixas = document.querySelectorAll(".faixa");

    // Sincronizar animação para as duas faixas
    faixas.forEach((faixa, index) => {
        faixa.style.animationDelay = `${index * 5}s`; // Diferencia o tempo de início
    });
});
