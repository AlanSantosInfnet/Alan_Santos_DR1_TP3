

nome_vencedor = ''
nota_vencedor = 0.0

def imprimir():
    print(f'O(a) vencedor(a) foi {nome_vencedor} com nota {nota_vencedor}!')


for contador in range(1,6):
    nome = input(f'Informe o nome do {contador}º participante: ')
    nota = float(input(f'Informe a nota do {contador}° participante: '))

    if nota >= 0 and nota <= 10:
        if nota > nota_vencedor:
            nome_vencedor = nome
            nota_vencedor = nota
    else:
        print('Nota Invalida!!!')

imprimir()

