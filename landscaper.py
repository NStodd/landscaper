#################################
#   Landscaper Game
#################################

'''
This is a comment that takes up multiple lines.
I can't tell if it works, though.
I guess so.
'''

# Game State Variables
money = 0
tools = ["teeth"]
day = 1

# Game Functions

      # morning function, to run at the start of each new day.
def morning ():
    print(f"It is day {day}, and you have ${money}.")
    print("[1] Cut the Grass")
    print("[2] Get a new tool")
    print("[Q] Quit")
    return input("What will you do today?")

      # mow_the_grass function, when the user selects mowing the grass.
def mow_the_grass ():
      print("""Ok, good. A good work ethic is critical to success in this world.
Your tools are:""")
      for tool in tools:
            print(f"[{tools.index(tool) + 1}] {tool}")
      tool_choice = input("What will you use?")
      print(tool_choice)
      break

def buy_new_tools ():
      print("Welcome to the tool store!")
      break

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
