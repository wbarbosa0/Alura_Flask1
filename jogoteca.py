from flask import Flask, render_template

app=Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/inicio')
def ola():
    lista=[Jogo('Super Mario', 'Plataforma', 'NES'),
           Jogo('Sonic', 'Plataforma', 'SMS'),
           Jogo('Halo', 'Shooting', 'XBOX')]
    return render_template('lista.html', titulo = 'Jogos', jogos = lista)#'<h1>Olá Flask!</h1>'

app.run()
