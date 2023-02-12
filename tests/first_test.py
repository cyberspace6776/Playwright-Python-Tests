from playwright.sync_api import Page, expect
from pages.cim_page import CIMpage
from pages.login_page import LoginPage


email = ""
password = ""
customer_name = ""


def test_CIM_form(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(email, password)

    login_page.login_user(customer_name)
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="login as user").click()
    page1 = page1_info.value

    page1.get_by_role("link", name="CIM").click()
    cim_page = CIMpage(page1)
    row = 0
    while row < 5:
        relevance = ["high", "medium", "low", "none", ""]
        impact = ["high", "medium", "low", "none", ""]
        if row == 4:
            continue
        cim_page.select_record(row)
        cim_page.select_relevance(relevance[row])
        cim_page.select_impact(impact[row])
        cim_page.save_and_close()
        incident_relevance = ["High", "Medium",
                              "Low", "Not Relevant", "Not Set"]
        expect(page1.locator(f'div[data-rowindex="{row}"]').get_by_test_id(
            "relevance")).to_contain_text(incident_relevance[row])
        row += 1
