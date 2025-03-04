programa {
  funcao inicio() {
    inteiro dia, mes, dias_passados

    escreva("Insira o dia: ")
    leia(dia)

    escreva("Insira o mês (numeral): ")
    leia(mes)

    dias_passados = ((mes - 1) * 30) + dia

    escreva("Já se passaram ", dias_passados, " dias do ano.")
  }
}
