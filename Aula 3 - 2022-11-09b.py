# criação de funções

preco = 1999.90

# Calcular 5% de imposto, guardar na vaiavel imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma função calcular_imposto() que calcula 5% e retorna a quem pediu
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

#Aqui é o uso... aqui é imposto a calcular.. e exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(imposto)

#Explicação de variável local x global
print(preco) #??
preco_produto = 100
print(preco_produto) #??

#agora calcular imposto a alíquota agora é 7%

valores = [1.99, 24.50, 78.27, 1515.5]
# se eu quiser calcular o imposto destes quatro valores... e exibir na tela assim: "O imposto de .... é ...." (1o. preço, 2o. imposto)
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")

#Declarar um função calcula_imposto_aliquota que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão.

def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor)}")

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 7)}")

#E se agora o imposto for 10%?
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")
