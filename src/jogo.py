
import os
import shutil
import keyboard
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def center_text(text, width):
    lines = text.splitlines()
    return '\n'.join(line.center(width) for line in lines)

def get_terminal_size():
    size = shutil.get_terminal_size()
    return size.columns, size.lines

def draw_ring(nome_jogador="", pontos_jogador=0, nome_oponente="", pontos_oponente=0):
    terminal_width, terminal_height = get_terminal_size()
    ring_width = min(105, terminal_width - 4)
    ring_height = min(30, terminal_height - 4)

    horizontal_margin = (terminal_width - ring_width) // 2
    vertical_margin = (terminal_height - ring_height) // 2

    ring_top = "╔" + "═" * (ring_width - 2) + "╗"
    ring_middle = "║" + " " * (ring_width - 2) + "║"
    ring_bottom = "╚" + "═" * (ring_width - 2) + "╝"

    clear_screen()

    for i in range(vertical_margin):
        print()

    if nome_oponente and nome_jogador:
        oponente_info = f"{nome_oponente}: {pontos_oponente}"
        jogador_info = f"{nome_jogador}: {pontos_jogador}"
        espaco = " " * (ring_width - len(oponente_info) - len(jogador_info))
        print(" " * horizontal_margin + oponente_info + espaco + jogador_info)

    print(" " * horizontal_margin + ring_top)
    for _ in range(ring_height - 2):
        print(" " * horizontal_margin + ring_middle)
    print(" " * horizontal_margin + ring_bottom)

    for i in range(vertical_margin - 1):
        print()

    return ring_width, ring_height

def obter_nome_jogador():
    terminal_width, _ = get_terminal_size()
    ring_width = min(80, terminal_width - 4)

    horizontal_margin = (terminal_width - ring_width) // 2
    
    while True:
        ring_width, ring_height = draw_ring()
        print("\n" + " " * horizontal_margin + "Qual seu nome, lutador?")
        nome = input(" " * horizontal_margin)
        if nome.strip():
            draw_ring(nome)
            print("\n" + " " * horizontal_margin + f"Bem-vindo, {nome}!")
            input(" " * horizontal_margin + "Pressione Enter para começar...")
            return nome
        else:
            print(" " * horizontal_margin + "Por favor, digite um nome válido.")
            input(" " * horizontal_margin + "Pressione Enter para tentar novamente...")

def new_game():
    terminal_width, terminal_height = get_terminal_size()
    ring_width, ring_height = draw_ring()

    horizontal_margin = (terminal_width - ring_width) // 2
    vertical_margin = (terminal_height - ring_height) // 2

    nome_jogador = obter_nome_jogador()
    personagem = Personagem(nome_jogador, x=2, y=ring_height // 2 - 2, lado="esquerda")
    oponente = Oponente("Inimigo", x=ring_width - 7, y=ring_height // 2 - 2, lado="direita")

    print("\nPressione 'w', 'a', 's', 'd' para mover o personagem, e 'Espaço' para atacar.")
    time.sleep(2)

    while True:
        if keyboard.is_pressed('w') or keyboard.is_pressed('a') or keyboard.is_pressed('s') or keyboard.is_pressed('d'):
            if keyboard.is_pressed('w'):
                personagem.mover('w', ring_width, ring_height)
            elif keyboard.is_pressed('a'):
                personagem.mover('a', ring_width, ring_height)
            elif keyboard.is_pressed('s'):
                personagem.mover('s', ring_width, ring_height)
            elif keyboard.is_pressed('d'):
                personagem.mover('d', ring_width, ring_height)

        if keyboard.is_pressed('SPACE'):
            personagem.atacar(oponente, ring_width)
        else:
            personagem.atacando = False

        ring_width, ring_height = draw_ring(personagem.nome, personagem.pontos, oponente.nome, oponente.pontos)
        personagem.desenhar(horizontal_margin=horizontal_margin, vertical_margin=vertical_margin, ring_width=ring_width, ring_height=ring_height)
        oponente.desenhar(horizontal_margin=horizontal_margin, vertical_margin=vertical_margin, ring_width=ring_width, ring_height=ring_height)

        if keyboard.is_pressed('q'):
            print("Saindo do jogo.")
            break

        time.sleep(0.05)  # Pequeno delay para evitar uso excessivo de CPU

def main_menu():
    ascii_art = '''
                                                                                                               
 /$$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$ /$$   /$$  /$$$$$$ 
| $$__  $$ /$$__  $$| $$  / $$|_  $$_/| $$$ | $$ /$$__  $$
| $$  \ $$| $$  \ $$|  $$/ $$/  | $$  | $$$$| $$| $$  \__/
| $$$$$$$ | $$  | $$ \  $$$$/   | $$  | $$ $$ $$| $$ /$$$$
| $$__  $$| $$  | $$  >$$  $$   | $$  | $$  $$$$| $$|_  $$
| $$  \ $$| $$  | $$ /$$/\  $$  | $$  | $$\  $$$| $$  \ $$
 | $$$$$$$/|  $$$$$$/| $$  \ $$ /$$$$$$| $$ \  $$|  $$$$$$/ 
|_______/  \______/ |__/  |__/|______/|__/  \__/ \______/ 
                                                          
                                                                   
    '''

    menu_options = ["Novo jogo", "Continuar", "Ranking", "Opções", "Sair"]
    selected_index = 0

    def render_menu():
        terminal_width = shutil.get_terminal_size().columns
        centered_ascii_art = center_text(ascii_art, terminal_width)
        clear_screen()
        print(centered_ascii_art)

        for i, option in enumerate(menu_options):
            if i == selected_index:
                print(center_text(f"- {option} -", terminal_width))
            else:
                print(center_text(option, terminal_width))

    render_menu()

    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name in ['up', 'w']:
                selected_index = (selected_index - 1) % len(menu_options)
                render_menu()
            elif event.name in ['down', 's']:
                selected_index = (selected_index + 1) % len(menu_options)
                render_menu()
            elif event.name == 'enter':
                return selected_index
            elif event.name == 'q':
                return -1

if __name__ == "__main__":
    while True:
        user_choice = main_menu()
        if user_choice == 0:
            new_game()
        elif user_choice == 1:
            print("\nContinuar selecionado!")
            input("Pressione Enter para voltar ao menu principal...")
        elif user_choice == 2:
            print("\nRanking selecionado!")
            input("Pressione Enter para voltar ao menu principal...")
        elif user_choice == 3:
            print("\nOpções selecionadas!")
            input("Pressione Enter para voltar ao menu principal...")
        elif user_choice == 4 or user_choice == -1:
            print("\nSaindo do jogo.")
            break

    input("Pressione Enter para sair...")
