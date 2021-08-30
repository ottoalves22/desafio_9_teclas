class Grafo:
    def __init__(self):
        self.grafo = [[] for i in range(10)] # representacao do grafo como listas de listas que contem arestas sem pesos, range 10 para termos 0 a 9, 0 nao possuira arestas


    # adiciona em ambas listas a aresta com o outro vertice
    def adiciona_aresta(self, origem, destino):
        self.grafo[origem].append(destino)
        self.grafo[destino].append(origem)


    def busca_largura(self, origem, destino):
        fila = [] # armazenara vertices verificados
        visitados =[False for i in range(10)] # vertices verificados
        self.anterior = [0 for i in range(10)] # vertice anterior ao verificado
        self.distancia = [0 for i in range(10)] # distancia do no sendo testado

        for i in range(10):
            self.distancia[i] = 1000000
            self.anterior[i] = -1;

        visitados[origem] = True
        self.distancia[origem] = 0
        fila.append(origem)

        while (len(fila) != 0):
            aux = fila.pop(0)

            for i in range(len(self.grafo[aux])):
                if visitados[self.grafo[aux][i]] == False:
                    visitados[self.grafo[aux][i]] = True
                    self.distancia[self.grafo[aux][i]] = self.distancia[aux]+1
                    self.anterior[self.grafo[aux][i]] = aux
                    fila.append(self.grafo[aux][i])

                    if self.grafo[aux][i] == destino:
                        return True;

        return False


    def print_menor_distancia(self, origem, destino):
        # funcao que registra o caminho entre dois vertices caminhando por busca em largura
        if self.busca_largura(origem, destino) == False:
            print('vertices nao conectados')
        caminho = []
        aux = destino
        caminho.append(aux)

        while self.anterior[aux] != -1:
            caminho.append(self.anterior[aux])
            aux = self.anterior[aux]
        caminho.reverse()
        return caminho


    def percorrer_teclas(self, entrada: str):
        caminho_percorrido = []
        for j in range(len(entrada)-1):
            '''
            Cada vertice entrará duas vezes na busca, uma vez como destino e
            outra como origem, sendo a distancia da primeira tecla para a segunda e
            depois da segunda para a terceira, e assim paulatinamente
            '''
            caminho = grafo.print_menor_distancia(int(entrada[j]), int(entrada[j+1]))
            caminho_percorrido += caminho
        remove_duplicatas(caminho_percorrido) # remove vertices duplicados do caminho percorrido


# funcoes auxiliares
def remove_duplicatas(lista):
    resultado = []
    for i in lista:
        if i not in resultado:
            resultado.append(i)
    print(f'Lista de movimentos: {list(resultado)}')
    print(f'Total de movimentos: {len(resultado)}')


if __name__ == '__main__':
    grafo = Grafo()

    # adicionando arestas que possibilitarao os movimentos horizontais, verticais e diagonais
    grafo.adiciona_aresta(1, 2)
    grafo.adiciona_aresta(1, 4)
    grafo.adiciona_aresta(1, 5)
    grafo.adiciona_aresta(2, 3)
    grafo.adiciona_aresta(2, 4)
    grafo.adiciona_aresta(2, 5)
    grafo.adiciona_aresta(2, 6)
    grafo.adiciona_aresta(3, 5)
    grafo.adiciona_aresta(3, 6)
    grafo.adiciona_aresta(4, 5)
    grafo.adiciona_aresta(4, 7)
    grafo.adiciona_aresta(4, 8)
    grafo.adiciona_aresta(5, 6)
    grafo.adiciona_aresta(5, 7)
    grafo.adiciona_aresta(5, 8)
    grafo.adiciona_aresta(5, 9)
    grafo.adiciona_aresta(6, 8)
    grafo.adiciona_aresta(6, 9)
    grafo.adiciona_aresta(7, 8)
    grafo.adiciona_aresta(8, 9)

    entrada = '82397' # sequencia de teclas a serem digitadas

    print(f'Sequencia de entrada: {entrada}\n')

    grafo.percorrer_teclas(entrada)


    '''
    Dado um teclado numérico comum de 9 teclas sem o zero

    |1 2 3|

    |4 5 6|

    |7 8 9|

    e levando em consideração as possíveis movimentações: horizontal, vertical e diagonal em uma casa.

    Dado uma sequência de números S, você deverá desenvolver um algoritmo que encontre o menor número de movimentos possível para percorrer todos esses números (em sequência).



    Exemplo:

    Dado como entrada S = 82397, temos como resultado: [85236987], ou seja, retorno = 7.

    ---------------RESOLUCAO---------------

    Aplicacao da estrutura de dados grafo, representando a abrangencia de movimento entre as teclas
    como arestas entre os vertices (sendo estes vertices as teclas de 1 a 9).
    Aplicando o algoritmo de busca em largura (Com analise assintotica O(V), onde V é a
    quantidade de vertices no grafo, e onde no pior caso seria necessário
    acessar todos vértices ao menos uma vez) podemos encontrar o menor caminho entre vertices.
    Utilizando a busca em largura e algumas funcoes auxiliares, como print_menor_distancia()
    cada par de teclas é passada para a busca de acordo com a entrada, verificando e registrando o caminho entre cada
    par, por exemplo, na sequencia '82397' seriam passados os pares vertice 8 e vertice 2, vertice 2 e vertice 3, etc.


    Em um cenário hipotético, caso mais teclas devessem ser implantandas, bastaria aumentar a quantidade de vertices e
    adicionar as arestas correspondentes, enquanto que no caso de haver uma mudança nos movimentos possíveis
    bastaria alterar as arestas entre cada tecla.


    Otto Alves - Agosto de 2021

    '''
