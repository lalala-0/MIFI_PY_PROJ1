from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room, random_event


def show_inventory(game_state):
    """Вывод содержимого инвентаря игрока."""
    inventory = game_state.get('player_inventory', [])
    if inventory:
        print("Ваш инвентарь:", ", ".join(inventory))
    else:
        print("Инвентарь пуст.")

def move_player(game_state, direction):
    """Перемещение игрока."""
    current_room_key = game_state['current_room']
    room = ROOMS[current_room_key]

    if direction in room['exits']:
        new_room = room['exits'][direction]
        if new_room == 'treasure_room':
            if 'rusty_key' in game_state['player_inventory']:
                print("Вы используете найденный ключ, " \
                "чтобы открыть путь в комнату сокровищ.")
            else:
                print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
                return
        game_state['current_room'] = new_room
        game_state['steps_taken'] += 1
        print(f"\nВы идете {direction}...\n")
        describe_current_room(game_state)
        random_event(game_state)
    else:
        print("Нельзя пойти в этом направлении.")

def take_item(game_state, item_name):
    """Взятие предмета."""
    if item_name == "treasure_chest":
        print("Вы не можете поднять сундук, он слишком тяжелый.")
        return
    current_room_key = game_state['current_room']
    room = ROOMS[current_room_key]

    if item_name in room['items']:
        game_state['player_inventory'].append(item_name)
        room['items'].remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")

def use_item(game_state, item_name):
    """Использование предмета"""
    inventory = game_state.get('player_inventory', [])

    if item_name not in inventory:
        print("У вас нет такого предмета.")
        return

    if item_name == "torch":
        print("Вы зажгли факел. Стало светлее.")
    elif item_name == "sword":
        print("Вы держите меч. Чувствуете себя уверенно.")
    elif item_name == "bronze_box":
        print("Вы открыли бронзовую шкатулку.")
        if "rusty_key" not in inventory:
            print("Внутри вы находите rusty_key!")
            inventory.append("rusty_key")
        else:
            print("Но внутри ничего нового нет.")
    else:
        print("Вы не знаете, как использовать этот предмет.")

def get_input(prompt="> "):
    """Считывание команды от пользователя."""
    try:
        return input(prompt).strip().lower().split(maxsplit=1)
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return ["quit"]
