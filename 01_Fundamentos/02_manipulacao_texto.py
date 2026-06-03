frase = ' Robert Emanuel Luna de Araujo '
print(frase[1:15:2]) #do caractere 1 ao 15 pulando de 2 em 2
print(frase[::2]) #do comeco ao final pulando de 2 em 2
print(frase.count('r')) #conta quantos r tem na frase
print(frase.upper().count('R')) #deixa a frase em maiusculo e conta quantos R tem na frase
print(frase.lower())  #Converte todos os caracteres da string para minúsculo.
print(len(frase)) #saber o tamanho da frase
print(len(frase.strip())) #saber o tamanho da frase sem os espacos do comeco e do final
print(frase.replace('Emanuel', 'E')) #fazer troca de palavra
print(frase.find('Luna')) #mostra quando comeca o Luna
print(frase.split()) #dividiu a frase criando listas
dividir_frase = frase.split()
print(dividir_frase[0][0:3]) #dividi e mostrei so os caracteres 0 e 3, Rob
print(frase.capitalize())  #Converte o primeiro caractere da string para maiúsculo e o restante para minúsculo.
print(frase.title())  #Converte o primeiro caractere de cada palavra para maiúsculo.
print('-'.join(dividir_frase)) #Junta os elementos de uma lista em uma string, usando um separador.