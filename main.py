from bruteforce import Bruteforce
from optimized import Optimized
from functions import Clean

def main():
    """ launching starting here """
    choice = ""

    while choice.upper() != "B" or choice.upper() != "O":
        choice = input("(B)ruteforce ou (O)ptimisé? ")
        if choice.upper() == "B":
            Clean()
            print("Execution du script Bruteforce")
            try:
                Bruteforce()
            except KeyboardInterrupt:
                print("\n\nFin du script par l'utilisateur.\n")
            exit()
        elif choice.upper() == "O":
            Clean()
            print("Execution du script Optimized")
            try:
                Optimized()
            except KeyboardInterrupt:
                print("\n\nFin du script par l'utilisateur.\n")
            exit()

if __name__ == "__main__":
    main()