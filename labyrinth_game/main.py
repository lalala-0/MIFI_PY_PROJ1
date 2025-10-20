#!/usr/bin/env python3

import labyrinth_game.utils as utils
import  labyrinth_game.player_actions as pa

def process_command(game_state, command):
    if not command:
        return True
    
    cmd = command[0]
    arg = command[1] if len(command) > 1 else None

    match cmd:
        case "look" | "осмотреться":
            utils.describe_current_room(game_state)
        case "inventory" | "инвентарь":
            pa.show_inventory(game_state)
        case "go" | "идти":
            if arg:
                pa.move_player(game_state, arg)
                #print("Шаги:", game_state['steps_taken'])
            else:
                print("Укажите направление (north, south, east, west).")
        case "take" | "взять":
            if arg:
                pa.take_item(game_state, arg)
            else:
                print("Укажите, что хотите взять.")
        case "use" | "использовать":
            if arg:
                pa.use_item(game_state, arg)
            else:
                print("Укажите предмет для использования.")
        case "solve" | "решить":
            if game_state['current_room'] == 'treasure_room':
                utils.attempt_open_treasure(game_state)
            else:
                utils.solve_puzzle(game_state)
        case "help":
            utils.show_help()
        case "quit" | "exit" | "выход":
            print("Вы покидаете игру. До новых встреч!")
            return False  # сигнал завершения игры
        case _:
            print("Неизвестная команда. Введите 'help' для списка команд.")
    return True  # игра продолжается
  
def main():
    game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0 # Количество шагов
   }
    
    print("Добро пожаловать в Лабиринт сокровищ!")
    utils.describe_current_room(game_state)

    while not game_state['game_over']:
        command_str = pa.get_input()
        if not process_command(game_state, command_str):
            break

if __name__ == "__main__":
    main()