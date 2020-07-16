from Mediator import Mediator


class Main:
    if __name__ == '__main__':
        mediator = Mediator()

        print("Welcome to the Movie Integrator 3000")
        print("")
        print("Please enter")
        print("If you want to search by movie name please enter '1; <your movie>' (Example: '1; John Wick)'")
        print("If you want to search by imdb-ID please enter '2; <imdb-ID>' (Example: '2; tt2911666')")
        # Probiere den String zu Teilen, wird ein falscher Separator, kein Separator oder zuviele Separators verwendet
        # wird ValueError geworfen
        try:
            dir, input = input().split(';')
            input = input.lstrip()
            if dir == "1":
                print("Processing..")
                mediator.showData(input, "1")

            elif dir == "2":
                print("Processing..")
                mediator.showData(input, "2")
        except ValueError:
            print("Your input contained an invalid separator, no separator or multiple separators or contained no mode selector"
                  ", allowed separators are ';'. Please try again! (ValueError)")
        else:
            print('Your input contained an invalid mode selector, allowed values are 1 and 2. Please try again! (InvalidModeError)')