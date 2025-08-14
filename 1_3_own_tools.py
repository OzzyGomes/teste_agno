from agno.agent import Agent
from agno.tools.tavily import TavilyTools
# from agno.models.groq import Groq
from agno.models.openai import OpenAIChat

from agno.storage.sqlite import SqliteStorage

from agno.playground import Playground, serve_playground_app


from dotenv import load_dotenv
load_dotenv()

def celsius_to_fh(temp_c: float):
    """
    Converte temperatura de Celsius para Fahrenheit.

    Args:
        temp_c: Temperatura em Celsius

    Returns:
        Temperatura em Fahrenheit
    """
    return (temp_c * 9/5) + 32

db = SqliteStorage(table_name="agent_session", db_file='tmp/agent.db')


agent = Agent(
    # model=Groq(id="llama-3.3-70b-versatile"),
    name="Agente do tempo",
    model=OpenAIChat("gpt-4.1-mini"),
    tools=[TavilyTools(),
    celsius_to_fh],
    storage=db,
    add_history_to_messages=True,
    num_history_runs=3,
    debug_mode=True,
)

playground_app = Playground(agents=[agent])
app = playground_app.get_app()

if __name__ == "__main__":
    playground_app.serve("1_3_own_tools:app", reload=True)






# agent.print_response("Qual a temperatura hoje a noite em Barueri? Me retorne em Fahrenheit.")