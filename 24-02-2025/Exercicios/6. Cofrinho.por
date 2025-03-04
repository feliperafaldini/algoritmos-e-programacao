programa {
  funcao inicio() {
    inteiro moedas[6]
    inteiro quantidadeMoedas[6]
    real valorTotal

    moedas[0] = 1
    moedas[1] = 5
    moedas[2] = 10
    moedas[3] = 25
    moedas[4] = 50
    moedas[5] = 100

    valorTotal = 0

    inteiro i 

    para (i = 0; i < 6; i++)
    se (i < 5)
    {
      escreva("Insira a quantidade de moedas de ", moedas[i], " centavos: ")
      leia(quantidadeMoedas[i])
      valorTotal = valorTotal + (moedas[i] * quantidadeMoedas[i])
    }
    senao {
      escreva("Insira a quantidade de moedas de ", moedas[i], " reais: ")
      leia(quantidadeMoedas[i])
      valorTotal = valorTotal + (moedas[i] * quantidadeMoedas[i])
    }

    valorTotal = valorTotal / 100
    escreva("O valor total no cofre é de R$ ", valorTotal)
  }
}
