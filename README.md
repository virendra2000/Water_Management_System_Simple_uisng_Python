# Water Tank Management Simulation

This is a simple Python project that simulates a water tank management scenario. It was created as a coding practice exercise to demonstrate basic programming concepts such as input handling, conditionals, and loops.

## Project Overview

The project simulates a scenario where a user repeatedly requests a certain amount of water until the tank is empty. The program tracks the remaining tank size, handles out-of-range requests, and provides the user with real-time updates.

## Getting Started

To run the simulation on your local machine, follow these steps:

1. Ensure you have Python installed on your computer.
2. Clone this repository to your local machine.
3. Open a terminal or command prompt in the project directory.
5. Run the following command:
   notepad water_tank_simulation.py
6. Copy & Paste the Following Code :
   tank_size = 500
   for i in range(1,tank_size+1):
    print("Asking At Stop",i)
    user_ip = int(input("How Many Litre of Water Do You Want : \n"))
    if(user_ip>tank_size):
        print("Out Of Range")
        print("Remaining Tank Size : ",tank_size)
        if(tank_size==0):
            break
        else:
            user_ip = int(input("Enter in Sufficient Amount From Remaining \n"))
            tank_size = tank_size - user_ip
            print("Remaining Tank Size : ",tank_size)
    else:
        tank_size = tank_size - user_ip
        print("Remaining Tank Size : ",tank_size)
    i=tank_size
7. Save Your File.
8. Again go to Command Prompt You have opened Last time .
9. Run the Following Command  :
    python water_tank_simulation.py
# Contributing
If you'd like to contribute to this project or make improvements, please feel free to fork the repository, make your changes, and submit a pull request.

# License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

# Acknowledgments
This project was created as a coding practice exercise and for educational purposes. It's a simple illustration of basic programming concepts in Python.

# Happy Coding! 🚀
