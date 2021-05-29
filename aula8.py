#import math
#num = float(input("Digite um número separado por um ponto: "))
#print('O número {} tem a parte inteira {}'.format(num, math.floor(num)))

#import math
#n1 = int(input('Calcular a hipotenusa, digite o cateto oposto'))
#n2 = int(input('digite o cateto adjacente'))
#res = math.pow(n1, 2) + math.pow(n2, 2)
#print('a hipotenusa desse triângulo é {}'.format(res))


#n3 = int(input('Digite um ângulo e obtenha: '))
#print("o seno desse angulo é {}".format(math.sin(n3)))
#print("o coseno desse ângulo é {}".format(math.cos(n3)))
#print('a tangente desse ângulo é {}'.format(math.tan(n3)))

import random
#n4 = input('quem vai apagar o quadro? Aluno 1, digite seu nome ')
#n5 = input('aluno 2, digite o seu nome ')
#n6 = input('aluno 3, digite o seu nome aqui ')
#lista = [n4, n5, n6]
#n7 = random.choice(lista)  #sorteio
#print('o escolhido é o {}'.format(n7))

#n8 = input('digite o nome do grupo 1 ')
#n9 = input('digite o nome do grupo 2 ')
#n10 = input('digite o nome do grupo3 ')
#lista2 = [n8, n9, n10]
#n11 = random.sample(lista2, 3)
#print('a ordem da apresentação será: {}'.format(n11))

#with open('pi.txt') as file_object:
#    contents = file_object.read()
#    print(contents)

from playsound import playsound
playsound('test.mp3')
