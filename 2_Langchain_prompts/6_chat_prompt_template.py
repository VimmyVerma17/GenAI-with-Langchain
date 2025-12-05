from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# chat_template = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful {domain} expert."),
#     ("human", "Explain in simple terms, what is {topic}?")
# ])

# prompt = chat_template.invoke({
#     "domain": "cricket",
#     "topic": "Dusra"
# })

# result = model.invoke(prompt)

# print(result.content)
