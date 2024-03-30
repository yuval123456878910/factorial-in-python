def factorial():
    print("this is factorial calculator.")
    math = input("choose '!' : ")

    factorailSetings = None
    time = None
    forQB = None

    if math == "!":
        try:




            factorailSetings = int(input("now choose a number: "))
            time = factorailSetings -1
            forQB = factorailSetings

        except:
            print("you need a number")
        try:
            while time != 0 and forQB != 0:

                if time == 1:

                    print(forQB * (factorailSetings - 1))

                forQB = forQB * (factorailSetings - 1)

                factorailSetings = factorailSetings - 1

                time = time - 1
        except:
            print("to big number!")

factorial()
