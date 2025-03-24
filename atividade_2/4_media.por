programa {
  funcao inicio() {
    real prova1, peso1, prova2, peso2, prova3, peso3, media

    escreva("Insira a nota da prova 1: ")
    leia(prova1)

    escreva("Insira o peso da prova 1: ")
    leia(peso1)

    escreva("Insira a nota da prova 2: ")
    leia(prova2)

    escreva("Insira o peso da prova 2: ")
    leia(peso2)

    escreva("Insira a nota da prova 3: ")
    leia(prova3)

    escreva("Insira o peso da prova 3: ")
    leia(peso3)

    media = ((prova1 * peso1) + (prova2 * peso2) + (prova3 * peso3)) / (peso1 + peso2 + peso3)

    se (media >= 7) {
      escreva("Média: ", media, " Aprovado")
    } senao se (media >= 5 e media < 7) {
      escreva("Média: ", media, " Em recuperação")
    } senao se (media < 5) {
      escreva("Média: ", media, " Reprovado")
    }
  }
}
