from typing import Any
import requests
from bs4 import BeautifulSoup
import pandas as pd

SAVE_TO_PATH = '05-Professional-Section/Day-093 - Professional Portfolio Project - [Web Scraping]/'

url = "https://justjoin.it/all-locations/python/employment-type_b2b.permanent/remote_yes/salary_9000.100000/working-hours_full-time"

def fetch_job_data(url: str) -> Any:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad status codes

        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    return None

def extract_jobs(soup) -> list:
    jobs_data = []
    job_cards = soup.select('div[data-index]')

    for job in job_cards:
        try:
            title = job.find('h3', class_='css-1gehlh0').text.strip() if job.find('h3', class_='css-1gehlh0') else "N/A"
            company = job.find('div', class_='css-1mx97sn').find('span').text.strip() if job.find('div', class_='css-1mx97sn') else "N/A"
            salary = job.find('div', class_='MuiBox-root css-70qvj9').text.strip() if job.find('div', class_='MuiBox-root css-70qvj9') else "N/A"
            location = job.find('span', class_='css-1o4wo1x').text.strip() if job.find('span', class_='css-1o4wo1x') else "N/A"
            skills = [skill.text.strip() for skill in job.select('div[class^="skill-tag-"] .css-1qruno6')]

            jobs_data.append({
                'Title': title,
                'Company': company,
                'Salary': salary,
                'Location': location,
                'Skills': ', '.join(skills)
            })

        except Exception as e:
            print(f"Error extracting data for a job: {e}")
            continue

    return jobs_data

def save_to_csv(jobs_data: list, filename: str, file_path: str = SAVE_TO_PATH) -> None:
    try:
        df = pd.DataFrame(jobs_data)
        df.to_csv(file_path+filename, index=False)
        print(f"Data scraped and saved to {file_path+filename}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")  # Log any errors during saving

def main():
    # Fetch job data
    soup = fetch_job_data(url)
    if soup:
        # Extract job listings
        jobs_data = extract_jobs(soup)
        # Save data to CSV
        if jobs_data:  # Only save if there's data
            save_to_csv(jobs_data, 'justjoin_jobs.csv')

if __name__ == "__main__":
    main()
