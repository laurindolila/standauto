# 🚗 StandAuto

Aplicação de consola, em Python, para gestão de um stand de automóveis.
Projeto da UC **Ambientes de Desenvolvimento Colaborativo** — ISE, Universidade do Algarve (2026/2027).

## ✨ Funcionalidades
| Opção | Funcionalidade | User Story |
|:-----:|----------------|:----------:|
| 1 | Registar viatura | US1 |
| 2 | Listar viaturas | US3 |
| 3 | Editar viatura | US5 |
| 4 | Eliminar viatura (com confirmação) | US2 |
| 5 | Pesquisar por matrícula, marca ou modelo | US4 |
| 6 | Vender viatura (muda o estado para "vendida") | US13 |
| — | Validação dos dados introduzidos | US17 |
| — | Gravação automática em `viaturas.json` | US20 |

## ▶️ Como executar
Requisitos: **Python 3.10+** (sem bibliotecas externas).

```bash
git clone https://github.com/laurindolila/standauto.git
cd standauto
python main.py
```

## 📁 Estrutura do projeto
```
standauto/
├── main.py         # menu principal (ponto de entrada)
├── viatura.py      # classe Viatura
├── dados.py        # guardar/carregar em JSON
├── operacoes.py    # operações CRUD, pesquisa e venda
├── validacao.py    # validação dos dados introduzidos
└── docs/           # documentação Sphinx
```

## 📚 Documentação
```bash
python -m pip install sphinx sphinx-rtd-theme
python -m sphinx -b html docs docs/_build/html
```
Depois abrir `docs/_build/html/index.html` no browser.

## 🌿 Fluxo de trabalho (Git Flow)
- `main` — apenas versões estáveis (releases)
- `develop` — integração do trabalho
- `feature/*` — uma funcionalidade por ramo, integrada por Pull Request
- `release/*` e `hotfix/*` — preparação de versões e correções urgentes

Mais informação na [Wiki do projeto](https://github.com/laurindolila/standauto/wiki).

## 👥 Grupo
| Número | Nome |
|--------|------|
| 94101 | Marcio Galamba |
| 94103 | David Silva |
| 94193 | Laurindo Lila |