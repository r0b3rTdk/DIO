texto = input("Digite um texto: ")

if texto.isnumeric():
    print("O texto contém apenas números.")
elif texto.isalpha():
    print("O texto contém apenas letras.")
elif texto.isalnum():
    print("O texto contém apenas letras e números.")
elif texto.isspace():
    print("O texto contém apenas espaços em branco.")
elif texto.islower():
    print("O texto contém apenas letras minúsculas.")
elif texto.isupper():
    print("O texto contém apenas letras maiúsculas.")
else:
    print("O texto contém uma mistura de caracteres.")