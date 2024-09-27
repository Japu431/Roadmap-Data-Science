# resposta="SIM"
# while resposta=="SIM":
#     nivel=input("Digite o nível de acesso: ").upper()
#     if nivel=="ADM" or nivel=="USR":
#         genero=input("Digite o seu gênero: ").upper()
#         if nivel=="ADM":
#             if genero=="FEMININO":
#                 print("Olá administradora")
#             else:
#                 print("Olá administrador")
#         else:
#             if genero=="FEMININO":
#                 print("Olá usuária")
#             else:
#                 print("Olá usuario")
#     elif nivel=="GUEST":
#         print("Olá visitante")
#     else:
#         print("Olá desconhecido(a)")
#     resposta=input("Digite SIM para continuar: ").upper()



# For

# for numero in range(1,int(input("Digite um numero para determinar o fim: ")),1):
#     print ("	" + str(numero))    



# tabuada=int(input("Digite um número para exibir a tabuada: "))
# print("Tabuada do número ", tabuada)
# for valor in range(1,11,1):
#     print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))