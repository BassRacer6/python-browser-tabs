from browser import Navegador

class Menu:
    def __init__(self):
        self.navegador = Navegador()

    def exibir_menu(self):
        """Exibe o menu de navegação"""
        while True:
            print("\nMenu:")
            print("1. Navegar para uma nova página")
            print("2. Voltar para a página anterior")
            print("3. Avançar para a próxima página")
            print("4. Ver o estado atual das pilhas")
            print("5. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                url = input("Digite o endereço da nova página: ")
                self.navegador.navigate_to(url)
            
            elif opcao == "2":
                self.navegador.back()
            
            elif opcao == "3":
                self.navegador.forward()
            
            elif opcao == "4":
                self.navegador.print_size()
                self.navegador.print_queue()
            
            elif opcao == "5":
                print("Saindo...")
                break  # Sai do loop e termina o programa
            
            else:
                print("Opção inválida, tente novamente.")
