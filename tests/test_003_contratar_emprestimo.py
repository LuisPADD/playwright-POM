from playwright.sync_api import Page, expect


def test_003_contratar_emprestimo( common_page, login_page, home_page, emprestimos_page) -> None:
    login_page.login("user1","pass1")
    home_page.acessar_menu("Empréstimos")
    emprestimos_page.contratar_emprestimo("2.000,00")
    common_page.assert_text("A transação foi concluída com sucesso.")
    common_page.voltar_home()
    common_page.assert_text("R$ 7.000,00")
    home_page.acessar_menu("Ver Extrato")
    common_page.assert_text("Empréstimo contratado - R$ 2000,00")