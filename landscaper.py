#################################
#   Landscaper Game
#################################

'''
This is a comment that takes up multiple lines.
I can't tell if it works, though.
I guess so.
'''

# Game class for keeping game properties and functions
class Game:
      def __init__(self, money, my_tools, day, store_tools):
            self.money = money
            self.my_tools = my_tools
            self.day = day
            self.store_tools = [
                        {"name": "Rusty Scissors", "profit": 5, "cost": 0},
                        {"name": "Ol' Timey Push Mower", "profit": , "cost":},
                        {"name": "Fancy Battery-Powered Lawnmower", "profit": "cost":,}
                        {"name": "Hire a team of starving students", "profit": "cost":}]

      # Game Class Methods
      # morning function, runs at the start of each new day.
      def morning (self):
            print("GOOD MORNING! IT'S A NEW DAY!")
            print(f"It is day {self.day}, and you have ${self.money}.")
            print("[1] Cut the Grass")
            print("[2] Get a new tool")
            print("[Q] Quit")
            return input("What will you do today?")

      # mow_the_grass function, when the user selects mowing the grass.
      def mow_the_grass (self):
            print("""Ok, good. A good work ethic is critical to success in this world.
      Your tools are:""")
            for tool in self.my_tools:
                  print(f"[{self.my_tools.index(tool) + 1}] {tool}")
            tool_choice_int = int(input("What will you use?"))
            tool_choice = self.my_tools[tool_choice_int - 1]
            pay = 0
            print(tool_choice)
            if (tool_choice_int == 1):
                  pay = 1
            print(f"You did a great job cutting the grass with your {tool_choice} and made ${pay}. Great Job!")
            print("______________________________________________________")
            self.money = self.money + pay
            self.day += 1
      
      def buy_new_tools (self):
            print("______________________________________________________")
            print(f'''Welcome to the tool store!
      You have ${self.money}.''')
            
            if (self.money < 5): # rather have it be: self.money < lowest_price_tool
                  print("Sorry, you can't afford anything.")
            else:
                  print("This is what we have.")
                  for tool in self.store_tools:
                        print(f"[{self.store_tools.index(tool) + 1}] {tool}")
                  new_tool_int = int(input("What would you like to buy?")) - 1
                  new_tool_cost = self.calculate_price(new_tool_int)
                  print(f"Oooooh, that {self.store_tools[new_tool_int]} is a Beauty!")
                  print(f"That'll be ${new_tool_cost}")
                  if (self.money - new_tool_cost < 0):
                        print("Oops, sorry, you can't afford that one.")
                  else:
                        choice = input("Do you want to buy it? (Y/N)")
                        if (choice == 'Y'):
                              print("Good choice, you won't regret it.")
                              # append new tool to the my_tools array
                              
                              # remove the tool from the store_tools array
                              
                        else:
                              print("Okeedokee")
                              self.buy_new_tools()
                  


      def calculate_price(self, index):
            price_array = [5, 25, 250, 500]
            return price_array[index]


# Instantiate a game object
game = Game(5, # starting money TODO: TURN IT BACK TO ZERO
            {"name": "teeth", "profit": 1,  "cost":0}, # starting tool
            1, # starting day
            # store tool inventory
)

# Initial Prompt
print("""Welcome to your new Landscaping Business!
      There is a lot of grass to cut, and you're the one to do it.
      Hope you're wearing your work pants.
      """)

# Game Loop
while (True):
      choice = game.morning()
      if choice == "Q" or choice == 'q':
          print("Ok, Quitter.")
          break
      elif choice == "1":
            game.mow_the_grass()
      elif choice == "2":
            game.buy_new_tools()