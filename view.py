import time

class View:

    BOARD_STRING = "|------------|" \
                   "\n|  1  |   2  |" \
                   "\n|------------|" \
                   "\n|  3  |   4  |" \
                   "\n-------------|"

    def __init__(self, argument=1):
        pass

    def display_initial_message(self, username):
            self.display_board()
            time.sleep(3)
            print("Whacker : " + username)
            time.sleep(3)
            print("\nThere's a mole out there...")
            time.sleep(3)
            print("It exists here, there and everywhere ... at once")
            time.sleep(3)
            print("We bestow upon you the Quantum Hammer!!!")
            time.sleep(3)
            print("Use it and end the terror of the Quantum-mole!")

    def accept_move(self):
        valid_in = False
        while not valid_in:
            x = input("What are you going to do? Enter c for classical smash and q for quantum smash (e.g. q1): ")
            valid_in = (len(x)==2 and 0 < int(x[1]) <= 4 and (x[0] == 'c' or x[0] == 'q'))
            if not valid_in:
                print("Invalid input, try again!!")
        return x

    def final_message(self, username, win):
        if win:
            print("Wow ...")
            time.sleep(3)
            print("The Quantum-Mole is really gone ...")
            time.sleep(3)
            print("You did it " + username)
            print("Congratulations!!!")

        else:
            print("Alas...")
            print("The quantum mole lives on ... it is here, there and everywhere ... at once")

    def display_quantum_message(self, hint, hole):
        print("New Information!!!")
        time.sleep(3)
        print("Probability amplitude of mole being in hole " + hole + " is ", hint)
        time.sleep(3)

    def display_board(self):
        print(View.BOARD_STRING)

    def accept_quantum_gate(self):
        result = []
        gate = input("What quantum gate do you wish to add to the circuit? ")
        result.append(gate)

        if gate == 'r' or gate == 'R':
            invalid_in = True
            while invalid_in:
                angle = input("Enter phase")
                try:
                    result.append(angle)
                    invalid_in = False
                except:
                    print("Invalid input, please try again!")
                    invalid_in = True

            target_qubit = input("Enter target qubit: ")
            result.append(target_qubit)


        elif gate == 'cx' or gate == 'CX':
            control_qubit = input("Enter control qubit: ")
            result.append(control_qubit)
            target_qubit = input("Enter target qubit: ")
            result.append(target_qubit)


        elif gate == 'ancilla' or gate == 'ANCILLA':
            num_ancilla = input("How many ancilla qubits do you want? Please enter a positive integer: ")
            num_ancilla = int(num_ancilla)
            result.append(num_ancilla)

        else:
          result.append("b")
          target_qubit = input("Enter target qubit: ")
          result.append(target_qubit)

        return result