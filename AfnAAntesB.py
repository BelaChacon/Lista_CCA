#questão 25 da lista

class AfnAAntesB:
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q0', 'q1'} 
        self.estado_atual = self.estado_inicial

    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == 'a':
                self.estado_atual = 'q0'  
            elif char == 'b':
                self.estado_atual = 'q1'  
        elif self.estado_atual == 'q1':
            if char == 'a':
                self.estado_atual = 'q2'  
            elif char == 'b':
                self.estado_atual = 'q1'  
              
    def reconhece(self, string):
        self.estado_atual = self.estado_inicial
        for char in string:
            self.transicao(char)

        return self.estado_atual in self.estados_aceitacao

afn = AfnAAntesB()

#Teste
strings = ['aab', 'bab', 'ba', 'aba', 'aabbb', 'bbaa']

for string in strings:
    resultado = afn.reconhece(string)
    print(f"A string '{string}' segue a regra 'a' antes de 'b'? {resultado}")
