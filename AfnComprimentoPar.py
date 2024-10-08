#questão 15 da lista 

class AfnComprimentoPar:
    
    def __init__(self):
        self.estado_atual = 'q0'
        self.estado_aceitacao = 'q0'
    
    def transicao(self, char):
        if self.estado_atual == 'q0':
            self.estado_atual = 'q1'
        elif self.estado_atual == 'q1':
            self.estado_atual = 'q0'
            
    def reconhece(self, string):
        self.estado_atual = 'q0'
        for char in string:
            self.transicao(char)
        
        return self.estado_atual in self.estado_aceitacao
            
afn = AfnComprimentoPar()

#Teste
strings = ['a', 'b', 'aa', 'bb', 'ab', 'ba', 'aabb', 'abab', 'aab']

for string in strings:
    resultado = afn.reconhece(string)
    print(f"A string '{string}' possui comprimento par? {resultado}")
