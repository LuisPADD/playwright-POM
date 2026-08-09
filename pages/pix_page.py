from playwright.sync_api import Page, expect

class PixPage:
    def __init__(self, page:Page):
        self.page = page
        self.chave_pix = page.get_by_role("textbox", name="Chave Pix:")
        self.valor_pix = page.get_by_role("textbox", name="Valor:")
        self.enviar_pix = page.get_by_role("button", name="Enviar Pix")
        self.voltar_para_home = page.get_by_role("button", name="Voltar para a Home")

    def fazer_pix(self, chave, valor):
        self.chave_pix.fill(chave)
        self.valor_pix.fill(valor)
        self.enviar_pix.click()

    def assert_pix_realizado(self):
        expect(self.page.get_by_role("heading", name="Transação Realizada com")).to_be_visible()
        expect(self.page.get_by_text("A transação foi concluída com")).to_be_visible()
               
    def voltar_home(self):
        self.voltar_para_home.click()
