# 🎭 Playwright POM - SimulaBank Automation

Este repositório contém uma suíte de testes automatizados End-to-End (E2E) para a aplicação **SimulaBank**, desenvolvida em **Python** utilizando **Playwright** e **Pytest**, seguindo o padrão de arquitetura **Page Object Model (POM)**.

---

## 📌 Visão Geral

O projeto automatiza fluxos críticos da aplicação bancária [SimulaBank](https://leogcarvalho.github.io/simulabank/login.html), incluindo:
- Autenticação e Login.
- Realização de transferências Pix e validação de extrato/saldo.
- Validação de limites operacionais para envio de Pix.
- Contratação de empréstimos e verificação de regras de negócio para novos empréstimos.

---

## 🏗️ Arquitetura do Projeto

O projeto adota o padrão **Page Object Model (POM)** para separação de responsabilidades entre as interações de interface e a lógica dos testes.

```text
Playwright-POM/
├── .github/
│   └── workflows/
│       └── playwright.yml        # Pipeline de Integração Contínua (GitHub Actions)
├── pages/                        # Camada de Page Objects (elementos e ações de UI)
│   ├── common_page.py            # Ações e validações comuns a múltiplas páginas
│   ├── emprestimos_page.py       # Interações da tela de Empréstimos
│   ├── home_page.py              # Navegação no Dashboard e validação de saldo
│   ├── login_page.py             # Autenticação e formulário de Login
│   └── pix_page.py               # Formulário e confirmações de transação Pix
├── tests/                        # Casos de teste E2E
│   ├── test_001_login_successful.py
│   ├── test_002_fazer_pix.py
│   ├── test_003_contratar_emprestimo.py
│   ├── test_004_verificar_emprestimo_contratado.py
│   └── test_005_verificar_pix_acima_limite.py
├── conftest.py                   # Configurações do Pytest e Fixtures de Páginas
├── requirements.txt              # Dependências do projeto Python
└── README.md                     # Documentação do projeto
```

---

## 🧪 Suíte de Testes

| Arquivo | Descrição do Teste |
| :--- | :--- |
| `test_001_login_successful.py` | Valida o login com credenciais válidas e exibição da mensagem de boas-vindas. |
| `test_002_fazer_pix.py` | Valida envio de Pix com sucesso, atualização do saldo e registro no extrato. |
| `test_003_contratar_emprestimo.py` | Valida contratação de empréstimo, atualização de saldo e extrato. |
| `test_004_verificar_emprestimo_contratado.py` | Valida o bloqueio de nova contratação quando já existe empréstimo ativo. |
| `test_005_verificar_pix_acima_limite.py` | Valida a mensagem de erro ao tentar realizar um Pix acima do limite permitido (R$ 3.000,00). |

---

## 🚀 Pré-requisitos

- **Python**: versão 3.10 ou superior (recomendado 3.13)
- **Git**

---

## 🔧 Configuração do Ambiente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/Playwright-POM.git
   cd Playwright-POM
   ```

2. **Crie e ative um ambiente virtual:**
   - **Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - **Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Instale os navegadores do Playwright:**
   ```bash
   python -m playwright install --with-deps
   ```

---

## ⚙️ Execução dos Testes

- **Executar todos os testes (modo headless):**
  ```bash
  pytest
  ```

- **Executar os testes em modo visualizável (headed):**
  ```bash
  pytest --headed
  ```

- **Executar com retenção de Tracing em caso de falha:**
  ```bash
  pytest --tracing=retain-on-failure
  ```

- **Visualizar relatório de trace do Playwright:**
  ```bash
  playwright show-trace test-results/<caminho-do-trace>.zip
  ```

---

## 🔄 Integração Contínua (CI/CD)

O projeto possui um workflow configurado no **GitHub Actions** (`.github/workflows/playwright.yml`) que é disparado em todo `push` ou `pull_request` para a branch `main`.

A pipeline executa:
1. Setup do Python (v3.13).
2. Instalação das dependências e navegadores do Playwright.
3. Execução dos testes automatizados via Pytest.
4. Upload de artefatos de trace (`playwright-traces`) em caso de falhas.
