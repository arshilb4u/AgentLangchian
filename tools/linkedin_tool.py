from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv
load_dotenv()


def get_profile_url_travily(name: str):
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]

if __name__ == "__main__":
    print(get_profile_url_travily("Arshil Singh Bhatia"))
