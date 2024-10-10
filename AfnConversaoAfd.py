#questão 17 da lista

class Afn:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2'}
        self.alfabeto = {'0', '1'}
        self.transicoes = {
            'q0': {'0': {'q0'}, '1': {'q0', 'q1'}},  
            'q1': {'0': {'q2'}, '1': {'q0', 'q1'}},  
            'q2': {'0': {'q0'}, '1': {'q0'}}           
        }
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q2'}

    def transicao(self, estado, simbolo):
        return self.transicoes.get(estado, {}).get(simbolo, set())

class Afd:
    def __init__(self):
        self.estados = set() 
        self.estado_inicial = frozenset({'q0'}) 
        self.estados_aceitacao = set() 
        self.transicoes = {}  
        self.alfabeto = {'0', '1'}

        self.adicionar_estado(self.estado_inicial)

    def adicionar_estado(self, conjunto):
        if conjunto not in self.estados:
            self.estados.add(conjunto)
            if conjunto & {'q2'}:
                self.estados_aceitacao.add(conjunto)

    def construir(self, afn):
        for estado in list(self.estados):
            for simbolo in self.alfabeto:
                novo_conjunto = set()
                for e in estado:
                    novo_conjunto.update(afn.transicao(e, simbolo))
                if novo_conjunto:
                    novo_estado = frozenset(novo_conjunto)
                    self.adicionar_estado(novo_estado)
                    self.transicoes[estado] = self.transicoes.get(estado, {})
                    self.transicoes[estado][simbolo] = novo_estado

    def reconhece(self, string):
        estado_atual = self.estado_inicial
        for simbolo in string:
            estado_atual = self.transicoes.get(estado_atual, {}).get(simbolo, frozenset())
            if not estado_atual:
                return False
        return estado_atual in self.estados_aceitacao

afn = Afn()

afd = Afd()
afd.construir(afn)

#Teste
strings = ['0', '1', '01', '10', '001', '0101', '1101', '111', '101', '0001']

for string in strings:
    resultado = afd.reconhece(string)  
    print(f"A string '{string}' termina com '01'? {resultado}")
