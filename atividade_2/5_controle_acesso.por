programa {
  funcao inicio() {
    inteiro idade, socio

    escreva("Insira a idade: ")
    leia(idade)

    escreva("É sócio?\n(1) - SIM\n(2) - NÃO\n")
    leia(socio)

    se ((idade < 18 e socio ==1) ou (idade >= 18 e idade < 65) ou (idade >= 65 e socio == 1)) {
      escreva("Acesso permitido")
    } senao {
      escreva("Acesso negado")
    }
    }
  }
}
