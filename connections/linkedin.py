import os
import requests
from dotenv import load_dotenv

load_dotenv()  

def scrape_linkedin_profile(linked_profile_url: str,mock:bool=False):
    """scrape information from a linkedin profile"""

    if mock:
        linked_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json"
        response = requests.get(
            linked_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        headers = {'Authorization': f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            headers=headers,
            params={'url': linked_profile_url},
            timeout=10,
        )
    data  = response.json()
    data = {
        k:v
        for k, v in data.items()
        if v not in ([],"","", None)
        and k not in ["people_also_viewed","certifications"]
    }
    return data

if __name__ == '__main__':
    print(
        scrape_linkedin_profile(
            linked_profile_url='https://www.linkedin.com/in/arshil-singh-bhatia/',
            mock=True
        )
    )