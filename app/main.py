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

    # Exibindo todos os usuários cadastrados.
    print("\nListando usuários cadastrados: ")
    lista_usuario = service.listar_todos_usuarios()
    for usuario in lista_usuario:
        print(f"\nNome: {usuario.nome} \nEmail: {usuario.email} \nSenha: {usuario.senha}")
    
    # Iniciando o loop para remoção de usuário
    while True:
        remover = input(f"\nDeseja remover algum usuário? (sim/não): ")
        if remover == "sim":
            nome_usuario = input("Digite o nome do usuário que deseja remover: ")

            # Buscar e remover o usuário pelo nome
            usuario_para_remover = repository.pesquisar_usuario_por_nome(nome_usuario)
            if usuario_para_remover:
                service.excluir_usuario(usuario_para_remover)  # Removendo o usuário através do serviço
                print("\nUsuário removido com sucesso.")
            else:
                print("\nUsuário não encontrado.")
        else:
            print("\nFinalizando as remoções.")
            break  # Sai do loop enquanto

        # Exibindo a lista de usuários após a remoção para confirmação
        print("\nListando usuários após a remoção: ")
        lista_usuario = service.listar_todos_usuarios()
        for usuario in lista_usuario:
            print(f"\nNome: {usuario.nome} \nEmail: {usuario.email} \nSenha: {usuario.senha}")

if __name__ == "__main__":
    os.system("cls || clear")
    main()
