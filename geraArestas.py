#IdTrabalho IdAutor Autor
#import sys print
nomeArquivo = input('Digite o arquivo de entrada, com "/": ')
#'entrada/AutoresComTrabalhos.csv'
arquivo = open(nomeArquivo,'r')
arquivoSaida = open('saida/arestas.csv','w')
texto = arquivo.readlines()
matriz = []
#iniciando variável matriz
for l in texto:
        matriz.append(l.split(";"))
print('tamanho da matriz')
print(len(matriz)-1)
print('ID-SOURCE-TARGET')
textoSaida = []
textoSaida.append("SOURCE;TARGET"+"\n")


for i in range(1 , len(matriz) -1 ):
    idAtual = matriz[i][0]
    autorOrigem = matriz[i][1]
    #print(matriz[i][1]+ ' - '+ matriz[i][2])
    j = i
    while (idAtual == matriz[j][0]):
        if (autorOrigem != matriz[j][1]):
            print(idAtual+ "-" +autorOrigem + "-" + matriz[j][1])
            textoSaida.append(autorOrigem + ";" + matriz[j][1]+"\n")
        j = j+1


arquivoSaida.writelines(textoSaida)    
#print(matriz)
arquivoSaida.close()
arquivo.close()
