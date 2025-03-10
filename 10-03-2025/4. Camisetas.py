pequena = int(input("Insira a quantidade de camisetas pequenas: "))
media = int(input("Insira a quantidade de camisetas médias: "))
grande = int(input("Insira a quantidade de camisetas grandes: "))

valor_pequena = pequena * 10
valor_media = media * 12
valor_grande = grande * 15

valor_total = valor_pequena + valor_media + valor_grande

print(
    f"{pequena} camisetas pequenas.\n{media} camisetas médias.\n{grande} camisetas grandes."
)
print(f"\nValor total: {valor_total}")
