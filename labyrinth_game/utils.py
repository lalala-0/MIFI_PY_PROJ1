from labyrinth_game.constants import ROOMS

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
