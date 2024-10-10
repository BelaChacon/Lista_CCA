def valida_placa(placa, texto):
    estado = 'q0'
    paises = ['Argentina', 'Brasil', 'Venezuela', 'Paraguai', 'Uruguai']

    if len(placa) != 7:
        return "Número da placa inválido!"

    for char in placa:
        if estado == 'q0':
            if char.isalpha():
                estado = 'q1'
            else:
                estado = 'q_rejeita'
                break
        elif estado == 'q1':
            if char.isalpha():
                estado = 'q2'
            else:
                estado = 'q_rejeita'
                break
        elif estado == 'q2':
            if char.isalpha():
                estado = 'q3'
            else:
                estado = 'q_rejeita'
                break
        elif estado == 'q3':
            if char.isdigit():
                estado = 'q4'
            else:
                estado = 'q_rejeita'
                break
        elif estado == 'q4':
            if char.isalpha():
                estado = 'q5'
            else:
                estado = 'q_rejeita'
                break
        elif estado == 'q5':
            if char.isdigit():
                estado = 'q6'
            else:
                estado = 'q_rejeita'
                break
        elif estado == 'q6':
            if char.isdigit():
                estado = 'q7'
            else:
                estado = 'q_rejeita'
                break
    
    if estado == 'q7':
        if texto in paises:
            return "Mercosul"
        else:
            return "Modelo Antigo"
    else:
        return "Placa está com caracteres fora do padrão!"

# Testes
print(valida_placa("ABC1D23", "Brasil"))  # Saída esperada: "Mercosul"
print(valida_placa("A2C1D23", "Joao Pessoa - Paraíba")) # Saída esperada: "Placa está com caracteres fora do padrão!"
print(valida_placa("A4C1D23", "Brasil")) # Saída esperada: "Modelo Antigo"
print(valida_placa("ABC1D23", "Joao Pessoa - Paraíba")) # Saída esperada: "Modelo Antigo"
