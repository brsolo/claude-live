from claude_live import *

llm = ChatAnthropic(model=model, max_tokens=max_tokens, temperature=temperature)

retriever = TavilySearchAPIRetriever(k=10)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Answer the user's question based on the below context. Be concise with your answer. \n\n{context}",
        ),
        ("user", "{input}"),
    ]
)

document_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke(
    {"input": "Who did the Commanders draft in the 2024 NFL draft?"}
)
print(response["answer"])
