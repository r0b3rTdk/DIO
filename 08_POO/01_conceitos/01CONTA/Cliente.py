class Cliente:
    def __init__(self, n, i):
        self._nome = n
        self._idade = i

    # metodo get
    def get_nome(self):
        return self._nome
    
    # metodo set
    def set_nome(self, nome):
        self._nome = nome