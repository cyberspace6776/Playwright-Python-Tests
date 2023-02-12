
from playwright.sync_api import Page, expect


class CIMpage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.relevance_dropdown = page.get_by_test_id(
            "incident-relevance-select")
        self.impact_dropdown = page.get_by_test_id("incident-impact-select")
        self.save_icon = page.get_by_test_id("form-action-submit")
        self.close_button = page.get_by_test_id("details-dialog-close")
        self.incident_tab = page.get_by_test_id("incident-info-tab")

    def select_record(self, row: int):
        self.page.locator(
            f'div[data-rowindex="{row}"] > div[data-colindex="0"]').click()
        expect(self.incident_tab).to_have_attribute("aria-selected", "true")

    def select_impact(self, value: str):
        self.relevance_dropdown.get_by_role("button", name="Not Set").click()
        self.page.get_by_test_id(f"relevance-option-{value}").click()

    def select_relevance(self, value: str):
        self.impact_dropdown.get_by_role("button", name="Not Set").click()
        self.page.get_by_test_id(f"impact-option-{value}").click()

    def save_and_close(self):
        self.save_icon.click()
        self.close_button.click()
