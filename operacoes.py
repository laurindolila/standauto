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


def registar_viatura(viaturas):
    """Pede os dados de uma nova viatura e adiciona-a ao stand (US1).

    Args:
        viaturas (list[Viatura]): Lista de viaturas do stand (é alterada).
    """
    print("\n--- Registar viatura ---")
    matricula = input("Matrícula: ").strip().upper()
    if procurar_por_matricula(viaturas, matricula):
        print("Já existe uma viatura com essa matrícula.")
        return
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()
    ano = input("Ano: ").strip()
    preco = input("Preço (EUR): ").strip().replace(",", ".")
    viaturas.append(Viatura(matricula, marca, modelo, ano, preco))
    dados.guardar(viaturas)
    print(f"Viatura {matricula} registada com sucesso.")