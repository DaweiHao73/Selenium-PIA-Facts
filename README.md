# PIA Facts Selenium Scraper

This project is a Selenium-based web scraper designed to automate the process of logging into PIA Facts, searching for product information using article numbers, and downloading product images.

## Features

- Automated login to PIA Facts
- Batch processing of article numbers from an Excel file
- Automated search and download of product images
- Handling of various image formats (JPEG, PNG)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- pip (Python package manager) installed
- Chrome browser installed
- ChromeDriver compatible with your Chrome version

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/dwhao84/Selenium-PIA-Facts
   cd Selenium-PIA-Facts
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `private_data.py` file in the project root and add your login credentials:
   ```python
   url = "XXXX"
   email_address = "your_emai.com"
   account = "your_username"
   password = "your_password"
   ```

## Usage

1. Prepare an Excel file named `file_1.xlsx` with a column named "貨號" containing the article numbers you want to search for.

2. Run the script:
   ```
   python main.py
   ```

3. The script will login to PIA Facts, search for each article number, and download the corresponding product images.

## Project Structure

- `main.py`: The main script that orchestrates the web scraping process
- `private_data.py`: Contains login credentials and URL (not tracked by Git)
- `private_data_template.py`: A template for `private_data.py`
- `file_1.xlsx`: Excel file containing article numbers to search for
- `.gitignore`: Specifies intentionally untracked files to ignore

## Contributing

Contributions to this project are welcome. Please ensure you update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)