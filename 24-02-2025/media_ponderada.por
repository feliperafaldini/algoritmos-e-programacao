programa {
  funcao inicio() {
    real prova1, atividade1, atividade2, desafio, atividade3, atividade4, n1, n2, media
		cadeia nome
	
		escreva("******* Média ponderada ******")
		escreva("\nInsira o nome do aluno: ")
		leia(nome)
	
		escreva("Insira a nota da Prova avaliativa individual: ")
		leia(prova1)
	
		escreva("Insira a nota da primeira atividade: ")
		leia(atividade1)
	
		escreva("Insira a nota da segunda atividade: ")
		leia(atividade2)
	
		escreva("Insira a nota do desafio em grupo: ")
		leia(desafio)
	
		escreva("Insira a nota da terceira atividade: ")
		leia(atividade3)
	
		escreva("Insira a nota da quarta atividade: ")
		leia(atividade4)
	
		n1 = ((prova1 * 0.6) + (atividade1 * 0.2) + (atividade2 * 0.2))
		n2 = ((desafio * 0.6) + (atividade3 * 0.2) + (atividade4 * 0.2))
		
		n1 = n1 * 0.4
		n2 = n2 * 0.6
	
		media = n1 + n2
	
		escreva("A média do aluno ", nome, " foi de ", media)
  }
}
