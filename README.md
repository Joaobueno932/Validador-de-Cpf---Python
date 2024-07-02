João Lucas Bueno da Silva Pinheiro

# Validador de CPF em Python

Este repositório contém um script Python para validar números de CPF (Cadastro de Pessoas Físicas) usando expressões regulares e a biblioteca NumPy.

## Como funciona

O script verifica se um CPF é válido seguindo os passos:

1. Remove todos os caracteres não numéricos do CPF.
2. Converte os dígitos do CPF em um array NumPy.
3. Calcula os dígitos verificadores a partir dos nove primeiros dígitos.
4. Compara os dígitos calculados com os dois últimos dígitos do CPF fornecido.
5. Informa se o CPF é válido ou inválido.

## Requisitos

- Python 3.x
- NumPy

## Instalação

Clone este repositório e instale os pacotes necessários:

```bash
git clone https://github.com/seu-usuario/validador-de-cpf.git
cd validador-de-cpf
pip install numpy
