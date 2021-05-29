'''nome = str(input('seu nome? '))
if nome == 'gustavo':
    print('nome de viado')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Nome de pobre')
elif nome in 'Ana da Silva Puta':
    print('nome de vadia')
else:
    print('seu nome é normal')
print('tenha bom dia, {}'.format(nome))'''

'''def fatorial_for(numero):
    resultado = 1

    for i in range(1, numero +1):
        resultado = resultado * i
    return resultado
print(fatorial_for(5))'''

'''valor = int(input('Quanto custa a casa nova ?  '))
salario = int(input('Quanto voce ganha? '))
anos = valor / salario
print(anos)

if anos >= float(anos*0.3):
    print('Vc não pode pagar')
else: 
    print('grana liberada')'''


'''n = int(input('insira um número aqui para converter: '))

print('Escolha a base para conversão 1- binário 2- octal 3- hexa')
op = int(input('qual a base? '))

if op == int(1):
    print(bin(n))
elif op == 2:
    print(oct(n))
elif op == 3:
    print(hex(n))

print('terminei. ')'''


'''n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

if n1 > n2:
    print('o primeiro foi maior')
elif n2 > n1: 
    print('O segundo foi maior ')
elif n2 == n1:
    print('são iguais')'''

'''
from datetime import date

atual = date.today().year
nasc  = int(input('Ano que vc nasceu: '))
idade = atual - nasc

print('Quem nasceu em {} e tem {} anos em {}. '.format(nasc, idade, atual))

if idade == 18:
    print('se aliste agora ')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(saldo))
    print("Seu alistamento será em {}".format(ano))
    
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('voce deveria ter se alistado há {} anos'.format(saldo))
    print('seu alistamento foi em {}'.format(ano)) '''

'''nota = float(input('Qual a sua nota no mês passado? '))
nota2 = float(input('Qual a sua nota no mês atual? '))
med = float((nota+nota2)/2)

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota, nota2, med))

if med >= 5.0 and med <7: 
    print('RECUPERAÇÃO')
elif med < 5:
    print('REPROVADO')
elif med >= 7.0:
    print('aprovado') '''

#exercício 40

'''
from datetime import date
atual = date.today().year
age = int(input(' Qual o ano que você nasceu? '))
idade = atual - age
print('O atleta tem {} anos.'.format(idade))

if age <= 9:
    print('Classe Mirim')
elif idade <=14:
    print('classe Infantil')
elif idade <=19:
    print('classe Junior')
elif idade <=25: 
    print('Clasee Sênior')
else:
    print('Classe Master')

'''

#42
'''
r1 = float(input('Primeiro segmendo do lado '))
r2 = float(input('Segundo segmento do lado '))
r3 = float(input('Terceiro segimento do lado '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1 == r2 and r2 == r3: 
        print('Equilátero')
    elif  r1 != r2 != r3 and r1!=r3:
        print('Escaleno') 
    else: 
        print('Isósceles')

else: 
    print('Os segmentos acima não podem formar um triângulo ')'''

#43

#IMC = peso / altura x altura
'''
peso = float(input('Insira o seu peso pelado (kg) '))
alt = float(input('Insira a porra da sua altura seu gordo '))
imc = float(peso / alt**2)
ideal = (alt**2 * 25) 
print('seu IMC é: {}'.format(round(imc, 4)))
print('seu peso ideal {:.1f}'.format(round(ideal, 3)))


if imc < float(18.5):
    print('Abaixo do peso, porra')
elif imc >= 18.5 and imc<= 25: 
    print('peso ideal cara!')
elif imc >=25 and imc<=30:
        print("sobrepeso porra")    
elif imc <=30 and imc<=40:
        print('obesidade porra! seu viado')
elif imc >= 40:
        print('mórbido, emgrace seu filha da puta')'''

#44

preco = float(input(' Qual é o preço do produto, seu canalha? '))
preco2 = int(input('digite a forma de pagamento para:\n1 - grana/cheque \n2 - cartão à vista \n3- cartão em 2x \n4 - cartão em 3x \n Qual a sua opção, seu fudido? '))
if preco2 == 1:
    print(float(preco -(preco*0.1)))
elif preco2 == 2:
    print(float(preco- (preco*0.05)))
elif preco2 == 3:
    print(float(preco))
elif preco2 == 4:
    print(float(preco + (preco*0.2)))

#print('a sua compra de R${:.2f} vai custar R${:.2f} no final, valeu?  '.format(float(preco,total)))





















