#################################
#   Landscaper Game
#################################
# There was a different version of the game that I was originally building that attempted to use classes.
# After watching Alex's poolcleaner video I decided to remake it using his model.
# Check out landscaper_classes.py for the other version I was attempting.


## Game State, for properties and functions.
game = {"tool": 0, "money": 0, "day": 0}

tools = [
      {"name": "Rusty Scissors", "profit": 5, "cost": 5},
      {"name": "Ol' Timey Push Mower", "profit": 50, "cost": 25},
      {"name": "Fancy Battery-Powered Lawnmower", "profit": 100, "cost": 250,},
      {"name": "Hire a team of starving students", "profit": 250, "cost": 500}
]

## Game Functions
# morning function, runs at the start of each new day.
def morning ():
      print("GOOD MORNING! IT'S A NEW DAY!")
      print(f"It is day {game['day']}, and you have ${game['money']}.")
      print("[1] Cut the Grass")
      print("[2] Get a new tool")
      print("[Q] Quit")
      return input("What will you do today?")

# mow_the_grass function, when the user selects mowing the grass.
def mow_the_grass ():
      tool = tools[game["tool"]]
      print(f'''Ok, good. A good work ethic is critical to success in this world.
You are currently using a {tool['name']}''')
      print(f"You did a great job cutting the grass with your {tool['name']} and made ${tool['profit']}. Great Job!")
      game['money'] += tool['profit']
      game['day'] += 1
      print("______________________________________________________")

# buy_new_tools, for when the user wants a new tool      
def buy_new_tools ():
      print(f'Welcome to the tool store!')
      if (game['tool'] >= len(tools)):
            print("Oops, sorry, you already bought everything. Go start your own store.")
            return 0
      next_tool = tools[game["tool"] + 1]
      if (game['money'] < next_tool['cost']):
            print(f"Sorry, you don't have enough money for {next_tool['name']}")
            print(f"You need ${next_tool['cost'] - game['money']} more to get it.")
            return 0
      print(f"Okeedokee, we have a beautiful {next_tool['name']} for sale for ${next_tool['cost']}.")
      i = input("You want to buy it? Y/N")
      if (i == 'Y' or 'y'):
            print("Good choice, you won't regret it.")
            game['money'] -= next_tool['cost']
            game['tool'] += 1
      else:
            print("Ok, goodbye.")

def win_game():
      if (game['tool'] == len(tools) - 1 and game['money'] >= 1000):
            print("You win! You've cut all the lawns in the Tri-State Area!")
            print(f"It took you {game['day']} days. Very impressive.")
            return True
      return False

# Initial Prompt
print("""Welcome to your new Landscaping Business!
      There is a lot of grass to cut, and you're the one to do it.
      Hope you're wearing your work pants.
      """)

# Game Loop
while (True):
      choice = morning()
      if choice == "Q" or choice == 'q':
          print("Ok, Quitter.")
          break
      elif choice == "1":
            mow_the_grass()
      elif choice == "2":
            buy_new_tools()