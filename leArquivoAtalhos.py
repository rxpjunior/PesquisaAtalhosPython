nomeArquivo='ASPIRE.txt' #Variavel com o nome do arquivo txt
parametroPesquisa='Shortcut Filename :' #Pequisar linhas que contenham este parametro

arquivo = open(nomeArquivo,'r') 
resultado = open('resultado.txt','a')

vetTemp=[]
vetResultado=[]

for x in arquivo: #Carregando em vetTemp apenas as linhas com parametro de pesquisa
    if parametroPesquisa in x:
        vetTemp.append(x)

#Salvando os resultados no arquivo
resultado.write('Computador: '+nomeArquivo+'\n')
for y in vetTemp:
    if 'rxpjunior' in y:
        resultado.write(y)
resultado.write('\n\n\n')

arquivo.close()
resultado.close()
        
