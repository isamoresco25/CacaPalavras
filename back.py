import string, random
 
class Jogo:
    def __init__(self):
        self.listaDePalavras = ['comunicacao', 'email', 'informacao', 'custos', 'estimativa','controle', 'tempo', 'entregar', 'cronograma']
        self.lista_copia_palavras = self.listaDePalavras.copy()

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
        return '[%s]' % ' '.join(map(str, novaLista))

    def validaInputs(self, resposta):
        if resposta in self.listaDePalavras:
            self.lista_copia_palavras.remove(resposta)
            return "Encontrou a palavra " + resposta
        else:
            return "Palavra não existe!!"
    
    def iniciar(self):
        print(self.splitaLista())
        while len(self.lista_copia_palavras) > 0:
            print(self.validaInputs(input('Digite a palavra encontrada!')))
        return "Fim de jogo!"