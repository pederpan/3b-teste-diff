import os

def limpar_tela():
    # Limpa o terminal dependendo do sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    print("="*30)
    print("   MEME GENERATOR (ASCII)   ")
    print("="*30)
    print("1 - Pinguim do Linux (Tux)")
    print("2 - Sair")
    print("="*30)

def desenhar_tux():
    print(r"""
          .--.
         |o_o |
         |:_/ |
        //   \ \
       (|     | )
      /'\_   _/` \
      \___)=(___/
    """)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-2): ")
        
        limpar_tela()
        
        if opcao == '1':
            desenhar_tux()
        elif opcao == '2':
            print("Saindo... Até a próxima!")
            break
        else:
            print("Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para voltar ao menu...")
        limpar_tela()

if __name__ == "__main__":
    main()