programa {
  funcao inicio() {
    real num1, num2, resultado
    escreva("Insira o primeiro número: ")
    leia(num1)
    escreva("Insira o segundo número: ")
    leia(num2)

    se (num1 == num2) {
      resultado = num1 + num2
      escreva("O resultado de ", num1, " + ", num2, " foi ", resultado)
    } senao {
      resultado = num1 * num2
      escreva("O resultado de ", num1, " * ", num2, " foi ", resultado)
    }
  }
}
