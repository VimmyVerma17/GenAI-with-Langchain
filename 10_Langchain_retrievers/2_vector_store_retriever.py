from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

model = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash",
    temperature = 0.4
)

load_dotenv()

documents = [
    Document(page_content = "LangChain helps developers build LLM applications easily."),
    Document(page_content = "Chroma is a vector database optimized for LLM-based search."),
    Document(page_content = "Embeddings convert text into high-dimensional vectors."),
    Document(page_content = "OpenAI provides powerful embedding models."),
]

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Creating Chroma vector store in memory
vectorstore = Chroma.from_documents(
    documents = documents,
    embedding = embeddings,
    collection_name = "my_collection"
)

# Converting vectorstore into a retriever
retriever = vectorstore.as_retriever(search_kwargs = {"k": 2})

query = "What is Chroma used for?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content) 