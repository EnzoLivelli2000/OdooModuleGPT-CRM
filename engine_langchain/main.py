from langchain_odoo import ChatAgentLangChain

if __name__ == "__main__":
    # Instancia la clase ChatAgent
    agent = ChatAgentLangChain(
        database_uri="postgresql://postgres:postgres@44.201.40.20:5432/db_prueba",
        openai_model="gpt-3.5-turbo",
        openai_api_key="PONER API KEY ACÁ"
    )

    # Realiza una consulta usando el método query
    result_engine = agent.query("Cual es el numero celular de Theodore Gardner ?")