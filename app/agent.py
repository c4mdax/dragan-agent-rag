from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from app.settings import LLM_CONFIG
from app.vectorstore import get_vectorstore, get_retriever
from app.loader import list_valid_files, load_documents

# Prompt template
PROMPT_TEMPLATE = """
Eres un asistente especializado en análisis de documentos. Responde en español usando ÚNICAMENTE la información proporcionada en el contexto, haciendo paráfrasis de la información evitando redundancias, cacofonias y enunciados sin sentido. 

Si el contexto no contiene información relevante a la pregunta, reporta agradablemente (si quieres puedes usar emojis) que no hay información suficiente en los documentos proporcionados, invitando al usuario a proporcionar más documentos relacionados.

Contexto:
{context}

Pregunta: 
{question}

Respuesta (en español):
"""

def setup_llm_chain():
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    
    # LLM manager
    llm = OllamaLLM(**LLM_CONFIG)
        
    return (
        {"context": RunnablePassthrough(), "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

def answer_question(question: str, docs_path: str, rebuild: bool = False) -> str:
    # 1. Loading files
    files = list_valid_files(docs_path)
    docs = load_documents(files)
    
    # 2. Vector basis
    vectordb = get_vectorstore(docs, rebuild)
    retriever = get_retriever()
    
    # 3. Recovering relevant context
    relevant_docs = retriever.invoke(question)
    context = "\n\n".join([d.page_content for d in relevant_docs]) if relevant_docs else None
    
    if not context:
        return "No encontré información relevante en los documentos proporcionados."
    
    # 4. LLM consult
    llm_chain = setup_llm_chain()
    return llm_chain.invoke({"context": context, "question": question})
