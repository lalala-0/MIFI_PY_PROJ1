#!/usr/bin/env python3

from labyrinth_game.constants import ROOMS
import labyrinth_game.utils as utils
import  labyrinth_game.player_actions as pa


   
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
        command = pa.get_input("> ").lower()

        if command in ["выход", "exit", "quit"]:
            print("Вы покидаете игру. До новых встреч!")
            break
        elif command in ["осмотреться", "look"]:
            utils.describe_current_room(game_state)
        elif command in ["инвентарь", "inventory"]:
            pa.show_inventory(game_state)
        else:
            print("Неизвестная команда. Попробуйте 'look' для осмотра или 'inventory' для инвентаря.")

    
if __name__ == "__main__":
    main()