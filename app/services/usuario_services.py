from models.usuario_model import Usuario
from repositories.usuario_reporitorie import UsuarioRepositorie

class UsuarioService:
    def __init__(self, repository: UsuarioRepositorie):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastrado = self.repository.pesquisar_usuario_por_email(email=usuario.email)

            if cadastrado:
                print("Usuário já cadastrado!")
                return

            self.repository.salvar_usuario(usuario=usuario)
            print("Usuário cadastrado com sucesso!")
        except TypeError as erro: 
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuario()
    
    def excluir_usuario(self, usuario: Usuario):
        """Exclui um usuário do banco de dados."""
        try:
            self.repository.excluir_usuario(usuario)
            print("Usuário excluído com sucesso!")
        except Exception as erro:
            print(f"Erro ao excluir o usuário: {erro}")
