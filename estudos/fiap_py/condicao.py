# IF ELSE in Python

# nome=input("Digite o nome: ")
# idade=int(input("Digite a idade: "))
# prioridade="NÃO"
# if idade>=65:
#     prioridade="SIM"
# print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)


# nome=input("Digite o nome: ")
# idade=int(input("Digite a idade: "))
# doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa?").upper()

# if idade>=65:
#     print("O paciente " + nome + " POSSUI atendimento prioritário!")
# elif doenca_infectocontagiosa=="SIM":
#     print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")
# else:
#     print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala comum!")



while True:
    print("\n\n")
    nome=input("Digite o nome: ")
    idade=int(input("Digite a idade: "))
    doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa? (SIM/NAO): ").upper()

    if idade >= 65 and doenca_infectocontagiosa == "SIM":
        print("Sala amarela com PRIORIDADE")
    elif idade < 65 and doenca_infectocontagiosa == "SIM":
        print("Sala Amarela NOT Prioridade")
    elif idade >= 65 and doenca_infectocontagiosa == "NAO":
        print("Sala Branca com PRIORIDADE")
    elif idade < 65 and doenca_infectocontagiosa == "NAO":
        print("Sala BRanca NOT prioridade")
    else:
        print("Responda apenas com SIM OU NAO!!!")

    validaContinue = input("Deseja continuar com o atendimento? (SIM/NAO): ").upper()
    if validaContinue == "NAO":
        print("\n\n")
        break
    


        
    
    



