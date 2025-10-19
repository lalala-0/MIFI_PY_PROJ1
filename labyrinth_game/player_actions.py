from labyrinth_game.constants import ROOMS

def show_inventory(game_state):
    """Вывод содержимого инвентаря игрока."""
    inventory = game_state.get('player_inventory', [])
    if inventory:
        print("Ваш инвентарь:", ", ".join(inventory))
    else:
        print("Инвентарь пуст.")

def get_input(prompt="> "):
    """Считывание команды от пользователя."""
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit" 