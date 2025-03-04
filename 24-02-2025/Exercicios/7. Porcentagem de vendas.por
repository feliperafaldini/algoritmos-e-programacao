programa {
  funcao inicio() {
    real fixo, vendas, total

    escreva("Insira o salário fixo do funcionário: ")
    leia(fixo)

    escreva("Insira o valor de vendas do funcionário: ")
    leia(vendas)

    total = fixo + (vendas * 0.04)

    escreva("O salário total do funcionário foi de R$ ", total)
  }
}
