import Projeto.banco as banco
import Projeto.Inimigos as Iny
import Projeto.lore as lore
import random as rn
import os
import time
import Projeto.battle as battle
import Projeto.Bestiary as Bt
import Projeto.viagem as v
import threading

def clear():
    os.system("cls")

select = "" #Opção escolhida
status = {}
name = ""
banco.coins = 0

#----------------------------------------------------------------------------------PRÉ-GAME---------------------------------------------------------------------------

while True: #Selecionar a classe de jogo
    try:
        clear()
        print("Olá jogador, seja bem-vindo! Digite o número da classe correspondente para analisá-la.\n1 - Clérigo\n2 - Mago\n3 - Tank\n4 - Berserker" )
        pclass = input("\n")
        if pclass == "1":
            clear()
            print("Clérigo:\nVida = 120\nDano = 15\nMana = 100\nPorcentagem de cura = +15%\n")
            select = input("Digite 1 para confirmar ou qualquer outa coisa para voltar a lista de classes:  ")
            if select == "1":
                clear()
                input("Você selecionou: Clérigo!")
                break
        if pclass == "2":
            clear()
            print("Mago:\nVida = 100\nDano = 20\nMana = 150\nBola de fogo inicial\n")
            select = input("Digite 1 para confirmar ou qualquer outa coisa para voltar a lista de classes:  ")
            if select == "1":
                clear()
                input("Você selecionou: Mago!")
                break
        if pclass == "3":
            clear()
            print("Tank:\nVida = 200\nDano = 15\nMana = 50\nRedução de dano = 10%")
            select = input("Digite 1 para confirmar ou qualquer outa coisa para voltar a lista de classes:  ")
            if select == "1":
                clear()
                input("Você selecionou: Tank!")
                break
        if pclass == "4":
            clear()
            print("Berserker:\nVida = 75\nDano = 35\nMana = 75\n")
            select = input("Digite 1 para confirmar ou qualquer outa coisa para voltar a lista de classes:  ")
            if select == "1":
                clear()
                input("Você selecionou: Berserker!")
                break
    except:
        clear()
        input("Algo deu errado, selecione apenas as opções correspondentes!")
        clear()

#----------------------------------------------------------------------------------GAME---------------------------------------------------------------------------

clear()
def SetStatusBase():
    global status
    if pclass == "1":
        status = {"totallife" : 120,
        "danobase" : 15,
        "manabase" : 100,
        "fireball" : 0,
        "classregeneration" : 15/100,
        "armor" : 0/100}
    elif pclass == "2":
        status = {"totallife" : 100,
        "danobase" : 20,
        "manabase" : 150,
        "fireball" : 1,
        "classregeneration" : 0/100,
        "armor" : 0/100}
    elif pclass == "3":
        status = {"totallife" : 200,
        "danobase" : 15,
        "manabase" : 50,
        "fireball" : 0,
        "classregeneration" : 0/100,
        "armor" : 10/100}
    elif pclass == "4":
        status = {"totallife" : 75,
        "danobase" : 35,
        "manabase" : 75,
        "fireball" : 0,
        "classregeneration" : 0/100,
        "armor" : 0/100}
SetStatusBase()
vida = status["totallife"]
mana = status["manabase"]
armadura = status["armor"]

def atualizar_bestiario():
    print(inimigo['encontrado'])
    if inimigo['encontrado'] == 1 and (inimigo not in Iny.inimigos):
        Bt.Bestiario[str(len(Bt.Bestiario) + 1)] = inimigo['nome']
        Iny.inimigos.append(inimigo)

def Action():
    clear()
    print("Escolha uma das ações abaixo: \n1 - Viajar até algum ponto do mundo.\n2 - Inventário de itens.\n3 - Inventário de habilidades.\n4 - Status atual.\n5 - Abrir bestiário.\n")
    select = input("\nSua resposta: ")
    if select == "4":
        clear()
        print(f"Vida: {vida}/{status['totallife']}",f"\nMana: {mana}/{status['manabase']}",f"\nArmadura: {armadura}/{status['armor']}")
        input("\nAperte novamente para voltar ao jogo!\nSua resposta: ")
    elif select == "5":
        atualizar_bestiario()
        Bt.abrir()
    elif select == "1":
        Viajar()
    elif select == "6":
        pass


def SelecionarInimigo():
    global inimigo
    if local == "Floresta do Vilareijo":
        Iny.slime_inicial()
        inimigo = Iny.slime_iniciante
        
def Combate_Inicial():
    Iny.slime_inicial()
    global vida
    inimigo['encontrado'] += 1
    if inimigo['encontrado'] == 1 and (inimigo not in Iny.inimigos):
        Bt.Bestiario[str(len(Bt.Bestiario) + 1)] = inimigo['nome']
        Iny.inimigos.append(inimigo)
    while True:
        clear()
        select = input(f"Você está lutando contra {Iny.slime_iniciante['nome']}, qual ação deseja tomar:\n1 - Atacar.\n2 - Ver status do inimigo.\n3 - Correr.\n4 - Utilizar item.\n5 - Utilizar menu de ações.\nSua resposta: ")
        if select == "1":
            Iny.ivida -= status['danobase']
            if Iny.ivida <= 0:
                Iny.ivida = 0
            clear()
            input(f"Você causou {status['danobase']} pontos de dano! {Iny.ivida} pontos de vida restante.\n")
            clear()
            if Iny.ivida <= 0:
                clear()
                input("Você venceu o combate inicial, está pronto para continuar!\n")
                break
            Iny.amplitude = rn.randint(0, inimigo['amplitude'])
            Iny.danototal = Iny.idano + (Iny.amplitude) - (Iny.idano +(Iny.amplitude))*status['armor']
            vida -= Iny.danototal
            input(f"{Iny.slime_iniciante['nome']} causou {Iny.danototal} pontos de dano! {vida}/{status['totallife']}\n")
        elif select == "5":
            Action()
        elif select == "2":
            clear()
            input(f"Status do inimigo: \n{Iny.ivida} Pontos de vida.\n{Iny.idano} Pontos de dano base.\n{Iny.idefesa} Pontos de defesa.\n")


def batalha():
    global inimigo
    clear()
    Iny.pode_cair()
    inimigo = rn.choice(Iny.aptos)
    Iny.ivida = inimigo['vida']
    Iny.idano = inimigo['dano']
    Iny.idefesa = inimigo['defesa']
    inimigo['encontrado'] += 1
    if inimigo['encontrado'] == 1 and (inimigo not in Iny.inimigos):
        Bt.Bestiario[str(len(Bt.Bestiario) + 1)] = inimigo['nome']
        Iny.inimigos.append(inimigo)
    print(inimigo)
    while Iny.ivida > 0:
        input(Bt.Bestiario)
        Iny.ivida = 0

def Viajar():
    try:
        clear()
        print("Você deseja viajar para:\n")
        for v.local in range(1,len(v.locais) + 1):
            print(f"{v.local} - {v.locais[str(v.local)]}")
        v.local = str(input("\nSua resposta: "))
        v.local = v.locais[str(v.local)]
        clear()
        input(v.local)
        batalha()
    except:
        pass

while True:
    lore.Ato1()
    local = "Floresta do Vilareijo"
    SelecionarInimigo()
    Combate_Inicial()
    lore.Ato2()
    v.locais["2"] = "Floresta Raizal."
    v.locais["3"] = "Montanha Ophidia."
    break

while True:
    Action()

    #aaaaaaaaaaaaa