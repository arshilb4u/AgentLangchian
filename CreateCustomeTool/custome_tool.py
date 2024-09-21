from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.tools import Tool,tool
from langchain.tools.render import render_text_description
from langchain.agents.output_parsers import ReActSingleInputOutputParser

@tool
def get_text_length(text:str)->str :
    """Return the length of text by character"""
    text = text.strip("\n").strip()
    return len(text)

@tool
def covert_to_lower(text:str)->str :
    """Return the lower case text by character"""
    return text.lower().strip()

if __name__ == '__main__':
    print("Custome tools loading....")

    tools = [get_text_length,covert_to_lower]

    templates = """
            Answer the following questions as best you can. You have access to the following tools:

            {tools}

            Use the following format:

            Question: the input question you must answer

            Thought: you should always think about what to do

            Action: the action to take, should be one of [{tool_names}]

            Action Input: the input to the action

            Observation: the result of the action

            ... (this Thought/Action/Action Input/Observation can repeat N times)

            Thought: I now know the final answer

            Final Answer: the final answer to the original input question

            Begin!

            Question: {input}

            Thought:
                    """
    

    prompt = PromptTemplate.from_template(template=templates).partial(
        tools = render_text_description(tools),
        tool_names = ", ".join(t.name for t in tools)
    )

    llm = ChatOpenAI(temperature=0,
                     stop=["\nObservation","Observation"])
    

    agent = (
        {
            "input": lambda x: x["input"]
        }
        | prompt
        | llm
        | ReActSingleInputOutputParser()
    )

    agent_steps = agent.invoke({"input": "What is the lower case of  'DOG' "})
    print(agent_steps)
   