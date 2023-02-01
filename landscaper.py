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

# Initial Prompt
print("""Welcome to your new Landscaping Business!
      There is a lot of grass to cut, and you're the one to do it.
      Hope you're wearing your work pants.
      """)

# Game Loop
while (True):
    print(f"It is day {day}, and you have ${money}, what will you do?")
    print("[1] Cut the Grass")
    print("[2] Get a new tool")
    print("[Q] Quit")
    