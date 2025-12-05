from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  
    temperature=0.3
)

# Defining Tool
@tool
def multiply(a: int, b: int) -> int:
    """Given 2 numbers a and b this tool returns their product"""
    return a * b

# Binding tools
llm_with_tools = llm.bind_tools([multiply])

# Asking model to use tool
query = HumanMessage("can you multiply 3 with 1000?")
messages = [query]

# LLM response (with tool call)
result = llm_with_tools.invoke(messages)
messages.append(result)

# Executing tool if requested
tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)

final = llm_with_tools.invoke(messages)
print(final.content)

print(multiply.name)
print(multiply.description)
print(multiply.args)
