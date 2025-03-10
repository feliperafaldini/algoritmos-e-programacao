programa {
  funcao inicio() {
    real reais, dolar, euro, libras

    escreva("Insira a quantidade de reais (. para casa decimal): ")
    leia(reais)

    dolar = reais * 0.2
    euro = reais * 0.18
    libras = reais * 0.15

    escreva("R$ ", reais, "\nDolar: ", dolar, "\nEuro: ", euro, "\nLibras: ", libras)
  }
}
