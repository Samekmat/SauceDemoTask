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
├── .github/
│   └── workflows/
│       └── playwright.yml  # GitHub Actions CI workflow
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

---

## Approach and Experience (Brief Description)

**Architecture & Design Choices**
To ensure the test suite is robust and easily maintainable, I implemented the **Page Object Model (POM)** pattern. The logic for interacting with web elements is encapsulated in dedicated classes (`LoginPage` and `InventoryPage`), which keeps the actual test file (`test_saucedemo.py`) clean, readable, and focused purely on business logic. 

I chose the **synchronous Playwright API** because it integrates seamlessly with `pytest` via the `pytest-playwright` plugin, and since our test suite consists of straightforward E2E flows, synchronous execution is simpler and avoids the unnecessary complexity of managing async event loops. This allowed me to utilize built-in fixtures (like `page`) natively. To further improve stability, I exclusively used Playwright's auto-retrying web-first assertions (e.g., `expect(locator).to_be_visible()`) to eliminate flaky tests caused by timing issues.

**Going Beyond the Basics**
To demonstrate modern Python engineering standards, I incorporated **`uv`** for extremely fast and deterministic dependency management (via `uv.lock`) and **`Ruff`** for strict linting and code formatting. Additionally, I set up a GitHub Actions workflow to ensure Continuous Integration (CI) runs tests across all target browsers automatically.

**Test Scenarios Selected**
1. **Successful Login (Happy Path):** Validates core access functionality.
2. **Locked Out User (Edge Case):** Validates negative paths, error handling, and correct UI feedback.
3. **Add to Cart (E2E Flow):** Validates the interaction between multiple pages and UI state changes (cart badge updates).

**Overall Experience**
Using AI in this task was a huge time-saver. Since Python and pytest are the core tools in my daily tech stack, I felt very comfortable with the base setup. However, my previous test automation experience was primarily with Cypress. By delegating repetitive tasks - like generating boilerplate code and page locators - to the AI, I had more time to focus on Playwright's best practices. My main focus was reviewing the AI's output, ensuring it aligned with modern Playwright standards (such as web-first assertions), and building a clean architecture with solid documentation.



---

## AI Assistance & Prompts Used

I utilized AI (Gemini / Antigravity) as a pair-programming partner to accelerate the generation of boilerplate code, POM structures, and standard locators. The AI was highly effective at saving time on repetitive tasks. However, I maintained architectural control by specifically instructing the AI to use the POM pattern, the synchronous Playwright API, and strict web-first assertions. 

Below are the exact prompts used during the development process:

### Prompt 1: Initial POM Generation
> "Act as a Senior QA Automation Engineer. I need to automate tests for saucedemo.com using Python, pytest, and Playwright. The testing strategy must support cross-browser execution (Chromium, Firefox, WebKit). Please generate a Page Object Model class for the Login page. Include locators for username, password, login button, and error message. You can use chaining and filtering if needed. Use Playwright's sync API and include type hints."

### Prompt 2: Test Creation and Second POM
> "Now, let's write the actual tests in a `test_saucedemo.py` file. The 3 test scenarios are: 1. Successful login for 'standard_user'. 2. Failed login for 'locked_out_user'. 3. E2E flow: successful login, adding a specific item to the cart, and verifying the cart badge updates to '1'. To maintain the POM architecture, first generate an `InventoryPage` class for the third test. Then, generate the pytest file. Use Playwright's built-in auto-retrying assertions (`expect`) to prevent flaky tests. Assume we are using the built-in `page` fixture provided by pytest-playwright."

### Prompt 3: Refactoring and Configuration
> "To complete our test architecture, let's set up the configuration. Please generate a `conftest.py` file that creates pytest fixtures for our Page Objects (`login_page` and `inventory_page`), utilizing Playwright's built-in `page` fixture. Additionally, generate a `pytest.ini` file to configure the `base_url` and define default CLI options for our cross-browser execution strategy."

### Future Enhancements (Next Steps)
While the current test suite strictly satisfies the requirement of three automated tests, the architecture is designed to easily scale. The logical next steps for expanding this project would be:
* **Full E2E Checkout Flow:** Introducing `CartPage` and `CheckoutPage` objects to validate the entire purchase journey (filling shipping data, overview, and successful order submission).
* **Negative Checkout Scenarios:** Testing validation errors in the checkout form (e.g., missing postal code).
* **Parallel Execution:** Implementing `pytest-xdist` to run tests concurrently, drastically reducing execution time as the test suite grows.


