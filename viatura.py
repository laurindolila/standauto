"""Modelo de dados de uma viatura do stand."""

ESTADO_DISPONIVEL = "disponivel"
ESTADO_VENDIDA = "vendida"


class Viatura:
    """Representa uma viatura do stand.

    Attributes:
        matricula (str): Matrícula da viatura (ex.: "AA-00-BB").
        marca (str): Marca da viatura.
        modelo (str): Modelo da viatura.
        ano (int): Ano de fabrico.
        preco (float): Preço de venda em euros.
        estado (str): "disponivel" ou "vendida".
    """

    def __init__(self, matricula, marca, modelo, ano, preco, estado=ESTADO_DISPONIVEL):
        """Cria uma nova viatura.

        Args:
            matricula (str): Matrícula da viatura.
            marca (str): Marca da viatura.
            modelo (str): Modelo da viatura.
            ano (int): Ano de fabrico.
            preco (float): Preço em euros.
            estado (str, optional): Estado inicial. Por defeito "disponivel".
        """
        self.matricula = matricula.upper()
        self.marca = marca
        self.modelo = modelo
        self.ano = int(ano)
        self.preco = float(preco)
        self.estado = estado

    def para_dict(self):
        """Converte a viatura num dicionário, para gravar em JSON.

        Returns:
            dict: Dados da viatura.
        """
        return {
            "matricula": self.matricula,
            "marca": self.marca,
            "modelo": self.modelo,
            "ano": self.ano,
            "preco": self.preco,
            "estado": self.estado,
        }

    @staticmethod
    def de_dict(dados):
        """Cria uma viatura a partir de um dicionário lido do JSON.

        Args:
            dados (dict): Dicionário com os dados da viatura.

        Returns:
            Viatura: A viatura criada.
        """
        return Viatura(**dados)

    def __str__(self):
        """Devolve a viatura numa linha formatada para a consola."""
        return (f"{self.matricula:<10} {self.marca:<12} {self.modelo:<12} "
                f"{self.ano:<6} {self.preco:>10.2f} EUR  {self.estado}")