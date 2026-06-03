# 1. Definição das variáveis
numero_inteiro = 420
numero_pi = 3.1415926535
numero_grande = 123456789.0

# 2. Utilização dos especificadores de formato (Máscaras de Sintaxe) com f-strings

print("--- Demonstração das Máscaras de Sintaxe em Python ---")

# 1. Ponto flutuante com 4 casas decimais (similar ao %.4f)
print(f"1 f: O valor de Pi com 4 casas decimais é: {numero_pi:.4f}")

# 2. Formato Octal (similar ao %o)
print(f"2 o: O inteiro 420 em Octal é: {numero_inteiro:o}")

# 3. Formato Hexadecimal em maiúsculas (similar ao %X)
print(f"3 h: O inteiro 420 em Hexadecimal é: {numero_inteiro:X}")

# 4. Notação científica em minúsculas (similar ao %e)
print(f"4 e: O número grande em Notação Científica é: {numero_grande:e}")

# 5. Formato com separador de milhar e 0 casas decimais (nova 'máscara' do Python)
print(f"5 ,: O número grande com separador de milhar é: {numero_grande:,.0f}")

# 6. Alinhamento à direita em um campo de 10 caracteres (similar ao %10d)
print(f"6 r: O inteiro 420 alinhado à direita: {numero_inteiro:>10d}")

print("-------------------------------------------------------")