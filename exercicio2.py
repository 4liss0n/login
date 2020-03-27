nome = input("qual o seu nome? ")
nivel = input(print("bom dia, o que você é? Adm, User ou Visitante")).upper()
genero = input(print("qual o seu nome?(M/F) ")).upper()
if nivel == "ADM" and genero == "M":
    print("bem-vindo administrador, por favor ensira seu e-mail e senha")
elif nivel == "ADM" and genero =="F":
    print("bem-vindo administradora, por favor ensira seu e-mail e senha")
elif nivel == "USER" and genero == "M":
    print("bem-vindo usuario, por favor ensira seu nome e senha")
elif nivel == "USERA"and genero == "F":
    print("bem-vindo usuaria, por favor ensira seu nome e senha")
elif nivel == "VISITANTE":
    print("bem-vindo visitante, alguns dos seus acessos foram limitados")
else:
    print("bem-vindo estranho")
