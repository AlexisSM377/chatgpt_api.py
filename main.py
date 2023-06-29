import openai
import congif
import typer
from rich import print
from rich.table import Table

def main():

    openai.api_key = congif.api_key

    print("🍔 [bold green]Bienvenido al asistente de AlexAI[/bold green]")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir del asistente")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    #Contexto del asistente
    context = {"role": "system", 
                "content": "Eres un asistente muy útil. "}
    messages = [context]

    while True:

        content = __prompt()

        if content == "new":
            print("👍 Nueva conversación creada.")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content}) 

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                    messages=messages)
        
        response_content = response.choices[0].message.content
        
        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")

def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué quieres hablar? ")

    if prompt == "exit":
            exit = typer.confirm("✋ ¿Estás seguro de que quieres salir?")
            if exit:
                print("👋 ¡Hasta pronto!")
                raise typer.Abort()
            
            return __prompt()
    
    return prompt

if __name__ == "__main__":
    typer.run(main)

