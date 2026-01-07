# Indeed Job Scraper

This Python script scrapes job postings from Indeed.com using a modular architecture that enhances maintainability and scalability. It leverages Selenium for robust browser automation and BeautifulSoup for efficient HTML parsing. The scraped data, including job titles, company names, and locations, is saved to a CSV file named `jobs_finder.csv`.

The script is designed with improved error handling and dynamic pagination, allowing it to navigate through job listings until no more pages are available. It also runs in headless mode by default to ensure a smooth, automated execution experience.

## Features

-   **Modular Design:** The script is organized into separate functions for scraping, saving data, and orchestrating the main process, making the codebase easier to manage and extend.
-   **Dynamic Pagination:** Instead of a fixed number of pages, the scraper dynamically detects and navigates to the next page, ensuring all available job postings are captured.
-   **Robust Error Handling:** The script includes `try-except` blocks to gracefully handle common issues like page load timeouts and missing elements, preventing unexpected crashes.
-   **Headless Operation:** By default, the script runs Chrome in headless mode, allowing it to execute in environments without a graphical user interface.
-   **CSV Header Management:** The script checks if the output CSV file already exists to avoid writing duplicate headers on subsequent runs.

## Setup

1.  **Install Python:** Make sure you have Python 3 installed on your system.
2.  **Install Dependencies:** Open your terminal or command prompt and run the following command to install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Install WebDriver:** This script uses Selenium with Chrome. You will need to have Google Chrome installed and the corresponding ChromeDriver. You can download ChromeDriver from the official website. Make sure the ChromeDriver executable is in your system's PATH.

## How to Run

1.  Open your terminal or command prompt.
2.  Navigate to the project directory.
3.  Run the script using the following command:
    ```bash
    python WebScraping_Project.py
    ```
4.  The script will prompt you to enter a job title/keyword and a location.
5.  After the script finishes, you will find the scraped data in `jobs_finder.csv`.
