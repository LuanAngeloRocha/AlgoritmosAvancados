from rich import print
import math

n_col = int(input("Qual a quantidade de colunas no teatro ?"))
n_lin = int(input("Qual a quantidade de linhas no teatro  ?"))
total =0
preco_acento = 100



matriz = []
matriz_usu=[]



for i in range (n_lin):
    matriz_fileira = []
    for y in range (n_col):
        matriz_fileira.append("D")
    matriz.append(matriz_fileira)



print(matriz)


print("==================================================================================")
while True:

    print("------------------------------------------------------------------------------------")
    print("O preço de cada cadeira é 100 reais")

    print("------------------------------------------------------------------------------------")

    print("Qual acento deseja: ")
    fileira= int(input("Qual a fileira do acento que voce deseja ?-->"))-1
    coluna= int(input("Qual a coluna do acento que voce deseja?-->"))-1

    if fileira > n_lin or coluna > n_col:
        print("------------------------------------------------------------------------------------")
        input("ERRO: Digite um valor que esteja dentro das diretrzes")
        print("------------------------------------------------------------------------------------")
    else:

    
        if matriz [fileira][coluna] == "D":
            cond= input("Esta cadeira está LIBERADA, deseja RESERVAR ou COMPRAR? :")
            if cond == "comprar":
                total += preco_acento
                matriz[fileira][coluna]= "V"
            elif cond== "reservar":
                total += preco_acento * 0.3
                matriz[fileira][coluna] = "R"

        elif matriz[fileira][coluna] == "V":
            print("Esta cadeira foi vendida, não é possivel reservar e nem comprar...")
        
        elif matriz[fileira][coluna] == "R":
            print("Esta cadeira está reservada!")
            print("Neste caso, voce pagará 70% do valor total da cadeira.")

            cond_2 = input("Deseja comprala? (s/n):  ")

            if cond_2 == "s":
                total += preco_acento * 0.7
                matriz[fileira][coluna] = "V"
            



            
    print(f"Sua carteira é igual a: {total}")

    print( "===========================================================================")
                

    sair = input("quer sair ? (s/n)")
    if sair == "s":
        cont = 0
        for x in range (n_lin):
            for y in range (n_col):
                if(matriz[x][y] !="L"):
                    cont +=1
            qtd_minima = math.floor(n_col * n_lin)/2+1
            if cont>= qtd_minima:
                   break  
            else:
                input("Você nao atingiu o numero minimo de poltronas, não é possvel encerrar agora")         














