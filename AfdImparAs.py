#questão 11 das lista 

class AfdImparAs:
    def __init__(self):
        self.estado_atual = 'q0'  

    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == 'a':
                self.estado_atual = 'q1'  
        elif self.estado_atual == 'q1':
            if char == 'a':
                self.estado_atual = 'q0' 

    def reconhece(self, string):
        self.estado_atual = 'q0'  
        for char in string:
            self.transicao(char)
        return self.estado_atual == 'q1'

afd = AfdImparAs()

#Teste
strings = ['a', 'b', 'ab', 'ba', 'aa', 'aaa', 'aab', 'aba', 'bba', 'bbb']

for string in strings:
    resultado = afd.reconhece(string)
    print(f"A string '{string}' possui número ímpar de a's? {resultado}")
