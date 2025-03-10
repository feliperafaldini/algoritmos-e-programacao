programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    real x1, x2, y1, y2, distancia

    escreva("Insira o x do ponto 1: ")
    leia(x1)

    escreva("Insira o y do ponto 1: ")
    leia(y1)

    escreva("Insira o x do ponto 2: ")
    leia(x2)

    escreva("Insira o y do ponto 2: ")
    leia(y2)

    distancia = mat.raiz(mat.potencia(x2-x1, 2) + mat.potencia(y2-y1, 2), 2)

    escreva("A distância entre os pontos é de: ", distancia)
  }
}
