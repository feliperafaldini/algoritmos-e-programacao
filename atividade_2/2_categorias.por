programa {
  funcao inicio() {
    cadeia nome
    inteiro idade

    escreva("Insira o nome do nadador: ")
    leia(nome)

    escreva("Insira a idade do nadador ", nome, ": ")
    leia(idade)

    se (idade >= 5 e idade <= 7) {
      escreva("O nadador ", nome, " está na categoria Infantil A")
    } senao se (idade > 7 e idade <= 10) {
      escreva("O nadador ", nome, " está na categoria Infantil B")
    } senao se (idade > 11 e idade <= 13) {
      escreva("O nadador ", nome, " está na categoria Juvenil A")
    } senao se (idade > 13 e idade <= 17) {
      escreva("O nadador ", nome, " está na categoria Juvenil B")
    } senao  se (idade > 17){
      escreva("O nadador ", nome, " está na categoria Sênior")
    }
  }
}
