#questão 23 da lista

class Afn101_110:
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q3', 'q6'} 
        self.estados_atuais = {self.estado_inicial} 

    def transicao(self, estados, char):
        novos_estados = set()
        for estado in estados:
            if estado == 'q0':
                if char == '1':
                    novos_estados.add('q1')
            elif estado == 'q1':
                if char == '0':
                    novos_estados.add('q2')
                elif char == '1':
                    novos_estados.add('q4')
            elif estado == 'q2':
                if char == '1':
                    novos_estados.add('q3')
            elif estado == 'q4':
                if char == '0':
                    novos_estados.add('q5')
            elif estado == 'q5':
                if char == '1':
                    novos_estados.add('q6')

        return novos_estados

    def reconhece(self, string):
        self.estados_atuais = {self.estado_inicial} 
        for char in string:
            self.estados_atuais = self.transicao(self.estados_atuais, char)

        return any(estado in self.estados_aceitacao for estado in self.estados_atuais)

afn = Afn101_110()

#Teste
strings = ['110', '101', '1001', '1110', '0101', '00110', '111', '100', '1010', '0110']

for string in strings:
    resultado = afn.reconhece(string)
    print(f"A string '{string}' contém '101' ou '110'? {resultado}")
