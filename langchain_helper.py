import logging
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import load_tools, initialize_agent, AgentType
from dotenv import load_dotenv
import os

# load_dotenv()

def langchain_agent(query, openai_api_key):
    try:
        os.environ["OPENAI_API_KEY"] = openai_api_key
        llm = OpenAI(temperature=0.5)

        tools = load_tools(["wikipedia"], llm=llm)

        agent = initialize_agent(
            tools,
            llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )

        result = agent.run(question=query)

        return result
    
    except Exception as e:
        logging.error(f"An error occured: {e}")

        return "Sorry, I couldn't process your request at the moment. Please try again later"