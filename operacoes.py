"""Operações sobre as viaturas do stand (CRUD)."""

import dados
import validacao
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
    matricula = validacao.pedir_matricula()
    if procurar_por_matricula(viaturas, matricula):
        print("Já existe uma viatura com essa matrícula.")
        return
    marca = validacao.pedir_texto("Marca: ")
    modelo = validacao.pedir_texto("Modelo: ")
    ano = validacao.pedir_ano("Ano: ")
    preco = validacao.pedir_preco("Preço (EUR): ")
    viaturas.append(Viatura(matricula, marca, modelo, ano, preco))
    dados.guardar(viaturas)
    print(f"Viatura {matricula} registada com sucesso.")


def listar_viaturas(viaturas):
    """Mostra na consola todas as viaturas do stand (US3).

    Args:
        viaturas (list[Viatura]): Lista de viaturas do stand.
    """
    print("\n--- Consultar viaturas ---")
    if not viaturas:
        print("Não há viaturas registadas.")
        return
    print(f"{'Matrícula':<10} {'Marca':<12} {'Modelo':<12} "
          f"{'Ano':<6} {'Preço':>10}      Estado")
    print("-" * 70)
    for v in viaturas:
        print(v)
    print(f"\nTotal: {len(viaturas)} viatura(s).")


def editar_viatura(viaturas):
    """Altera os dados de uma viatura existente (US5).

    Se o utilizador carregar Enter sem escrever nada, o valor atual mantém-se.

    Args:
        viaturas (list[Viatura]): Lista de viaturas do stand (é alterada).
    """
    print("\n--- Editar viatura ---")
    matricula = input("Matrícula da viatura a editar: ")
    v = procurar_por_matricula(viaturas, matricula)
    if v is None:
        print("Viatura não encontrada.")
        return
    print(f"Dados atuais: {v}")
    print("(Carregue Enter para manter o valor atual)")
    marca = validacao.pedir_texto(f"Marca [{v.marca}]: ", permite_vazio=True)
    modelo = validacao.pedir_texto(f"Modelo [{v.modelo}]: ", permite_vazio=True)
    ano = validacao.pedir_ano(f"Ano [{v.ano}]: ", permite_vazio=True)
    preco = validacao.pedir_preco(f"Preço [{v.preco:.2f}]: ", permite_vazio=True)
    if marca:
        v.marca = marca
    if modelo:
        v.modelo = modelo
    if ano is not None:
        v.ano = ano
    if preco is not None:
        v.preco = preco
    dados.guardar(viaturas)
    print(f"Viatura {v.matricula} atualizada com sucesso.")


def eliminar_viatura(viaturas):
    """Remove uma viatura do stand, depois de pedir confirmação (US2).

    Args:
        viaturas (list[Viatura]): Lista de viaturas do stand (é alterada).
    """
    print("\n--- Eliminar viatura ---")
    matricula = input("Matrícula da viatura a eliminar: ")
    v = procurar_por_matricula(viaturas, matricula)
    if v is None:
        print("Viatura não encontrada.")
        return
    print(f"Vai eliminar: {v}")
    confirmacao = input("Tem a certeza? (s/n): ").strip().lower()
    if confirmacao != "s":
        print("Operação cancelada.")
        return
    viaturas.remove(v)
    dados.guardar(viaturas)
    print(f"Viatura {v.matricula} eliminada com sucesso.")


def pesquisar_viaturas(viaturas):
    """Pesquisa viaturas por matrícula, marca ou modelo (US4)."""
    print("\n--- Pesquisar viaturas ---")
    termo = input("Matrícula, marca ou modelo: ").strip().lower()
    if not termo:
        print("Tem de escrever algo para pesquisar.")
        return
    encontradas = [
        v for v in viaturas
        if termo in v.matricula.lower()
        or termo in v.marca.lower()
        or termo in v.modelo.lower()
    ]
    if not encontradas:
        print("Nenhuma viatura encontrada.")
        return
    for v in encontradas:
        print(v)
    print(f"\n{len(encontradas)} viatura(s) encontrada(s).")


def vender_viatura(viaturas):
    """Regista a venda de uma viatura, mudando o estado para "vendida" (US13).

    Args:
        viaturas (list[Viatura]): Lista de viaturas do stand (é alterada).
    """
    print("\n--- Vender viatura ---")
    matricula = input("Matrícula da viatura a vender: ")
    v = procurar_por_matricula(viaturas, matricula)
    if v is None:
        print("Viatura não encontrada.")
        return
    if v.esta_vendida():
        print(f"A viatura {v.matricula} já foi vendida.")
        return
    print(f"Vai vender: {v}")
    confirmacao = input("Confirmar a venda? (s/n): ").strip().lower()
    if confirmacao != "s":
        print("Venda cancelada.")
        return
    v.vender()
    dados.guardar(viaturas)
    print(f"Viatura {v.matricula} vendida por {v.preco:.2f} EUR. Parabéns pela venda!")