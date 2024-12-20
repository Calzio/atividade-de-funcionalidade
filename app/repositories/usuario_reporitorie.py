from models.usuario_model import Usuario
from sqlalchemy.orm import Session

class UsuarioRepositorie:
    def __init__(self, session: Session) -> None:
        self.session = session

    def salvar_usuario(self, usuario: Usuario):
        """Salva um novo usuário no banco de dados."""
        self.session.add(usuario)
        self.session.commit()

    def pesquisar_usuario_por_email(self, email: str):
        """Pesquisa um usuário pelo email no banco de dados."""
        return self.session.query(Usuario).filter_by(email=email).first()

    def excluir_usuario(self, usuario: Usuario):
        """Exclui um usuário do banco de dados."""
        self.session.delete(usuario)
        self.session.commit()

    def listar_todos_usuario(self):
        """Retorna todos os usuários cadastrados."""
        return self.session.query(Usuario).all()

    def pesquisar_usuario_por_nome(self, nome: str):
        """Pesquisa um usuário pelo nome no banco de dados."""
        return self.session.query(Usuario).filter_by(nome=nome).first()
