import json
import os

DEFAULT_CONFIG = {
  "enable_debug": True,
  "sword_keybind": "q",
  "jump_keybind": "space",
  "jump_cycles": 0,
  "hit_delay": 0.64,
  "legit_delays": False,
  "eat_food": False,
  "food_hotkey": "7",
  "food_png": "assets/food.png",
  "sell_items": False,
  "sell_command": "sellall inventory",
  "sell_cycles": 100,
  "spam_chat": False,
  "spam_messages": [
    "Hello!",
    "I am AFK farming!",
    "Bot by Drexxy!",
    "Have a nice day!"
  ],
  "spam_cycles": 5,
  "hold": True,
  "hold_key": "f"
}


CONFIG_PATH = "config.json"
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "r") as f:
        user_config = json.load(f)
else:
    user_config = {}


# god i love python. this basically ensures every variable is present. future proofs all configs <3
config = DEFAULT_CONFIG.copy()
config.update(user_config)

with open(CONFIG_PATH, "w") as f:
    json.dump(config, f, indent=4)
