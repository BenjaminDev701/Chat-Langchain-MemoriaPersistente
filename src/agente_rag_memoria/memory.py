from langchain_community.chat_message_histories import SQLChatMessageHistory


def get_session_history(session_id: str):
    # SQLChatMessageHistory nos sirve para crear automaticamente una tabla llamada message_store, dentro de donde ponemos el path,
    return SQLChatMessageHistory(
        session_id=session_id,
        connection="sqlite:///data/memoria.db"
    )
