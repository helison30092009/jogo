print("********************")
print("bem vindo ao jogo de adivinhação")
print("*********************")
numero_secret = 2008
total_de_tentativas = 3
rodada = 1
while (rodada <= total_de_tentativas):
print("tentativas {} de {}".format(rodada, total_de_tentativas))

chute_str = input("digite seu números:")
print("Você digitou",chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < nmero secreto

IF (numero_secreto == chute):
print ("voce acertou")

else :
if(maior):  
print("seu chute é maior que o numero secreto")
elif(menor):
print("seu chute é maior que o numero secreto")

rodada = rodada + 1

print("fim de jogo")