import re #Esta linha importa o módulo 're' em Python, que fornece suporte para expressões regulares
import numpy as np # Esta linha importa o módulo numpy e o apelida como np.


cpf= "123.456.789-00"
def ValidadorDeCpf(cpf: str):  # Define uma função chamada ValidadorDeCpf que recebe um argumento cpf, que deve ser uma string
    cpf_numerico = re.sub("[^0-9]", "", cpf)  # Remove todos os caracteres não numéricos da string cpf
    cpf_como_np = np.array([int(i) for i in cpf_numerico])  # Converte a string de dígitos em uma lista de inteiros e depois em um array NumPy
    numeros_10_a_2 = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2])  # Cria um array NumPy contendo os números de 10 a 2
    numeros_11_a_2 = np.array([11, 10, 9, 8, 7, 6, 5, 4, 3, 2])  # Cria um array NumPy contendo os números de 11 a 2
    primeiro_digito_valido = sum(cpf_como_np[0:9] * 10 * numeros_10_a_2) % 11  # Calcula o primeiro dígito verificador 
    segundo_digito_valido = sum(cpf_como_np[0:10] * 10 * numeros_11_a_2) % 11  # Calcula o segundo dígito verificador 
    
    # Verifica se os dígitos verificadores do CPF são iguais aos dígitos verificadores calculados
    if cpf_como_np[9] == primeiro_digito_valido and cpf_como_np[10] == segundo_digito_valido:
        print(cpf, "é valido")  # Imprime que o CPF é válido
    else:
        print(cpf, "não é valido")  # Imprime que o CPF não é válido
		
ValidadorDeCpf(cpf) #Realiza o teste