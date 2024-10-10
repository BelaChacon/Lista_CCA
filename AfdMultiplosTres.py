#questão 22 da lista

class AfdMultiplosTres:
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estado_atual = self.estado_inicial
        self.estados_aceitacao = {'q0'}  

    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == 'a':
                self.estado_atual = 'q1'  
            elif char == 'b':
                self.estado_atual = 'q2' 
        elif self.estado_atual == 'q1':
            if char == 'a':
                self.estado_atual = 'q2'  
            elif char == 'b':
                self.estado_atual = 'q0'  
        elif self.estado_atual == 'q2':
            if char == 'a':
                self.estado_atual = 'q0'  
            elif char == 'b':
                self.estado_atual = 'q1'  

    def reconhece(self, string):
        self.estado_atual = self.estado_inicial
        for char in string:
            self.transicao(char)
        
        return self.estado_atual in self.estados_aceitacao  

afd = AfdMultiplosTres()

#Teste
strings = ['aaabbb', 'aab', 'ab', 'aaa', 'bb', 'a', 'b', 'abab', 'aabb', 'aaabb']

for string in strings:
    resultado = afd.reconhece(string)
    print(f"A string '{string}' tem diferença múltipla de 3 entre 'a' e 'b'? {resultado}")
