# Testing Strategy

## Scope

This framework tests the SauceDemo e-commerce web application — a standard Sauce Labs demo platform used for automation practice. The test suite covers the complete user journey from login through checkout completion.

## Approach

### Page Object Model

Every page in the application has a corresponding Python class in the `pages/` directory. Page classes encapsulate all selectors and user interactions. Test files never reference raw selectors — they call page methods. This separation means if the UI changes, only the page class is updated; all tests using that page remain untouched.

### Data-Driven Testing

All test data lives in `fixtures/` as JSON files. Credentials, product data, and checkout information are externalized from test code. Tests load fixture data through pytest fixtures defined in `conftest.py`. This makes it easy to add new test data without modifying test logic.

### Test Organization

Tests are grouped by feature area:
- `test_login.py` — authentication and access control
- `test_inventory.py` — product display and cart interaction
- `test_sorting.py` — sort functionality across all options
- `test_cart.py` — cart operations and state management
- `test_checkout.py` — purchase flow and validation

### User Type Coverage

Unlike most SauceDemo automation projects that only test `standard_user`, this suite tests all six user types:
- `standard_user` — happy path baseline
- `locked_out_user` — negative authentication test
- `problem_user` — UI rendering defect detection
- `performance_glitch_user` — slow response handling
- `error_user` — error state validation
- `visual_user` — visual inconsistency detection

### Browser Isolation

Every test runs in a fresh browser context. No cookies, localStorage, or session state carries over between tests. This ensures tests are independent and can run in any order without affecting each other. pytest-playwright manages the browser lifecycle automatically — each test function receives a clean `page` instance.

### Screenshot on Failure

When a test fails, Playwright automatically captures a screenshot of the browser at the point of failure. Screenshots are saved to `reports/screenshots/<test_name>.png` and embedded in the HTML report. This eliminates the need to reproduce failures manually — the evidence is captured at the moment of failure.

### Timeout Strategy

- Navigation timeout: 30 seconds (accommodates performance_glitch_user's intentional delays)
- Action timeout: 10 seconds (clicking, filling, selecting)
- Timeouts are configured globally in conftest.py, not scattered across individual tests

### CI/CD Integration

GitHub Actions runs the full suite on every push to `main`. The workflow installs Python, Playwright, and dependencies, executes all tests headlessly, and uploads the HTML report as an artifact. A failing test blocks the build. Reports are retained for 30 days.

### Reporting

pytest-html generates a self-contained HTML report after every run. Reports include pass/fail status, execution time, failure details with screenshots, and test duration per suite.

## Coverage Matrix

| Area | Test Count | Positive | Negative |
|---|---|---|---|
| Login | 8 | 3 | 5 |
| Inventory | 8 | 7 | 1 |
| Sorting | 5 | 5 | 0 |
| Cart | 6 | 5 | 1 |
| Checkout | 8 | 3 | 5 |
| **Total** | **35** | **23** | **12** |

## Tools

| Tool | Purpose |
|---|---|
| Playwright | Browser automation |
| Python 3.11 | Programming language |
| pytest | Test framework |
| pytest-html | HTML report generation |
| GitHub Actions | CI/CD pipeline |
