"""Testes unitários do módulo validacao (US17)."""

import unittest
from datetime import date
from unittest.mock import patch

import validacao


class TestMatriculaValida(unittest.TestCase):
    """Testes da função matricula_valida."""

    def test_formatos_validos(self):
        for matricula in ("AA-00-BB", "12-AB-34", "00-00-AA"):
            with self.subTest(matricula=matricula):
                self.assertTrue(validacao.matricula_valida(matricula))

    def test_formatos_invalidos(self):
        for matricula in ("", "AA0000", "AA-00", "AA-00-BBB", "aa-00-bb", "A-00-BB"):
            with self.subTest(matricula=matricula):
                self.assertFalse(validacao.matricula_valida(matricula))


class TestPedirMatricula(unittest.TestCase):
    """Testes da função pedir_matricula."""

    @patch("builtins.input", side_effect=["aa-00-bb"])
    def test_converte_para_maiusculas(self, _):
        self.assertEqual(validacao.pedir_matricula(), "AA-00-BB")

    @patch("builtins.input", side_effect=["xxx", "AA-00", "  ab-12-cd  "])
    def test_repete_ate_ser_valida(self, _):
        self.assertEqual(validacao.pedir_matricula(), "AB-12-CD")


class TestPedirTexto(unittest.TestCase):
    """Testes da função pedir_texto."""

    @patch("builtins.input", side_effect=["", "   ", "Audi"])
    def test_obrigatorio_repete_ate_ter_texto(self, _):
        self.assertEqual(validacao.pedir_texto("Marca: "), "Audi")

    @patch("builtins.input", side_effect=[""])
    def test_permite_vazio(self, _):
        self.assertEqual(validacao.pedir_texto("Marca: ", permite_vazio=True), "")


class TestPedirAno(unittest.TestCase):
    """Testes da função pedir_ano."""

    @patch("builtins.input", side_effect=["2020"])
    def test_ano_valido(self, _):
        self.assertEqual(validacao.pedir_ano("Ano: "), 2020)

    @patch("builtins.input", side_effect=["abc", "1899", "3000", "1900"])
    def test_rejeita_invalidos_e_aceita_limite_inferior(self, _):
        self.assertEqual(validacao.pedir_ano("Ano: "), 1900)

    @patch("builtins.input")
    def test_aceita_ano_atual_e_rejeita_o_seguinte(self, mock_input):
        ano_atual = date.today().year
        mock_input.side_effect = [str(ano_atual + 1), str(ano_atual)]
        self.assertEqual(validacao.pedir_ano("Ano: "), ano_atual)

    @patch("builtins.input", side_effect=[""])
    def test_vazio_devolve_none_se_permitido(self, _):
        self.assertIsNone(validacao.pedir_ano("Ano: ", permite_vazio=True))


class TestPedirPreco(unittest.TestCase):
    """Testes da função pedir_preco."""

    @patch("builtins.input", side_effect=["12500"])
    def test_preco_inteiro(self, _):
        self.assertEqual(validacao.pedir_preco("Preço: "), 12500.0)

    @patch("builtins.input", side_effect=["12500,50"])
    def test_aceita_virgula_decimal(self, _):
        self.assertEqual(validacao.pedir_preco("Preço: "), 12500.5)

    @patch("builtins.input", side_effect=["abc", "0", "-5", "100"])
    def test_rejeita_texto_zero_e_negativos(self, _):
        self.assertEqual(validacao.pedir_preco("Preço: "), 100.0)

    @patch("builtins.input", side_effect=[""])
    def test_vazio_devolve_none_se_permitido(self, _):
        self.assertIsNone(validacao.pedir_preco("Preço: ", permite_vazio=True))


if __name__ == "__main__":
    unittest.main()
