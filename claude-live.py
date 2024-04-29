print("Generating response...\n")

import sys

if len(sys.argv) != 2:
    print(
        """\nError: Correct uses is claude-live.py "question"\nExample: python claude-live.py "Who did the Commanders draft in the 2024 NFL draft?"\n"""
    )

question = sys.argv[1]
from claude_live import *

llm = ChatAnthropic(model=model, max_tokens=max_tokens, temperature=temperature)

retriever = TavilySearchAPIRetriever(k=10)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Answer the user's question based on the below context.\n\n{context}",
        ),
        ("user", '''{input}'''),
    ]
)

document_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": question})

print(f"You asked: {question}\n")
print(response["answer"])
