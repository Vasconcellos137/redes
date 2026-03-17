j = "pedra"
j2 = "pedra"

ganhador = None

# if j == j2:
#     msg = "empate"

match j:
    case "pedra":
        if j2 == "papel":
            msg = "j2 ganhou"
        if j2 == "tesoura":
            msg = "j ganhou"
        if j2 == "pedra":
            msg = "Empate"
    case "papel":
        if j2 == "pedra":
            msg = "j ganhou"
        if j2 == "tesoura":
            msg = "j2 ganhou"
        if j2 == "papel":
            msg = "Empate"
    case "tesoura":
        if j2 == "pedra":
            msg = "j2 ganhou"
        if j2 == "papel":
            msg = "j ganhou"
        if j2 == "tesoura":
            msg = "Empate"