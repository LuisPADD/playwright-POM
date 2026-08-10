from playwright.sync_api import Page, expect


def test_004_verificar_emprestimo_contratado( common_page, login_page, home_page, emprestimos_page) -> None:
    login_page.login("user1","pass1")
    home_page.acessar_menu("Empréstimos")
    emprestimos_page.selecionar_valor_emprestimo("5.000,00")
    emprestimos_page.clicar_contratar_emprestimo()
    common_page.assert_text("A transação foi concluída com sucesso.")
    common_page.voltar_home()
    common_page.assert_text("R$ 10.000,00")
    home_page.acessar_menu("Empréstimos")
    common_page.assert_text("Você já tem um empréstimo contratado em andamento. Novos empréstimos não estão disponíveis.")

