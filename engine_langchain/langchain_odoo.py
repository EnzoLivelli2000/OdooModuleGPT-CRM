import psycopg2
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

class ChatAgentLangChain:
    def __init__(self, database_uri, openai_model, openai_api_key):
        self.db = SQLDatabase.from_uri(database_uri)
        self.llm = ChatOpenAI(model=openai_model, temperature=0, api_key=openai_api_key)
        self.agent_executor = create_sql_agent(self.llm, db=self.db, agent_type="openai-tools", verbose=True)

    def query(self, query_text):
        response = self.agent_executor.invoke(query_text)
        return response["output"]
    

