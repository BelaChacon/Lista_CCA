#questão 20 da lista 

class AfdABUmaVez:
    def __init__(self):
        self.estado_atual = 'q0'  
        self.estado_aceitacao = 'q3' 
    
    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == 'a':
                self.estado_atual = 'q1' 
            elif char == 'b':
                self.estado_atual = 'q0'  
        elif self.estado_atual == 'q1':
            if char == 'a':
                self.estado_atual = 'q1'  
            elif char == 'b':
                self.estado_atual = 'q2'  
        elif self.estado_atual == 'q2':
            if char == 'a':
                self.estado_atual = 'q1'  
            elif char == 'b':
                self.estado_atual = 'q3'        
        elif self.estado_atual == 'q3':
            if char == 'a':
                self.estado_atual = 'q3' 
            elif char == 'b':
                self.estado_atual = 'q3'  

    def reconhece(self, string):
        self.estado_atual = 'q0'
        for char in string:
            self.transicao(char)
        return self.estado_atual == self.estado_aceitacao  

afd = AfdABUmaVez()

#Teste
strings = ['abab', 'aabb', 'aaabbb', 'aaaabbbb', 'ababa', 'ababaa', 'ba', 'a']

for string in strings:
    resultado = afd.reconhece(string)
    print(f"A string '{string}' contém 'ab' exatamente uma vez? {resultado}")
