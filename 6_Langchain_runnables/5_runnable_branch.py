from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Write a deatiled report on the {topic}',
    input_variables = ['topic'] 
)

prompt2 = PromptTemplate(
    template = 'Summarize the following \n {text}',
    input_variables = ['text'] 
)

model = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash",
    temperature = 0.4
)

parser = StrOutputParser()

report_generate_chain = RunnableSequence(prompt1, model, parser)

# branch_chain = RunnableBranch(
#     (condition, runnable)
#     deafult()
# )

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, prompt2 | model | parser), #x is the output of parser
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_generate_chain, branch_chain)

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))

