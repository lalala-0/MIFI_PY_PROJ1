# labyrinth_game/constants.py
ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта. Стены покрыты мхом. На полу лежит старый факел.',
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. По центру стоит пьедестал с запечатанным сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room'},
        'items': [],
        'puzzle': {
            'question': 'На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой или словом.',
            'answer':  ["10", "десять", "ten", '10.', 'десять.'],
            'reward': 'silver_coin'
        }
    },
    'trap_room': {
        'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',
        'exits': {'west': 'entrance'},
        'items': ['rusty_key'],
        'puzzle': {
            'question': 'Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")',
            'answer': 'шаг шаг шаг',
            'reward': 'healing_potion'
        }
    },
    'library': {
        'description': 'Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.',
        'exits': {'east': 'hall', 'north': 'armory'},
        'items': ['ancient_book'],
        'puzzle': {
            'question': 'В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)',
            'answer': ['резонанс', 'resonance', 'резонанс.', 'resonance.'],
            'reward': 'magic_scroll'
        }
    },
    'armory': {
        'description': 'Старая оружейная комната. На стене висит меч, рядом — небольшая бронзовая шкатулка.',
        'exits': {'south': 'library',  'north': 'hidden_passage'},
        'items': ['sword', 'bronze_box'],
        'puzzle': None
    },
    'treasure_room': {
        'description': 'Комната, на столе большой сундук. Дверь заперта — нужен особый ключ.',
        'exits': {'south': 'hall'},
        'items': ['treasure_chest'],
        'puzzle': {
            'question': 'Дверь защищена кодом. Введите код (подсказка: это число пятикратного шага, 2*5= ? )',
            'answer':  ["10", "десять", "ten", '10.', 'десять.'],
            'reward': 'treasure_key'
        }
    },
    'hidden_passage': {
        'description': 'Узкий скрытый проход. Каменные стены покрыты древними символами. На севере видна дверь с таинственным механизмом.',
        'exits': {'south': 'armory', 'north': 'secret_chamber'},
        'items': [],
        'puzzle': {
            'question': 'На стене надпись: "Что открывает путь, когда вокруг тьма?"',
            'answer': ['свет', 'light', 'свет.', 'light.'],
            'reward': 'torch_upgrade'
        }
    },
    'secret_chamber': {
        'description': 'Тайная комната. В центре лежит небольшой сундук. Внутри поблескивает золотой ключ.',
        'exits': {'south': 'hidden_passage'},
        'items': ['treasure_key'],
        'puzzle': None
    }
}

COMMANDS = {
    "[go] <direction>": "перейти в направлении (north/south/east/west)",
    "look": "осмотреть текущую комнату",
    "take <item>": "поднять предмет",
    "use <item>": "использовать предмет из инвентаря",
    "inventory": "показать инвентарь",
    "solve": "попытаться решить загадку в комнате",
    "quit": "выйти из игры",
    "help": "показать это сообщение"
}