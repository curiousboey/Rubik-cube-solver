import numpy as np

T= np.array([[1,3,4],
            [1,1,1],
            [1,4,3]])
F= np.array([[5,6,1],
            [3,2,2],
            [5,6,2]])
R= np.array([[2,5,6],
            [4,3,1],
            [3,4,5]])
L= np.array([[2,4,3],
            [6,4,1],
            [6,3,4]])
B= np.array([[5,3,4],
            [2,5,2],
            [4,6,2]])
D= np.array([[1,5,6],
            [2,6,5],
            [3,5,6]])

# rot= input('Enter the rotation= ')

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

rotation('f')
rotation('r')
rotation('l1')

solutions= []

# Left

left_white = np.hstack((T, F, R, L, B, D))

while left_white[0,[10]] == 6:
    if left_white[0,[10]] == 6:
        rotation('l')
        solutions.append('l')
        if left_white[2,[1]] == 6:
            rotation('u')
            solutions.append('u')
            if left_white[2,[1]] == 6:
                rotation('u')
                solutions.append('u')
                if left_white[2,[1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    if left_white[2,[1]] == 6:
                        rotation('u')
                        solutions.append('u')
                    else:
                        rotation('f')
                        solutions.append('f')
                else:
                    rotation('f')
                    solutions.append('f')
            else:
                rotation('f')
                solutions.append('f')
        else:
            rotation('f')
            solutions.append('f')
    else:
        pass
    left_white = np.hstack((T, F, R, L, B, D))


while left_white[1,[9]] == 6:
    if left_white[1,[9]] == 6:
        if left_white[0,[1]] == 6:
            rotation('u')
            solutions.append('u')
            if left_white[0,[1]] == 6:
                rotation('u')
                solutions.append('u')
                if left_white[0,[1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    if left_white[0,[1]] == 6:
                        rotation('u')
                        solutions.append('u')
                    else:
                        rotation('b1')
                        solutions.append('b1')
                else:
                    rotation('b1')
                    solutions.append('b1')
            else:
                rotation('b1')
                solutions.append('b1')
        else:
            rotation('b1')
            solutions.append('b1')
    else:
        pass
    left_white = np.hstack((T, F, R, L, B, D))


while left_white[1,[11]] == 6:
    if left_white[1,[11]] == 6:
        if left_white[2,[1]] == 6:
            rotation('u')
            solutions.append('u')
            if left_white[2,[1]] == 6:
                rotation('u')
                solutions.append('u')
                if left_white[2,[1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    if left_white[2,[1]] == 6:
                        rotation('u')
                        solutions.append('u')
                    else:
                        rotation('f')
                        solutions.append('f')
                else:
                    rotation('f')
                    solutions.append('f')
            else:
                rotation('f')
                solutions.append('f')
        else:
            rotation('f')
            solutions.append('f')
    else:
        pass
    left_white = np.hstack((T, F, R, L, B, D))


while left_white[2,[10]] == 6:
    if left_white[2,[10]] == 6:
        if left_white[1,[0]] == 6:
            rotation('u')
            solutions.append('u')
            left_white = np.hstack((T, F, R, L, B, D))
            if left_white[1,[0]] == 6:
                rotation('u')
                solutions.append('u')
                left_white = np.hstack((T, F, R, L, B, D))
                if left_white[1,[0]] == 6:
                    rotation('u')
                    solutions.append('u')
                    left_white = np.hstack((T, F, R, L, B, D))
                    if left_white[1,[0]] == 6:
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
    if left_white[1,[11]] == 6:
        if left_white[2,[1]] == 6:
            rotation('u')
            solutions.append('u')
            left_white = np.hstack((T, F, R, L, B, D))
            if left_white[2,[1]] == 6:
                rotation('u')
                solutions.append('u')
                left_white = np.hstack((T, F, R, L, B, D))
                if left_white[2,[1]] == 6:
                    rotation('u')
                    solutions.append('u')
                    left_white = np.hstack((T, F, R, L, B, D))
                    if left_white[2,[1]] == 6:
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






















































