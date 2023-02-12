# Playwright-Python-Tests
Test to select values from 2 dropdowns over 4 records and verifing that values are visible in the table (only one is currently present in UI)

This is only part of End to End flow

Logging is through admin system that is frequently needed but here could be further refactored

### Running tests locally

pytest --headed tests/first_test.py

PWDEBUG=1 pytest -s tests/first_test.py

Note: url and login information are removed, __init__.py also not included


#### To create new tests :D
Playwright codegen

Versions: Python 3.11.2 Playwright 1.30.0
