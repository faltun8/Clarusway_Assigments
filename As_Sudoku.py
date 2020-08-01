def sudok(list1):
    line = 0
    for i in list1:
        count = 0
        if line % 3 == 0:
            print("- - - - - - - - - - - - - - -")
        for j in i:
            if count < 3:
                print(f"{j}  ",end="")
                count +=1
            else:
                print(f"| {j}  ",end="")
                count = 1
        print("")
        line += 1

sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

sudok(sudoku)
