from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools()],
    debug_mode=True,
    instructions="Use tabelas para mostrar a informação final. Não inclua nenhum outro texto além da tabela."
)

agent.print_response("Qual a cotação do APPLE hoje? Me retorne em dolar e em reais", stream=True)
