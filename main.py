from rich import print
from random import randint 
num = randint(0,100)

max_tries = 7
cur_tries = 0
past_guesses = []

while cur_tries < max_tries:
    guess = int(input("Guess the number: "))
    if guess in past_guesses:
        print("[black]Already used this number, Try again[/black]")
        continue
    else:
        past_guesses.append(guess)
    if guess == num:
        print("[green]You won in[/green]", cur_tries, "[green]guesses![/green]")
        break
    elif guess > num:
        print("[yellow]Guess a lower number[/yellow]")
        cur_tries += 1
    else:
        print("[yellow]Guess a higher number[/yellow]")
        cur_tries += 1
print("[red]You lost! No guesses left[/red]")