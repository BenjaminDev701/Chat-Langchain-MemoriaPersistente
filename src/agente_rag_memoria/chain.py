from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from agente_rag_memoria.config import get_llm
from agente_rag_memoria.memory import get_session_history


def get_chain():
    prompt = ChatPromptTemplate.from_messages(
        [
            # prompt de el modelo
            ("system", "Eres un asistente útil y directo. Responde de forma clara."),
            MessagesPlaceholder(variable_name="history"),
            # lo que manda el usuario
            ("human", "{input}")
        ]
    )

    # Union del modelo y de el prompt
    chain = prompt | get_llm

    # esto sirve para dar memoria al modelo
    return RunnableWithMessageHistory(
        chain,
        # esto da la memoria de la session = session_id
        get_session_history,
        # aqui ponemos la variable por el cual entra el mensaje del usuario
        input_messages_key="input",
        # la variable que el prompt que espera insertar los mensajes anteriores
        history_messages_key="history"
    )
