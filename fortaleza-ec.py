import turtle as t

#comfiguração da tela
screen = t.Screen()
screen.title('escudo Fortaleza')
screen.bgcolor('white')
t.speed(3)

def fortalezaec(zoom: int, posx: int, posy: int):

    #Ajusta a posição e o zoom
    def adx(n: float) -> float:
        return (n*zoom) + posx
    def ady(n: float) -> float:
        return (n*zoom) + posy
    
    #exterior
    t.up()
    t.goto(adx(-20), ady(20))
    t.down()
    t.goto(adx(20),ady(20))
    t.goto(adx(20),ady(10))
    t.goto(adx(-20),ady(10))
    t.goto(adx(-20),ady(20))
    t.up()
    t.goto(adx(-20),ady(10))
    t.down()
    t.goto(adx(0.1),ady(-25))
    t.goto(adx(20),ady(10))
    t.up()

    #triangulo azul
    t.fillcolor('blue')
    t.goto(adx(-17),ady(7))
    t.down()
    t.begin_fill()
    t.goto(adx(-1),ady(7))
    t.goto(adx(-1),ady(-20))
    t.goto(adx(-17),ady(7))
    t.end_fill()
    t.up()

    #triangulo vermelho
    t.fillcolor('red')
    t.begin_fill()
    t.goto(adx(1),ady(7))
    t.down()
    t.goto(adx(17),ady(7))
    t.goto(adx(1),ady(-20))
    t.goto(adx(1),ady(7))
    t.up()
    t.end_fill()

    #estrela
    t.fillcolor('gold')
    t.begin_fill()
    t.goto(adx(0.1),ady(35))
    t.down()
    t.goto(adx(5),ady(20))
    t.goto(adx(-10),ady(30))
    t.goto(adx(10),ady(30))
    t.goto(adx(-5),ady(20))
    t.goto(adx(0.1),ady(35))
    t.up()
    t.end_fill()

    #Nome
    t.goto(adx(0.1),ady(11))
    t.down()
    t.color('black')
    t.write('FORTALEZA', align='center', font=('arial', 5*zoom, 'bold'))
    t.up()

    #base
    t.fillcolor('yellow')
    t.begin_fill()
    t.goto(adx(-25),ady(-25))
    t.down()
    t.goto(adx(25),ady(-25))
    t.goto(adx(25),ady(-30))
    t.goto(adx(-25),ady(-30))
    t.goto(adx(-25),ady(-25))
    t.end_fill()
input("pressione enter para continuar")
fortalezaec(3,0,0)
# ↑ Chama a função com os argumentos de zoom, posição do eixo x e y

t.done()
    