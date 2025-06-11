from langchain_community.chat_models import ChatOllama
from langchain.agents import initialize_agent
from langchain.tools import Tool
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StdOutCallbackHandler
from tools import calculator, wiki_search
from logger_config import setup_logger

# Initialize the local LLM
llm = ChatOllama(model="mistral")
# Setup logger
logger = setup_logger()
# Tools
tools = [
    Tool(
    name="Calculator",
    func=calculator,
    description="Useful for evaluating math expressions like '3 + 5 * 2'."
),
Tool(
    name="Wikipedia Search",
    func=wiki_search,
    description="Useful for answering general knowledge questions by searching Wikipedia."
)
]

# Enable callback for tracing steps
handler = StdOutCallbackHandler()

# Build agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
    callbacks=[handler]
)

# REPL loop
print("🤖 Local Smart Assistant (type 'exit' to quit)")

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break

    logger.info(f"User Query: {query}")
    
    try:
        response = agent.run(query)
        logger.info(f"Assistant Response: {response}")
    except Exception as e:
        response = f"Error: {str(e)}"
        logger.error(f"Assistant Error: {str(e)}")

    print(f"Assistant: {response}")