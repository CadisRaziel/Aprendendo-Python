#==================================== CONCATENANDO VARIAVIES ==================================================
#Tipos de dados
# string = "Vitor" (texto)
# inteiro = 10 (pode ser positivos, negativos ou 0)
# float = 1.90 (pode ser positivos, negativos ou 0.0)
# bool = False (False ou True)

nome = 'Vitor' 
idade = 28
gosto_de = 'Programação'


#para utilizar concatenação utilizamos dessa forma, colocamos um 'f' antes de tudo e utilizamos {} 
print(f"Meu é {nome}")
print(f"Eu gosto de {gosto_de}")
print(f"Eu tenho {idade} anos")

#ATENÇÃO, EU POSSO REATRIBUIR A VARIVAVEL
#O PYTHON EXECUTA LINHA A LINHA OU SEJA, SE EU REATRIBUIR ALGO AQUI, A PROXIMA LINHA QUE TIVER ISSO VAI SER EXECUTADA COM 
#O VALOR ATRIBUIDO AQUI
idade = 5

print(f"{nome} gosta de {gosto_de} e tem {idade} anos")

#==============================================================================================================