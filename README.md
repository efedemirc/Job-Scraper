# Indeed Job Scraper

This Python script scrapes job postings from Indeed.com based on user-provided keywords and locations. The scraped data, including job titles, company names, and locations, is saved to a CSV file named `jobs_finder.csv`.

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

## Limitations

-   **Pagination:** The current pagination logic is basic and might not scrape all available pages. It iterates through a fixed range of pages.
-   **Error Handling:** The script has minimal error handling. If a page doesn't load or an element is not found, the script might fail.
-   **Dynamic Content:** The script might not work correctly if Indeed.com changes its website structure or uses more dynamic content loading that this script doesn't handle.
