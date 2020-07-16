from Mediator import Mediator


class Main:
    if __name__ == '__main__':
        mediator = Mediator()

        print("Welcome to the Movie Integrator 3000")
        print("")
        print("Please enter")
        print("If you want to search by movie name please enter '1, <your movie>' (Example: 1, John Wick)")
        print("If you want to search by imdb-ID please enter '2, <imdb-ID>' (Example: 2, tt2911666")

        dir, input = input().split(',')
        input = input.lstrip()

        if dir == "1":
            print("Processing..")
            mediator.showData(input, "1")

        elif dir == "2":
            print("Processing..")
            mediator.showData(input, "2")

        else:
            print("Your input was wrong.")