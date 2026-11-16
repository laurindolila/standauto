"""Operações sobre as viaturas do stand (CRUD)."""

import dados
from viatura import Viatura


def procurar_por_matricula(viaturas, matricula):
    """Procura uma viatura pela matrícula.

    Args:
        viaturas (list[Viatura]): Lista de viaturas do stand.
        matricula (str): Matrícula a procurar (maiúsculas ou minúsculas).

    Returns:
        Viatura | None: A viatura encontrada, ou None se não existir.
    """
    matricula = matricula.strip().upper()
    for v in viaturas:
        if v.matricula == matricula:
            return v
    return None