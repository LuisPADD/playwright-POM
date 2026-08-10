from playwright.sync_api import Page, expect

class EmprestimosPage:
    def __init__(self, page:Page):
        self.page = page 
        self.contratar_emprestimo_button = self.page.get_by_role("button", name="Contratar Empréstimo")       

    def clicar_contratar_emprestimo(self):
        self.page.once("dialog",lambda dialog: dialog.accept())
        self.contratar_emprestimo_button.click()


    def selecionar_valor_emprestimo(self, valor):
        self.page.get_by_role("radio", name=f"R$ {valor}").check()