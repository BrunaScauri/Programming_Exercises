# CAR GAME
readLine = input('>')
helpCommand = print("""start - to start the car
stop - to stop the car
quit - to exit""")
car_started = False

while True:
    readLine = input('>')
    if readLine == 'start':
        if car_started:
            (print('The car is already on!'))
        else:
            car_started = True
            print('Car started, ready to go!')
    elif readLine == 'stop':
        if not car_started:
            print('the car is already stopped!')
        else:
            car_started = False
            print('Car stopped.')
    elif readLine == 'help':
        print(helpCommand)
    elif readLine == 'quit':
        break
    else:
        print("I don't understand that...")
