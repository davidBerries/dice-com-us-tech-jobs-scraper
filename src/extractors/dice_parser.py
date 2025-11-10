thonimport requests
from bs4 import BeautifulSoup

class DiceParser:
    def __init__(self, settings):
        self.base_url = "https://www.dice.com/jobs"
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.settings = settings

    def scrape_jobs(self):
        job_list = []
        params = {
            "q": self.settings["job_query"],
            "l": self.settings["location"],
            "start": 0
        }

        response = requests.get(self.base_url, params=params, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        job_cards = soup.find_all("div", class_="card")
        for card in job_cards:
            job = self.parse_job(card)
            job_list.append(job)

        return job_list

    def parse_job(self, card):
        job = {}
        job['url'] = card.find("a", class_="jobTitle")['href']
        job['title'] = card.find("a", class_="jobTitle").text.strip()
        job['company_name'] = card.find("div", class_="company").text.strip()
        job['location'] = card.find("div", class_="location").text.strip()
        job['salary'] = card.find("div", class_="salary").text.strip() if card.find("div", class_="salary") else 'N/A'
        job['skills'] = [skill.text.strip() for skill in card.find_all("span", class_="skill")]
        return job