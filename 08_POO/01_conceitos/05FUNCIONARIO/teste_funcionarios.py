from funcionario import Funcionario

# Criando o objeto com seus dados reais
funcionario = Funcionario('r0b3rT', 'r0b3rT@30praum.com')

# --- POPULANDO OS DADOS (Estado do Objeto) ---

# Janeiro: Trabalhou 300h ganhando 30/h
funcionario.cadastro_hora('Jan', 300)
funcionario.cadastro_hora('Fev', 200)

# Fevereiro: Trabalhou 200h ganhando 30/h
funcionario.cadastro_salario_hora('Jan', 30)
funcionario.cadastro_salario_hora('Fev', 30)

# --- VISUALIZANDO O OBJETO ---
# Aqui o Python chama o __repr__ automaticamente.
# Você verá os dicionários preenchidos: {'Jan': 300, 'Fev': 200}
print(funcionario)

# --- EXECUTANDO LÓGICA DE NEGÓCIO ---
# O método busca a chave 'Jan' nos dois dicionários e multiplica.
print(funcionario.calcula_salario('Jan'))

# O método busca a chave 'Fev' nos dois dicionários e multiplica.
print(funcionario.calcula_salario('Fev')) 