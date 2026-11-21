"""Funções para pedir e validar os dados introduzidos (US17)."""

import re
from datetime import date

PADRAO_MATRICULA = re.compile(r"^[A-Z0-9]{2}-[A-Z0-9]{2}-[A-Z0-9]{2}$")


def matricula_valida(matricula):
    """Verifica se a matrícula tem o formato português (ex.: AA-00-BB).

    Args:
        matricula (str): Matrícula já em maiúsculas.

    Returns:
        bool: True se o formato for válido.
    """
    return bool(PADRAO_MATRICULA.match(matricula))


def pedir_matricula(mensagem="Matrícula (ex.: AA-00-BB): "):
    """Pede uma matrícula até o formato ser válido.

    Args:
        mensagem (str, optional): Texto mostrado ao utilizador.

    Returns:
        str: Matrícula válida, em maiúsculas.
    """
    while True:
        matricula = input(mensagem).strip().upper()
        if matricula_valida(matricula):
            return matricula
        print("Erro: matrícula inválida. Use o formato AA-00-BB.")


def pedir_texto(mensagem, permite_vazio=False):
    """Pede um texto obrigatório (ou opcional, se permite_vazio for True).

    Args:
        mensagem (str): Texto mostrado ao utilizador.
        permite_vazio (bool, optional): Aceita Enter sem texto. Por defeito False.

    Returns:
        str: O texto escrito (pode ser "" se permite_vazio for True).
    """
    while True:
        texto = input(mensagem).strip()
        if texto or permite_vazio:
            return texto
        print("Erro: este campo é obrigatório.")