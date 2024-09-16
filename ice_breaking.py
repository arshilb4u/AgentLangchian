from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from connections.linkedin import scrape_linkedin_profile
load_dotenv()

information = """
        Elon Reeve Musk FRS  is a businessman and investor known for his key roles in the space company SpaceX and the automotive company Tesla, Inc. Other involvements include ownership of X Corp., the company that operates the social media platform X (formerly known as Twitter), and his role in the founding of The Boring Company, xAI, Neuralink, and OpenAI. He is one of the wealthiest individuals in the world; as of August 2024 Forbes estimates his net worth to be US$247 billion.[4]

            Musk was born in Pretoria to Maye (née Haldeman), a model, and Errol Musk, a businessman and engineer. Musk briefly attended the University of Pretoria before immigrating to Canada at the age of 18, acquiring citizenship through his Canadian-born mother. Two years later he matriculated at Queen's University at Kingston in Canada. Musk later transferred to the University of Pennsylvania and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University, but dropped out after two days and, with his brother Kimbal, co-founded the online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999. That same year Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal. In October 2002, eBay acquired PayPal for $1.5 billion. Using $100 million of the money he made from the sale of PayPal, Musk founded SpaceX, a spaceflight services company, in 2002.

            In 2004, Musk was an early investor who provided most of the initial financing in the electric-vehicle manufacturer Tesla Motors, Inc. (later Tesla, Inc.), assuming the position of the company's chairman. He later became the product architect and, in 2008, the CEO. In 2006, Musk helped create SolarCity, a solar energy company that was acquired by Tesla in 2016 and became Tesla Energy. In 2013, he proposed a hyperloop high-speed vactrain transportation system. In 2015, he co-founded OpenAI, a nonprofit artificial intelligence research company. The following year Musk co-founded Neuralink—a neurotechnology company developing brain–computer interfaces—and The Boring Company, a tunnel construction company. In 2018 the U.S. Securities and Exchange Commission (SEC) sued Musk, alleging that he had falsely announced that he had secured funding for a private takeover of Tesla. To settle the case Musk stepped down as the chairman of Tesla and paid a $20 million fine. In 2022, he acquired Twitter for $44 billion, merged the company into the newly-created X Corp. and rebranded the service as X the following year. In March 2023, Musk founded xAI, an artificial-intelligence company.

            Musk has expressed views that have made him a polarizing figure.[5] He has been criticized for making unscientific and misleading statements, including COVID-19 misinformation, promoting right-wing conspiracy theories, and "endorsing an antisemitic theory"; he later apologized for the latter.[6][5][7] His ownership of Twitter has been similarly controversial given the layoffs of large numbers of employees, an increase in hate speech, misinformation and disinformation posts on the website, and changes to Twitter Blue verification.

            Early life and education
            Childhood and family
            See also: Family of Elon Musk
            Elon Reeve Musk was born on June 28, 1971, in Pretoria, South Africa's administrative capital.[8][9] He is of British and Pennsylvania Dutch ancestry.[10][11] His mother, Maye (née Haldeman), is a model and dietitian born in Saskatchewan, Canada, and raised in South Africa.[12][13][14] His father, Errol Musk, is a South African electromechanical engineer, pilot, sailor, consultant, emerald dealer, and property developer, who partly owned a rental lodge at the Timbavati Private Nature Reserve.[15][16][17][18] Elon has a younger brother, Kimbal, and a younger sister, Tosca.[14][19] Elon has four paternal half-siblings.[20][21][22]

            The family was wealthy during Elon's youth.[18] Despite both Musk and Errol previously stating that Errol was a part owner of a Zambian emerald mine,[18] in 2023, Errol recounted that the deal he made was to receive "a portion of the emeralds produced at three small mines."[23][24] Errol was elected to the Pretoria City Council as a representative of the anti-apartheid Progressive Party and has said that his children shared their father's dislike of apartheid.[8]

            Elon's maternal grandfather, Joshua N. Haldeman, was an American-born Canadian who took his family on record-breaking journeys to Africa and Australia in a single-engine Bellanca airplane; Haldeman died when Elon was still a toddler.[21][25][26][27]

            Elon has recounted trips to a wilderness school ("veldskool") that he described as a "paramilitary Lord of the Flies" where "bullying was a virtue" and children were encouraged to fight over rations.[28]

        """
if __name__ == "__main__":
    print("Hello Langchain")
    summary_template = """
            given the information {information} about a person from I want you to create:
            1. a short summary
            2. two interesting facts about them
        """
    
    
    
    summary_prompt_template = PromptTemplate(input_variables = ["information"], template = summary_template)

    llm = ChatOpenAI(temperature=0,model_name = "gpt-3.5-turbo")

    chain = summary_prompt_template | llm
    linkedin_data = scrape_linkedin_profile(linked_profile_url = "https://www.linkedin.com/in/arshil-singh-bhatia/",mock=True)

    res = chain.invoke(input = {"information":linkedin_data})
    print(res)