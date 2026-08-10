# SauceDemo E2E Test Suite

Automated End-to-End (E2E) test suite for [SauceDemo](https://www.saucedemo.com/) built with **Python**, **Pytest**, **Playwright**, **uv**, and **Ruff**. The project implements the **Page Object Model (POM)** design pattern and supports automated cross-browser test execution across **Chromium**, **Firefox**, and **WebKit**.

---

## Tech Stack & Libraries

- **Python**: Programming language
- **Pytest**: Test runner and assertion framework
- **Playwright & pytest-playwright**: Browser automation library and pytest plugin
- **uv**: Python package and virtual environment manager
- **Ruff**: Linter and code formatter
- **Page Object Model (POM)**: Design pattern separating page element locators/actions from test assertions

---

## Project Structure

```text
hitachi_task/
├── pages/
│   ├── __init__.py
│   ├── login_page.py       # Page Object for Login Page
│   └── inventory_page.py   # Page Object for Inventory/Products Page
├── tests/
│   ├── conftest.py         # Pytest fixtures for Page Objects
│   └── test_saucedemo.py   # Automated E2E test scenarios
├── .gitignore
├── .python-version
├── pyproject.toml          # Dependencies & Ruff configuration
├── pytest.ini             # Pytest & default cross-browser options
├── README.md
├── requirements.txt        # Dependencies for standard pip setup
└── uv.lock                 # Lockfile ensuring exact dependency versions
```

---

## Setup Instructions

### Option 1: Using uv (Recommended)

1. Sync virtual environment and install dependencies:
   ```bash
   uv sync
   ```

2. Install Playwright browser binaries:
   ```bash
   uv run playwright install chromium firefox webkit
   ```

---

### Option 2: Using standard pip (without uv)

1. Create and activate virtual environment:
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\activate
     ```
   - **macOS / Linux**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

2. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright browser binaries:
   ```bash
   playwright install chromium firefox webkit
   ```

---

## Running Tests

### Run All Test Scenarios (Cross-Browser)
By default, running `pytest` executes all test scenarios across **Chromium**, **Firefox**, and **WebKit**:
- Using **uv**:
  ```bash
  uv run pytest
  ```
- Using active virtual environment:
  ```bash
  pytest
  ```

### Run on a Specific Browser
Target a single browser engine (e.g., Chromium or Firefox):
```bash
uv run pytest --browser chromium
```

### Run in Headed (GUI) Mode
Observe browser interactions visually:
```bash
uv run pytest --headed --browser chromium
```

---

## Code Quality (Ruff)

### Run Linter Check
```bash
uv run ruff check .
```

### Automatically Fix Linting Issues
```bash
uv run ruff check --fix .
```

### Format Codebase
```bash
uv run ruff format .
```
