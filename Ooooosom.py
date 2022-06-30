import random

while True:
    user_action = input("Masukkan pilihan anda: (batu, air, burung): ")
    possible_actions = ["batu", "air", "burung"]
    computer_action = random.choice(possible_actions)
    print(f"\nPilihan anda: {user_action}, Pilihan komputer: {computer_action}.\n")

    if user_action == computer_action:
        print(f"Pilihan sama {user_action}. Seri")
    elif user_action == "batu":
        if computer_action == "burung":
            print(" Batu baling burung! Anda menang!")
        else:
            print("Air tenggelam dalam batu! Anda kalah.")
    elif user_action == "air":
        if computer_action == "batu":
            print("Batu tenggelam dalam air! Anda menang!")
        else:
            print("Burung minum air! Anda kalah.")
    elif user_action == "burung":
        if computer_action == "air":
            print("Burung minum air! Anda menang!")
        else:
            print("Batu baling burung! Anda kalah.")

    play_again = input("main semula? (y/n): ")
    if play_again.lower() != "y":
        break
