Numero = 0

def on_forever():
    global Numero
    while Numero == 0:
        Numero += 1
    basic.show_number(Numero)
basic.forever(on_forever)
