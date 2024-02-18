import tkinter as tk
import random
import numpy as np
import colorama
from tkinter import font
from colorama import Fore

# Define the colors
colors = {'1': 'yellow', '2': 'red', '3': 'green', '4': 'blue', '5': 'orange', '6': 'white'}

# Function to generate a random Rubik's Cube configuration
def generate_cube():
    cube = {}
    color_code_sides = []  # List to store color code sides
    for side in ['Top', 'Front', 'Right', 'Left', 'Back', 'Down']:
        color_code_side = [[random.randint(1, 6) for _ in range(3)] for _ in range(3)]  # Generate color code side
        color_code_sides.append(color_code_side)  # Append to the list
        cube[side] = color_code_side  # Store in the cube dictionary
    return cube, color_code_sides

# Create a Tkinter window
root = tk.Tk()
root.title("Rubik's Cube")

# Generate a random Rubik's Cube and get the color code sides
rubiks_cube, color_code_sides = generate_cube()

# Function to update the labels with Rubik's Cube colors
def update_cube_display(cube):
    max_rows = max(len(side) for side in cube.values())
    max_cols = max(len(row) for side in cube.values() for row in side)
    
    block_size = 60  # Size of each block
    padding = 10  # Padding between sides

    window_width = max_cols * block_size * 6 + padding * 5  # 6 sides in total with padding in between
    window_height = max_rows * block_size + 100  # Added some extra height for the side names

    root.geometry(f"{window_width}x{window_height}")

    for side, side_colors in cube.items():
        for i, row in enumerate(side_colors):
            for j, item in enumerate(row):
                label = tk.Label(root, bg=colors[str(item)], width=4, height=2, text=str(item))
                label.grid(row=i + 1, column=j + 1 + (max_cols + padding) * ['Top', 'Front', 'Right', 'Left', 'Back', 'Down'].index(side), padx=1, pady=1)
                label.bind('<Button-1>', lambda event, s=side, r=i, c=j: change_color(event, s, r, c))  # Bind click event
        name_label = tk.Label(root, text=f"{side}", font=("Helvetica", 12))  # Full name
        name_label.grid(row=max_rows + 2, column=(max_cols + padding) * ['Top', 'Front', 'Right', 'Left', 'Back', 'Down'].index(side) + max_cols // 2, columnspan=max_cols, pady=5)



# Function to change the color of a block on a side
def change_color(event, side, row, col):
    current_color = rubiks_cube[side][row][col]  # Get the current color
    new_color = (current_color % 6) + 1  # Change to the next color (cycling through 1 to 6)
    rubiks_cube[side][row][col] = new_color  # Update the cube data
    event.widget.config(bg=colors[str(new_color)], text=str(new_color))  # Update the label
    
    # Update the color code sides
    update_color_code_sides()

# Function to update the color code sides after user changes
def update_color_code_sides():
    global color_code_sides, rubiks_cube
    for i, side in enumerate(['Top', 'Front', 'Right', 'Left', 'Back', 'Down']):
        color_code_sides[i] = rubiks_cube[side]

# Update the labels with Rubik's Cube colors for all sides
update_cube_display(rubiks_cube)

# Run the Tkinter event loop
root.mainloop()

T = np.array(color_code_sides[0])
F = np.array(color_code_sides[1])
R = np.array(color_code_sides[2])
L = np.array(color_code_sides[3])
B = np.array(color_code_sides[4])
D = np.array(color_code_sides[5])


print(Fore.BLUE + 'Please wait! Solution is loading...')
def rotation(rot):
    global T, F, R, L, B, D
    if (rot == 'u' or rot == 'U'):
        Ver_u = np.vstack((T, F, R, L, B, D))
        Ver_u[[3, 6, 9, 14]] = Ver_u[[6, 14, 3, 9]]
        F = Ver_u[3:6]
        R_x = Ver_u[6:9]
        R_x[0:1, [0, 2]] = R_x[0:1, [2, 0]]
        R = R_x
        L = Ver_u[9:12]
        B_x = Ver_u[12:15]
        B_x[2:3, [0, 2]] = B_x[2:3, [2, 0]]
        B = B_x
        Up_U = np.transpose(Ver_u[0:3])
        Up_U[:, [0, 2]] = Up_U[:, [2, 0]]
        T = Up_U
    elif (rot == 'u1' or rot == 'U1'):
        Ver_u1 = np.vstack((T, F, R, L, B, D))
        Ver_u1[[3, 6, 9, 14]] = Ver_u1[[9, 3, 14, 6]]
        F = Ver_u1[3:6]
        R = Ver_u1[6:9]
        L_x = Ver_u1[9:12]
        L_x[0:1, [0, 2]] = L_x[0:1, [2, 0]]
        L = L_x
        B_x = Ver_u1[12:15]
        B_x[2:3, [0, 2]] = B_x[2:3, [2, 0]]
        B = B_x
        T_x = np.transpose(Ver_u1[0:3])
        T_x[[0, 2], 0:3] = T_x[[2, 0], 0:3]
        T = T_x
    elif (rot == 'd' or rot == 'D'):
        Ver_d = np.vstack((T, F, R, L, B, D))
        Ver_d[[5, 8, 11, 12]] = Ver_d[[11, 5, 12, 8]]
        F = Ver_d[3:6]
        R = Ver_d[6:9]
        L_x = Ver_d[9:12]
        L_x[2:3, [0, 2]] = L_x[2:3, [2, 0]]
        L = L_x
        B_x = Ver_d[12:15]
        B_x[0:1, [0, 2]] = B_x[0:1, [2, 0]]
        B = B_x
        Down_d = np.transpose(Ver_d[15:18])
        Down_d[:, [0, 2]] = Down_d[:, [2, 0]]
        D = Down_d
    elif (rot == 'd1' or rot == 'D1'):
        Ver_d1 = np.vstack((T, F, R, L, B, D))
        Ver_d1[[5, 8, 11, 12]] = Ver_d1[[8, 12, 5, 11]]
        F = Ver_d1[3:6]
        R_x = Ver_d1[6:9]
        R_x[2:3, [0, 2]] = R_x[2:3, [2, 0]]
        R = R_x
        L = Ver_d1[9:12]
        B_x = Ver_d1[12:15]
        B_x[0:1, [0, 2]] = B_x[0:1, [2, 0]]
        B = B_x
        D_x = np.transpose(Ver_d1[15:18])
        D_x[[0, 2], 0:3] = D_x[[2, 0], 0:3]
        D = D_x
    elif (rot == 'r' or rot == 'R'):
        Hor_r = np.hstack((T, F, R, L, B, D))
        Hor_r[:, [2, 5, 14, 17]] = Hor_r[:, [5, 17, 2, 14]]
        T = Hor_r[:, [0, 1, 2]]
        F = Hor_r[:, [3, 4, 5]]
        B = Hor_r[:, [12, 13, 14]]
        D = Hor_r[:, [15, 16, 17]]
        Right_R = np.transpose(Hor_r[:, [6, 7, 8]])
        Right_R[:, [0, 2]] = Right_R[:, [2, 0]]
        R = Right_R
    elif (rot == 'r1' or rot == 'R1'):
        Hor_r1 = np.hstack((T, F, R, L, B, D))
        Hor_r1[:, [2, 5, 14, 17]] = Hor_r1[:, [14, 2, 17, 5]]
        T = Hor_r1[:, [0, 1, 2]]
        F = Hor_r1[:, [3, 4, 5]]
        B = Hor_r1[:, [12, 13, 14]]
        D = Hor_r1[:, [15, 16, 17]]
        R_x = np.transpose(Hor_r1[:, [6, 7, 8]])
        R_x[[0, 2], 0:3] = R_x[[2, 0], 0:3]
        R = R_x
    elif (rot == 'l' or rot == 'L'):
        Hor_l = np.hstack((T, F, R, L, B, D))
        Hor_l[:, [0, 3, 12, 15]] = Hor_l[:, [12, 0, 15, 3]]
        T = Hor_l[:, [0, 1, 2]]
        F = Hor_l[:, [3, 4, 5]]
        B = Hor_l[:, [12, 13, 14]]
        D = Hor_l[:, [15, 16, 17]]
        Left_l = np.transpose(Hor_l[:, [9, 10, 11]])
        Left_l[:, [0, 2]] = Left_l[:, [2, 0]]
        L = Left_l
    elif (rot == 'l1' or rot == 'L1'):
        Hor_l1 = np.hstack((T, F, R, L, B, D))
        Hor_l1[:, [0, 3, 12, 15]] = Hor_l1[:, [3, 15, 0, 12]]
        T = Hor_l1[:, [0, 1, 2]]
        F = Hor_l1[:, [3, 4, 5]]
        B = Hor_l1[:, [12, 13, 14]]
        D = Hor_l1[:, [15, 16, 17]]
        L_x = np.transpose(Hor_l1[:, [9, 10, 11]])
        L_x[[0, 2], 0:3] = L_x[[2, 0], 0:3]
        L = L_x
    elif (rot == 'f' or rot == 'F'):
        Hor_f = np.hstack((T, F, R, L, B, D))
        T_a = Hor_f[0:2, 0:3]
        L_c = Hor_f[:, 11]
        T_x = np.append(T_a, [L_c], axis=0)
        T_x[2:3, [0, 2]] = T_x[2:3, [2, 0]]
        T = T_x
        R_a = Hor_f[0:3, 7:9]
        T_c = Hor_f[2:3, 0:3]
        R = np.transpose(np.vstack([T_c, np.transpose(R_a)]))
        L_c = Hor_f[0:3, 9:11]
        D_a = Hor_f[0:1, 15:18]
        L = np.transpose(np.vstack([np.transpose(L_c), D_a]))
        D_bc = Hor_f[1:3, 15:18]
        R_a_col = Hor_f[:, 6]
        D_x = np.vstack((R_a_col, D_bc))
        D_x[0:1, [0, 2]] = D_x[0:1, [2, 0]]
        D = D_x
        Front_f = np.transpose(Hor_f[:, [3, 4, 5]])
        Front_f[:, [0, 2]] = Front_f[:, [2, 0]]
        F = Front_f
    elif (rot == 'f1' or rot == 'F1'):
        Hor_f1 = np.hstack((T, F, R, L, B, D))
        T_a = Hor_f1[0:2, 0:3]
        R_c = Hor_f1[:, 6]
        T = np.append(T_a, [R_c], axis=0)
        R_a = Hor_f1[0:3, 7:9]
        D_a = Hor_f1[0:1, 15:18]
        R_x = np.transpose(np.vstack([D_a, np.transpose(R_a)]))
        R_x[[0, 2], 0:1] = R_x[[2, 0], 0:1]
        R = R_x
        L_c = Hor_f1[0:3, 9:11]
        T_c = Hor_f1[2:3, 0:3]
        L_x = np.transpose(np.vstack([np.transpose(L_c), T_c]))
        L_x[[0, 2], 2:3] = L_x[[2, 0], 2:3]
        L = L_x
        D_bc = Hor_f1[1:3, 15:18]
        L_a_col = Hor_f1[:, 11]
        D = np.vstack((L_a_col, D_bc))
        F_x = np.transpose(Hor_f1[:, [3, 4, 5]])
        F_x[[0, 2], 0:3] = F_x[[2, 0], 0:3]
        F = F_x
    elif (rot == 'b' or rot == 'B'):
        Hor_b = np.hstack((T, F, R, L, B, D))
        T_bc = Hor_b[1:3, 0:3]
        R_c = Hor_b[:, 8]
        Top_t = np.append(T_bc, [R_c], axis=0)
        Top_t[[0, 1, 2], :] = Top_t[[2, 0, 1], :]
        T = Top_t
        R_ab = Hor_b[0:3, 6:8]
        D_c = Hor_b[2:3, 15:18]
        R_x = np.hstack((R_ab, np.transpose(D_c)))
        R_x[[0, 2], 2:3] = R_x[[2, 0], 2:3]
        R = R_x
        L_bc = Hor_b[0:3, 10:12]
        T_a = Hor_b[0:1, 0:3]
        L_x = np.hstack((np.transpose(T_a), L_bc))
        L_x[[0, 2], 0:1] = L_x[[2, 0], 0:1]
        L = L_x
        D_ab = Hor_b[0:2, 15:18]
        L_a_col = Hor_b[:, 9]
        D = np.vstack((D_ab, L_a_col))
        Back_b = np.transpose(Hor_b[:, [12, 13, 14]])
        Back_b[:, [0, 2]] = Back_b[:, [2, 0]]
        B = Back_b
    elif (rot == 'b1' or rot == 'B1'):
        Hor_b1 = np.hstack((T, F, R, L, B, D))
        T_bc = Hor_b1[1:3, 0:3]
        L_a = Hor_b1[:, 9]
        T_x = np.vstack((L_a, T_bc))
        T_x[0:1, [0, 2]] = T_x[0:1, [2, 0]]
        T = T_x
        R_ab = Hor_b1[0:3, 6:8]
        T_a = Hor_b1[0:1, 0:3]
        R = np.hstack((R_ab, np.transpose(T_a)))
        L_bc = Hor_b1[0:3, 10:12]
        D_c = Hor_b1[2:3, 15:18]
        L = np.hstack((np.transpose(D_c), L_bc))
        D_ab = Hor_b1[0:2, 15:18]
        R_c_col = Hor_b1[:, 8]
        D_x = np.vstack((D_ab, R_c_col))
        D_x[2:3, [0, 2]] = D_x[2:3, [2, 0]]
        D = D_x
        B_x = np.transpose(Hor_b1[0:3, [12, 13, 14]])
        B_x[[0, 2], 0:3] = B_x[[2, 0], 0:3]
        B = B_x
    elif (rot == 'm' or rot == 'M'):
        Hor_m = np.hstack((T, F, R, L, B, D))
        Hor_m[:, [1, 4, 13, 16]] = Hor_m[:, [4, 16, 1, 13]]
        T = Hor_m[:, [0, 1, 2]]
        F = Hor_m[:, [3, 4, 5]]
        B = Hor_m[:, [12, 13, 14]]
        D = Hor_m[:, [15, 16, 17]]

print(Fore.GREEN + '> Assembling the rotation-----------------Completed')
solutions = []

while (T[0][1] != 6 or T[1][0] != 6 or T[1][2] != 6 or T[2][1] != 6):
    # Front
    front_white = np.hstack((T, F, R, L, B, D))

    while front_white[0, [4]] == 6:
        if front_white[0, [4]] == 6:
            rotation('f')
            solutions.append('f')
            front_white = np.hstack((T, F, R, L, B, D))
            if front_white[1, [2]] == 6:
                rotation('u')
                solutions.append('u')
                front_white = np.hstack((T, F, R, L, B, D))
                if front_white[1, [2]] == 6:
                    rotation('u')
                    solutions.append('u')
                    front_white = np.hstack((T, F, R, L, B, D))
                    if front_white[1, [2]] == 6:
                        rotation('u')
                        solutions.append('u')
                        front_white = np.hstack((T, F, R, L, B, D))
                        if front_white[1, [2]] == 6:
                            rotation('u')
                            solutions.append('u')
                            front_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('r')
                            solutions.append('r')
                            front_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('r')
                        solutions.append('r')
                        front_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('r')
                    solutions.append('r')
                    front_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('r')
                solutions.append('r')
                front_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        front_white = np.hstack((T, F, R, L, B, D))

    while front_white[1, [3]] == 6:
        if front_white[1, [3]] == 6:
            if front_white[1, [0]] == 6:
                rotation('u')
                solutions.append('u')
                front_white = np.hstack((T, F, R, L, B, D))
                if front_white[1, [0]] == 6:
                    rotation('u')
                    solutions.append('u')
                    front_white = np.hstack((T, F, R, L, B, D))
                    if front_white[1, [0]] == 6:
                        rotation('u')
                        solutions.append('u')
                        front_white = np.hstack((T, F, R, L, B, D))
                        if front_white[1, [0]] == 6:
                            rotation('u')
                            solutions.append('u')
                            front_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('l1')
                            solutions.append('l1')
                            front_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('l1')
                        solutions.append('l1')
                        front_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('l1')
                    solutions.append('l1')
                    front_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('l1')
                solutions.append('l1')
                front_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        front_white = np.hstack((T, F, R, L, B, D))

    while front_white[1, [5]] == 6:
        if front_white[1, [5]] == 6:
            if front_white[1, [2]] == 6:
                rotation('u')
                solutions.append('u')
                front_white = np.hstack((T, F, R, L, B, D))
                if front_white[1, [2]] == 6:
                    rotation('u')
                    solutions.append('u')
                    front_white = np.hstack((T, F, R, L, B, D))
                    if front_white[1, [2]] == 6:
                        rotation('u')
                        solutions.append('u')
                        front_white = np.hstack((T, F, R, L, B, D))
                        if front_white[1, [2]] == 6:
                            rotation('u')
                            solutions.append('u')
                            front_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('r')
                            solutions.append('r')
                            front_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('r')
                        solutions.append('r')
                        front_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('r')
                    solutions.append('r')
                    front_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('r')
                solutions.append('r')
                front_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        front_white = np.hstack((T, F, R, L, B, D))

    while front_white[2, [4]] == 6:
        if front_white[2, [4]] == 6:
            if front_white[2, [1]] == 6:
                rotation('u')
                solutions.append('u')
                front_white = np.hstack((T, F, R, L, B, D))
                if front_white[2, [1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    front_white = np.hstack((T, F, R, L, B, D))
                    if front_white[2, [1]] == 6:
                        rotation('u')
                        solutions.append('u')
                        front_white = np.hstack((T, F, R, L, B, D))
                        if front_white[2, [1]] == 6:
                            rotation('u')
                            solutions.append('u')
                            front_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('f')
                            solutions.append('f')
                            front_white = np.hstack((T, F, R, L, B, D))
                            rotation('f')
                            solutions.append('f')
                            front_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('f')
                        solutions.append('f')
                        front_white = np.hstack((T, F, R, L, B, D))
                        rotation('f')
                        solutions.append('f')
                        front_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('f')
                    solutions.append('f')
                    front_white = np.hstack((T, F, R, L, B, D))
                    rotation('f')
                    solutions.append('f')
                    front_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('f')
                solutions.append('f')
                front_white = np.hstack((T, F, R, L, B, D))
                rotation('f')
                solutions.append('f')
                front_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        front_white = np.hstack((T, F, R, L, B, D))
        if front_white[0, [4]] == 6:
            rotation('f')
            solutions.append('f')
            front_white = np.hstack((T, F, R, L, B, D))
            if front_white[1, [2]] == 6:
                rotation('u')
                solutions.append('u')
                front_white = np.hstack((T, F, R, L, B, D))
                if front_white[1, [2]] == 6:
                    rotation('u')
                    solutions.append('u')
                    front_white = np.hstack((T, F, R, L, B, D))
                    if front_white[1, [2]] == 6:
                        rotation('u')
                        solutions.append('u')
                        front_white = np.hstack((T, F, R, L, B, D))
                        if front_white[1, [2]] == 6:
                            rotation('u')
                            solutions.append('u')
                            front_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('r')
                            solutions.append('r')
                            front_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('r')
                        solutions.append('r')
                        front_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('r')
                    solutions.append('r')
                    front_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('r')
                solutions.append('r')
                front_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        front_white = np.hstack((T, F, R, L, B, D))

    # Right

    right_white = np.hstack((T, F, R, L, B, D))

    while right_white[0, [7]] == 6:
        if right_white[0, [7]] == 6:
            rotation('r')
            solutions.append('r')
            right_white = np.hstack((T, F, R, L, B, D))
            if right_white[0, [1]] == 6:
                rotation('u')
                solutions.append('u')
                right_white = np.hstack((T, F, R, L, B, D))
                if right_white[0, [1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    right_white = np.hstack((T, F, R, L, B, D))
                    if right_white[0, [1]] == 6:
                        rotation('u')
                        solutions.append('u')
                        right_white = np.hstack((T, F, R, L, B, D))
                        if right_white[0, [1]] == 6:
                            rotation('u')
                            solutions.append('u')
                            right_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('b')
                            solutions.append('b')
                            right_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('b')
                        solutions.append('b')
                        right_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('b')
                    solutions.append('b')
                    right_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('b')
                solutions.append('b')
                right_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        right_white = np.hstack((T, F, R, L, B, D))

    while right_white[1, [6]] == 6:
        if right_white[1, [6]] == 6:
            if right_white[2, [1]] == 6:
                rotation('u')
                solutions.append('u')
                right_white = np.hstack((T, F, R, L, B, D))
                if right_white[2, [1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    right_white = np.hstack((T, F, R, L, B, D))
                    if right_white[2, [1]] == 6:
                        rotation('u')
                        solutions.append('u')
                        right_white = np.hstack((T, F, R, L, B, D))
                        if right_white[2, [1]] == 6:
                            rotation('u')
                            solutions.append('u')
                            right_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('f1')
                            solutions.append('f1')
                            right_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('f1')
                        solutions.append('f1')
                        right_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('f1')
                    solutions.append('f1')
                    right_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('f1')
                solutions.append('f1')
                right_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        right_white = np.hstack((T, F, R, L, B, D))

    while right_white[1, [8]] == 6:
        if right_white[1, [8]] == 6:
            if right_white[0, [1]] == 6:
                rotation('u')
                solutions.append('u')
                right_white = np.hstack((T, F, R, L, B, D))
                if right_white[0, [1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    right_white = np.hstack((T, F, R, L, B, D))
                    if right_white[0, [1]] == 6:
                        rotation('u')
                        solutions.append('u')
                        right_white = np.hstack((T, F, R, L, B, D))
                        if right_white[0, [1]] == 6:
                            rotation('u')
                            solutions.append('u')
                            right_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('b')
                            solutions.append('b')
                            right_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('b')
                        solutions.append('b')
                        right_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('b')
                    solutions.append('b')
                    right_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('b')
                solutions.append('b')
                right_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        right_white = np.hstack((T, F, R, L, B, D))

    while right_white[2, [7]] == 6:
        if right_white[2, [7]] == 6:
            if right_white[1, [2]] == 6:
                rotation('u')
                solutions.append('u')
                right_white = np.hstack((T, F, R, L, B, D))
                if right_white[1, [2]] == 6:
                    rotation('u')
                    solutions.append('u')
                    right_white = np.hstack((T, F, R, L, B, D))
                    if right_white[1, [2]] == 6:
                        rotation('u')
                        solutions.append('u')
                        right_white = np.hstack((T, F, R, L, B, D))
                        if right_white[1, [2]] == 6:
                            rotation('u')
                            solutions.append('u')
                            right_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('r1')
                            solutions.append('r1')
                            right_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('r1')
                        solutions.append('r1')
                        right_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('r1')
                    solutions.append('r1')
                    right_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('r1')
                solutions.append('r1')
                right_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        right_white = np.hstack((T, F, R, L, B, D))
        if right_white[1, [8]] == 6:
            if right_white[0, [1]] == 6:
                rotation('u')
                solutions.append('u')
                right_white = np.hstack((T, F, R, L, B, D))
                if right_white[0, [1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    right_white = np.hstack((T, F, R, L, B, D))
                    if right_white[0, [1]] == 6:
                        rotation('u')
                        solutions.append('u')
                        right_white = np.hstack((T, F, R, L, B, D))
                        if right_white[0, [1]] == 6:
                            rotation('u')
                            solutions.append('u')
                            right_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('b')
                            solutions.append('b')
                            right_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('b')
                        solutions.append('b')
                        right_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('b')
                    solutions.append('b')
                    right_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('b')
                solutions.append('b')
                right_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        right_white = np.hstack((T, F, R, L, B, D))

    # Left

    left_white = np.hstack((T, F, R, L, B, D))

    while left_white[0, [10]] == 6:
        if left_white[0, [10]] == 6:
            rotation('l')
            solutions.append('l')
            left_white = np.hstack((T, F, R, L, B, D))
            if left_white[2, [1]] == 6:
                rotation('u')
                solutions.append('u')
                left_white = np.hstack((T, F, R, L, B, D))
                if left_white[2, [1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    left_white = np.hstack((T, F, R, L, B, D))
                    if left_white[2, [1]] == 6:
                        rotation('u')
                        solutions.append('u')
                        left_white = np.hstack((T, F, R, L, B, D))
                        if left_white[2, [1]] == 6:
                            rotation('u')
                            solutions.append('u')
                            left_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('f')
                            solutions.append('f')
                            left_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('f')
                        solutions.append('f')
                        left_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('f')
                    solutions.append('f')
                    left_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('f')
                solutions.append('f')
                left_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        left_white = np.hstack((T, F, R, L, B, D))

    while left_white[1, [9]] == 6:
        if left_white[1, [9]] == 6:
            if left_white[0, [1]] == 6:
                rotation('u')
                solutions.append('u')
                left_white = np.hstack((T, F, R, L, B, D))
                if left_white[0, [1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    left_white = np.hstack((T, F, R, L, B, D))
                    if left_white[0, [1]] == 6:
                        rotation('u')
                        solutions.append('u')
                        left_white = np.hstack((T, F, R, L, B, D))
                        if left_white[0, [1]] == 6:
                            rotation('u')
                            solutions.append('u')
                            left_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('b1')
                            solutions.append('b1')
                            left_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('b1')
                        solutions.append('b1')
                        left_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('b1')
                    solutions.append('b1')
                    left_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('b1')
                solutions.append('b1')
                left_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        left_white = np.hstack((T, F, R, L, B, D))

    while left_white[1, [11]] == 6:
        if left_white[1, [11]] == 6:
            if left_white[2, [1]] == 6:
                rotation('u')
                solutions.append('u')
                left_white = np.hstack((T, F, R, L, B, D))
                if left_white[2, [1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    left_white = np.hstack((T, F, R, L, B, D))
                    if left_white[2, [1]] == 6:
                        rotation('u')
                        solutions.append('u')
                        left_white = np.hstack((T, F, R, L, B, D))
                        if left_white[2, [1]] == 6:
                            rotation('u')
                            solutions.append('u')
                            left_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('f')
                            solutions.append('f')
                            left_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('f')
                        solutions.append('f')
                        left_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('f')
                    solutions.append('f')
                    left_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('f')
                solutions.append('f')
                left_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        left_white = np.hstack((T, F, R, L, B, D))

    while left_white[2, [10]] == 6:
        if left_white[2, [10]] == 6:
            if left_white[1, [0]] == 6:
                rotation('u')
                solutions.append('u')
                left_white = np.hstack((T, F, R, L, B, D))
                if left_white[1, [0]] == 6:
                    rotation('u')
                    solutions.append('u')
                    left_white = np.hstack((T, F, R, L, B, D))
                    if left_white[1, [0]] == 6:
                        rotation('u')
                        solutions.append('u')
                        left_white = np.hstack((T, F, R, L, B, D))
                        if left_white[1, [0]] == 6:
                            rotation('u')
                            solutions.append('u')
                            left_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('l1')
                            solutions.append('l1')
                            left_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('l1')
                        solutions.append('l1')
                        left_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('l1')
                    solutions.append('l1')
                    left_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('l1')
                solutions.append('l1')
                left_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        left_white = np.hstack((T, F, R, L, B, D))
        if left_white[1, [11]] == 6:
            if left_white[2, [1]] == 6:
                rotation('u')
                solutions.append('u')
                left_white = np.hstack((T, F, R, L, B, D))
                if left_white[2, [1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    left_white = np.hstack((T, F, R, L, B, D))
                    if left_white[2, [1]] == 6:
                        rotation('u')
                        solutions.append('u')
                        left_white = np.hstack((T, F, R, L, B, D))
                        if left_white[2, [1]] == 6:
                            rotation('u')
                            solutions.append('u')
                            left_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('f')
                            solutions.append('f')
                            left_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('f')
                        solutions.append('f')
                        left_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('f')
                    solutions.append('f')
                    left_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('f')
                solutions.append('f')
                left_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        left_white = np.hstack((T, F, R, L, B, D))

    # Back

    back_white = np.hstack((T, F, R, L, B, D))

    while back_white[2, [13]] == 6:
        if back_white[2, [13]] == 6:
            rotation('b')
            solutions.append('b')
            back_white = np.hstack((T, F, R, L, B, D))
            if back_white[1, [0]] == 6:
                rotation('u')
                solutions.append('u')
                back_white = np.hstack((T, F, R, L, B, D))
                if back_white[1, [0]] == 6:
                    rotation('u')
                    solutions.append('u')
                    back_white = np.hstack((T, F, R, L, B, D))
                    if back_white[1, [0]] == 6:
                        rotation('u')
                        solutions.append('u')
                        back_white = np.hstack((T, F, R, L, B, D))
                        if back_white[1, [0]] == 6:
                            rotation('u')
                            solutions.append('u')
                            back_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('l')
                            solutions.append('l')
                            back_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('l')
                        solutions.append('l')
                        back_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('l')
                    solutions.append('l')
                    back_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('l')
                solutions.append('l')
                back_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        back_white = np.hstack((T, F, R, L, B, D))

    while back_white[1, [12]] == 6:
        if back_white[1, [12]] == 6:
            if back_white[1, [0]] == 6:
                rotation('u')
                solutions.append('u')
                back_white = np.hstack((T, F, R, L, B, D))
                if back_white[1, [0]] == 6:
                    rotation('u')
                    solutions.append('u')
                    back_white = np.hstack((T, F, R, L, B, D))
                    if back_white[1, [0]] == 6:
                        rotation('u')
                        solutions.append('u')
                        back_white = np.hstack((T, F, R, L, B, D))
                        if back_white[1, [0]] == 6:
                            rotation('u')
                            solutions.append('u')
                            back_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('l')
                            solutions.append('l')
                            back_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('l')
                        solutions.append('l')
                        back_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('l')
                    solutions.append('l')
                    back_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('l')
                solutions.append('l')
                back_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        back_white = np.hstack((T, F, R, L, B, D))

    while back_white[1, [14]] == 6:
        if back_white[1, [14]] == 6:
            if back_white[1, [2]] == 6:
                rotation('u')
                solutions.append('u')
                back_white = np.hstack((T, F, R, L, B, D))
                if back_white[1, [2]] == 6:
                    rotation('u')
                    solutions.append('u')
                    back_white = np.hstack((T, F, R, L, B, D))
                    if back_white[1, [2]] == 6:
                        rotation('u')
                        solutions.append('u')
                        back_white = np.hstack((T, F, R, L, B, D))
                        if back_white[1, [2]] == 6:
                            rotation('u')
                            solutions.append('u')
                            back_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('r1')
                            solutions.append('r1')
                            back_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('r1')
                        solutions.append('r1')
                        back_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('r1')
                    solutions.append('r1')
                    back_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('r1')
                solutions.append('r1')
                back_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        back_white = np.hstack((T, F, R, L, B, D))

    while back_white[0, [13]] == 6:
        if back_white[0, [13]] == 6:
            if back_white[0, [1]] == 6:
                rotation('u')
                solutions.append('u')
                back_white = np.hstack((T, F, R, L, B, D))
                if back_white[0, [1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    back_white = np.hstack((T, F, R, L, B, D))
                    if back_white[0, [1]] == 6:
                        rotation('u')
                        solutions.append('u')
                        back_white = np.hstack((T, F, R, L, B, D))
                        if back_white[0, [1]] == 6:
                            rotation('u')
                            solutions.append('u')
                            back_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('b1')
                            solutions.append('b1')
                            back_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('b1')
                        solutions.append('b1')
                        back_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('b1')
                    solutions.append('b1')
                    back_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('b1')
                solutions.append('b1')
                back_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        back_white = np.hstack((T, F, R, L, B, D))
        if back_white[1, [12]] == 6:
            if back_white[1, [0]] == 6:
                rotation('u')
                solutions.append('u')
                back_white = np.hstack((T, F, R, L, B, D))
                if back_white[1, [0]] == 6:
                    rotation('u')
                    solutions.append('u')
                    back_white = np.hstack((T, F, R, L, B, D))
                    if back_white[1, [0]] == 6:
                        rotation('u')
                        solutions.append('u')
                        back_white = np.hstack((T, F, R, L, B, D))
                        if back_white[1, [0]] == 6:
                            rotation('u')
                            solutions.append('u')
                            back_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('l')
                            solutions.append('l')
                            back_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('l')
                        solutions.append('l')
                        back_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('l')
                    solutions.append('l')
                    back_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('l')
                solutions.append('l')
                back_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        back_white = np.hstack((T, F, R, L, B, D))

    # Down

    down_white = np.hstack((T, F, R, L, B, D))

    while down_white[0, [16]] == 6:
        if down_white[0, [16]] == 6:
            if down_white[2, [1]] == 6:
                rotation('u')
                solutions.append('u')
                down_white = np.hstack((T, F, R, L, B, D))
                if down_white[2, [1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    down_white = np.hstack((T, F, R, L, B, D))
                    if down_white[2, [1]] == 6:
                        rotation('u')
                        solutions.append('u')
                        down_white = np.hstack((T, F, R, L, B, D))
                        if down_white[2, [1]] == 6:
                            rotation('u')
                            solutions.append('u')
                            down_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('f')
                            solutions.append('f')
                            down_white = np.hstack((T, F, R, L, B, D))
                            rotation('f')
                            solutions.append('f')
                            down_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('f')
                        solutions.append('f')
                        down_white = np.hstack((T, F, R, L, B, D))
                        rotation('f')
                        solutions.append('f')
                        down_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('f')
                    solutions.append('f')
                    down_white = np.hstack((T, F, R, L, B, D))
                    rotation('f')
                    solutions.append('f')
                    down_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('f')
                solutions.append('f')
                down_white = np.hstack((T, F, R, L, B, D))
                rotation('f')
                solutions.append('f')
                down_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        down_white = np.hstack((T, F, R, L, B, D))

    while down_white[1, [15]] == 6:
        if down_white[1, [15]] == 6:
            if down_white[1, [0]] == 6:
                rotation('u')
                solutions.append('u')
                down_white = np.hstack((T, F, R, L, B, D))
                if down_white[1, [0]] == 6:
                    rotation('u')
                    solutions.append('u')
                    down_white = np.hstack((T, F, R, L, B, D))
                    if down_white[1, [0]] == 6:
                        rotation('u')
                        solutions.append('u')
                        down_white = np.hstack((T, F, R, L, B, D))
                        if down_white[1, [0]] == 6:
                            rotation('u')
                            solutions.append('u')
                            down_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('l')
                            solutions.append('l')
                            down_white = np.hstack((T, F, R, L, B, D))
                            rotation('l')
                            solutions.append('l')
                            down_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('l')
                        solutions.append('l')
                        down_white = np.hstack((T, F, R, L, B, D))
                        rotation('l')
                        solutions.append('l')
                        down_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('l')
                    solutions.append('l')
                    down_white = np.hstack((T, F, R, L, B, D))
                    rotation('l')
                    solutions.append('l')
                    down_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('l')
                solutions.append('l')
                down_white = np.hstack((T, F, R, L, B, D))
                rotation('l')
                solutions.append('l')
                down_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        down_white = np.hstack((T, F, R, L, B, D))

    while down_white[1, [17]] == 6:
        if down_white[1, [17]] == 6:
            if down_white[1, [2]] == 6:
                rotation('u')
                solutions.append('u')
                down_white = np.hstack((T, F, R, L, B, D))
                if down_white[1, [2]] == 6:
                    rotation('u')
                    solutions.append('u')
                    down_white = np.hstack((T, F, R, L, B, D))
                    if down_white[1, [2]] == 6:
                        rotation('u')
                        solutions.append('u')
                        down_white = np.hstack((T, F, R, L, B, D))
                        if down_white[1, [2]] == 6:
                            rotation('u')
                            solutions.append('u')
                            down_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('r')
                            solutions.append('r')
                            down_white = np.hstack((T, F, R, L, B, D))
                            rotation('r')
                            solutions.append('r')
                            down_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('r')
                        solutions.append('r')
                        down_white = np.hstack((T, F, R, L, B, D))
                        rotation('r')
                        solutions.append('r')
                        down_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('r')
                    solutions.append('r')
                    down_white = np.hstack((T, F, R, L, B, D))
                    rotation('r')
                    solutions.append('r')
                    down_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('r')
                solutions.append('r')
                down_white = np.hstack((T, F, R, L, B, D))
                rotation('r')
                solutions.append('r')
                down_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        down_white = np.hstack((T, F, R, L, B, D))

    while down_white[2, [16]] == 6:
        if down_white[2, [16]] == 6:
            if down_white[0, [1]] == 6:
                rotation('u')
                solutions.append('u')
                down_white = np.hstack((T, F, R, L, B, D))
                if down_white[0, [1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    down_white = np.hstack((T, F, R, L, B, D))
                    if down_white[0, [1]] == 6:
                        rotation('u')
                        solutions.append('u')
                        down_white = np.hstack((T, F, R, L, B, D))
                        if down_white[0, [1]] == 6:
                            rotation('u')
                            solutions.append('u')
                            down_white = np.hstack((T, F, R, L, B, D))
                        else:
                            rotation('b1')
                            solutions.append('b1')
                            down_white = np.hstack((T, F, R, L, B, D))
                            rotation('b1')
                            solutions.append('b1')
                            down_white = np.hstack((T, F, R, L, B, D))
                    else:
                        rotation('b1')
                        solutions.append('b1')
                        down_white = np.hstack((T, F, R, L, B, D))
                        rotation('b1')
                        solutions.append('b1')
                        down_white = np.hstack((T, F, R, L, B, D))
                else:
                    rotation('b1')
                    solutions.append('b1')
                    down_white = np.hstack((T, F, R, L, B, D))
                    rotation('b1')
                    solutions.append('b1')
                    down_white = np.hstack((T, F, R, L, B, D))
            else:
                rotation('b1')
                solutions.append('b1')
                down_white = np.hstack((T, F, R, L, B, D))
                rotation('b1')
                solutions.append('b1')
                down_white = np.hstack((T, F, R, L, B, D))
        else:
            pass
        down_white = np.hstack((T, F, R, L, B, D))

# making white cross

cross_white = np.hstack((T, F, R, L, B, D))

# Front
while (F[0][1] != 2 or T[2][1] != 6):
    rotation('u')
    solutions.append('u')
    cross_white = np.hstack((T, F, R, L, B, D))
rotation('f')
solutions.append('f')
cross_white = np.hstack((T, F, R, L, B, D))
rotation('f')
solutions.append('f')
cross_white = np.hstack((T, F, R, L, B, D))

# Right
while (R[0][1] != 3 or T[1][2] != 6):
    rotation('u')
    solutions.append('u')
    cross_white = np.hstack((T, F, R, L, B, D))
rotation('r')
solutions.append('r')
cross_white = np.hstack((T, F, R, L, B, D))
rotation('r')
solutions.append('r')
cross_white = np.hstack((T, F, R, L, B, D))

# Left
while (L[0][1] != 4 or T[1][0] != 6):
    rotation('u')
    solutions.append('u')
    cross_white = np.hstack((T, F, R, L, B, D))
rotation('l')
solutions.append('l')
cross_white = np.hstack((T, F, R, L, B, D))
rotation('l')
solutions.append('l')
cross_white = np.hstack((T, F, R, L, B, D))

# Back
while (B[2][1] != 5 or T[0][1] != 6):
    rotation('u')
    solutions.append('u')
    cross_white = np.hstack((T, F, R, L, B, D))
rotation('b1')
solutions.append('b1')
cross_white = np.hstack((T, F, R, L, B, D))
rotation('b1')
solutions.append('b1')
cross_white = np.hstack((T, F, R, L, B, D))


print(Fore.GREEN + '> Making White cross-----------------------Completed')
#
# #-------------------------First Layer---------------------------------
#
def first_layer():
    global T, F, R, L, B, D
    while (F[0][0] == 6 or F[0][2] == 6 or L[0][0] == 6 or L[0][2] == 6 or B[2][0] == 6 or B[2][2] == 6 or R[0][
        0] == 6 or R[0][2] == 6):
        if (F[0][0] == 6 or L[0][0] == 6 or B[2][2] == 6 or R[0][0] == 6):
            if L[0][0] == 6:
                rotation('u1')
                solutions.append('u1')
                if (F[0][0] == 6 and T[2][0] == 2 and L[0][2] == 4):
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (L[0][0] == 6 and T[0][0] == 4 and B[2][0] == 5):
                        rotation('u1')
                        rotation('b1')
                        rotation('u')
                        rotation('b')
                        solutions.append('u1')
                        solutions.append('b1')
                        solutions.append('u')
                        solutions.append('b')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][2] == 6 and T[0][2] == 5 and R[0][2] == 3):
                            rotation('u1')
                            rotation('r1')
                            rotation('u')
                            rotation('r')
                            solutions.append('u1')
                            solutions.append('r1')
                            solutions.append('u')
                            solutions.append('r')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][0] == 6 and T[2][2] == 3 and F[0][2] == 2):
                                rotation('u1')
                                rotation('f1')
                                rotation('u')
                                rotation('f')
                                solutions.append('u1')
                                solutions.append('f1')
                                solutions.append('u')
                                solutions.append('f')
                            else:
                                rotation('u')
                                solutions.append('u')
            elif B[2][2] == 6:
                rotation('u')
                rotation('u')
                solutions.append('u')
                solutions.append('u')
                if (F[0][0] == 6 and T[2][0] == 2 and L[0][2] == 4):
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (L[0][0] == 6 and T[0][0] == 4 and B[2][0] == 5):
                        rotation('u1')
                        rotation('b1')
                        rotation('u')
                        rotation('b')
                        solutions.append('u1')
                        solutions.append('b1')
                        solutions.append('u')
                        solutions.append('b')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][2] == 6 and T[0][2] == 5 and R[0][2] == 3):
                            rotation('u1')
                            rotation('r1')
                            rotation('u')
                            rotation('r')
                            solutions.append('u1')
                            solutions.append('r1')
                            solutions.append('u')
                            solutions.append('r')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][0] == 6 and T[2][2] == 3 and F[0][2] == 2):
                                rotation('u1')
                                rotation('f1')
                                rotation('u')
                                rotation('f')
                                solutions.append('u1')
                                solutions.append('f1')
                                solutions.append('u')
                                solutions.append('f')
                            else:
                                rotation('u')
                                solutions.append('u')
            elif R[0][0] == 6:
                rotation('u')
                solutions.append('u')
                if (F[0][0] == 6 and T[2][0] == 2 and L[0][2] == 4):
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (L[0][0] == 6 and T[0][0] == 4 and B[2][0] == 5):
                        rotation('u1')
                        rotation('b1')
                        rotation('u')
                        rotation('b')
                        solutions.append('u1')
                        solutions.append('b1')
                        solutions.append('u')
                        solutions.append('b')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][2] == 6 and T[0][2] == 5 and R[0][2] == 3):
                            rotation('u1')
                            rotation('r1')
                            rotation('u')
                            rotation('r')
                            solutions.append('u1')
                            solutions.append('r1')
                            solutions.append('u')
                            solutions.append('r')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][0] == 6 and T[2][2] == 3 and F[0][2] == 2):
                                rotation('u1')
                                rotation('f1')
                                rotation('u')
                                rotation('f')
                                solutions.append('u1')
                                solutions.append('f1')
                                solutions.append('u')
                                solutions.append('f')
                            else:
                                rotation('u')
                                solutions.append('u')
            elif F[0][0] == 6:
                if (F[0][0] == 6 and T[2][0] == 2 and L[0][2] == 4):
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (L[0][0] == 6 and T[0][0] == 4 and B[2][0] == 5):
                        rotation('u1')
                        rotation('b1')
                        rotation('u')
                        rotation('b')
                        solutions.append('u1')
                        solutions.append('b1')
                        solutions.append('u')
                        solutions.append('b')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][2] == 6 and T[0][2] == 5 and R[0][2] == 3):
                            rotation('u1')
                            rotation('r1')
                            rotation('u')
                            rotation('r')
                            solutions.append('u1')
                            solutions.append('r1')
                            solutions.append('u')
                            solutions.append('r')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][0] == 6 and T[2][2] == 3 and F[0][2] == 2):
                                rotation('u1')
                                rotation('f1')
                                rotation('u')
                                rotation('f')
                                solutions.append('u1')
                                solutions.append('f1')
                                solutions.append('u')
                                solutions.append('f')
                            else:
                                rotation('u')
                                solutions.append('u')

        else:
            if L[0][2] == 6:
                rotation('u1')
                solutions.append('u1')
                if (F[0][2] == 6 and T[2][2] == 2 and R[0][0] == 3):
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (L[0][2] == 6 and T[2][0] == 4 and F[0][0] == 2):
                        rotation('u')
                        rotation('f')
                        rotation('u1')
                        rotation('f1')
                        solutions.append('u')
                        solutions.append('f')
                        solutions.append('u1')
                        solutions.append('f1')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][0] == 6 and T[0][0] == 5 and L[0][0] == 4):
                            rotation('u')
                            rotation('l')
                            rotation('u1')
                            rotation('l1')
                            solutions.append('u')
                            solutions.append('l')
                            solutions.append('u1')
                            solutions.append('l1')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][2] == 6 and T[0][2] == 3 and B[2][2] == 5):
                                rotation('u')
                                rotation('b')
                                rotation('u1')
                                rotation('b1')
                                solutions.append('u')
                                solutions.append('b')
                                solutions.append('u1')
                                solutions.append('b1')
                            else:
                                rotation('u')
                                solutions.append('u')
            elif B[2][0] == 6:
                rotation('u1')
                rotation('u1')
                solutions.append('u1')
                solutions.append('u1')
                if (F[0][2] == 6 and T[2][2] == 2 and R[0][0] == 3):
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (L[0][2] == 6 and T[2][0] == 4 and F[0][0] == 2):
                        rotation('u')
                        rotation('f')
                        rotation('u1')
                        rotation('f1')
                        solutions.append('u')
                        solutions.append('f')
                        solutions.append('u1')
                        solutions.append('f1')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][0] == 6 and T[0][0] == 5 and L[0][0] == 4):
                            rotation('u')
                            rotation('l')
                            rotation('u1')
                            rotation('l1')
                            solutions.append('u')
                            solutions.append('l')
                            solutions.append('u1')
                            solutions.append('l1')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][2] == 6 and T[0][2] == 3 and B[2][2] == 5):
                                rotation('u')
                                rotation('b')
                                rotation('u1')
                                rotation('b1')
                                solutions.append('u')
                                solutions.append('b')
                                solutions.append('u1')
                                solutions.append('b1')
                            else:
                                rotation('u')
                                solutions.append('u')
            elif R[0][2] == 6:
                rotation('u')
                solutions.append('u')
                if (F[0][2] == 6 and T[2][2] == 2 and R[0][0] == 3):
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (L[0][2] == 6 and T[2][0] == 4 and F[0][0] == 2):
                        rotation('u')
                        rotation('f')
                        rotation('u1')
                        rotation('f1')
                        solutions.append('u')
                        solutions.append('f')
                        solutions.append('u1')
                        solutions.append('f1')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][0] == 6 and T[0][0] == 5 and L[0][0] == 4):
                            rotation('u')
                            rotation('l')
                            rotation('u1')
                            rotation('l1')
                            solutions.append('u')
                            solutions.append('l')
                            solutions.append('u1')
                            solutions.append('l1')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][2] == 6 and T[0][2] == 3 and B[2][2] == 5):
                                rotation('u')
                                rotation('b')
                                rotation('u1')
                                rotation('b1')
                                solutions.append('u')
                                solutions.append('b')
                                solutions.append('u1')
                                solutions.append('b1')
                            else:
                                rotation('u')
                                solutions.append('u')
            elif F[0][2] == 6:
                if (F[0][2] == 6 and T[2][2] == 2 and R[0][0] == 3):
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (L[0][2] == 6 and T[2][0] == 4 and F[0][0] == 2):
                        rotation('u')
                        rotation('f')
                        rotation('u1')
                        rotation('f1')
                        solutions.append('u')
                        solutions.append('f')
                        solutions.append('u1')
                        solutions.append('f1')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][0] == 6 and T[0][0] == 5 and L[0][0] == 4):
                            rotation('u')
                            rotation('l')
                            rotation('u1')
                            rotation('l1')
                            solutions.append('u')
                            solutions.append('l')
                            solutions.append('u1')
                            solutions.append('l1')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][2] == 6 and T[0][2] == 3 and B[2][2] == 5):
                                rotation('u')
                                rotation('b')
                                rotation('u1')
                                rotation('b1')
                                solutions.append('u')
                                solutions.append('b')
                                solutions.append('u1')
                                solutions.append('b1')
                            else:
                                rotation('u')
                                solutions.append('u')


# #Top
while ((D[0][0] != 6) or (D[0][1] != 6) or (D[0][2] != 6) or (D[1][0] != 6) or (D[1][1] != 6) or (D[1][2] != 6) or (
        D[2][0] != 6) or (D[2][1] != 6) or (D[2][2] != 6) or (F[2][0] != 2) or (F[2][1] != 2) or (F[2][2] != 2) or (
               R[2][0] != 3) or (R[2][1] != 3) or (R[2][2] != 3) or (L[2][0] != 4) or (L[2][1] != 4) or (
               L[2][2] != 4) or (B[0][0] != 5) or (B[0][1] != 5) or (B[0][2] != 5)):
    while (F[0][0] == 6 or F[0][2] == 6 or L[0][0] == 6 or L[0][2] == 6 or B[2][0] == 6 or B[2][2] == 6 or R[0][
        0] == 6 or R[0][2] == 6):
        if (F[0][0] == 6 or L[0][0] == 6 or B[2][2] == 6 or R[0][0] == 6):
            if L[0][0] == 6:
                rotation('u1')
                solutions.append('u1')
                if (F[0][0] == 6 and T[2][0] == 2 and L[0][2] == 4):
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (L[0][0] == 6 and T[0][0] == 4 and B[2][0] == 5):
                        rotation('u1')
                        rotation('b1')
                        rotation('u')
                        rotation('b')
                        solutions.append('u1')
                        solutions.append('b1')
                        solutions.append('u')
                        solutions.append('b')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][2] == 6 and T[0][2] == 5 and R[0][2] == 3):
                            rotation('u1')
                            rotation('r1')
                            rotation('u')
                            rotation('r')
                            solutions.append('u1')
                            solutions.append('r1')
                            solutions.append('u')
                            solutions.append('r')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][0] == 6 and T[2][2] == 3 and F[0][2] == 2):
                                rotation('u1')
                                rotation('f1')
                                rotation('u')
                                rotation('f')
                                solutions.append('u1')
                                solutions.append('f1')
                                solutions.append('u')
                                solutions.append('f')
                            else:
                                rotation('u')
                                solutions.append('u')
            elif B[2][2] == 6:
                rotation('u')
                rotation('u')
                solutions.append('u')
                solutions.append('u')
                if (F[0][0] == 6 and T[2][0] == 2 and L[0][2] == 4):
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (R[0][0] == 6 and T[0][0] == 4 and B[2][0] == 5):
                        rotation('u1')
                        rotation('b1')
                        rotation('u')
                        rotation('b')
                        solutions.append('u1')
                        solutions.append('b1')
                        solutions.append('u')
                        solutions.append('b')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][2] == 6 and T[0][2] == 5 and R[0][2] == 3):
                            rotation('u1')
                            rotation('r1')
                            rotation('u')
                            rotation('r')
                            solutions.append('u1')
                            solutions.append('r1')
                            solutions.append('u')
                            solutions.append('r')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][0] == 6 and T[2][2] == 3 and F[0][2] == 2):
                                rotation('u1')
                                rotation('f1')
                                rotation('u')
                                rotation('f')
                                solutions.append('u1')
                                solutions.append('f1')
                                solutions.append('u')
                                solutions.append('f')
                            else:
                                rotation('u')
                                solutions.append('u')
            elif R[0][0] == 6:
                rotation('u')
                solutions.append('u')
                if (F[0][0] == 6 and T[2][0] == 2 and L[0][2] == 4):
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (R[0][0] == 6 and T[0][0] == 4 and B[2][0] == 5):
                        rotation('u1')
                        rotation('b1')
                        rotation('u')
                        rotation('b')
                        solutions.append('u1')
                        solutions.append('b1')
                        solutions.append('u')
                        solutions.append('b')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][2] == 6 and T[0][2] == 5 and R[0][2] == 3):
                            rotation('u1')
                            rotation('r1')
                            rotation('u')
                            rotation('r')
                            solutions.append('u1')
                            solutions.append('r1')
                            solutions.append('u')
                            solutions.append('r')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][0] == 6 and T[2][2] == 3 and F[0][2] == 2):
                                rotation('u1')
                                rotation('f1')
                                rotation('u')
                                rotation('f')
                                solutions.append('u1')
                                solutions.append('f1')
                                solutions.append('u')
                                solutions.append('f')
                            else:
                                rotation('u')
                                solutions.append('u')
            elif F[0][0] == 6:
                if (F[0][0] == 6 and T[2][0] == 2 and L[0][2] == 4):
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (L[0][0] == 6 and T[0][0] == 4 and B[2][0] == 5):
                        rotation('u1')
                        rotation('b1')
                        rotation('u')
                        rotation('b')
                        solutions.append('u1')
                        solutions.append('b1')
                        solutions.append('u')
                        solutions.append('b')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][2] == 6 and T[0][2] == 5 and R[0][2] == 3):
                            rotation('u1')
                            rotation('r1')
                            rotation('u')
                            rotation('r')
                            solutions.append('u1')
                            solutions.append('r1')
                            solutions.append('u')
                            solutions.append('r')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][0] == 6 and T[2][2] == 3 and F[0][2] == 2):
                                rotation('u1')
                                rotation('f1')
                                rotation('u')
                                rotation('f')
                                solutions.append('u1')
                                solutions.append('f1')
                                solutions.append('u')
                                solutions.append('f')
                            else:
                                rotation('u')
                                solutions.append('u')
        else:
            if L[0][2] == 6:
                rotation('u1')
                solutions.append('u1')
                if (F[0][2] == 6 and T[2][2] == 2 and R[0][0] == 3):
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (L[0][2] == 6 and T[2][0] == 4 and F[0][0] == 2):
                        rotation('u')
                        rotation('f')
                        rotation('u1')
                        rotation('f1')
                        solutions.append('u')
                        solutions.append('f')
                        solutions.append('u1')
                        solutions.append('f1')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][0] == 6 and T[0][0] == 5 and L[0][0] == 4):
                            rotation('u')
                            rotation('l')
                            rotation('u1')
                            rotation('l1')
                            solutions.append('u')
                            solutions.append('l')
                            solutions.append('u1')
                            solutions.append('l1')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][2] == 6 and T[0][2] == 3 and B[2][2] == 5):
                                rotation('u')
                                rotation('b')
                                rotation('u1')
                                rotation('b1')
                                solutions.append('u')
                                solutions.append('b')
                                solutions.append('u1')
                                solutions.append('b1')
                            else:
                                rotation('u')
                                solutions.append('u')
            elif B[2][0] == 6:
                rotation('u1')
                rotation('u1')
                solutions.append('u1')
                solutions.append('u1')
                if (F[0][2] == 6 and T[2][2] == 2 and R[0][0] == 3):
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (L[0][2] == 6 and T[2][0] == 4 and F[0][0] == 2):
                        rotation('u')
                        rotation('f')
                        rotation('u1')
                        rotation('f1')
                        solutions.append('u')
                        solutions.append('f')
                        solutions.append('u1')
                        solutions.append('f1')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][0] == 6 and T[0][0] == 5 and L[0][0] == 4):
                            rotation('u')
                            rotation('l')
                            rotation('u1')
                            rotation('l1')
                            solutions.append('u')
                            solutions.append('l')
                            solutions.append('u1')
                            solutions.append('l1')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][2] == 6 and T[0][2] == 3 and B[2][2] == 5):
                                rotation('u')
                                rotation('b')
                                rotation('u1')
                                rotation('b1')
                                solutions.append('u')
                                solutions.append('b')
                                solutions.append('u1')
                                solutions.append('b1')
                            else:
                                rotation('u')
                                solutions.append('u')
            elif R[0][2] == 6:
                rotation('u')
                solutions.append('u')
                if (F[0][2] == 6 and T[2][2] == 2 and R[0][0] == 3):
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (L[0][2] == 6 and T[2][0] == 4 and F[0][0] == 2):
                        rotation('u')
                        rotation('f')
                        rotation('u1')
                        rotation('f1')
                        solutions.append('u')
                        solutions.append('f')
                        solutions.append('u1')
                        solutions.append('f1')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][0] == 6 and T[0][0] == 5 and L[0][0] == 4):
                            rotation('u')
                            rotation('l')
                            rotation('u1')
                            rotation('l1')
                            solutions.append('u')
                            solutions.append('l')
                            solutions.append('u1')
                            solutions.append('l1')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][2] == 6 and T[0][2] == 3 and B[2][2] == 5):
                                rotation('u')
                                rotation('b')
                                rotation('u1')
                                rotation('b1')
                                solutions.append('u')
                                solutions.append('b')
                                solutions.append('u1')
                                solutions.append('b1')
                            else:
                                rotation('u')
                                solutions.append('u')
            elif F[0][2] == 6:
                if (F[0][2] == 6 and T[2][2] == 2 and R[0][0] == 3):
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    solutions.append('u')
                    if (L[0][2] == 6 and T[2][0] == 4 and F[0][0] == 2):
                        rotation('u')
                        rotation('f')
                        rotation('u1')
                        rotation('f1')
                        solutions.append('u')
                        solutions.append('f')
                        solutions.append('u1')
                        solutions.append('f1')
                    else:
                        rotation('u')
                        solutions.append('u')
                        if (B[2][0] == 6 and T[0][0] == 5 and L[0][0] == 4):
                            rotation('u')
                            rotation('l')
                            rotation('u1')
                            rotation('l1')
                            solutions.append('u')
                            solutions.append('l')
                            solutions.append('u1')
                            solutions.append('l1')
                        else:
                            rotation('u')
                            solutions.append('u')
                            if (R[0][2] == 6 and T[0][2] == 3 and B[2][2] == 5):
                                rotation('u')
                                rotation('b')
                                rotation('u1')
                                rotation('b1')
                                solutions.append('u')
                                solutions.append('b')
                                solutions.append('u1')
                                solutions.append('b1')
                            else:
                                rotation('u')
                                solutions.append('u')

        # Top
    if T[0][0] == 6:
        if (D[2][0] == 6 and L[2][0] == 4 and B[0][0] == 5):
            rotation('u')
            solutions.append('u')
            if (D[2][2] == 6 and R[2][2] == 3 and B[0][2] == 5):
                rotation('u')
                solutions.append('u')
                if (D[0][2] == 6 and F[2][2] == 2 and R[2][0] == 3):
                    rotation('u')
                    solutions.append('u')
                    if (D[0][0] == 6 and F[2][0] == 2 and L[2][2] == 4):
                        rotation('u')
                        solutions.append('u')
                    else:
                        rotation('f')
                        solutions.append('f')
                        rotation('u1')
                        solutions.append('u1')
                        rotation('f1')
                        solutions.append('f1')
                        first_layer()
                else:
                    rotation('r')
                    solutions.append('r')
                    rotation('u1')
                    solutions.append('u1')
                    rotation('r1')
                    solutions.append('r1')
                    first_layer()
            else:
                rotation('r1')
                solutions.append('r1')
                rotation('u')
                solutions.append('u')
                rotation('r')
                solutions.append('r')
                first_layer()
        else:
            rotation('b1')
            solutions.append('b1')
            rotation('u')
            solutions.append('u')
            rotation('b')
            solutions.append('b')
            first_layer()
    else:
        pass

    if T[0][2] == 6:
        if (D[2][2] == 6 and R[2][2] == 3 and B[0][2] == 5):
            rotation('u')
            solutions.append('u')
            if (D[0][2] == 6 and R[2][0] == 3 and F[2][2] == 2):
                rotation('u')
                solutions.append('u')
                if (D[0][0] == 6 and F[2][0] == 2 and L[2][2] == 4):
                    rotation('u')
                    solutions.append('u')
                    if (D[2][0] == 6 and B[0][0] == 5 and L[2][0] == 4):
                        rotation('u')
                        solutions.append('u')
                    else:
                        rotation('b1')
                        solutions.append('b1')
                        rotation('u')
                        solutions.append('u')
                        rotation('b')
                        solutions.append('b')
                        first_layer()
                else:
                    rotation('f')
                    solutions.append('f')
                    rotation('u1')
                    solutions.append('u1')
                    rotation('f1')
                    solutions.append('f1')
                    first_layer()
            else:
                rotation('r')
                solutions.append('r')
                rotation('u1')
                solutions.append('u1')
                rotation('r1')
                solutions.append('r1')
                first_layer()
        else:
            rotation('r1')
            solutions.append('r1')
            rotation('u')
            solutions.append('u')
            rotation('r')
            solutions.append('r')
            first_layer()
    else:
        pass

    if T[2][2] == 6:
        if (D[0][2] == 6 and F[2][2] == 2 and R[2][0] == 3):
            rotation('u')
            solutions.append('u')
            if (D[0][0] == 6 and F[2][0] == 2 and L[2][2] == 4):
                rotation('u')
                solutions.append('u')
                if (D[2][0] == 6 and B[0][0] == 5 and L[2][0] == 4):
                    rotation('u')
                    solutions.append('u')
                    if (D[2][2] == 6 and R[2][2] == 3 and B[0][2] == 5):
                        rotation('u')
                        solutions.append('u')
                    else:
                        rotation('b')
                        solutions.append('b')
                        rotation('u1')
                        solutions.append('u1')
                        rotation('b1')
                        solutions.append('b1')
                        first_layer()
                else:
                    rotation('b1')
                    solutions.append('b1')
                    rotation('u')
                    solutions.append('u')
                    rotation('b')
                    solutions.append('b')
                    first_layer()
            else:
                rotation('f')
                solutions.append('f')
                rotation('u1')
                solutions.append('u1')
                rotation('f1')
                solutions.append('f1')
                first_layer()
        else:
            rotation('r')
            solutions.append('r')
            rotation('u1')
            solutions.append('u1')
            rotation('r1')
            solutions.append('r1')
            first_layer()
    else:
        pass

    if T[2][0] == 6:
        if (D[0][0] == 6 and F[2][0] == 2 and L[2][2] == 4):
            rotation('u')
            solutions.append('u')
            if (D[2][0] == 6 and L[2][0] == 4 and B[0][0] == 5):
                rotation('u')
                solutions.append('u')
                if (D[2][2] == 6 and B[0][2] == 5 and R[2][2] == 3):
                    rotation('u')
                    solutions.append('u')
                    if (D[0][2] == 6 and F[2][2] == 2 and R[2][0] == 3):
                        rotation('u')
                        solutions.append('u')
                    else:
                        rotation('r')
                        solutions.append('r')
                        rotation('u1')
                        solutions.append('u1')
                        rotation('r1')
                        solutions.append('r1')
                        first_layer()
                else:
                    rotation('r1')
                    solutions.append('r1')
                    rotation('u')
                    solutions.append('u')
                    rotation('r')
                    solutions.append('r')
                    first_layer()
            else:
                rotation('b1')
                solutions.append('b1')
                rotation('u')
                solutions.append('u')
                rotation('b')
                solutions.append('b')
                first_layer()
        else:
            rotation('f')
            solutions.append('f')
            rotation('u1')
            solutions.append('u1')
            rotation('f1')
            solutions.append('f1')
            first_layer()
    else:
        pass

    # Down

    if (D[0][0] == 6 and (F[2][0] != 2 or L[2][2] != 4)):
        rotation('l1')
        rotation('u1')
        rotation('l')
        solutions.append('l1')
        solutions.append('u1')
        solutions.append('l')
        first_layer()
    else:
        pass

    if (D[0][2] == 6 and (F[2][2] != 2 or R[2][0] != 3)):
        rotation('r')
        rotation('u')
        rotation('r1')
        solutions.append('r')
        solutions.append('u')
        solutions.append('r1')
        first_layer()
    else:
        pass

    if (D[2][0] == 6 and (L[2][0] != 4 or B[0][0] != 5)):
        rotation('l')
        rotation('u')
        rotation('l1')
        solutions.append('l')
        solutions.append('u')
        solutions.append('l1')
        first_layer()
    else:
        pass

    if (D[2][2] == 6 and (R[2][2] != 3 or B[0][2] != 5)):
        rotation('r1')
        rotation('u')
        rotation('r')
        solutions.append('r1')
        solutions.append('u')
        solutions.append('r')
        first_layer()
    else:
        pass

    if F[2][0] == 6:
        rotation('f')
        rotation('u')
        rotation('f1')
        rotation('u1')
        solutions.append('f')
        solutions.append('u')
        solutions.append('f1')
        solutions.append('u1')
        first_layer()
    elif F[2][2] == 6:
        rotation('f1')
        rotation('u1')
        rotation('f')
        rotation('u')
        solutions.append('f1')
        solutions.append('u1')
        solutions.append('f')
        solutions.append('u')
        first_layer()
    elif R[2][0] == 6:
        rotation('r')
        rotation('u')
        rotation('r1')
        solutions.append('r')
        solutions.append('u')
        solutions.append('r1')
        first_layer()
    elif R[2][2] == 6:
        rotation('r1')
        rotation('u1')
        rotation('r')
        solutions.append('r1')
        solutions.append('u1')
        solutions.append('r')
        first_layer()
    elif L[2][0] == 6:
        rotation('l')
        rotation('u')
        rotation('l1')
        solutions.append('l')
        solutions.append('u')
        solutions.append('l1')
        first_layer()
    elif L[2][2] == 6:
        rotation('l1')
        rotation('u1')
        rotation('l')
        solutions.append('l1')
        solutions.append('u1')
        solutions.append('l')
        first_layer()
    elif B[0][0] == 6:
        rotation('b1')
        rotation('u1')
        rotation('b')
        solutions.append('b1')
        solutions.append('u1')
        solutions.append('b')
        first_layer()
    elif B[0][2] == 6:
        rotation('b')
        rotation('u')
        rotation('b1')
        solutions.append('b')
        solutions.append('u')
        solutions.append('b1')
        first_layer()
    else:
        pass

print(Fore.GREEN + '> Assembling the First Layer-----------------Completed')
# --------------------------Second Layer-----------------------------------------------

def second_layer():
    global T, F, R, L, B, D
    while ((F[0][1] != 1 and T[2][1] != 1) or (R[0][1] != 1 and T[1][2] != 1) or (L[0][1] != 1 and T[1][0] != 1) or (
            B[2][1] != 1 and T[0][1] != 1)):
        # Front
        if (F[0][1] != 1 and T[2][1] != 1):
            if F[0][1] == 2:
                if T[2][1] == 3:
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                else:
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
            elif F[0][1] == 3:
                rotation('u1')
                solutions.append('u1')
                if T[1][2] == 2:
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
            elif F[0][1] == 4:
                rotation('u')
                solutions.append('u')
                if T[1][0] == 2:
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
            elif F[0][1] == 5:
                rotation('u')
                rotation('u')
                solutions.append('u')
                solutions.append('u')
                if T[0][1] == 3:
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                else:
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
            else:
                pass
        elif (R[0][1] != 1 and T[1][2] != 1):
            rotation('u')
            solutions.append('u')
            if F[0][1] == 2:
                if T[2][1] == 3:
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                else:
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
            elif F[0][1] == 3:
                rotation('u1')
                solutions.append('u1')
                if T[1][2] == 2:
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
            elif F[0][1] == 4:
                rotation('u')
                solutions.append('u')
                if T[1][0] == 2:
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
            elif F[0][1] == 5:
                rotation('u')
                rotation('u')
                solutions.append('u')
                solutions.append('u')
                if T[0][1] == 3:
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                else:
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
            else:
                pass
        elif (L[0][1] != 1 and T[1][0] != 1):
            rotation('u1')
            solutions.append('u1')
            if F[0][1] == 2:
                if T[2][1] == 3:
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                else:
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
            elif F[0][1] == 3:
                rotation('u1')
                solutions.append('u1')
                if T[1][2] == 2:
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
            elif F[0][1] == 4:
                rotation('u')
                solutions.append('u')
                if T[1][0] == 2:
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
            elif F[0][1] == 5:
                rotation('u')
                rotation('u')
                solutions.append('u')
                solutions.append('u')
                if T[0][1] == 3:
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                else:
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
            else:
                pass
        elif (B[2][1] != 1 and T[0][1] != 1):
            rotation('u')
            rotation('u')
            solutions.append('u')
            solutions.append('u')
            if F[0][1] == 2:
                if T[2][1] == 3:
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                else:
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
            elif F[0][1] == 3:
                rotation('u1')
                solutions.append('u1')
                if T[1][2] == 2:
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
            elif F[0][1] == 4:
                rotation('u')
                solutions.append('u')
                if T[1][0] == 2:
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
            elif F[0][1] == 5:
                rotation('u')
                rotation('u')
                solutions.append('u')
                solutions.append('u')
                if T[0][1] == 3:
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                else:
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
            else:
                pass
        else:
            pass


# Start second layer
while (F[1][0] != 2 or F[1][2] != 2 or R[1][0] != 3 or R[1][2] != 3 or L[1][0] != 4 or L[1][2] != 4 or B[1][0] != 5 or
       B[1][2] != 5):
    while ((F[0][1] != 1 and T[2][1] != 1) or (R[0][1] != 1 and T[1][2] != 1) or (L[0][1] != 1 and T[1][0] != 1) or (
            B[2][1] != 1 and T[0][1] != 1)):
        # Front
        if (F[0][1] != 1 and T[2][1] != 1):
            if F[0][1] == 2:
                if T[2][1] == 3:
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                else:
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
            elif F[0][1] == 3:
                rotation('u1')
                solutions.append('u1')
                if T[1][2] == 2:
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
            elif F[0][1] == 4:
                rotation('u')
                solutions.append('u')
                if T[1][0] == 2:
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
            elif F[0][1] == 5:
                rotation('u')
                rotation('u')
                solutions.append('u')
                solutions.append('u')
                if T[0][1] == 3:
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                else:
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
            else:
                pass
        elif (R[0][1] != 1 and T[1][2] != 1):
            rotation('u')
            solutions.append('u')
            if F[0][1] == 2:
                if T[2][1] == 3:
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                else:
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
            elif F[0][1] == 3:
                rotation('u1')
                solutions.append('u1')
                if T[1][2] == 2:
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
            elif F[0][1] == 4:
                rotation('u')
                solutions.append('u')
                if T[1][0] == 2:
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
            elif F[0][1] == 5:
                rotation('u')
                rotation('u')
                solutions.append('u')
                solutions.append('u')
                if T[0][1] == 3:
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                else:
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
            else:
                pass
        elif (L[0][1] != 1 and T[1][0] != 1):
            rotation('u1')
            solutions.append('u1')
            if F[0][1] == 2:
                if T[2][1] == 3:
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                else:
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
            elif F[0][1] == 3:
                rotation('u1')
                solutions.append('u1')
                if T[1][2] == 2:
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
            elif F[0][1] == 4:
                rotation('u')
                solutions.append('u')
                if T[1][0] == 2:
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
            elif F[0][1] == 5:
                rotation('u')
                rotation('u')
                solutions.append('u')
                solutions.append('u')
                if T[0][1] == 3:
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                else:
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
            else:
                pass
        elif (B[2][1] != 1 and T[0][1] != 1):
            rotation('u')
            rotation('u')
            solutions.append('u')
            solutions.append('u')
            if F[0][1] == 2:
                if T[2][1] == 3:
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                else:
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
            elif F[0][1] == 3:
                rotation('u1')
                solutions.append('u1')
                if T[1][2] == 2:
                    rotation('u1')
                    rotation('f1')
                    rotation('u')
                    rotation('f')
                    rotation('u')
                    rotation('r')
                    rotation('u1')
                    rotation('r1')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u1')
                    solutions.append('r1')
                else:
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
            elif F[0][1] == 4:
                rotation('u')
                solutions.append('u')
                if T[1][0] == 2:
                    rotation('u')
                    rotation('f')
                    rotation('u1')
                    rotation('f1')
                    rotation('u1')
                    rotation('l1')
                    rotation('u')
                    rotation('l')
                    solutions.append('u')
                    solutions.append('f')
                    solutions.append('u1')
                    solutions.append('f1')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u')
                    solutions.append('l')
                else:
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
            elif F[0][1] == 5:
                rotation('u')
                rotation('u')
                solutions.append('u')
                solutions.append('u')
                if T[0][1] == 3:
                    rotation('u1')
                    rotation('r1')
                    rotation('u')
                    rotation('r')
                    rotation('u')
                    rotation('b')
                    rotation('u1')
                    rotation('b1')
                    solutions.append('u1')
                    solutions.append('r1')
                    solutions.append('u')
                    solutions.append('r')
                    solutions.append('u')
                    solutions.append('b')
                    solutions.append('u1')
                    solutions.append('b1')
                else:
                    rotation('u')
                    rotation('l')
                    rotation('u1')
                    rotation('l1')
                    rotation('u1')
                    rotation('b1')
                    rotation('u')
                    rotation('b')
                    solutions.append('u')
                    solutions.append('l')
                    solutions.append('u1')
                    solutions.append('l1')
                    solutions.append('u1')
                    solutions.append('b1')
                    solutions.append('u')
                    solutions.append('b')
            else:
                pass
        else:
            pass

    if (F[1][0] != 1 and L[1][2] != 1 and F[1][0] != 2 and L[1][2] != 4):
        rotation('f')
        rotation('u')
        rotation('f1')
        rotation('u1')
        rotation('u1')
        rotation('f')
        rotation('u1')
        rotation('f1')
        rotation('u')
        rotation('u')
        rotation('f')
        rotation('u1')
        rotation('f1')
        solutions.append('f')
        solutions.append('u')
        solutions.append('f1')
        solutions.append('u1')
        solutions.append('u1')
        solutions.append('f')
        solutions.append('u1')
        solutions.append('f1')
        solutions.append('u')
        solutions.append('u')
        solutions.append('f')
        solutions.append('u1')
        solutions.append('f1')
        second_layer()
    elif (F[1][2] != 1 and R[1][0] != 1 and F[1][2] != 2 and R[1][0] != 3):
        rotation('r')
        rotation('u')
        rotation('r1')
        rotation('u1')
        rotation('u1')
        rotation('r')
        rotation('u1')
        rotation('r1')
        rotation('u')
        rotation('u')
        rotation('r')
        rotation('u1')
        rotation('r1')
        solutions.append('r')
        solutions.append('u')
        solutions.append('r1')
        solutions.append('u1')
        solutions.append('u1')
        solutions.append('r')
        solutions.append('u1')
        solutions.append('r1')
        solutions.append('u')
        solutions.append('u')
        solutions.append('r')
        solutions.append('u1')
        solutions.append('r1')
        second_layer()
    elif (B[1][0] != 1 and L[1][0] != 1 and B[1][0] != 5 and L[1][0] != 4):
        rotation('l')
        rotation('u')
        rotation('l1')
        rotation('u1')
        rotation('u1')
        rotation('l')
        rotation('u1')
        rotation('l1')
        rotation('u')
        rotation('u')
        rotation('l')
        rotation('u1')
        rotation('l1')
        solutions.append('l')
        solutions.append('u')
        solutions.append('l1')
        solutions.append('u1')
        solutions.append('u1')
        solutions.append('l')
        solutions.append('u1')
        solutions.append('l1')
        solutions.append('u')
        solutions.append('u')
        solutions.append('l')
        solutions.append('u1')
        solutions.append('l1')
        second_layer()
    elif (B[1][2] != 1 and R[1][2] != 1 and B[1][2] != 5 and R[1][2] != 3):
        rotation('b')
        rotation('u')
        rotation('b1')
        rotation('u1')
        rotation('u1')
        rotation('b')
        rotation('u1')
        rotation('b1')
        rotation('u')
        rotation('u')
        rotation('b')
        rotation('u1')
        rotation('b1')
        solutions.append('b')
        solutions.append('u')
        solutions.append('b1')
        solutions.append('u1')
        solutions.append('u1')
        solutions.append('b')
        solutions.append('u1')
        solutions.append('b1')
        solutions.append('u')
        solutions.append('u')
        solutions.append('b')
        solutions.append('u1')
        solutions.append('b1')
        second_layer()
    else:
        pass

print(Fore.GREEN + '> Assembling the Second layer-----------------Completed')
#-------------------------------------TOP CROSS--------------------------

def L_cross():
    global T, F, R, L, B, D
    if (T[0][1] == 1 and T[1][1] == 1 and T[1][0] == 1):
        rotation('f')
        rotation('r')
        rotation('u')
        rotation('r1')
        rotation('u1')
        rotation('r')
        rotation('u')
        rotation('r1')
        rotation('u1')
        rotation('f1')
        solutions.append('f')
        solutions.append('r')
        solutions.append('u')
        solutions.append('r1')
        solutions.append('u1')
        solutions.append('r')
        solutions.append('u')
        solutions.append('r1')
        solutions.append('u1')
        solutions.append('f1')
    else:
        pass

while (T[0][1] != 1 or T[1][0] != 1 or T[1][1] != 1 or T[1][2] != 1 or T[2][1] != 1):
    if (T[0][1] == 1 and T[1][1] == 1 and T[1][0] == 1):
        L_cross()
    elif (T[0][1] == 1 and T[1][1] == 1 and T[1][2] == 1):
        rotation('u1')
        solutions.append('u1')
        L_cross()
    elif (T[1][2] == 1 and T[1][1] == 1 and T[2][1] == 1):
        rotation('u')
        rotation('u')
        solutions.append('u')
        solutions.append('u')
        L_cross()
    elif (T[1][0] == 1 and T[1][1] == 1 and T[2][1] == 1):
        rotation('u')
        solutions.append('u')
        L_cross()
    elif (T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1):
        rotation('f')
        rotation('r')
        rotation('u')
        rotation('r1')
        rotation('u1')
        rotation('f1')
        solutions.append('f')
        solutions.append('r')
        solutions.append('u')
        solutions.append('r1')
        solutions.append('u1')
        solutions.append('f1')
    elif (T[0][1] == 1 and T[1][1] == 1 and T[2][1] == 1):
        rotation('u')
        rotation('f')
        rotation('r')
        rotation('u')
        rotation('r1')
        rotation('u1')
        rotation('f1')
        solutions.append('u')
        solutions.append('f')
        solutions.append('r')
        solutions.append('u')
        solutions.append('r1')
        solutions.append('u1')
        solutions.append('f1')
    elif T[1][1] == 1:
        L_cross()
        if (T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1):
            rotation('f')
            rotation('r')
            rotation('u')
            rotation('r1')
            rotation('u1')
            rotation('f1')
            solutions.append('f')
            solutions.append('r')
            solutions.append('u')
            solutions.append('r1')
            solutions.append('u1')
            solutions.append('f1')
        else:
            rotation('u')
            rotation('f')
            rotation('r')
            rotation('u')
            rotation('r1')
            rotation('u1')
            rotation('f1')
            solutions.append('u')
            solutions.append('f')
            solutions.append('r')
            solutions.append('u')
            solutions.append('r1')
            solutions.append('u1')
            solutions.append('f1')
    else:
        pass

print(Fore.GREEN + '> Forming the Top Cross-----------------------Completed')

#------------------------------orienting Last Layer(OLL)---------------------
def algo_oll():
    global T, F, R, L, B, D
    if (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][0] == 1 and T[2][1] == 1 and F[0][2] == 1 and T[0][2] != 1):
        rotation('r')
        rotation('u')
        rotation('r1')
        rotation('u')
        rotation('r')
        rotation('u')
        rotation('u')
        rotation('r1')
        solutions.append('r')
        solutions.append('u')
        solutions.append('r1')
        solutions.append('u')
        solutions.append('r')
        solutions.append('u')
        solutions.append('u')
        solutions.append('r1')
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[0][2] == 1 and T[2][1] == 1 and F[0][0] == 1 and T[2][2] != 1):
        rotation('r')
        rotation('u')
        rotation('u')
        rotation('r1')
        rotation('u1')
        rotation('r')
        rotation('u1')
        rotation('r1')
        solutions.append('r')
        solutions.append('u')
        solutions.append('u')
        solutions.append('r1')
        solutions.append('u1')
        solutions.append('r')
        solutions.append('u1')
        solutions.append('r1')
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and F[0][0] == 1 and F[0][2] == 1 and B[2][0] == 1 and B[2][2] == 1):
        rotation('r')
        rotation('u')
        rotation('u')
        rotation('r1')
        rotation('u1')
        rotation('r')
        rotation('u')
        rotation('r1')
        rotation('u1')
        rotation('r')
        rotation('u1')
        rotation('r1')
        solutions.append('r')
        solutions.append('u')
        solutions.append('u')
        solutions.append('r1')
        solutions.append('u1')
        solutions.append('r')
        solutions.append('u')
        solutions.append('r1')
        solutions.append('u1')
        solutions.append('r')
        solutions.append('u1')
        solutions.append('r1')
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and L[0][0] == 1 and L[0][2] == 1 and F[0][2] == 1):
        rotation('r')
        rotation('u')
        rotation('u')
        rotation('r')
        rotation('r')
        rotation('u1')
        rotation('r')
        rotation('r')
        rotation('u1')
        rotation('r')
        rotation('r')
        rotation('u')
        rotation('u')
        rotation('r')
        solutions.append('r')
        solutions.append('u')
        solutions.append('u')
        solutions.append('r')
        solutions.append('r')
        solutions.append('u1')
        solutions.append('r')
        solutions.append('r')
        solutions.append('u1')
        solutions.append('r')
        solutions.append('r')
        solutions.append('u')
        solutions.append('u')
        solutions.append('r')
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[0][0] == 1 and T[0][2] == 1 and F[0][0] == 1 and F[0][2] == 1):
        rotation('r')
        rotation('r')
        rotation('d')
        rotation('r1')
        rotation('u')
        rotation('u')
        rotation('r')
        rotation('d1')
        rotation('r1')
        rotation('u')
        rotation('u')
        rotation('r1')
        solutions.append('r')
        solutions.append('r')
        solutions.append('d')
        solutions.append('r1')
        solutions.append('u')
        solutions.append('u')
        solutions.append('r')
        solutions.append('d1')
        solutions.append('r1')
        solutions.append('u')
        solutions.append('u')
        solutions.append('r1')
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and F[0][0] == 1 and B[2][0] == 1 and T[0][2] == 1 and T[2][2] == 1):
        rotation('r')
        rotation('m')
        rotation('u')
        rotation('r1')
        rotation('u1')
        rotation('r1')
        rotation('m')
        rotation('m')
        rotation('m')
        rotation('f')
        rotation('r')
        rotation('f1')
        solutions.append('r')
        solutions.append('m')
        solutions.append('u')
        solutions.append('r1')
        solutions.append('u1')
        solutions.append('r1')
        solutions.append('m')
        solutions.append('m')
        solutions.append('m')
        solutions.append('f')
        solutions.append('r')
        solutions.append('f1')
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[0][2] == 1 and T[2][0] == 1):
        rotation('f1')
        rotation('r')
        rotation('m')
        rotation('u')
        rotation('r1')
        rotation('u1')
        rotation('r1')
        rotation('m')
        rotation('m')
        rotation('m')
        rotation('f')
        rotation('r')
        solutions.append('f1')
        solutions.append('r')
        solutions.append('m')
        solutions.append('u')
        solutions.append('r1')
        solutions.append('u1')
        solutions.append('r1')
        solutions.append('m')
        solutions.append('m')
        solutions.append('m')
        solutions.append('f')
        solutions.append('r')
    else:
        pass
#algo A
while (T[0][1] != 1 or T[1][0] != 1 or T[1][1] != 1 or T[1][2] != 1 or T[2][1] != 1 or T[0][2] != 1 or T[2][0] != 1 or T[0][0] != 1 or T[2][2] != 1):
    if (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][0] == 1 and T[2][1] == 1 and F[0][2] == 1):
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[2][2] == 1 and R[0][2] == 1):
        rotation('u')
        solutions.append('u')
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[0][2] == 1 and B[2][0] == 1):
        rotation('u')
        rotation('u')
        solutions.append('u')
        solutions.append('u')
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[0][0] == 1 and L[0][2] == 1 and T[0][2] != 1):
        rotation('u1')
        solutions.append('u1')
        algo_oll()

#algo B
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[0][2] == 1 and F[0][0] == 1):
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[0][0] == 1 and R[0][0] == 1):
        rotation('u')
        solutions.append('u')
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[2][0] == 1 and B[2][2] == 1):
        rotation('u')
        rotation('u')
        solutions.append('u')
        solutions.append('u')
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[2][2] == 1 and L[0][0] == 1):
        rotation('u1')
        solutions.append('u1')
        algo_oll()

#algo C
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and F[0][0] == 1 and F[0][2] == 1 and B[2][0] == 1 and B[2][2] == 1):
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and L[0][0] == 1 and L[0][2] == 1 and R[0][0] == 1 and R[0][2] == 1):
        rotation('u')
        solutions.append('u')
        algo_oll()

#algo D
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and L[0][0] == 1 and L[0][2] == 1 and F[0][2] == 1):
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and F[0][0] == 1 and F[0][2] == 1 and R[0][2] == 1):
        rotation('u')
        solutions.append('u')
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and R[0][0] == 1 and R[0][2] == 1 and B[2][0] == 1):
        rotation('u')
        rotation('u')
        solutions.append('u')
        solutions.append('u')
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and B[2][0] == 1 and B[2][2] == 1 and L[0][2] == 1):
        rotation('u1')
        solutions.append('u1')
        algo_oll()

#algo E
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[0][0] == 1 and T[0][2] == 1 and F[0][0] == 1 and F[0][2] == 1):
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[0][0] == 1 and T[2][0] == 1 and R[0][0] == 1 and R[0][2] == 1):
        rotation('u')
        solutions.append('u')
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[2][0] == 1 and T[2][2] == 1 and B[2][0] == 1 and B[2][2] == 1):
        rotation('u')
        rotation('u')
        solutions.append('u')
        solutions.append('u')
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[2][2] == 1 and T[0][2] == 1 and L[0][0] == 1 and L[0][2] == 1):
        rotation('u1')
        solutions.append('u1')
        algo_oll()


#algo F
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[2][2] == 1 and T[0][2] == 1 and F[0][0] == 1 and B[2][0] == 1):
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[0][0] == 1 and T[0][2] == 1 and R[0][0] == 1 and L[0][2] == 1):
        rotation('u')
        solutions.append('u')
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[0][0] == 1 and T[2][0] == 1 and F[0][2] == 1 and B[2][2] == 1):
        rotation('u')
        rotation('u')
        solutions.append('u')
        solutions.append('u')
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[2][0] == 1 and T[2][2] == 1 and L[0][0] == 1 and R[0][2] == 1):
        rotation('u1')
        solutions.append('u1')
        algo_oll()

#algo G
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[0][2] == 1 and T[2][0] == 1):
        algo_oll()
    elif (T[0][1] == 1 and T[1][0] == 1 and T[1][1] == 1 and T[1][2] == 1 and T[2][1] == 1 and T[0][0] == 1 and T[2][2] == 1):
        rotation('u')
        solutions.append('u')
        algo_oll()
    else:
        pass

print(Fore.GREEN + '> Orienting the Last Layer(OLL)-----------------Completed')
#---------------------------------PERMUTING LAST LAYER--------------------------------------------------
def first_step_PLL():
    global T, F, R, L, B, D
    if ((F[0][0] != F[0][2]) and (R[0][0] != R[0][2]) and (L[0][0] != L[0][2]) and (B[2][0] != B[2][2])):
        rotation('r1')
        rotation('f')
        rotation('r1')
        rotation('b')
        rotation('b')
        rotation('r')
        rotation('f1')
        rotation('r1')
        rotation('b')
        rotation('b')
        rotation('r')
        rotation('r')
        solutions.append('r1')
        solutions.append('f')
        solutions.append('r1')
        solutions.append('b')
        solutions.append('b')
        solutions.append('r')
        solutions.append('f1')
        solutions.append('r1')
        solutions.append('b')
        solutions.append('b')
        solutions.append('r')
        solutions.append('r')
        if (F[0][0] == F[0][2]):
            rotation('u')
            rotation('u')
            rotation('r1')
            rotation('f')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('f1')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('r')
            solutions.append('u')
            solutions.append('u')
            solutions.append('r1')
            solutions.append('f')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('f1')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('r')
        elif (R[0][0] == R[0][2]):
            rotation('u1')
            rotation('r1')
            rotation('f')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('f1')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('r')
            solutions.append('u1')
            solutions.append('r1')
            solutions.append('f')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('f1')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('r')
        elif (L[0][0] == L[0][2]):
            rotation('u')
            rotation('r1')
            rotation('f')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('f1')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('r')
            solutions.append('u')
            solutions.append('r1')
            solutions.append('f')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('f1')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('r')
        elif (B[2][0] == B[2][2]):
            rotation('r1')
            rotation('f')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('f1')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('r')
            solutions.append('r1')
            solutions.append('f')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('f1')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('r')
        else:
            pass

    elif ((F[0][0] == F[0][2] and R[0][0] != R[0][2] and L[0][0] != L[0][2] and B[2][0] != B[2][2]) or (F[0][0] != F[0][2] and R[0][0] == R[0][2] and L[0][0] != L[0][2] and B[2][0] != B[2][2]) or (F[0][0] != F[0][2] and R[0][0] != R[0][2] and L[0][0] == L[0][2] and B[2][0] != B[2][2]) or (F[0][0] != F[0][2] and R[0][0] != R[0][2] and L[0][0] != L[0][2] and B[2][0] == B[2][2])):
        if (F[0][0] == F[0][2]):
            rotation('u')
            rotation('u')
            rotation('r1')
            rotation('f')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('f1')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('r')
            solutions.append('u')
            solutions.append('u')
            solutions.append('r1')
            solutions.append('f')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('f1')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('r')
        elif (R[0][0] == R[0][2]):
            rotation('u1')
            rotation('r1')
            rotation('f')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('f1')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('r')
            solutions.append('u1')
            solutions.append('r1')
            solutions.append('f')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('f1')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('r')
        elif (L[0][0] == L[0][2]):
            rotation('u')
            rotation('r1')
            rotation('f')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('f1')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('r')
            solutions.append('u')
            solutions.append('r1')
            solutions.append('f')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('f1')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('r')
        elif (B[2][0] == B[2][2]):
            rotation('r1')
            rotation('f')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('f1')
            rotation('r1')
            rotation('b')
            rotation('b')
            rotation('r')
            rotation('r')
            solutions.append('r1')
            solutions.append('f')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('f1')
            solutions.append('r1')
            solutions.append('b')
            solutions.append('b')
            solutions.append('r')
            solutions.append('r')
        else:
            pass
    else:
        pass


def Pll_algo():
    global T, F, R, L, B, D
    if ((F[0][0] == 2 and F[0][1] == 4) or (F[0][0] == 3 and F[0][1] == 2) or (F[0][0] == 5 and F[0][1] == 3) or (F[0][0] == 4 and F[0][1] == 5)):
        rotation('r')
        rotation('r')
        rotation('u')
        rotation('r')
        rotation('u')
        rotation('r1')
        rotation('u1')
        rotation('r1')
        rotation('u1')
        rotation('r1')
        rotation('u')
        rotation('r1')
        solutions.append('r')
        solutions.append('r')
        solutions.append('u')
        solutions.append('r')
        solutions.append('u')
        solutions.append('r1')
        solutions.append('u1')
        solutions.append('r1')
        solutions.append('u1')
        solutions.append('r1')
        solutions.append('u')
        solutions.append('r1')
    else:
        rotation('r')
        rotation('u1')
        rotation('r')
        rotation('u')
        rotation('r')
        rotation('u')
        rotation('r')
        rotation('u1')
        rotation('r1')
        rotation('u1')
        rotation('r')
        rotation('r')
        solutions.append('r')
        solutions.append('u1')
        solutions.append('r')
        solutions.append('u')
        solutions.append('r')
        solutions.append('u')
        solutions.append('r')
        solutions.append('u1')
        solutions.append('r1')
        solutions.append('u1')
        solutions.append('r')
        solutions.append('r')

while (F[0][0] != F[0][1] or F[0][1] != F[0][2] or R[0][0] != R[0][1] or R[0][1] != R[0][2] or L[0][0] != L[0][1] or L[0][1] != L[0][2] or B[2][0] != B[2][1] or B[2][1] != B[2][2]):
    if (F[0][0] == F[0][2] and R[0][0] == R[0][2] and L[0][0] == L[0][2] and B[2][0] == B[2][2]):
        if (F[0][0] != F[0][1] and R[0][0] != R[0][1] and L[0][0] != L[0][1] and B[2][0] != B[2][1]):
            if (F[0][0] == R[0][1] or F[0][0] == L[0][1]):
                rotation('m')
                rotation('m')
                rotation('u')
                rotation('m')
                rotation('m')
                rotation('u')
                rotation('m')
                rotation('u')
                rotation('u')
                rotation('m')
                rotation('m')
                rotation('u')
                rotation('u')
                rotation('m')
                solutions.append('m')
                solutions.append('m')
                solutions.append('u')
                solutions.append('m')
                solutions.append('m')
                solutions.append('u')
                solutions.append('m')
                solutions.append('u')
                solutions.append('u')
                solutions.append('m')
                solutions.append('m')
                solutions.append('u')
                solutions.append('u')
                solutions.append('m')
            else:
                rotation('m')
                rotation('m')
                rotation('u1')
                rotation('m')
                rotation('m')
                rotation('u1')
                rotation('u1')
                rotation('m')
                rotation('m')
                rotation('u1')
                rotation('m')
                rotation('m')
                solutions.append('m')
                solutions.append('m')
                solutions.append('u1')
                solutions.append('m')
                solutions.append('m')
                solutions.append('u1')
                solutions.append('u1')
                solutions.append('m')
                solutions.append('m')
                solutions.append('u1')
                solutions.append('m')
                solutions.append('m')
        else:
            if (F[0][0] == F[0][1]):
                rotation('u')
                rotation('u')
                solutions.append('u')
                solutions.append('u')
                Pll_algo()
            elif (R[0][0] == R[0][1]):
                rotation('u1')
                solutions.append('u1')
                Pll_algo()
            elif (L[0][0] == L[0][1]):
                rotation('u')
                solutions.append('u')
                Pll_algo()
            else:
                Pll_algo()
    else:
        first_step_PLL()

print(Fore.GREEN + '> Permuting the Last Layer(PLL)-----------------Completed')
if F[0][0] == 3:
    rotation('u1')
    solutions.append('u1')
elif F[0][0] == 4:
    rotation('u')
    solutions.append('u')
elif F[0][0] == 5:
    rotation('u')
    rotation('u')
    solutions.append('u')
    solutions.append('u')
else:
    pass

print(Fore.LIGHTGREEN_EX + '>COMPLETED! THANK YOU!!!')


#------------------------------------Solutions----------------------------------
print(np.size(solutions))
for j in range(2):
    Cube_solutions = []
    for i in range(len(solutions)):
        if (solutions[i] == 'u' and solutions[i + 1] == 'u' and solutions[i + 2] == 'u'):
            Cube_solutions.append('u1')
            solutions.pop(i + 1)
            solutions.pop(i + 1)
            solutions.append(0)
            solutions.append(0)
        elif (solutions[i] == 'u1' and solutions[i + 1] == 'u1' and solutions[i + 2] == 'u1'):
            Cube_solutions.append('u')
            solutions.pop(i + 1)
            solutions.pop(i + 1)
            solutions.append(0)
            solutions.append(0)
        elif ((solutions[i] == 'u' and solutions[i + 1] == 'u1') or (
                solutions[i] == 'u1' and solutions[i + 1] == 'u')):
            solutions.pop(i + 1)
            solutions.append(0)
        elif ((solutions[i] == 'f' and solutions[i + 1] == 'f1') or (
                solutions[i] == 'f1' and solutions[i + 1] == 'f')):
            solutions.pop(i + 1)
            solutions.append(0)
        elif ((solutions[i] == 'b' and solutions[i + 1] == 'b1') or (
                solutions[i] == 'b1' and solutions[i + 1] == 'b')):
            solutions.pop(i + 1)
            solutions.append(0)
        elif ((solutions[i] == 'r' and solutions[i + 1] == 'r1') or (
                solutions[i] == 'r1' and solutions[i + 1] == 'r')):
            solutions.pop(i + 1)
            solutions.append(0)
        elif ((solutions[i] == 'l' and solutions[i + 1] == 'l1') or (
                solutions[i] == 'l1' and solutions[i + 1] == 'l')):
            solutions.pop(i + 1)
            solutions.append(0)
        elif ((solutions[i] == 'd' and solutions[i + 1] == 'd1') or (
                solutions[i] == 'd1' and solutions[i + 1] == 'd')):
            solutions.pop(i + 1)
            solutions.append(0)
        elif (solutions[i] == 'u' and solutions[i + 1] == 'u' and solutions[i + 2] == 'u' and solutions[
            i + 3] == 'u'):
            solutions.pop(i + 1)
            solutions.pop(i + 1)
            solutions.pop(i + 1)
            solutions.append(0)
            solutions.append(0)
            solutions.append(0)
        else:
            Cube_solutions.append(solutions[i])
    del Cube_solutions[len(Cube_solutions) - Cube_solutions.count(0):]
    solutions = Cube_solutions



def display_solutions(solutions):
    # Calculate the size of the square matrix
    n = int(len(solutions) ** 0.5) + 1

    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Rotations")
    
    # Set background color
    window.configure(bg="#f0f0f0")

    # Create a custom font
    custom_font = font.Font(family="Helvetica", size=25)

    # Create a frame to contain the labels
    frame = tk.Frame(window, bg="#f0f0f0")
    frame.pack()

    # Create labels to display the solutions with arrows between them in a square matrix format
    for i in range(n):
        for j in range(n):
            index = i * n + j
            if index < len(solutions):
                label_text = solutions[index]
                # Add arrow if not the last solution in row
                if j < n - 1:
                    label_text += " -> "
                label = tk.Label(frame, text=label_text, font=custom_font, bg="#f0f0f0", padx=10, pady=10)
                label.grid(row=i, column=j)

    # Run the Tkinter event loop
    window.mainloop()


# Call the function to display solutions in a new window
display_solutions(solutions)

