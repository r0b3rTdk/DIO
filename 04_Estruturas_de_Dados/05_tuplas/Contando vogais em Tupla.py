listagem = (
    'sao paulo', 'lucas moura', 'messi',
    'angelina', 'matue', 'calleri',
    'programador', 'futuro', 'sorte'
)
for p in listagem:
    print(f"\nna palavra {p.upper()} temos: ", end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')    