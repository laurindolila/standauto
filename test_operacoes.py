"""Testes unitários do módulo operacoes (CRUD das viaturas)."""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import operacoes
from viatura import Viatura


def criar_viaturas():
    """Cria uma lista de viaturas de exemplo para os testes."""
    return [
        Viatura("AA-00-BB", "Audi", "A3", 2019, 18000),
        Viatura("CC-11-DD", "BMW", "Serie 1", 2021, 25000),
    ]


def capturar(funcao, *args):
    """Executa a função e devolve o texto que ela escreveu na consola."""
    saida = io.StringIO()
    with redirect_stdout(saida):
        funcao(*args)
    return saida.getvalue()


class TestProcurarPorMatricula(unittest.TestCase):
    """Testes da função procurar_por_matricula."""

    def test_encontra_ignorando_maiusculas_e_espacos(self):
        viaturas = criar_viaturas()
        v = operacoes.procurar_por_matricula(viaturas, "  aa-00-bb ")
        self.assertIs(v, viaturas[0])

    def test_devolve_none_se_nao_existir(self):
        self.assertIsNone(operacoes.procurar_por_matricula(criar_viaturas(), "ZZ-99-ZZ"))


@patch("operacoes.dados.guardar")
class TestRegistar(unittest.TestCase):
    """Testes da função registar_viatura."""

    @patch("builtins.input", side_effect=["ee-22-ff", "Fiat", "500", "2018", "9500,50"])
    def test_regista_nova_viatura(self, _, mock_guardar):
        viaturas = criar_viaturas()
        capturar(operacoes.registar_viatura, viaturas)
        self.assertEqual(len(viaturas), 3)
        nova = viaturas[-1]
        self.assertEqual((nova.matricula, nova.marca, nova.ano, nova.preco),
                         ("EE-22-FF", "Fiat", 2018, 9500.5))
        mock_guardar.assert_called_once_with(viaturas)

    @patch("builtins.input", side_effect=["AA-00-BB"])
    def test_recusa_matricula_repetida(self, _, mock_guardar):
        viaturas = criar_viaturas()
        saida = capturar(operacoes.registar_viatura, viaturas)
        self.assertEqual(len(viaturas), 2)
        self.assertIn("Já existe", saida)
        mock_guardar.assert_not_called()


class TestListar(unittest.TestCase):
    """Testes da função listar_viaturas."""

    def test_lista_vazia(self):
        self.assertIn("Não há viaturas registadas.", capturar(operacoes.listar_viaturas, []))

    def test_mostra_viaturas_e_total(self):
        saida = capturar(operacoes.listar_viaturas, criar_viaturas())
        self.assertIn("AA-00-BB", saida)
        self.assertIn("CC-11-DD", saida)
        self.assertIn("Total: 2 viatura(s).", saida)


@patch("operacoes.dados.guardar")
class TestEditar(unittest.TestCase):
    """Testes da função editar_viatura."""

    @patch("builtins.input", side_effect=["AA-00-BB", "", "A4", "", "20000"])
    def test_altera_so_os_campos_preenchidos(self, _, mock_guardar):
        viaturas = criar_viaturas()
        capturar(operacoes.editar_viatura, viaturas)
        v = viaturas[0]
        self.assertEqual((v.marca, v.modelo, v.ano, v.preco), ("Audi", "A4", 2019, 20000.0))
        mock_guardar.assert_called_once()

    @patch("builtins.input", side_effect=["ZZ-99-ZZ"])
    def test_viatura_inexistente(self, _, mock_guardar):
        saida = capturar(operacoes.editar_viatura, criar_viaturas())
        self.assertIn("não encontrada", saida)
        mock_guardar.assert_not_called()


@patch("operacoes.dados.guardar")
class TestEliminar(unittest.TestCase):
    """Testes da função eliminar_viatura."""

    @patch("builtins.input", side_effect=["AA-00-BB", "s"])
    def test_elimina_com_confirmacao(self, _, mock_guardar):
        viaturas = criar_viaturas()
        capturar(operacoes.eliminar_viatura, viaturas)
        self.assertEqual([v.matricula for v in viaturas], ["CC-11-DD"])
        mock_guardar.assert_called_once()

    @patch("builtins.input", side_effect=["AA-00-BB", "n"])
    def test_cancela_sem_confirmacao(self, _, mock_guardar):
        viaturas = criar_viaturas()
        saida = capturar(operacoes.eliminar_viatura, viaturas)
        self.assertEqual(len(viaturas), 2)
        self.assertIn("cancelada", saida)
        mock_guardar.assert_not_called()


class TestPesquisar(unittest.TestCase):
    """Testes da função pesquisar_viaturas."""

    @patch("builtins.input", side_effect=["bmw"])
    def test_pesquisa_por_marca_sem_distinguir_maiusculas(self, _):
        saida = capturar(operacoes.pesquisar_viaturas, criar_viaturas())
        self.assertIn("CC-11-DD", saida)
        self.assertNotIn("AA-00-BB", saida)
        self.assertIn("1 viatura(s) encontrada(s).", saida)

    @patch("builtins.input", side_effect=["-"])
    def test_pesquisa_por_parte_do_texto(self, _):
        saida = capturar(operacoes.pesquisar_viaturas, criar_viaturas())
        self.assertIn("2 viatura(s) encontrada(s).", saida)

    @patch("builtins.input", side_effect=["tesla"])
    def test_sem_resultados(self, _):
        saida = capturar(operacoes.pesquisar_viaturas, criar_viaturas())
        self.assertIn("Nenhuma viatura encontrada.", saida)

    @patch("builtins.input", side_effect=["   "])
    def test_termo_vazio(self, _):
        saida = capturar(operacoes.pesquisar_viaturas, criar_viaturas())
        self.assertIn("Tem de escrever algo", saida)


@patch("operacoes.dados.guardar")
class TestVender(unittest.TestCase):
    """Testes da função vender_viatura."""

    @patch("builtins.input", side_effect=["AA-00-BB", "s"])
    def test_vende_com_confirmacao(self, _, mock_guardar):
        viaturas = criar_viaturas()
        capturar(operacoes.vender_viatura, viaturas)
        self.assertTrue(viaturas[0].esta_vendida())
        mock_guardar.assert_called_once()

    @patch("builtins.input", side_effect=["AA-00-BB", "n"])
    def test_cancela_venda(self, _, mock_guardar):
        viaturas = criar_viaturas()
        capturar(operacoes.vender_viatura, viaturas)
        self.assertFalse(viaturas[0].esta_vendida())
        mock_guardar.assert_not_called()

    @patch("builtins.input", side_effect=["AA-00-BB"])
    def test_nao_vende_duas_vezes(self, _, mock_guardar):
        viaturas = criar_viaturas()
        viaturas[0].vender()
        saida = capturar(operacoes.vender_viatura, viaturas)
        self.assertIn("já foi vendida", saida)
        mock_guardar.assert_not_called()


if __name__ == "__main__":
    unittest.main()
