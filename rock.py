import random
class Game:
    
    def __init__(self):
        
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.options = {'rock': 0, 'paper': 1, 'scissors': 2}

    def shuffle(self):
        
        return random.choice(list(self.options.keys()))

    def score(self, player, opponent):
        
        final = (player - opponent) % 3
        if final == 0:
            self.ties += 1
            print("It's a draw!")
        elif final == 1:
            self.wins += 1
            print("You win!!")
        elif final == 2:
            self.losses += 1
            print("You lose!")

    def start(self):
        
        while True:
            userchoice = input("Pick 'Rock' / 'Paper' / 'Scissors'\n"
                               "Whats your decision? ").lower()
            if userchoice not in self.options.keys():
                print("Enter Rock / Paper / Scissors")
            else:
                break
        computer = self.shuffle()
        print(f"You chose {userchoice}, and your opponent chose {computer}.")
        self.score(self.options[userchoice], self.options[computer])

    def print_score(self):
        print(f"Scoreboard: {self.wins} wins, {self.losses} losses, and "
              f"{self.ties} ties.")

if __name__ == "__main__":
    run = Game()
    while True:
        run.start()
        run.print_score()
        while True:
            go = input('\nDo you want to play again? (yes/no): ').lower()
            if go == 'n' or 'no':
                print("Thanks for playing!")
                exit()
            elif go == 'y' or 'yes':
                break
            else:
                print("Try again\n")
                continue