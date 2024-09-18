from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from connections.linkedin import scrape_linkedin_profile
load_dotenv()
from agents.linkedin_agents import lookup as linkedin_lookup_agent
from output_parsers import summary_parser

def ice_break_with(name: str):
    linked_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linked_profile_url=linked_username)
    summary_template = """
            given the information {information} about a person from I want you to create:
            1. a short summary
            2. two interesting facts about them

            \n {format_instructions}
        """
    
    
    
    summary_prompt_template = PromptTemplate(input_variables = ["information"], 
                                             template = summary_template,
                                             partial_variables={"format_instructions":summary_parser.get_format_instructions()}
                                             )

    llm = ChatOpenAI(temperature=0,model_name = "gpt-3.5-turbo")

    chain = summary_prompt_template | llm | summary_parser
    

    res = chain.invoke(input = {"information":linkedin_data})
    print(res)

if __name__ == "__main__":
    print("Ice Break Enter")
    ice_break_with(name="Arshil Singh Bhatia Globant ")
    