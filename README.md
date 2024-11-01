# Automated Testing with Selenium, Pytest, and Allure

This project contains automated test cases using **Selenium WebDriver** and **Pytest** with **Allure** reporting to validate the sorting functionality on the [OpenCart](https://www.opencart.com/index.php?route=cms/demo) website.

---

## Table of Contents

- [Requirements](https://github.com/quangxuan98765/ktpm?tab=readme-ov-file#requirements)
- [Setup Instructions](https://github.com/quangxuan98765/ktpm?tab=readme-ov-file#setup-instructions)
- [Running the Tests](https://github.com/quangxuan98765/ktpm?tab=readme-ov-file#running-the-tests)
- [Generating Allure Reports](https://github.com/quangxuan98765/ktpm?tab=readme-ov-file#generating-allure-reports)
- [Notes](https://github.com/quangxuan98765/ktpm?tab=readme-ov-file#notes)

---

## Requirements

### 1. Software

- **Python**: Version 3.9 or higher
- **Browser**: Microsoft Edge (or modify to use Chrome, Firefox, etc.)
- **Edge WebDriver**: Should match the version of your Edge browser (see instructions below).
- **Allure**: For generating detailed reports.

### 2. Python Libraries

- **Selenium**: For browser automation
- **Pytest**: For running and managing test cases
- **Allure-Pytest**: For integrating Allure with Pytest

---

## Setup Instructions

### 1. Install Python

1. [Download Python](https://www.python.org/downloads/) and install it, making sure to select the option to "Add Python to PATH" during installation.
2. Verify the installation by running:
    
    ```bash

    python --version
    
    ```
    

### 2. Install Required Python Packages

1. Open a terminal in VS Code by navigating to **Terminal > New Terminal**.
2. Create a virtual environment by running:
    
    ```bash

    python -m venv venv
    
    ```
    
3. Activate the virtual environment:
    - On Windows:
        
        ```bash

        venv\Scripts\activate
        
        ```
        
    - On macOS/Linux:
        
        ```bash
        
        source venv/bin/activate
        
        ```
        
4. Use `pip` to install Selenium, Pytest, and Allure-Pytest:
    
    ```bash
    
    pip install selenium pytest allure-pytest
    
    ```
    

### 3. Install Allure Command-Line Tool

1. [Download Allure](https://github.com/allure-framework/allure2/releases) and follow the installation instructions for your operating system.
2. Verify the installation by running:
    
    ```bash

    allure --version
    
    ```
    

### 4. Set Up Edge WebDriver

To automate tests with Microsoft Edge:

1. Check your **Microsoft Edge** version by going to `edge://settings/help`.
2. Download the corresponding **Edge WebDriver** version from [Microsoft's WebDriver site](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
3. Place the `msedgedriver.exe` in a directory within your **system PATH**, or update the `driver` fixture in your script to point to the exact path of the driver file.

Alternatively, if using **Chrome**:

- Replace `webdriver.Edge()` with `webdriver.Chrome()` in the script, and download **ChromeDriver** instead.

### 5. Test Environment Configuration

1. Ensure a stable internet connection, as tests will interact with the online [OpenCart Demo](https://www.opencart.com/index.php?route=cms/demo) site.
2. Confirm that the elements on the page are up-to-date with the OpenCart demo setup.

---

## Running the Tests

### Command Line Execution

To execute all tests and generate Allure results, navigate to the project directory and run:

```bash

pytest <your_script_name>.py --alluredir=allure-results

```

This command will save test results in the `allure-results` directory.

---

## Generating Allure Reports

1. After running the tests, generate the Allure report using:
    
    ```bash

    allure serve allure-results
    
    ```
    
    This command will generate and open the Allure report in your default browser.
    


## Notes

- The Edge WebDriver version must match your installed Edge browser version to avoid compatibility issues.
- If the OpenCart elements or layout changes, you may need to update locators in your tests.

---

This setup should allow you to run tests, generate detailed Allure reports, and export the results to other formats if needed.
