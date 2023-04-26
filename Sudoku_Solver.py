# This function returns the row of the running (i,j) cell as a list of strings
def row(i,j):
    global sudoku
    list=sudoku[i]
    return list
# This function returns the column of the running (i,j) cell as a list of strings
def col(i,j):
    global sudoku
    list=[]
    for k in range(9):
        a=sudoku[k][j]
        list.append(a)
    return list
# This function returns the 3x3 tile of the running (i,j) cell as a list of strings
def tile(i,j):
    global sudoku
    if(i<3):
        a,b,c=0,1,2
    elif (i<6):
        a,b,c=3,4,5
    else:
        a,b,c=6,7,8

    if (j < 3):
        x,y,z = 0,1,2
    elif (j < 6):
        x,y,z = 3,4,5
    else:
        x,y,z = 6,7,8

    list=[sudoku[a][x],sudoku[a][y],sudoku[a][z],sudoku[b][x],sudoku[b][y],sudoku[b][z],sudoku[c][x],sudoku[c][y],sudoku[c][z]]
    return list
# This function calculates the probable numbers which can be present in a cell with co-ordinate (i,j)
def prob(a,b,c):
    list=[]
    for i in range(9):
        if (str(i+1) not in a) and (str(i+1) not in b) and (str(i+1) not in c):
            list.append(str(i+1))
    return list
#when method of elimination is not sufficient then , if a number is probable in a cell,
# and it is not probable in any other cell of that tile, then instead of being "probable" the number is confirmed.
def altlogic(i,j):
    global sudoku
    if (i<3):
        a=0
    elif (i<6):
        a=3
    else:
        a=6

    if (j<3):
        b=0
    elif (j<6):
        b=3
    else:
        b=6
    probi=[]
    for r in range(a,a+3):
        for c in range (b,b+3):
            if ((r==i) and (c==j)):
                pass
            elif (sudoku[r][c]==str()):
                d=prob(row(r, c), col(r, c), tile(r, c))
                probi.extend(d)
    result=list(set(probi))
    return result

# This function checks whether the problem is solved or not
def SolveStatus(sudoku):
    space_count = 0
    for i in range (9):
        for j in range(9):
            if sudoku[i][j] == str():
                space_count=space_count+1
    if space_count==0:
        stat="solved"
    else:
        stat="not_solved"
    return stat

# This function creates the output layout
def output_gui():
    global sudoku, boxwidth, boxheight
    Input_Frame.pack_forget()
    Output_Frame=LabelFrame(root,text="Output")
    Output_Frame.pack()
    if SolveStatus(sudoku)=="solved":
        show_text="Solved Sudoku is:"
    else:
        show_text="I cant solve it completely. This is how far I can go ..."

    Output_Prompt=Label(Output_Frame, text=show_text)
    Output_Prompt.grid(row=0,column=0, columnspan=9)
    for i in range(9):
        for j in range(9):
            if (i<3) or (i>5):
                if(j<3):
                    color="Yellow"
                elif(j<6):
                    color="Green"
                else:
                    color="Yellow"
            else:
                if (j < 3):
                    color = "Green"
                elif (j < 6):
                    color = "Yellow"
                else:
                    color = "Green"
            result=Entry(Output_Frame,width=boxwidth,font= boxheight,bg=color)
            result.insert(0,sudoku[i][j])
            result.grid(row=i+1,column=j)

# This function saves the data from GUI to sudoku variable
def My_Save():
    global sudoku

    sudoku[0]=[E11.get(),E12.get(),E13.get(),E14.get(),E15.get(),E16.get(),E17.get(),E18.get(),E19.get()]
    sudoku[1]=[E21.get(),E22.get(),E23.get(),E24.get(),E25.get(),E26.get(),E27.get(),E28.get(),E29.get()]
    sudoku[2]=[E31.get(),E32.get(),E33.get(),E34.get(),E35.get(),E36.get(),E37.get(),E38.get(),E39.get()]
    sudoku[3]=[E41.get(),E42.get(),E43.get(),E44.get(),E45.get(),E46.get(),E47.get(),E48.get(),E49.get()]
    sudoku[4]=[E51.get(),E52.get(),E53.get(),E54.get(),E55.get(),E56.get(),E57.get(),E58.get(),E59.get()]
    sudoku[5]=[E61.get(),E62.get(),E63.get(),E64.get(),E65.get(),E66.get(),E67.get(),E68.get(),E69.get()]
    sudoku[6]=[E71.get(),E72.get(),E73.get(),E74.get(),E75.get(),E76.get(),E77.get(),E78.get(),E79.get()]
    sudoku[7]=[E81.get(),E82.get(),E83.get(),E84.get(),E85.get(),E86.get(),E87.get(),E88.get(),E89.get()]
    sudoku[8]=[E91.get(),E92.get(),E93.get(),E94.get(),E95.get(),E96.get(),E97.get(),E98.get(),E99.get()]
#This function solves the grid by using above functions
def My_Submit():
    global sudoku
    loopcount=0
    while SolveStatus(sudoku) == "not_solved":
        loopcount+=1
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == str():
                    a = prob(row(i, j), col(i, j), tile(i, j))
                    if len(a) == 1:
                        sudoku[i][j] = a[0]
                    else:
                        d=altlogic(i, j)
                        for k in a:
                            if (k not in d):
                                sudoku[i][j] = k
        if (loopcount==200): break
    output_gui()

# Main GUI
from tkinter import *
root=Tk()
root.title("Sudoku Solver by Aloke Banerjee")
root.geometry("550x470")

Input_Frame=LabelFrame(root,text="Inputs")
Input_Frame.pack()
Input_Prompt=Label(Input_Frame, text="Enter Sudoku Here.")
Input_Prompt.grid(row=0,column=0, columnspan=9)
sudoku=[[],[],[],[],[],[],[],[],[]]

#Creating the Sudoku Grid
boxwidth=2
boxheight="Arial 15"
E11=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E11.grid(row=1,column=0)
E12=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E12.grid(row=1,column=1)
E13=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E13.grid(row=1,column=2)
E14=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E14.grid(row=1,column=3)
E15=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E15.grid(row=1,column=4)
E16=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E16.grid(row=1,column=5)
E17=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E17.grid(row=1,column=6)
E18=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E18.grid(row=1,column=7)
E19=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E19.grid(row=1,column=8)

E21=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E21.grid(row=2,column=0)
E22=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E22.grid(row=2,column=1)
E23=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E23.grid(row=2,column=2)
E24=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E24.grid(row=2,column=3)
E25=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E25.grid(row=2,column=4)
E26=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E26.grid(row=2,column=5)
E27=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E27.grid(row=2,column=6)
E28=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E28.grid(row=2,column=7)
E29=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E29.grid(row=2,column=8)

E31=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E31.grid(row=3,column=0)
E32=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E32.grid(row=3,column=1)
E33=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E33.grid(row=3,column=2)
E34=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E34.grid(row=3,column=3)
E35=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E35.grid(row=3,column=4)
E36=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E36.grid(row=3,column=5)
E37=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E37.grid(row=3,column=6)
E38=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E38.grid(row=3,column=7)
E39=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E39.grid(row=3,column=8)

E41=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E41.grid(row=4,column=0)
E42=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E42.grid(row=4,column=1)
E43=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E43.grid(row=4,column=2)
E44=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E44.grid(row=4,column=3)
E45=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E45.grid(row=4,column=4)
E46=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E46.grid(row=4,column=5)
E47=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E47.grid(row=4,column=6)
E48=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E48.grid(row=4,column=7)
E49=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E49.grid(row=4,column=8)

E51=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E51.grid(row=5,column=0)
E52=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E52.grid(row=5,column=1)
E53=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E53.grid(row=5,column=2)
E54=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E54.grid(row=5,column=3)
E55=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E55.grid(row=5,column=4)
E56=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E56.grid(row=5,column=5)
E57=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E57.grid(row=5,column=6)
E58=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E58.grid(row=5,column=7)
E59=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E59.grid(row=5,column=8)

E61=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E61.grid(row=6,column=0)
E62=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E62.grid(row=6,column=1)
E63=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E63.grid(row=6,column=2)
E64=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E64.grid(row=6,column=3)
E65=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E65.grid(row=6,column=4)
E66=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E66.grid(row=6,column=5)
E67=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E67.grid(row=6,column=6)
E68=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E68.grid(row=6,column=7)
E69=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E69.grid(row=6,column=8)

E71=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E71.grid(row=7,column=0)
E72=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E72.grid(row=7,column=1)
E73=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E73.grid(row=7,column=2)
E74=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E74.grid(row=7,column=3)
E75=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E75.grid(row=7,column=4)
E76=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E76.grid(row=7,column=5)
E77=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E77.grid(row=7,column=6)
E78=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E78.grid(row=7,column=7)
E79=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E79.grid(row=7,column=8)

E81=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E81.grid(row=8,column=0)
E82=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E82.grid(row=8,column=1)
E83=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E83.grid(row=8,column=2)
E84=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E84.grid(row=8,column=3)
E85=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E85.grid(row=8,column=4)
E86=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E86.grid(row=8,column=5)
E87=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E87.grid(row=8,column=6)
E88=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E88.grid(row=8,column=7)
E89=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E89.grid(row=8,column=8)

E91=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E91.grid(row=9,column=0)
E92=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E92.grid(row=9,column=1)
E93=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E93.grid(row=9,column=2)
E94=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E94.grid(row=9,column=3)
E95=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E95.grid(row=9,column=4)
E96=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="green")
E96.grid(row=9,column=5)
E97=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E97.grid(row=9,column=6)
E98=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E98.grid(row=9,column=7)
E99=Entry(Input_Frame,width=boxwidth,font= boxheight,bg="yellow")
E99.grid(row=9,column=8)

Save_Button=Button(Input_Frame,text="Save Data", command=My_Save)
Save_Button.grid(row=10, column=0,columnspan=4)
Submit_Button=Button(Input_Frame,text="Submit Data", command=My_Submit)
Submit_Button.grid(row=10, column=5,columnspan=4)

root.mainloop()

