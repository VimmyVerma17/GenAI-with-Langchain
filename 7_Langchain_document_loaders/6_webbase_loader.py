from langchain_community.document_loaders import WebBaseLoader
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
    template = 'Asnwer the following question \n {question} from the following text - \n {text}',
    input_variables = ['question', 'text']
)

parser = StrOutputParser()

url = 'https://www.dotandkey.com/products/watermelon-cooling-spf-50-face-sunscreen?utm_source=google&utm_medium=paid&utm_campaign=18108354709&utm_content=&utm_term=&gadid=&gad_source=1&gad_campaignid=18108358972&gbraid=0AAAAAC-nk22ck58in2n7rs1-M18q0K_5e&gclid=Cj0KCQiA0KrJBhCOARIsAGIy9wCm_RQkLXCVw5myzpA_SuZOSR297AmsEBBuIacMXtJJ0Ja8U6GGBfEaAk-bEALw_wcB'

loader = WebBaseLoader(url)

docs = loader.load()

# print(len(docs))

# print(docs[0].page_content)

chain = prompt | model | parser

print(chain.invoke({'question':'What is the price of the product?', 'text':docs[0].page_content}))