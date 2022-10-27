# comando input(): quero permitir que
# o usuario digite algo...
nome = input("Digite seu nome: ")
# pede a idade para o usuário "Qual sua idade"
idade = int(input("Digite sua idade: "))
# int seria para usar numero inteiro

# comando de saida...exibir a tela
print(f"Boa noite, seu nome é {nome};")
#exiba "sua idade é...
print("sua idade é {};".format(idade))

#e se eu quiser mostra o DOBRO da idade informada?
dobro = idade * 2
print("o dobro da idade informada  é {}".format(dobro))
#Estrutura condicional - o famoso "SE" (if)
# se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if(idade >=18):
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("Quando completar 18 anos, você será considerado adulto")

#E se eu quisesse perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)
genero = input("Qual seu gênero M=Masculino, F=Feminino, O=Outros :")
if idade >=18 and genero == "M":
  print("...e você também  precisa/precisou prestar o serviço militar obrigatório")