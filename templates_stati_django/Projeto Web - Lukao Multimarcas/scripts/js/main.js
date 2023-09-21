
//Pagamento

const cartao = document.querySelector('#pagamentoCartao')
const boleto = document.querySelector('#pagamentoBoleto')
const cartaoBtn = document.querySelector('#cartaoBtn')
const boletoBtn = document.querySelector('#boletoBtn')

function metodoCartao() {
    console.log("entrou")
    cartao.style.display = "block"
    boleto.style.display = "none"

    cartaoBtn.style.filter = "opacity(100%)"
    boletoBtn.style.filter = "opacity(60%)"
}

function metodoBoleto() {
    boleto.style.display = "block"
    cartao.style.display = "none"

    boletoBtn.style.filter = "opacity(100%)"
    cartaoBtn.style.filter = "opacity(60%)"
}