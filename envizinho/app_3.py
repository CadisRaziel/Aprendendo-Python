nome = input("Digite seu nome: ")
#Repare que a idade é um inteiro, então precisamos converter para um inteiro
idade = int(input(f"Qual a sua idade {nome}? Digite: "))

nascimento = 2021 - idade

print(f"{nome} é: ")
print(f"Seu nome é {nome} e sua idade é {idade}")
print(f"{nome} você nasceu em: {nascimento}")


# calculadora
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
resultado = num1 + num2
print(f"O resultado é: {resultado}")
