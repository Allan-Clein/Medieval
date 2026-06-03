import os
import Projeto.banco as banco

name = ""
def clear():
    os.system("cls")

def Ato1():
    clear()
    input("Você é um aventureiro de terras distantes, ao chegar em uma cidade avista ao longe uma taverna.")
    input("Taverneiro: Olá nobre guerreiro, vejo que é novo por aqui! Qual é o nome que devo horar esta visita?")
    while True:
        name = input("Digite seu nome: ")
        if len(name) > 10:
            clear()
            print("Seu nome é longo demais!")
        elif len(name) < 1:
            clear()
            print("Seu nome é curto demais!")
        else:
            break
    clear()
    input(f"Ah! Sim! {name}, bem-vindo(a) ao nosso humilde vilareijo, porém talvez não tão seguro no momento já que existem alguns slimes que aflingem a população por esses arredores.")
    input("Se puder, por favor eliminar eles ficarei grato.")
    clear()
    input("Você se dirige a uma floresta próxima aos relatos...")

def Ato2():
    input("Taverneiro: Você consegiu derrotar os inimigos, receba essas moedas e esse mapa como recompensa!\n\nViagem rápida adquirida!\n+100 Moedas!\n")
    banco.coins += 100
    input("Você se retira da taverna.")
    