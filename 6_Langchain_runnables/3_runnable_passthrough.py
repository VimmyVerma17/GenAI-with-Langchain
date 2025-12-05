from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Write a joke on {topic}',
    input_variables = ['topic'] 
)

prompt2 = PromptTemplate(
    template = 'Explain the following joke \n {text}',
    input_variables = ['text'] 
)

model = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash",
    temperature = 0.4
)

parser = StrOutputParser()

joke_generate_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),                           
    "explanation": RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_generate_chain, parallel_chain)

result = final_chain.invoke({"topic": "cricket"})

print("Joke: ", result["joke"])
print("Explanation:", result["explanation"])