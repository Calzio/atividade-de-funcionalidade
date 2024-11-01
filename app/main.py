from services.usuario_services import UsuarioService
from repositories.usuario_reporitorie import UsuarioRepositorie
from config.database import Session
import os 

def main():
    session = Session()
    repository = UsuarioRepositorie(session)
    service = UsuarioService(repository)

    # Solicitando dados do usuário.
    print("\nAdicionando usuário: ")
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    # Exibindo todos os usuários na tela usuário do banco de dados.
    print("\nListando usuário cadastrado: ")
    lista_usuario = service.listar_todos_usuarios()
    for usuario in lista_usuario:
        print(f"\nNome: {usuario.nome} \nEmail: {usuario.email} \nSenha: {usuario.senha}")

if __name__ == "__main__":
    os.system("cls || clear")