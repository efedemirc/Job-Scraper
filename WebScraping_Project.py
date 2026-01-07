# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:03:24 2024

@author: Asus
"""

from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import re
import os

def scrape_page(url, driver):
    """
    Scrapes a single page of job postings.
    """
    driver.get(url)
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.job_seen_beacon'))
        )
    except TimeoutException:
        print("Timeout while waiting for page to load.")
        return []

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    jobs = []
    job_elements = soup.find_all('div', class_='job_seen_beacon')

    for job_elem in job_elements:
        title_elem = job_elem.find('span', id=re.compile(r'^jobTitle-'))
        company_elem = job_elem.find('span', {'data-testid': 'company-name'})
        location_elem = job_elem.find('div', {'data-testid': 'text-location'})

        if title_elem and company_elem and location_elem:
            jobs.append([title_elem.text.strip(), company_elem.text.strip(), location_elem.text.strip()])

    return jobs

def save_to_csv(jobs, file_path):
    """
    Saves a list of jobs to a CSV file.
    """
    file_exists = os.path.isfile(file_path)
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Job Title', 'Company Name', 'Location'])
        writer.writerows(jobs)

def main():
    """
    Main function to orchestrate the scraping process.
    """
    query = input("Enter company name, keyword or job title: ")
    location = input("Enter desired location: ")
    base_url = f"https://de.indeed.com/jobs?q={query}&l={location}"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(options=options)
    all_jobs = []

    page = 0
    while True:
        url = f"{base_url}&start={page * 10}"
        print(f"Scraping page {page + 1}...")

        jobs = scrape_page(url, driver)
        if not jobs:
            print("No more jobs found, stopping.")
            break

        all_jobs.extend(jobs)

        # Check for the next page button
        try:
            driver.find_element(By.CSS_SELECTOR, 'a[data-testid="pagination-page-next"]')
            page += 1
        except NoSuchElementException:
            print("Reached the last page.")
            break

    driver.quit()

    file_path = 'jobs_finder.csv'
    save_to_csv(all_jobs, file_path)

    print(f'Job data have been saved to {file_path}')

if __name__ == "__main__":
    main()