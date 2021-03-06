import time
import math
from view import *
from model import *

isGameOver = False
winner = False

def play_game(username, view, model):
    view.display_initial_message(username)
    while not isGameOver:
        move = view.accept_move()
        execute(model, move)
    view.final_message(username, winner)
#    exit(0)

def execute(model, move):
    global isGameOver
    if move == 'show circuit':
        model.draw_current_circuit()
        return
    type_hammer, hole = move[0], move[1]
    
    if type_hammer == 'c':
        print("Classical Smash!!!")
        isGameOver = True
        global winner
        winner = classical_smash(model, hole)
        #print(winner)
    else:
        print('Quantum Smash!!!')
        quantum_smash(model, hole)

def classical_smash(model, hole):
    measured_hole = model.measureState()
    hole = int(hole)
    #print(measured_hole, hole, type(hole), (measured_hole==[0,0] and hole==1))
    result = (measured_hole==[0,0] and hole==1) or (measured_hole==[0,1] and hole==2) or (measured_hole==[1,0] and hole==3) or (measured_hole==[1,1] and hole==4)
    #print(result)
    return result

def translate_hole(hole):
    hole = int(hole)
    if hole==1:
        return [0,0]
    if hole==2:
        return [1,0]
    if hole==3:
        return [0,1]
    if hole==4:
        return [1,1]
    else:
        assert False, 'bug!!'


def quantum_smash(model, hole):
    #hint is a number or a complex number

    prob = model.getProbabilityOf(translate_hole(hole))
    hint = f"{'{0.real:.3f} + {0.imag:.3f}i'.format(prob)} \nProbability: {round(abs(prob)**2, 3)}"
    view.display_quantum_message(hint, hole)
    gate_details = view.accept_quantum_gate()

    if gate_details[0] == 'r' or gate_details[0] == 'R':
        model.add_r_gate(math.radians(float(gate_details[1])), int(gate_details[2]))

    if gate_details[0] == 'cx' or gate_details[0] == 'CX':
        model.add_cnot(int(gate_details[1]), int(gate_details[2]))

    if gate_details[0] == 'ancilla' or gate_details[0] == 'ANCILLA':
        model.add_ancilla(gate_details[1])

    else:
        model.add_unitary(gate_details[0], int(gate_details[2]))

    model.draw_current_circuit()

def initialize_game():
    username = input("What is your name? ")
    view = View()
    model = Model()
    return username, view, model

if __name__ == '__main__':
    x = input("Do you want to play Quantum Whack-a-Mole? (yes/no) ")
    if x == 'Yes' or x=="yes":
        username, view, model = initialize_game()
        play_game(username, view, model)
    else:
        exit(0)
