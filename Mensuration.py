print("This is a program which will help you in Mensuration.")
print("NOTE: While you Input the Measurements, DO NOT TYPE ITS UNIT. \n")


def main():
    print("On which Topic do you want help in ?")
    print("For Perimeter, Type 1.")
    print("For Area, Type 2.")
    print("For Volume, Type 3.")

    Type = int(input())

    if Type == 1:
        print("Whose Perimeter do you want to search?")

        print("For Triangle, Type 1.")
        print("For Square, Type 2.")
        print("For Rectangle, Type 3.")
        print("For the Circumference of a Circle, Type 4.")

        P_Figure = int(input())

    if Type == 1 and P_Figure == 1:
        print("What is the Type of the Triangle.")

        print("For Equilateral, Type 1")
        print("For Isosceles, Type 2")
        print("For Scalene, Type 3")

        T_Type = int(input())

    if Type == 1 and P_Figure == 1 and T_Type == 1:
        print("Enter the Length of each Side of the Triangle.")
        ET_1 = float(input())

        print("The Perimeter of the Triangle =", ET_1 * 3, "Units.")

    if Type == 1 and P_Figure == 1 and T_Type == 2:
        print("Please Enter the Length of each of the Equal Sides.")
        IT_1 = float(input())
        print("Now, enter the Length of the Unequal Side.")
        IT_2 = float(input())

        print("The Perimeter of the Triangle =", (IT_1 * 2) + IT_2, "Units.")

    if Type == 1 and P_Figure == 1 and T_Type == 3:
        print("Enter the Length of the First Side.")
        ST_1 = float(input())
        print("Enter the Length of the Second Side.")
        ST_2 = float(input())
        print("Enter the Length of the Third Side.")
        ST_3 = float(input())

        print("The Perimeter of the Triangle =", ST_1 + ST_2 + ST_3, "Units.")



    elif Type == 1 and P_Figure == 2:
        print("Enter the length of each Side.")
        S_1 = float(input())

        print("The Perimeter of the Square =", S_1 * 4, "Units.")



    elif Type == 1 and P_Figure == 3:
        print("What is the Length of the Rectangle?")
        L = float(input())
        print("What is its Breadth?")
        B = float(input())

        print("The Perimeter of the Rectangle =", 2 * (L + B), "Units.")


    elif Type == 1 and P_Figure == 4:
        print("What is the Radius of the Circle?")
        C_1 = float(input())

        print("The Circumference of the Circle =", 2 * 3.14159 * C_1, "Units.")

    if Type == 2:
        print("Whose Area do you wanna search?")
        print("For Triangle, Type 1.")
        print("For Square, Type 2.")
        print("For Rectangle, Type 3.")
        print("For Circle, Type 4")

        A_Figure = int(input())

    if Type == 2 and A_Figure == 1:
        print("What is the Length of the Base of the Triangle?")
        TB = float(input())
        print("Enter the Length of the Height of the Triangle.")
        TH = float(input())

        print("The Area of the Triangle =", (TB * TH) / 2, "Sq. Units.")

    if Type == 2 and A_Figure == 2:
        print("Enter the Length of each Side of the Square.")
        SA = float(input())

        print("The Area of the Square =", SA * SA, "Sq. Units.")

    if Type == 2 and A_Figure == 3:
        print("Enter the Length of the Rectangle.")
        RL = float(input())
        print("Enter the Breadth of the Rectangle.")
        RB = float(input())

        print("The Area of the Rectangle =", RL * RB, "Sq. Units.")

    if Type == 2 and A_Figure == 4:
        print("Enter the Radius of the Circle.")
        CR = float(input())

        print("The Area of the Circle =", 3.14159 * CR * CR, "Sq. Units.")



    elif Type == 3:
        print("Whose Volume do you wanna Find ?")
        print("For Cube, Type 1.")
        print("For Cuboid, Type 2.")

        V_Figure = int(input())

    if Type == 3 and V_Figure == 1:
        print("What is the Length of each Edge of the Cube ?")
        CE = float(input())

        print("The Volume of the Cube =", CE * CE * CE, "Cubic Units.")

    if Type == 3 and V_Figure == 2:
        print("Enter the Length of the Cuboid.")
        CL = float(input())
        print("Enter the Breadth of the Cuboid.")
        CB = float(input())
        print("Enter its Height.")
        CH = float(input())

        print("The Volume of the Cuboid =", CL * CB * CH, "Cubic Units.")


main()





def again():
    print("\n \n If you want to execute the program once more, Type YES, Otherwise Input NO.")
    Again = input().upper()

    if Again == "YES":
        print("")
        main()

    elif Again == "NO":
        print("\n Thanks for Using.")

    else:
        print("\n Wrong Input.")


again()
