def valida_cpf(cpf):
    estado = 'q0'
    cpf_mascarado = []                                                                              

  
    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido!"

    for i, char in enumerate(cpf):             
        if estado == 'q0':
            if char.isdigit():
                cpf_mascarado.append('X')  
                estado = 'q1'
            else:
                estado = 'q_rejeita'
                break
        elif estado == 'q1':
            if char.isdigit():
                cpf_mascarado.append('X')
                estado = 'q2'
            else:
                estado = 'q_rejeita'
                break
        elif estado == 'q2':
            if char.isdigit():
                cpf_mascarado.append('X')
                estado = 'q3'
            else:
                estado = 'q_rejeita'
                break
        elif estado == 'q3':
            cpf_mascarado.append(char)  
            estado = 'q4'
        elif estado == 'q4':
            cpf_mascarado.append(char)  
            estado = 'q5'
        elif estado == 'q5':
            cpf_mascarado.append(char) 
            estado = 'q6'
        elif estado == 'q6':
            cpf_mascarado.append(char) 
            estado = 'q7'
        elif estado == 'q7':
            cpf_mascarado.append(char) 
            estado = 'q8'
        elif estado == 'q8':
            cpf_mascarado.append(char) 
            estado = 'q9'
        elif estado == 'q9':
            cpf_mascarado.append('X')  
            estado = 'q10'
        elif estado == 'q10':
            cpf_mascarado.append('X') 
            estado = 'q11'
    
    if estado == 'q11':
        return ''.join(cpf_mascarado)
    else:
        return "CPF inválido!"

# Testes
print(valida_cpf("70468293493"))  # Saída: XXX682934XX
print(valida_cpf("12345678901"))  # Saída: XXX456789XX
print(valida_cpf("00000000000"))  # Saída: XXX000000XX
print(valida_cpf("01234567890"))  # Saída: XXX456789XX
print(valida_cpf("12345678abc"))  # Saída: CPF inválido! (não numérico)
print(valida_cpf("123456789"))    # Saída: CPF inválido! (tamanho errado)
