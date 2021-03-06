# ==================================== TRABALHANDO COM STRING ==================================================

minha_string = "qualquer texTo"

# deixando todo o texto em maiusculo
print(minha_string.upper())

# deixando todo o texto em minusculo
print(minha_string.lower())

# deixando a primeira letra maiuscula
print(minha_string.capitalize())

# verifica se o texto é maiusculo ou não (retorna um booleano)
print(minha_string.isupper())

# verifica se o texto é minusculo ou não (retorna um booleano)
print(minha_string.islower())

# remove espaços na frente ou antes do texto (muito util ao captar dados de usuarios)
print(minha_string.strip())

# substitui uma palavra ou um texto ou uma letra só por outra (cuidado aqui é case sensitive)
print(minha_string.replace("qualquer", "meu"))
# print(minha_string.replace("u", "U", 1)) # vai deixar maiusculo apenas o PRIMEIRO u que encontrar pois colcoamos o numero 1

# conta quantas letras tem a frase ou algo semelhante
print(len(minha_string))

# pegando letra por indice
print(minha_string[0])

# pra pega qual indice que ela começa e qual termina
print(minha_string[0:5])

# descobrindo qual é o indice de qual palavra, ou caracter, ou numero
print(minha_string.index("u"))

# pesquisando se a palavra exite ou não no texto (vai retornar um booleando)
x = "texto" in minha_string
print(x)

# colocando um texto em multiplas linhas (vai realizar quebra de linha)
multiplas_linhas = """ Olá 
esse é um texto
com varias linhas
e não vai dar erro
"""

# colocando um texto em multiplas linhas (vai realizar quebra de linha)  "\n"
multiplas_linhas2 = "linha1, \nlinha2,\nlinha3" 
print(multiplas_linhas2)

# escrevendo caracteres privados no texto
string = "adiciona entre \" aspas \" o texto "
print(string)