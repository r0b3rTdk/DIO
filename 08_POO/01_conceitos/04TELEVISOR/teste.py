from funcionalidades import *

# 1. CRIAR A TV
# Criamos o objeto 'tv' independente. Ele existe sozinho no mundo.
tv = Televisor('SONY', 'SONY-123')

# 2. CRIAR O CONTROLE E CONECTAR
# Aqui passamos a variável 'tv' (que é o objeto SONY) para dentro do controle.
# Agora o 'controle' sabe quem ele deve comandar.
controle = ControleRemoto(tv)

# 3. USANDO O CONTROLE
# Você chama o método do controle -> O controle chama o método da TV -> A TV muda a lista.
controle.sintonizaCanal('SBT')
# Você chama o controle -> O controle avisa a TV -> A TV muda o canal atual.
controle.trocaCanal('SBT')

# 4. VERIFICANDO O RESULTADO NA TV
# Acessamos diretamente a TV para ver se o controle funcionou.
print(tv.canal_atual)