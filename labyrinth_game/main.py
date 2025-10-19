#!/usr/bin/env python3

from labyrinth_game.constants import ROOMS
import labyrinth_game.utils as utils
import  labyrinth_game.player_actions as pa

game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0 # Количество шагов
  }
   
def main():
    print("Первая попытка запустить проект!")