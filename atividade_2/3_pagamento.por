programa {
  funcao inicio() {
    real valor, valor_parcela
    inteiro pagamento

    escreva("Insira o valor do produto: ")
    leia(valor)

    escreva("Insira o método de pagamento:\n(1) - Dinheiro ou Pix.\n(2) - À vista no Cartão de Crédito.\n(3) - Parcelado duas vezes.\n(4) - Parcelado três vezes.\n")
    leia(pagamento)

    se (pagamento == 1) {
      valor = valor - (valor * 0.1)
      escreva("Valor total: R$ ", valor)
    } senao se (pagamento == 2) {
      valor = valor - (valor * 0.15)
      escreva("Valor total: R$ ", valor)
    } senao se (pagamento == 3) {
      valor_parcela = valor / 2
      escreva("Valor total: R$ ", valor, "\nValor parcela: 2x R$", valor_parcela)
    } senao se (pagamento == 4) {
      valor = valor + (valor * 0.1)
      valor_parcela = valor / 3
      escreva("Valor total: R$ ", valor, "\nValor Parcela: 3x R$", valor_parcela)
    }
  }
}
