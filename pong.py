# Importar o módulo turtle
import turtle

# Criar a janela do jogo
janela = turtle.Screen()
janela.title("Jogo Pong")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)

# Criar a bola
bola = turtle.Turtle()
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2 # Velocidade horizontal da bola
bola.dy = 0.2 # Velocidade vertical da bola

# Criar a raquete A
raquete_a = turtle.Turtle()
raquete_a.shape("square")
raquete_a.color("white")
raquete_a.shapesize(stretch_wid=5, stretch_len=1)
raquete_a.penup()
raquete_a.goto(-350, 0)

# Criar a raquete B
raquete_b = turtle.Turtle()
raquete_b.shape("square")
raquete_b.color("white")
raquete_b.shapesize(stretch_wid=5, stretch_len=1)
raquete_b.penup()
raquete_b.goto(350, 0)

# Criar o placar
placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Jogador A: 0 Jogador B: 0", align="center", font=("Arial", 24, "normal"))

# Variáveis para guardar os pontos dos jogadores
pontos_a = 0
pontos_b = 0

# Funções para mover as raquetes
def raquete_a_cima():
    y = raquete_a.ycor() # Pegar a coordenada y da raquete A
    y += 20 # Adicionar 20 pixels à coordenada y da raquete A
    raquete_a.sety(y) # Atualizar a coordenada y da raquete A

def raquete_a_baixo():
    y = raquete_a.ycor() # Pegar a coordenada y da raquete A
    y -= 20 # Subtrair 20 pixels à coordenada y da raquete A
    raquete_a.sety(y) # Atualizar a coordenada y da raquete A

def raquete_b_cima():
    y = raquete_b.ycor() # Pegar a coordenada y da raquete B
    y += 20 # Adicionar 20 pixels à coordenada y da raquete B
    raquete_b.sety(y) # Atualizar a coordenada y da raquete B

def raquete_b_baixo():
    y = raquete_b.ycor() # Pegar a coordenada y da raquete B
    y -= 20 # Subtrair 20 pixels à coordenada y da raquete B
    raquete_b.sety(y) # Atualizar a coordenada y da raquete B

# Associar as teclas do teclado às funções de movimento das raquetes
janela.listen() # Fazer a janela escutar os eventos do teclado
janela.onkeypress(raquete_a_cima, "w") # Quando pressionar a tecla "w", chamar a função raquete_a_cima
janela.onkeypress(raquete_a_baixo, "s") # Quando pressionar a tecla "s", chamar a função raquete_a_baixo
janela.onkeypress(raquete_b_cima, "Up") # Quando pressionar a tecla "Up", chamar a função raquete_b_cima
janela.onkeypress(raquete_b_baixo, "Down") # Quando pressionar a tecla "Down", chamar a função raquete_b_baixo

# Loop principal do jogo
while True:
    janela.update() # Atualizar a janela do jogo

    # Colocar Limite que dê para mover cada raquete
    if raquete_a.ycor() > 280: # Se a raquete ultrapassar o limite superior da janela (300 - 20)
        raquete_a.sety(280) # Colocar a raquete na posição limite superior (280)
        
    if raquete_a.ycor() < -280: # Se a raquete ultrapassar o limite inferior da janela (300 - 20)
        raquete_a.sety(-280) # Colocar a raquete na posição limite inferior (-280)    
        
    if raquete_b.ycor() > 280: # Se a raquete ultrapassar o limite superior da janela (300 - 20)
        raquete_b.sety(280) # Colocar a raquete na posição limite superior (280)
        
    if raquete_b.ycor() < -280: # Se a raquete ultrapassar o limite inferior da janela (300 - 20)
        raquete_b.sety(-280) # Colocar a raquete na posição limite inferior (-280)    

    # Mover a bola
    bola.setx(bola.xcor() + bola.dx) # Atualizar a coordenada x da bola somando o valor de dx
    bola.sety(bola.ycor() + bola.dy) # Atualizar a coordenada y da bola somando o valor de dy

    # Verificar as colisões com as bordas da janela
    if bola.ycor() > 290: # Se a bola ultrapassar o limite superior da janela (300 - 10)
        bola.sety(290) # Colocar a bola na posição limite superior (290)
        bola.dy *= -1 # Inverter o sinal de dy para fazer a bola mudar de direção

    if bola.ycor() < -290: # Se a bola ultrapassar o limite inferior da janela (-300 + 10)
        bola.sety(-290) # Colocar a bola na posição limite inferior (-290)
        bola.dy *= -1 # Inverter o sinal de dy para fazer a bola mudar de direção

    if bola.xcor() > 390: # Se a bola ultrapassar o limite direito da janela (400 - 10)
        bola.goto(0, 0) # Colocar a bola na posição inicial (0, 0)
        bola.dx *= -1 # Inverter o sinal de dx para fazer a bola mudar de direção
        pontos_a += 1 # Adicionar um ponto ao jogador A
        placar.clear() # Limpar o placar anterior
        placar.write(f"Jogador A: {pontos_a} Jogador B: {pontos_b}", align="center", font=("Arial", 24, "normal")) # Escrever o novo placar

    if bola.xcor() < -390: # Se a bola ultrapassar o limite esquerdo da janela (-400 + 10)
        bola.goto(0, 0) # Colocar a bola na posição inicial (0, 0)
        bola.dx *= -1 # Inverter o sinal de dx para fazer a bola mudar de direção
        pontos_b += 1 # Adicionar um ponto ao jogador B
        placar.clear() # Limpar o placar anterior
        placar.write(f"Jogador A: {pontos_a} Jogador B: {pontos_b}", align="center", font=("Arial", 24, "normal")) # Escrever o novo placar
        
    # Verificar as colisões com as raquetes
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < raquete_b.ycor() + 50 and bola.ycor() > raquete_b.ycor() - 50): 
        
    # Se a bola estiver entre as coordenadas x da raquete B e entre as coordenadas y da raquete B
        bola.setx(340) # Colocar a bola na posição limite direita da raquete B (350 - 10)
        bola.dx *= -1 # Inverter o sinal de dx para fazer a bola mudar de direção

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < raquete_a.ycor() + 50 and bola.ycor() > raquete_a.ycor() - 50): 
    # Se a bola estiver entre as coordenadas x da raquete A e entre as coordenadas y da raquete A
        bola.setx(-340) # Colocar a bola na posição limite esquerda da raquete A (-350 + 10)
        bola.dx *= -1 # Inverter o sinal de dx para fazer a bola mudar de direção

# Fim do código
