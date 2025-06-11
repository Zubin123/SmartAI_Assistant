from langchain_community.chat_models import ChatOllama
from langchain.agents import initialize_agent
from langchain.tools import Tool
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StdOutCallbackHandler
from tools import calculator, wiki_search

# Initialize the local LLM
llm = ChatOllama(model="mistral")

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
    response = agent.invoke(query)  # ✅ correct method
    print(f"Assistant: {response}")
