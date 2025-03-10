programa {
  funcao inicio() {
    real salario, inss, imposto_renda, sindicato

    escreva("Insira o salário do funcionário: ")
    leia(salario)

    inss = salario * 0.08
    imposto_renda = salario * 0.11
    sindicato = salario * 0.05

    salario = salario - inss - imposto_renda - sindicato

    escreva("\nO salário do funcionário foi de R$ ", salario, "\nINSS R$ ", inss, "\nImposto de Renda R$ ", imposto_renda, "\nSindicato R$ ", sindicato)
  }
}
