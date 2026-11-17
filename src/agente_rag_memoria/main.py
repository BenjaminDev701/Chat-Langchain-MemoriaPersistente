from agente_rag_memoria.chain import get_chain

chain = get_chain()

respuesta = chain.invoke(
    {"input": "Hola me llamo benjamin quiero saber que me reocmeindas mas irme a AI engieneer o desarrollo web, quiero el mejor salario y futuro, vivo en mexico y soy ing en desarrollo del software con 8 meses de experiencia laboral"},
    config={"configurable": {"session_id": "Usuario_creado_ayer"}}
)

print(respuesta.content)
