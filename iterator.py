# next e iter implementam o protocolo de iteração
# dados = qualquer coleção


class MeuIteravel:
    def __init__(self, dados) -> None:
        self.dados = dados

    def __iter__(self):
        return MeuIterator(self.dados)


class MeuIterator:
    def __init__(self, dados) -> None:
        self.dados = dados
        self.index = 0

    def __next__(self):
        try:
            data = self.dados[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return data


lista = ["Junior", "Tanise", "Adalberto"]
iteravel = MeuIteravel(lista)
for pessoa in iteravel:
    print(pessoa)
