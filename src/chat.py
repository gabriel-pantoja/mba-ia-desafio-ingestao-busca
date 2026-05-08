from search import search_prompt

def main():
    print("=== CHAT RAG ===")
    print("Digite 'sair' para encerrar.\n")
    print("Faça sua pergunta:\n")

    while True:
        question = input("PERGUNTA: ")

        if question.lower() in ["sair", "exit", "quit"]:
            print("\nEncerrando chat...")
            break

        try:
            chain = search_prompt(question)

            if not chain:
                print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
                break

            print(f"RESPOSTA: {chain}\n")

        except Exception as e:
            print(f"\nErro: {e}\n")
    
if __name__ == "__main__":
    main()