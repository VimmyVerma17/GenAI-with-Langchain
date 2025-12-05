from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.4
)

# Step 1a - Indexing (Document Ingestion)
video_id = "Gfr50f6ZBvo"  # Only the video ID

try:
    # Fetch transcript (default English)
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    
    # Combine transcript chunks into a single string
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    print("Transcript fetched successfully!\n")
    print(transcript[:500], "...")  # Prints first 500 characters for preview

except TranscriptsDisabled:
    print("No captions available for this video.")
    transcript_list = []

# Step 1b - Indexing (Text Splitting)
# This is needed for embeddings, as models have token limits
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])

print(f"Total chunks created: {len(chunks)}")

print(chunks[0].page_content[:300], "...")

# Step 1c & 1d - Indexing (Embedding Generation and Storing in Vector Store)
# Initialize embeddings 
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001") 

vector_store = FAISS.from_documents(chunks, embeddings)

print("Vector store ready. Number of vectors:", len(vector_store.index_to_docstore_id))

# Step 2 - Retrieval
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}  
)

example_docs = retriever.invoke('What is deepmind')
print("Retrieved docs example:", example_docs)

# Step 3 - Augmentation
llm = ChatGoogleGenerativeAI("gemini-2.0-flash", temperature=0.2)

prompt = PromptTemplate(
    template="""
    You are a helpful assistant.
    Answer ONLY from the provided transcript context.
    If the context is insufficient, just say you don't know.

    {context}
    Question: {question}
    """,
    input_variables=['context', 'question']
)

question = "Is the topic of nuclear fusion discussed in this video? If yes then what was discussed"

retrieved_docs = retriever.invoke(question)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
print("Context for LLM:\n", context_text[:500], "...")  # preview

final_prompt = prompt.invoke({"context": context_text, "question": question})

answer = llm.invoke(final_prompt)
print("\nAnswer:\n", answer.content)

# Building a Chain
def format_docs(retrieved_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_text

# Create a parallel chain for question & context
parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})

print("\nParallel chain test:")
print(parallel_chain.invoke('Who is Demis?'))

parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

summary = main_chain.invoke('Can you summarize the video?')
print("\nVideo Summary:\n", summary)
