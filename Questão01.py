
def calculoConsumoxPessoas():
        valor_total = valor_total_consumo + (valor_total_consumo * taxa_servico / 100)
        valor_pessoa = valor_total / numero_pessoas

        valor_total = str(valor_total)
        valor_pessoa = str(valor_pessoa)

        print('O valor total da conta, com a taxa de serviço, será de R$', valor_total.replace('.', ','))
        print('Dividindo a conta por ', numero_pessoas, ' por pessoa(as), cada pessoa deverá pagar R$',
          valor_pessoa.replace('.', ','))


valor_total_consumo = float(input('Informe o valor total do consumo: '))
numero_pessoas = int(input('Informe o total de pessoas: '))


if numero_pessoas > 0:
    taxa_servico = float(input('Informe o percentual do serviço, entre 0 e 100: '))
    if (taxa_servico >= 0) and (taxa_servico <= 100):
      calculoConsumoxPessoas()
    else:
        print('Taxa de serviço invalida, pois não esta entre 0 e 100')
else:
    print('O numero de Pessoas invalido!!!')

