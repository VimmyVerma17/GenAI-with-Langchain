from langchain_community.retrievers import WikipediaRetriever
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.4
)

load_dotenv()

# Initializing the retriever 
retriever = WikipediaRetriever(top_k_results = 2, lang = "en")


# Defining the query
query = "the geopolitical history of india and pakistan from the perspective of a chinese"

# Getting relevant Wikipedia documents
docs = retriever.invoke(query)

print(docs)

# Printing retrieved content
for i, doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...")  # truncating for display