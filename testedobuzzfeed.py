print('QUAL O SEU TIPO DE PERSONALIDADE')
a = int(input('Qual voce prefere:\n1)Inverno\n2)Verão\n'))
b = int(input('O que voce é mais:\n1)Emocional\n2)Racional\n'))
c = int(input('Qual voce prefere:\n1)Dia\n2)Noite\n'))
d = int(input('Qual voce prefere:\n1)Balada\n2)Netflix\n'))
e = int(input('Com o que voce se identifica:\n1)Extrovertido\n2)Introvertido\n'))
f = int(input('Quem voce era/é na escola:\n1)Nerd\n2)Do fundão\n'))
g = int(input('Voce prefere:\n1)Refrigerante\n2)Suco\n3)Agua\n'))

if a==1 and b==1 and c==2 and d==2 and e==2 and f==1: 
    print('Voce tem a personalidade caseira.\n \nVoce é uma pessoa muito fechada e isolada, não gosta de aglomerações.')
elif a==2 and b==2 and c==1 and d==1 and e==1 and f==2:
    print('Voce tem a personalida festeira.\n \nVoce é uma pessoa aberta a novos relacionamentos e ama estar com seus amigos onde quer que eles estejam')
else: 
    print('Voce é normal!\n \nSem extremos para voce, sua personalidade é balanceada e de facil convivencia')

