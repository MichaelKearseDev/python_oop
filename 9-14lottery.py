from random import choice 

lottery_choices = (1, 3, 100, 45, 4, 2, 10, 22, 99, 65, "a", "b", "c", "d", "e")

def random_selection(winner):
    winner = []
    
    for _ in range(4):
        winning_ticket = choice(lottery_choices)
        winner.append(winning_ticket)
    print(f"Ticket number {winner} has won the raffle!")

random_selection(lottery_choices)