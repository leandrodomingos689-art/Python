class Book:
    def __init__(self, title: str, author: str, pages: int):
        self._title = title
        self._author = author
        self._pages = pages

    def get_info(self):
        return f"\"{self._title}\" — {self._author}, {self._pages} стр."

    def __str__(self):
        return self.get_info()

class Ebook(Book):
    def __init__(self, title, author, pages, format_type):
        # CORREÇÃO: Faltava o 'self' e é mais simples usar o super()
        super().__init__(title, author, pages)
        self._format = format_type

    def get_info(self):  
        # CORREÇÃO: Faltavam os parênteses no super().get_info()
        return super().get_info() + f" [{self._format}]"

    # NOVO MÉTODO:
    def get_download_link(self):
        # Jeito simples: transforma em minúsculo e troca espaço por traço
        link_titulo = self._title.lower().replace(" ", "-")
        return f"https://books.com/{link_titulo}"

# Testando o código:
livro = Ebook("Guerra e Paz", "Tolstoi", 1200, "PDF")
print(livro.get_info()) # Exibe as info com o formato
print(livro.get_download_link()) # Exibe o link formatado
