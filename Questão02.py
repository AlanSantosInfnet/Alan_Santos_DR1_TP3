def verificacaoIdade():
    if (idade >= 18) and (idade < 70):
        print('Tem Obrigação de Votar.')

    elif (idade >= 16) and (idade < 18):
        print('Não Tem Obrigação de Votar.')

    elif (idade >= 70):
        print('Não Tem Obrigação de Votar.')

    else:
        print('Não Tem Direito de Voto.')


def excecao():
    if idade > 0:
        verificacaoIdade()

    else:
        print("Idade tem que ser Maior que '0'")


idade = int(input('Informe a Idade: '))

excecao()


