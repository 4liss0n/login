nivel = input(print("bom dia, o que você é? Adm(a), User(a) ou Visitante")).upper()

if nivel == "ADM":
    print("bem-vindo administrador, por favor ensira seu e-mail e senha")
elif nivel == "ADMA":
    print("bem-vindo administradora, por favor ensira seu e-mail e senha")
elif nivel == "USER":
    print("bem-vindo usuario, por favor ensira seu nome e senha")
elif nivel == "USERA":
    print("bem-vindo usuaria, por favor ensira seu nome e senha")
elif nivel == "VISITANTE":
    print("bem-vindo visitante, alguns dos seus acessos foram limitados")
else:
    print("sai daqui estranho(a)")