programa {
  funcao inicio() {
    real hora_normal, hora_extra, bruto, liquido
    
    escreva("Insira a quantidade de horas trabalhadas: ")
    leia(hora_normal)

    escreva("Insira a quantidade de horas extras trabalhadas: ")
    leia(hora_extra)

    bruto = (hora_normal * 10) + (hora_extra * 15)
    liquido = bruto * 0.9

    escreva("Salário bruto: R$ ", bruto, "\nSalário líquido: R$ ", liquido)
  }
}
