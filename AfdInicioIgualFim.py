#questão 5 da lista

class AfdInicioIgualFim:
    def __init__(self):
        self.estado_atual = 'q0'  #Estado inicial
        self.inicio = None  #Armazena o primeiro caractere da string
    
    def transicao(self, char, posicao):
        if posicao == 0:
            self.inicio = char
        
        if posicao > 0:
            if char == self.inicio:
                self.estado_atual = 'q1'  
            else:
                self.estado_atual = 'q2'  
    
    def reconhece(self, string):
        if not string:
            return True
        
        self.estado_atual = 'q0'
        self.inicio = None
        
        for i, char in enumerate(string):
            self.transicao(char, i)

        return self.estado_atual == 'q1'

afd = AfdInicioIgualFim()

#Teste
strings = ['101', '111', '000', '0110', '001', '1']

for string in strings:
    resultado = afd.reconhece(string)
    print(f"O primeiro e último caractere da string - '{string}' - são iguais? {resultado}")
