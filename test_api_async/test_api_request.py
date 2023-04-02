import os
import pytest
from playwright.async_api import async_playwright, APIRequestContext
from api_createIM import ApiIndicatorMessage


@pytest.fixture(scope="session")
async def api_request_context():
    async with async_playwright() as api:
        request_context = await api.request.new_context(base_url=os.getenv("apiurl"))
        yield request_context
        await request_context.dispose()


async def test_incorrect_token(api_request_context: APIRequestContext) -> None:
    user_token = "abc"
    apiIM = ApiIndicatorMessage(api_request_context)

    response = await apiIM.create_message(user_token, "country", "RM0030", "de")
    assert response.status == 401
    # assert response.ok

# https://www.lambdatest.com/automation-testing-advisor/python/playwright-python-async_playwright
# https://earthly.dev/blog/playwright-python-api-testing/
# https://github.com/JoanEsquivel/playwright-python-test-framework/blob/master/api/pytest/api-testing.py
