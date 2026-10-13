let nome = document.getElementById("nome")
let botao = document.getElementById("botao")
let resultado = document.getElementById("resultado")

botao.addEventListener("click", function() {
    resultado.textContent = "Olá, " + nome.value + "!"
})