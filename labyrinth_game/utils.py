from labyrinth_game.constants import ROOMS
import math

def describe_current_room(game_state):
    """Вывод информации о текущей комнате."""
    current_room_key = game_state['current_room']
    room = ROOMS[current_room_key]

    print(f"\n== {current_room_key.upper()} ==")
    print(room['description'])
    if room['items']:
        print("Заметные предметы:", ", ".join(room['items']))
    print("Выходы:", ", ".join(room['exits'].keys()))
    if room['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).")

def solve_puzzle(game_state):
    """Решение загадки."""
    room = ROOMS[game_state['current_room']]
    puzzle = room['puzzle']
    if puzzle is None:
        print("Загадок здесь нет.")
        return
    print(puzzle['question'])
    user_answer = input("Ваш ответ: ").strip().lower()
    if puzzle['answer'].lower() == user_answer:
        print("Правильно! Загадка решена.")
        reward = puzzle['reward']
        if reward:
            game_state['player_inventory'].append(reward)
            print(f"Вы получили: {reward}")
        else:
            print("Награды за эту загадку нет.")
        room['puzzle'] = None
    else:
        print("Неверно. Попробуйте снова.")

    
def attempt_open_treasure(game_state):
    """Открываем финальный сундук."""
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]

    if 'treasure_key' in game_state['player_inventory']:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        room_data['items'].remove('treasure_chest')
        print("В сундуке сокровище! Вы победили!")
        game_state['game_over'] = True
        return

    answer = input("Сундук заперт. ... Ввести код? (да/нет)").strip().lower()
    if answer == 'да':
        puzzle = room_data['puzzle']
        if puzzle is None:
            print("Код неизвестен, вы не можете открыть сундук.")
            return
        code_input = input("Введите код: ").strip()
        if code_input.lower() == puzzle['answer'].lower():
            print("Код верный! Сундук открыт!")
            room_data['items'].remove('treasure_chest')
            print("В сундуке сокровище! Вы победили!")
            game_state['game_over'] = True
        else:
            print("Неверный код. Попробуйте снова позже.")
    else:
        print("Вы отступаете от сундука.")

def pseudo_random(seed, modulo):
    """
    Псевдослучайный генератор.
    Параметры:
        seed (int): Базовое значение для генерации (например, количество шагов)
        modulo (int): Верхняя граница диапазона (результат будет в [0, modulo))
    
    Возвращает:
        int: Псевдослучайное целое число в диапазоне [0, modulo)
    """
    
    val = math.sin(seed * 12.09876543) * 19567.987654
    fract = val - math.floor(val) 
    return int(fract * modulo)

def trigger_trap(game_state):
    """Активация ловушки"""
    print("Ловушка активирована! Пол стал дрожать...")
    inventory = game_state.get('player_inventory', [])
    if (inventory):
        lost_index = pseudo_random(game_state['steps_taken'], len(inventory))
        lost_item = inventory.pop(lost_index)
        print(f"Из вашего инвентаря выпал и потерялся: {lost_item}")
    else:
        survival_roll = pseudo_random(game_state['steps_taken'], 10)
        if survival_roll < 3:  # 30% шанс смерти
            print("Вас настигает смертоносный механизм! Вы погибли...")
            game_state['game_over'] = True
        else:
            print("Вам чудом удалось увернуться от смертельной ловушки!")


def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")

