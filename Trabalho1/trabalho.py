'''
                Trabalho Modelos Lineares
                Alunos: Gustavo de Souza Curty
                        Victor Hugo Almeida Rodrigues e Souza
'''

import matplotlib.pyplot as fig
import pandas as leitor
import numpy as np

dados = leitor.read_csv('covid.csv', sep=",")

dadosusados =leitor.DataFrame(dados,columns=['Deaths'])
dadosusados1 =leitor.DataFrame(dados,columns=['Confirmed'])
quantidade = len(dadosusados)

x =[0]*quantidade
y =[0]*quantidade
e =[0]*quantidade

xsoma = 0
ysoma = 0

for cont in range(quantidade):
    x[cont] = float(dadosusados.loc[cont])
    y[cont] = float(dadosusados1.loc[cont])
    xsoma = float (xsoma + x[cont])
    ysoma = float (ysoma + y[cont])


xmed = float(xsoma / quantidade)
ymed = float(ysoma / quantidade)

sxy = 0
syy = 0
sxx = 0
sqreg = 0
sqe = 0

for cont1 in range(quantidade):
    somx = float (x[cont1] - xmed)
    somy = float (y[cont1] - ymed)
    
    sxy = float (somx*somy + sxy)
    sxx = float (somx**2 + sxx)
    syy = float (somy**2 + syy)

correlacao = float(sxy / (pow(sxx*syy, 1/2)))
b = float(sxy / sxx)
a = float(ymed - (b*xmed))

for cont2 in range(quantidade):
    sqe = float (((y[cont2] - (a + (b*x[cont2])))**2 + sqe))
    sqreg = float ((a + (x[cont2]*b) - ymed)**2 + sqreg)
    
fo = float((sqreg)/((sqe)/(quantidade -2)))

X = np.arange(0,170000,0.1)
Y = []

print('\n')
print('Respostas do trabalho:')

'''a) O gráfico em relação aos valores de x:'''
fig.title('Gráfico em relação a X')
fig.ylabel('Confirmados[Y])')
fig.xlabel('Mortes[X]')
fig.hist(x, bins=40, ec = "k", rwidth = 0.7)
fig.show()

'''a) O gráfico em relação aos valores de y:'''
fig.title('Gráfico em relação a Y')
fig.ylabel('Confirmados[Y])')
fig.xlabel('Mortes[X]')
fig.hist(y, bins=40, ec = "k", rwidth = 0.7, alpha=0.7)
fig.show()
print('\n')
print('b) Feita a distribuição, foi possível enconrar pontos influentes, pontos que podem afetar uma reta de regressão de mínimos quadrados alterando o valor de y. ')

'''c) O gráfico da função:')'''
fig.title('Gráfico da função')
fig.ylabel('Confirmados[Y])')
fig.xlabel('Mortes[X]')
fig.plot(x,y,"o")
fig.show()

print('\n')
print('c) A partir do gráfico é possível identificar uma correlação se aproximando do 1.')
print('\n')
print('d) O coeficiente de correlação eh: %.3f' %correlacao )
print('O coeficiente de correlção se aproximando do 1 diz que a reta dos mínimos quadrados tende a crescer.')
print('\n')
print('e) A reta eh: Y = {} + {}X '.format(a, b))
print('  B1 = {}; B0 = {} e a variância = {}'.format(a, b, (syy/quantidade)))

for cont3 in range(len(X)):
    Y.append(a + b*X[cont3])

'''f) O gráfico xy ficará:'''
fig.title('Gráfico xy')
fig.ylabel('Confirmados[Y])')
fig.xlabel('Mortes[X]')
fig.plot(x,y,"o")
fig.plot(X,Y, color='orange')
fig.show()

print('\n')
print('g) Os resíduos são:')
for cont3 in range(quantidade):
    e[cont3] = float(y[cont3] - (a + (b*x[cont3])))     
    print('e{} = {}' .format((cont3 + 1), e[cont3]))  
print('\n')
print('i) Montando a tabela ANOVA:')
print('  FV     |    GL      |         SQ           |         QM        |  Fo')
print('Regressão|    1       |   {:.2f}  | {:.2f} | {:.2f}'.format((sqreg), (sqreg), fo))
print('Erro     |  {:.2f}    |   {:.2f}   | {:.2f}'.format((quantidade-2), (sqe), (sqe/(quantidade-2))))
print('Total    |  {:.2f}    |   {:.2f}'.format((quantidade-1), (ysoma**2)))
print('\n')
if (sqreg/(sqe/(quantidade - 2))) < 5.59:
    print('i) Rejeitamos H0!')
else:
    print('i) Rejeitamos h1!')    
''' j) Retirando os pontos influentes'''
fig.title('Gráfico xy(s/ pontos influentes)')
fig.ylabel('Confirmados[Y])')
fig.xlabel('Mortes[X]')
fig.xlim(0,175000)
fig.plot(x,y,"o")
fig.plot(X,Y, color='orange')
fig.show()