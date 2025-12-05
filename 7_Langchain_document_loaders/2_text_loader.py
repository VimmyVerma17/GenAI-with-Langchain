from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.4
)

prompt = PromptTemplate(
    template = 'Write a summary for the following article - \n {article}',
    input_variables = ['article']
)

parser = StrOutputParser()

loader = TextLoader('football.txt', encoding = 'utf-8')

docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0])

print(type(docs[0]))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

result = chain.invoke({'article': docs[0].page_content})

print(result)

