import random
 
class SnakeLadders:
     def __init__(self):
         self.snakes = {
             16: 6, 47: 26, 49: 11, 56: 53,
             62: 19, 64: 60, 87: 24, 93: 73,
             95: 75, 98: 78
         }
         self.ladders = {
             3: 22, 8: 30, 28: 84, 58: 77,
             75: 86, 80: 99, 90: 91
         }
         self.player_positions = [1, 1]  # Both players start at position 1
         self.current_player = 0         # Player 1 starts
 
     def roll_dice(self):
         return random.randint(1, 6)
 
     def move_player(self, player):
         roll = self.roll_dice()
         print(f"\n🎲 Player {player + 1} rolled a {roll}")
 
         current_position = self.player_positions[player]
         new_position = current_position + roll
 
         if new_position > 100:
             print(f"❌ Roll exceeded 100. Player {player + 1} stays at {current_position}")
             return
 
         if new_position in self.snakes:
             print(f"🐍 Oh no! Landed on a snake at {new_position}. Going down to {self.snakes[new_position]}")
             new_position = self.snakes[new_position]
         elif new_position in self.ladders:
             print(f"🪜 Yay! Found a ladder at {new_position}. Climbing up to {self.ladders[new_position]}")
             new_position = self.ladders[new_position]
 
         self.player_positions[player] = new_position
         print(f"📍 Player {player + 1} is now at position {new_position}")
 
     def play_game(self):
         print("🎮 Welcome to Snake and Ladders!")
         print("First to reach exactly 100 wins the game.\n")
 
         while True:
             input(f"Player {self.current_player + 1}, press Enter to roll the dice...")
             self.move_player(self.current_player)
 
             if self.player_positions[self.current_player] == 100:
                 print(f"\n🏆🎉 Player {self.current_player + 1} wins the game! 🎉🏆")
                 break
 
             self.current_player = 1 - self.current_player  # Switch player
 
 
 # Start the game
if __name__ == "__main__":
     game = SnakeLadders()
     game.play_game()
