command = "" # Initialize command variable
started = False # Initialize car state
while True: # Main game loop
    command = input("Enter command: ").lower() # Get user input
    if command == "start": # Start the car
        if started: # Check if the car is already started
            print("Car is already started!") # Inform the user that the car is already started
        else: 
            started = True # Update car state
            print("Car started....") # Inform the user that the car has started
    elif command == "stop": # Stop the car
        if not started: # Check if the car is already stopped
            print("Car is already stopped!") # Inform the user that the car is already stopped
        else:
            started = False # Update car state
            print("Car stopped.") # Inform the user that the car has stopped
    elif command == "help": # Show available commands
        print('''
Available commands:
- start: Start the car
- stop: Stop the car
- exit: Exit the game
        ''')
    elif command == "exit": # Exit the game
        print("Exiting the game...")
        break # Exit the main game loop
    else:
        print("Invalid command.")
        print("Type 'help' for a list of available commands.")