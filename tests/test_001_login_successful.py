from playwright.sync_api import Page, expect


def test_001_login_successful(page, login_page) -> None:
    login_page.login("user1","pass1")
    login_page.assert_login_successful()

    