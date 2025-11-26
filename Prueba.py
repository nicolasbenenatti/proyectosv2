# chatbot_trafico.py

def responder(pregunta):
    pregunta = pregunta.lower()
    
    if "turno" in pregunta:
        return "El coordinador de turno es María Fernández."
    elif "unidad 123" in pregunta:
        return (
            "Unidad 123:\n"
            "- Chofer: Carlos Gómez\n"
            "- Teléfono: 11-1234-5678\n"
            "- Ubicación: Ruta 9 km 123\n"
            "- ETA: 22:30\n"
            "- Tipo de carga: Grilla"
        )
    elif "retorno" in pregunta:
        return "La unidad 123 no tiene retorno asignado. Puede liberarse a Norlog."
    elif "coordinador" in pregunta:
        return "El teléfono del coordinador de tráfico de larga distancia es 11-4321-8765."
    else:
        return "No entendí la consulta. ¿Podés reformularla?"

def ejecutar_chatbot():
    print("📦 Bienvenido al asistente de tráfico 🚛")
    print("Escribí tu consulta o 'salir' para finalizar.")
    
    while True:
        entrada = input("Tú: ")
        if entrada.lower() in ["salir", "exit", "chau"]:
            print("Bot: ¡Hasta luego!")
            break
        respuesta = responder(entrada)
        print("Bot:", respuesta)

if __name__ == "__main__":
    ejecutar_chatbot()
