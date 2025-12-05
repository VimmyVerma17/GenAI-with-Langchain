from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt = PromptTemplate(
    template='Write a joke on {topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.4
)

parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser)

result = chain.invoke({'topic': 'AI'})
print(result)
