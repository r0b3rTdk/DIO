import pytest
'''
1. Copie a sua função multiplicar_positivos_por_dez(lista) para o novo arquivo.
'''
def multiplicar_positivos_por_dez(lista):
    resultado = [numero * 10 for numero in lista if numero > 0]
    return resultado
'''
2. Crie uma nova função chamada test_multiplicar_positivos_por_dez() (o prefixo test_ é obrigatório).
3. Dentro dessa função de teste, não use print(). Em vez disso, chame a sua função passando a lista [1, -2, 3] e 
use o comando assert para garantir que o retorno seja exatamente igual a .
4. Na linha seguinte, adicione mais um assert para verificar se passar uma lista vazia [] 
retorna corretamente uma lista vazia [].
'''
def test_multiplicar_positivos_por_dez():
    lista = [1, -2, 3] 
    assert multiplicar_positivos_por_dez(lista) == [10, 30]
    assert multiplicar_positivos_por_dez([]) == []
'''
5. (Apenas para rodar localmente, caso queira testar: no terminal, você digitaria pytest 12_testes_pytest.py. 
Mas no código a me enviar, basta a estrutura das duas funções).
'''