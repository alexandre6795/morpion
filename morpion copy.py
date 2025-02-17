import tkinter as tk
import json
import os
import random

# Initialiser la grille et l'état du jeu
board = [['' for _ in range(3)] for _ in range(3)]
game_over = False
game_file = ".game_ia.json"  # Nom du fichier de sauvegarde de l'état du jeu
winner = " "  # Par défaut, il n'y a pas de gagnant (partie en cours)
current_player = 'X'  # Le joueur 'X' commence par défaut
rnd = random.choice(['x', 'o'])  # Déterminer aléatoirement si l'IA commence ou pas
ai_has_played = False  # Indicateur pour savoir si l'IA a déjà joué


# Sauvegarder l'état du jeu dans un fichier JSON
def save_game_state():
    game_state = {
        "board": board,
        "game_over": game_over,
        "winner": winner  # Pas de current_player ici pour le mode IA
    }

    # Sauvegarder selon le mode de jeu
    if mode == "ai":
        game_file = ".game_ia.json"
    else:
        game_file = ".game_2p.json"

    with open(game_file, "w") as file:
        json.dump(game_state, file)


# Charger l'état du jeu depuis un fichier JSON (avec gestion du cas où le fichier peut être modifié)
def load_game_state():
    global board, game_over, winner, current_player
    if os.path.exists(game_file):
        with open(game_file, "r") as file:
            game_state = json.load(file)
            board = game_state["board"]
            game_over = game_state["game_over"]
            winner = game_state["winner"]
            if mode == "2p":  # Le mode 2 joueurs inclut current_player
                current_player = 'X'  # Recommence avec X pour le mode 2 joueurs
            draw_board()  # Redessiner le plateau avec l'état sauvegardé


# Supprimer le fichier de sauvegarde à la fin de la partie
def delete_game_state_file():
    if os.path.exists(game_file):
        os.remove(game_file)


def resize_buttons(event=None):
    width = window.winfo_width() // 3
    height = window.winfo_height() // 3
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(
                width=width // 10, height=height // 30, font=("normal", height // 5))


def check_win(board, player):
    return any(all(cell == player for cell in row) for row in board) or \
        any(all(board[row][col] == player for row in range(3)) for col in range(3)) or \
        all(board[i][i] == player for i in range(3)) or \
        all(board[i][2 - i] == player for i in range(3))


def is_full(board):
    return all(cell != '' for row in board for cell in row)


def minimax(board, depth, is_maximizing):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == '':
                    board[r][c] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[r][c] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == '':
                    board[r][c] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[r][c] = ''
                    best_score = min(score, best_score)
        return best_score


def best_move():
    if board[1][1] == '':
        return 1, 1

    best_score = -float('inf')
    move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == '':
                board[r][c] = 'O'
                score = minimax(board, 0, False)
                board[r][c] = ''
                if score > best_score:
                    best_score = score
                    move = (r, c)
    return move


def draw_board():
    global buttons
    buttons = []

    # Si un gagnant est déjà défini dans le fichier, on n'affiche pas de boutons supplémentaires
    if winner != " ":
        return
    
    for r in range(3):
        row_buttons = []
        for c in range(3):
            button = tk.Button(window, text=board[r][c], font=('normal', 20),
                               command=lambda r=r, c=c: on_click(r, c),
                               bg='black', fg='green', bd=3, relief='solid')
            button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
            row_buttons.append(button)
        buttons.append(row_buttons)

    for i in range(3):
        window.grid_rowconfigure(i, weight=1)
        window.grid_columnconfigure(i, weight=1)

    window.bind("<Configure>", resize_buttons)

    # Si c'est l'IA qui doit commencer et que ce n'est pas encore fait, on lance son premier coup
    if rnd == 'o' and not game_over and not ai_has_played:
        execute_ai_play()


def on_click(r, c):
    global game_over, winner, current_player, ai_has_played
    if board[r][c] == '' and not game_over and winner == " ":
        board[r][c] = current_player
        buttons[r][c].config(text=current_player)

        if check_win(board, current_player):
            winner = current_player
            game_over = True
            show_end_screen(f"{current_player} gagne !",
                            "green" if current_player == 'X' else "red")
        elif is_full(board):
            winner = '='
            game_over = True
            show_end_screen("Égalité !", "white")
        elif mode == "2p":
            switch_player()  # Alterner le joueur
        else:
            if current_player == 'X':  # Si c'est le joueur humain qui a joué, l'IA peut maintenant jouer
                ai_has_played = False
            window.after(1000, execute_ai_play)

        save_game_state()  # Sauvegarder l'état après chaque coup


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

    save_game_state()  # Sauvegarder après avoir changé de joueur


def execute_ai_play():
    global game_over, winner, ai_has_played
    if not game_over and winner == " " and not ai_has_played:
        move = best_move()
        if move:
            r, c = move
            if board[r][c] == '':
                board[r][c] = 'O'
                buttons[r][c].config(text='O')

        if check_win(board, 'O'):
            winner = 'O'
            show_end_screen("L'IA gagne !", "red")
        elif is_full(board):
            winner = '='
            show_end_screen("Égalité !", "white")

        ai_has_played = True  # L'IA a joué son coup
        save_game_state()  # Sauvegarder l'état après le coup de l'IA


def show_end_screen(message, color):
    for widget in window.winfo_children():
        widget.pack_forget()
        widget.grid_forget()

    end_frame = tk.Frame(window, bg='black')
    end_frame.pack(expand=True)

    end_label = tk.Label(end_frame, text=message, font=(
        'Arial', 30, 'bold'), fg=color, bg='black')
    end_label.pack(pady=20)

    restart_button = tk.Button(end_frame, text="Rejouer", font=('Arial', 15), command=restart_game,
                               bg='black', fg='green', bd=3, relief='solid')
    restart_button.pack(pady=10)

    back_button = tk.Button(end_frame, text="Retour", font=('Arial', 15), command=show_game_mode_screen,
                            bg='black', fg='green', bd=3, relief='solid')
    back_button.pack(pady=10)

    # Supprimer le fichier de sauvegarde de l'IA à la fin de la partie
    delete_game_state_file()


def restart_game():
    global board, game_over, winner, current_player, rnd, ai_has_played
    board = [['' for _ in range(3)] for _ in range(3)]
    game_over = False
    winner = " "  # Réinitialiser le gagnant
    current_player = 'X'  # Recommencer avec 'X'
    rnd = random.choice(['x', 'o'])  # Déterminer aléatoirement si l'IA commence ou pas
    ai_has_played = False  # Réinitialiser l'indicateur de l'IA

    for widget in window.winfo_children():
        widget.pack_forget()
        widget.grid_forget()

    draw_board()


def start_ai_game():
    global board, game_over, winner
    global game_file, mode, current_player, rnd, ai_has_played

    if os.path.exists(game_file):  # Supprimer l'ancien fichier de sauvegarde s'il existe
        delete_game_state_file()

    mode = "ai"
    game_file = ".game_ia.json"
    board = [['' for _ in range(3)] for _ in range(3)]
    game_over = False
    winner = " "  # Réinitialiser le gagnant
    current_player = 'X'  # Le joueur 'X' commence en mode IA
    rnd = random.choice(['x', 'o'])  # Déterminer aléatoirement si l'IA commence ou pas
    ai_has_played = False  # L'IA n'a pas encore joué

    for widget in window.winfo_children():
        widget.pack_forget()
        widget.grid_forget()

    draw_board()


def start_multiplayer_game():
    global board, game_over, winner
    global mode, game_file, current_player

    mode = "2p"
    game_file = ".game_2p.json"
    board = [['' for _ in range(3)] for _ in range(3)]
    game_over = False
    winner = " "  # Réinitialiser le gagnant
    current_player = 'X'  # Le joueur 'X' commence en mode 2 joueurs

    for widget in window.winfo_children():
        widget.pack_forget()
        widget.grid_forget()

    draw_board()


def show_game_mode_screen():
    for widget in window.winfo_children():
        widget.pack_forget()
        widget.grid_forget()

    start_screen_frame = tk.Frame(window, bg='black')
    start_screen_frame.pack(expand=True)

    title_label = tk.Label(start_screen_frame, text="Choisir un mode de jeu", font=(
        'Arial', 30, 'bold'), fg="green", bg='black')
    title_label.pack(pady=20)

    ai_button = tk.Button(start_screen_frame, text="Jouer contre l'IA", font=('Arial', 15), command=start_ai_game,
                          bg='black', fg='green', bd=3, relief='solid')
    ai_button.pack(pady=10)

    multiplayer_button = tk.Button(start_screen_frame, text="Jouer à 2 joueurs", font=('Arial', 15), command=start_multiplayer_game,
                                   bg='black', fg='green', bd=3, relief='solid')
    multiplayer_button.pack(pady=10)


# Charger l'état du jeu au démarrage
window = tk.Tk()
window.title("Morpion")
window.geometry("800x800")
window.resizable(False, False)
window.configure(bg='black')

show_game_mode_screen()  # Afficher l'écran du mode de jeu au lancement

window.mainloop()
