# NU Course Registration Automation Bot

This project is a Python automation script that helps automate the course registration process on the Nazarbayev University Registrar website.

The script uses **Selenium WebDriver** to simulate browser actions such as logging in, navigating to the course registration page, searching for a course, and completing the registration process.

## Features

The script performs the following steps automatically:

1. Opens the NU Registrar website
2. Logs into the user account
3. Navigates to the **Course Registration** page
4. Searches for a specified course
5. Selects the course from the results
6. Completes the registration process

## Technologies Used

- Python
- Selenium
- ChromeDriver

## Installation

Install required dependencies:

```bash
pip install selenium
```

Download and install **ChromeDriver** compatible with your Chrome version.

## Usage

Before running the script, replace the placeholders in the code with your credentials:

```python
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
```

Run the script:

```bash
python rega.py
```

The script will open a browser and perform the registration steps automatically.

## Disclaimer

This project was created for **educational purposes** to demonstrate browser automation using Selenium.

Users should ensure they comply with university policies when using automation tools.
