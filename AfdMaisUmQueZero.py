#questão 13 da lista

class AfdMaisUmQueZero:
    def __init__(self):
        self.contador_0 = 0  
        self.contador_1 = 0 

    def transicao(self, char):
        if char == '0':
            self.contador_0 += 1
        elif char == '1':
            self.contador_1 += 1

    def reconhece(self, string):
        # Reseta os contadores para cada nova string
        self.contador_0 = 0
        self.contador_1 = 0
        for char in string:
            self.transicao(char)
        
        return self.contador_1 > self.contador_0

afd = AfdMaisUmQueZero()

#Teste
strings = ['0', '1', '11', '00', '111', '110', '001', '1110', '0001', '101', '01010']

for string in strings:
    resultado = afd.reconhece(string)
    print(f"A string '{string}' possui mais número um do que zero? {resultado}")
