from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

MODEL = "gemma3:1b"

TEMPLATE = """
    Question: {question}
    Answer: Let's think step by step.
"""


def main():
    model = OllamaLLM(model=MODEL)
    prompt = ChatPromptTemplate.from_template(TEMPLATE)
    chain = prompt | model
    output = chain.invoke({"question": "What is Git?"})

    print(output)


if __name__ == "__main__":
    main()
