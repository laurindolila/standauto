"""Guardar e carregar as viaturas num ficheiro JSON (US20)."""

import json
import os

from standauto.viatura import Viatura

FICHEIRO = "viaturas.json"


def carregar(ficheiro=FICHEIRO):
    """Carrega as viaturas do ficheiro JSON.

    Args:
        ficheiro (str, optional): Caminho do ficheiro. Por defeito "viaturas.json".

    Returns:
        list[Viatura]: Lista de viaturas (vazia se o ficheiro não existir).
    """
    if not os.path.exists(ficheiro):
        return []
    with open(ficheiro, "r", encoding="utf-8") as f:
        return [Viatura.de_dict(d) for d in json.load(f)]


def guardar(viaturas, ficheiro=FICHEIRO):
    """Guarda a lista de viaturas no ficheiro JSON.

    Args:
        viaturas (list[Viatura]): Viaturas a guardar.
        ficheiro (str, optional): Caminho do ficheiro. Por defeito "viaturas.json".
    """
    with open(ficheiro, "w", encoding="utf-8") as f:
        json.dump([v.para_dict() for v in viaturas], f, ensure_ascii=False, indent=4)