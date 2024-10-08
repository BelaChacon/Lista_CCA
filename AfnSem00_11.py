#questão 14 da lista

class AfnSem00_11:
    def __init__(self):
        self.estado_atual = 'q0' 
        self.estados_aceitacao = {'q0', 'q1', 'q2'}  

    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == '0':
                self.estado_atual = 'q1' 
            elif char == '1':
                self.estado_atual = 'q2'  
        elif self.estado_atual == 'q1':
            if char == '1':
                self.estado_atual = 'q2'  
            else:
                self.estado_atual = None  # Nenhuma transição válida
        elif self.estado_atual == 'q2':
            if char == '0':
                self.estado_atual = 'q1'  
            else:
                self.estado_atual = None  # Nenhuma transição válida

    def reconhece(self, string):
        self.estado_atual = 'q0' 
        for char in string:
            self.transicao(char)
            if self.estado_atual is None:
                return False  # Rejeita a string se não houver transição válida

        return self.estado_atual in self.estados_aceitacao

afn = AfnSem00_11()

#Teste
strings = ['0', '1', '01', '10', '0101', '1010', '110', '001', '1001']

for string in strings:
    resultado = afn.reconhece(string)
    print(f"A string '{string}' está de acordo com AFN? {resultado}")
