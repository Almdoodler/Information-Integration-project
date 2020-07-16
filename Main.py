from Mediator import Mediator


class Main:
    if __name__ == '__main__':
        mediator = Mediator()

        print("Welcome to the Movie Integrator 3000")
        print("")
        print("Please enter")
        print("'1' + 'yourMovie' if you want to search by movie name")
        print("'2' + 'yourImdb-ID' if you want to search by imdb-ID")

        dir, input = input().split()

        if dir == "1":
            print("Processing..")
            mediator.showData(input, "1")

        elif dir == "2":
            print("Processing..")
            mediator.showData(input, "2")

        else:
            print("Your input was wrong.")
