programa {
  funcao inicio() {
    inteiro pequena, media, grande, valorPequena, valorMedia, valorGrande, valorTotal
    escreva("****** Calculo camisetas ******")
    escreva("Insira a quantidade de camisetas pequenas: ")
    leia(pequena)
    escreva("Insira a quantidade de camisetas medias: ")
    leia(media)
    escreva("Insira a quantidade de camisetas grandes: ")
    leia(grande)
    valorPequena = pequena * 10
    valorMedia = media * 12
    valorGrande = grande * 15
    valorTotal = valorPequena + valorMedia + valorGrande
    escreva("\nForam computadas ", pequena, " camisetas pequenas totalizando R$", valorPequena, ", ", media, " camisetas médias totalizando R$", valorMedia, " e ", grande, " camisetas grandes totalizando R$",valorGrande)
    escreva("\n\nValor total: R$", valorTotal)
  }
}
