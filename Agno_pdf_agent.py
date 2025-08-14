from agno.agent import Agent
from agno.playground import Playground, serve_playground_app
from agno.storage.sqlite import SqliteStorage
from agno.models.openai import OpenAIChat

from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.chroma import ChromaDb

from dotenv import load_dotenv
load_dotenv()

# RAG
vector_db = ChromaDb(collection="pdf_agent", path="tmp/chromadb", persistent_client=True)


knowledge = PDFKnowledgeBase(
path="GlobalEVOutlook2025.pdf",
vector_db=vector_db,
reader=PDFReader(chunk=True)
)
# knowledge.load(recreate=True)


db = SqliteStorage(table_name="agent_session", db_file='tmp/agent.db')


agent = Agent(
    # model=Groq(id="llama-3.3-70b-versatile"),
    name="Agente de pdf",
    model=OpenAIChat("gpt-4.1-mini"),
    storage=db,
    knowledge=knowledge,
    instructions="Você deve chamar o usuário de senhor",
    description="",
    add_history_to_messages=True,
    num_history_runs=3,
    debug_mode=True,
)

playground_app = Playground(agents=[agent])
app = playground_app.get_app()

if __name__ == "__main__":
    
    playground_app.serve("Agno_pdf_agent:app", reload=True)

