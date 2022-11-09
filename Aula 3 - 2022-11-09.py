print("Início da aula 3 (09/11/2022)")

contador = 1

#exibir  de 1 até 10 sequencial
while(contador <= 10):
  print(contador)
  contador = contador+1 #vai somar 1 de contador = 1


# Laço for (python for = for each)
fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pêra"

#Lista
frutas = ["morango", "laranja", "pêra"]


#mostra todas
print(frutas)
#quero exibir apenas a 3a. fruta (pêra)
print(frutas[2])

#Exibir quantas frutas tem na minha lista?
print(len(frutas)) # length = tamanho

#quero incluir uma fruta nova
frutas.append("manga")

print(len(frutas)) # lenght = tamanho
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])

print("Exemplo das frutas com while")
frutas.append("uva")

i=0 # (i = index ou variavel de incremento)
while(i<4):
  print(frutas[i])
  i = i + 1

# mais certo seria 
#while(i<len(frutas) ):
  #print (frutas[i])
  #i=i+1
