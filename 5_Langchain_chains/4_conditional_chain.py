from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash",
    temperature = 0.4
)

parser1 = StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description = 'Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object = feedback)

prompt1 = PromptTemplate(
    template = 'Classify the semtiment of the following feedback into positive or negative \n {feedback} \n {format_instruction}',
    input_variables = ['feedback'],
    partial_variables = {'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template = 'Write an appropriate response to this positive feedback \n {feedback}',
    input_variables = ['feedback'],
)

prompt3 = PromptTemplate(
    template = 'Write an appropriate response to this negative feedback \n {feedback}',
    input_variables = ['feedback'],
)

# syntax
# branch_chain = RunnableBranch(
#     (condition1, chain1),
#     (condition2, chain2),
#     default chain
# )

branch_chain = RunnableBranch(
     (lambda x:x.sentiment == 'positive', prompt2 | model | parser1),
     (lambda x:x.sentiment == 'negative', prompt3 | model | parser1),
     RunnableLambda(lambda x: "could not find sentiment")
)

final_chain = classifier_chain | branch_chain

# result = final_chain.invoke({'feedback': 'This is a terrible phone'})

result = final_chain.invoke({'feedback': 'This is a beautiful phone'})

print(result)

final_chain.get_graph().print_ascii()
