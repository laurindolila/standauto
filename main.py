"""Ponto de entrada da aplicação StandAuto."""

import dados
import operacoes

MENU = """
==============================
          STANDAUTO
==============================
 1 - Registar viatura
 2 - Listar viaturas
 3 - Editar viatura
 4 - Eliminar viatura
 5 - Pesquisar viatura
 6 - Vender viatura
 0 - Sair
"""


def main():
    """Mostra o menu principal e executa a opção escolhida."""
    viaturas = dados.carregar()
    while True:
        print(MENU)
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            operacoes.registar_viatura(viaturas)
        elif opcao == "0":
            dados.guardar(viaturas)
            print("Dados guardados. Até breve!")
            break
        else:
            print("Opção inválida ou ainda não implementada.")


if __name__ == "__main__":
    main()