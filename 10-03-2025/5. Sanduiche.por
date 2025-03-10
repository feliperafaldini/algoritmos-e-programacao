programa {
  funcao inicio() {
    inteiro sanduiches, queijos, presuntos, hamburguers

    escreva("Insira a quantidade de sanduiches: ")
    leia(sanduiches)

    queijos = sanduiches * 2 * 50
    presuntos = sanduiches * 1 * 50
    hamburguers = sanduiches * 1 * 100

    escreva("Será necessário a compra de:\n", queijos, " gramas de queijo. \n", presuntos, " gramas de presunto. \n", hamburguers, " gramas de hamburguer. ")
  }
}
