nomeDeUsuario = input("Por favor, insira seu nome de usuário: ")
senha = input("Por favor, insira sua senha: ")

nomeDeUsuarioEsperado = "usuario"
senhaEsperada = "123"

if nomeDeUsuario == nomeDeUsuarioEsperado and senha == senhaEsperada:
    print("Acesso concedido.")
else:
    print("Acesso negado.")
