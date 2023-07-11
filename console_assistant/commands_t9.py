from prompt_toolkit.completion import WordCompleter

#список команд для підказок
commands_at_statup = WordCompleter([
    "info",
    "exit",
    "address book",
    "notes",
    "sort folder",
    'weather'
])

commands_for_the_ab = WordCompleter([
    'exit',
    'add contact',
    'birthday',
    'search contact',
    'edit contact',
    'delete contact'
])

commands_for_notes = WordCompleter([
    'exit',
    'add note',
    'search',
    'edit',
    'show all',
    'sort by tags',
    'delete'
])

commands_for_weather = WordCompleter([
    'get weather',
    'exit'
])

commands_for_sf = WordCompleter([
    'sort folder',
    'exit'
])

PREVIEW = """
   _______  _____  __   _ _______  _____         _______      _______ _______ _______ _____ _______ _______ _______ __   _ _______
 |       |     | | \  | |______ |     | |      |______      |_____| |______ |______   |   |______    |    |_____| | \  |    |   
 |_____  |_____| |  \_| ______| |_____| |_____ |______      |     | ______| ______| __|__ ______|    |    |     | |  \_|    |   
                                                                                                                               
"""

PREVIE = """
   __________  _   _______ ____  __    ______   ___   __________ __________________    _   ________
  / ____/ __ \/ | / / ___// __ \/ /   / ____/  /   | / ___/ ___//  _/ ___/_  __/   |  / | / /_  __/
 / /   / / / /  |/ /\__ \/ / / / /   / __/    / /| | \__ \\__ \ / / \__ \ / / / /| | /  |/ / / /   
/ /___/ /_/ / /|  /___/ / /_/ / /___/ /___   / ___ |___/ /__/ // / ___/ // / / ___ |/ /|  / / /    
\____/\____/_/ |_//____/\____/_____/_____/  /_/  |_/____/____/___//____//_/ /_/  |_/_/ |_/ /_/     
                                                                                                
"""