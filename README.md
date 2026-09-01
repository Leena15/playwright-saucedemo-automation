# Playwright SauceDemo Portfolio

End-to-end test automation framework for [SauceDemo](https://www.saucedemo.com) built with **Playwright**, **Python**, and **pytest**.

## What This Covers

- **Login Tests** — valid login, locked-out user, empty fields, all user types
- **Inventory Tests** — product listing, add/remove cart, product detail navigation
- **Sorting Tests** — all four sort options verified
- **Cart Tests** — item persistence, removal, price accuracy, empty cart
- **Checkout Tests** — complete purchase flow, field validations, price calculations

## Architecture

- **Page Object Model** — every page is a class, tests read like sentences
- **Data-Driven** — credentials and test data in JSON fixture files
- **Cross-Browser** — configured for Chromium, Firefox, WebKit
- **CI/CD** — GitHub Actions runs tests on every push
- **HTML Reports** — pytest-html generates detailed test reports
- **Screenshot on Failure** — automatic screenshot capture on any test failure
- **Browser Isolation** — every test runs in a fresh browser context, no state leakage

## Setup

```
git clone https://github.com/<username>/playwright-saucedemo-portfolio.git
cd playwright-saucedemo-portfolio
pip install -r requirements.txt
playwright install
```

## Run Tests

```
pytest
```

## Run With Report

```
pytest --html=reports/report.html --self-contained-html
```

## Run Specific Suite

```
pytest tests/test_login.py
pytest tests/test_checkout.py
```

## Project Structure

```
pages/           — Page Object Model classes
tests/           — Test suites organized by feature
fixtures/        — Test data (JSON)
reports/         — Generated test reports
.github/         — CI/CD pipeline
```

## Author

Leena Deore  
leena.ahire15@gmail.com  
linkedin.com/in/leenadeore-261752169
