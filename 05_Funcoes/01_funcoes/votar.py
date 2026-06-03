def votar(n):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - data
    if 18 < idade < 65:
        return "VOTO OBRIGATORIO"    
    elif 16<= idade < 18 or idade > 65:
        return "VOTO OPCIONAL"
    else:
        return "NAO VOTA" 

data = int(input("digite seu ano de nascimento: "))
print(votar(data))