from collections import deque

class Navegador:
    def __init__(self):
        self.back_stack = deque()  # Pilha de voltar
        self.forward_stack = deque()  # Pilha de avançar
        self.current_page = None  # Página atual

    def print_size(self):
        """Exibe o tamanho das pilhas e da página atual"""
        print(f"Tamanho da pilha de Voltar: {len(self.back_stack)}")
        print(f"Tamanho da pilha de Avançar: {len(self.forward_stack)}")

    def navigate_to(self, url):
        """Navega para uma nova página e gerencia as pilhas"""
        if self.current_page is not None:
            self.back_stack.append(self.current_page)  # Adiciona a página atual à pilha de voltar
        
        self.forward_stack.clear()  # Limpa a pilha de avançar
        self.current_page = url  # Atualiza a página atual

    def back(self):
        """Volta para a página anterior"""
        if self.back_stack:
            self.forward_stack.append(self.current_page)  # Adiciona a página atual à pilha de avançar
            self.current_page = self.back_stack.pop()  # Pega a última página visitada
        else:
            print("Não há páginas para voltar.")

    def forward(self):
        """Avança para a próxima página"""
        if self.forward_stack:
            self.back_stack.append(self.current_page)  # Adiciona a página atual à pilha de voltar
            self.current_page = self.forward_stack.pop()  # Recupera a próxima página
        else:
            print("Não há páginas para avançar.")

    def print_queue(self):
        """Imprime o estado atual das pilhas de navegação"""
        print(f"\nPágina atual: {self.current_page}")
        print(f"Pilha de Voltar: {list(self.back_stack)}")
        print(f"Pilha de Avançar: {list(self.forward_stack)}")
