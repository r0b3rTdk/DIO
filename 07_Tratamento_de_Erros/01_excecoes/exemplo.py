try:      #tente fazer isso
    a = int(input("numerador: "))
    b = int(input("denominador: "))
    r = a / b

# tipos de except
except (ValueError, TypeError): #se der errado faca isso
    print("tivemos um problema com os tipos de daods que vc digitou")
except ZeroDivisionError:
    print("nao e possivel dividir po zero")
except KeyboardInterrupt:
    print("o usuario nao digitou")
except Exception as erro:
    print(f"o erro encontrado foi {erro.__cause__}")
else:     #se der certo faca isso
    print(f"o resultado e {r:.1f}")
finally:  #aparece se der certo ou errado
    print("volte sempre, muito obrigado")