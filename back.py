import string, random
 
class Jogo:
    def __init__(self):
        self.listaDePalavras = ['comunicacao', 'email', 'informacao', 'custos', 'estimativa','controle', 'tempo', 'entregar', 'cronograma']

    def gerarLetras(self):
        listaLetras = []
        for i in range(552):
            listaLetras.append(random.choice(string.ascii_letters).lower())
        return listaLetras

    def gerarMatriz(self):
        gera = self.gerarLetras()
        return gera + self.listaDePalavras
        

    def embaralhaMatriz(self):
        lista_embaralhada = self.gerarMatriz()
        random.shuffle(lista_embaralhada)
        return lista_embaralhada
        
    def splitaLista(self):
        listaOriginal = self.embaralhaMatriz()
        contador = 0
        for i in listaOriginal:
            contador += 1
            if (len(i) > 1):
                for j in i:
                    listaOriginal.insert(contador, j)

        novaLista = list(reversed(listaOriginal))
        for k in novaLista:
            if len(k) > 1:
                novaLista.remove(k)
        print(len(novaLista))
        return novaLista

    




j = Jogo()
listaSemAspas = '[%s]' % ' '.join(map(str, j.splitaLista()))
print(listaSemAspas)
