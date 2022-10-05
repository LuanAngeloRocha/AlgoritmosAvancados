from rich import print 
from rich import print 

n_col = 20
n_lin = 20

n_colunas_usuario = int(input("Qual a quantidade de colunas desejada ?"))
n_linhas_usuario = int(input("Qual a quantidade de linhas desejadas  ?"))

preco_acento = 100
total = 0
matriz = []
matriz_usu=[]



for i in range (n_lin):
    matriz_fileira = []
    for y in range (n_col):
        matriz_fileira.append("i")
    matriz.append(matriz_fileira)

for y in range (n_colunas_usuario):
    for z in range(n_linhas_usuario):
        matriz[y][z] = "d"
print(matriz)

while True:
    linha_acento= int(input("Qual a linha do acento que voce deseja ?-->"))-1
    coluna_acento= int(input("Qual a coluna do acento que voce deseja?-->"))-1

    if linha_acento > n_linhas_usuario or coluna_acento > n_colunas_usuario:
        input("ERRO ")
    else:

    
        if matriz [linha_acento][coluna_acento] == "d":
            
            cond= input("Esta cadeira está LIBERADA, deseja reservar ou comprar? :")
            if cond == "comprar":
                total += preco_acento
                matriz[linha_acento][coluna_acento]= "V"
            elif cond== "alugar":
                total += preco_acento * 0.3
                matriz[linha_acento][coluna_acento] = "R"
                sair = input("quer sair ? digite f")
            elif sair == "f":
                break
      
            
print[matriz]













