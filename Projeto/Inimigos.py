import random
idano = 0
ivida = 0
idefesa = 0
danototal = 0
Encontrados = 0
amplitude = 0
import threading
import Projeto.Bestiary as Bestiary
import Projeto.viagem as v

aptos = []

#-----------------------------------------------------------Inicial----------------------------------------------------------#

slime_iniciante = {"nome" : "Slime Iniciante",
                       "vida" : 50,
                       "dano" : 15,
                       "amplitude" : 5,
                       "encontrado" : 0,
                       "elemento" : False}

#-----------------------------------------------------------Montanha Ophidia----------------------------------------------------------#

gnomo_petrificado = {"nome" : "Gnomo Petrificado",
                     "vida" : 80,
                     "dano" : 15,
                     "amplitude" : 10,
                     "defesa" : 15/100,
                     "encontrado" : 0,
                     "elemento" : "geodo"}

serpente_alada = {"nome" : "Serpente Alada",
                     "vida" : 30,
                     "dano" : 25,
                     "amplitude" : 5,
                     "defesa" : 0/100,
                     "encontrado" : 0,
                     "elemento" : "anemoria"}

#-----------------------------------------------------------Floresta Raizal----------------------------------------------------------#

raiz_enfurecida = {"nome" : "Raiz Enfurecida",
                     "vida" : 80,
                     "dano" : 15,
                     "amplitude" : 10,
                     "defesa" : 0/100,
                     "encontrado" : 0,
                     "elemento" : "natura"}

inimigos = []

def pode_cair():
    global aptos
    if v.local == "Floresta Raizal.":
        aptos = [raiz_enfurecida]
    if v.local == "Montanha Ophidia.":
        aptos = [gnomo_petrificado,serpente_alada]


def slime_inicial():
    global idano, ivida, danototal, Encontrados
    global slime_iniciante
    idano = slime_iniciante['dano']
    ivida = slime_iniciante['vida']
    danototal = 0


#o iais dias idasoi da