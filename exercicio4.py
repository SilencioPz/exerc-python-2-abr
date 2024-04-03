x = float(input("Por favor, insira a coordenada x: "))
y = float(input("Por favor, insira a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no 1º Quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no 2º Quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no 3º Quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no 4º Quadrante.")
else:
    print("O ponto está localizado no eixo ou origem.")
