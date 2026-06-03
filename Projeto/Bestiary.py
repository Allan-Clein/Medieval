import os
select = 0

Bestiario = {}


def clear():
    os.system('cls')

def abrir():
    while True:
        global select
        clear()
        print("Página 1:")
        for i in range(1, len(Bestiario) + 1):
            print(f"{i} - {Bestiario[str(i)]}")
        select = input("\nDigite 0 para sair.\nSua resposta: ")
        if select == "0":
            break
        listar()

def listar():
    try:
        global select
        select = Bestiario[str(select)]
        if str(select) == "Slime Iniciante":
            clear()
            input("Slime Iniciante:\n\nLore: Só podem ser encontrados no tutorial do jogo. São criaturas esféricas feitas de algum tipo de gosma desconhecida, não aparentam ser muito forte.\n\nImunidade: Não possuem.\n\nHabilidade: Não possuem.\n\nAtaque de impacto: Slime Iniciante se joga na direção do inimigo causando 15 + (0 a 5) amplitude pontos de dano.\n\nDrops: Não possuem.\n")
    except:
        pass
            #[lista de inimigos] --> armazena em variavel para poder setar os ataques e poderes deles em dicionarios