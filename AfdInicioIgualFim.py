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
                self.estado_atual = 'q1'  #Estado de aceitação
            else:
                self.estado_atual = 'q2'  #Estado de rejeição
    
    def reconhece(self, string):
        # Verifica se a string está vazia, se estiver, é aceita
        if not string:
            return True
        
        # Reseta o estado e armazena o primeiro caractere
        self.estado_atual = 'q0'
        self.inicio = None
        
        # Percorre cada caractere da string e aplica a transição
        for i, char in enumerate(string):
            self.transicao(char, i)
        
        # Verifica se o último caractere corresponde ao primeiro
        return self.estado_atual == 'q1'

afd = AfdInicioIgualFim()

#Teste
strings = ['101', '111', '000', '0110', '001', '1']

for string in strings:
    resultado = afd.reconhece(string)
    print(f"O primeiro e último caractere da string - '{string}' - são iguais?: {resultado}")
