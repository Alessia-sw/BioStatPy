
    #Copyright (c) 2022 Alessia Stanistreet-Welsh

#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License along
#with this program; if not, write to the Free Software Foundation, Inc.,
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#Code written by Alessia Stanistreet-Welsh,


# GUI Interface ===========================================================

# from tkinter import *
# root = Tk()

# root.title('BioStat Py')
# root.iconbitmap('BioStat.ico')
# root.geometry('800x700')

# my_label = Label(root, text = 'Welcome to BioStat Py').pack()
# root.mainloop()
# ========================================================================



import os
import numpy as np
from numpy import sqrt
from scipy import stats
from scipy.stats import t
from statistics import mean
from statistics import median
from statistics import mode
from statistics import stdev
import matplotlib.pyplot as plt


# MAIN FUNCTION =========================================================

# Calculator Menu

# Operation Functions

def add():
    x = float(input("Enter x: </> "))
    y = float(input("Enter y: </> "))
    print("Answer: ", x + y)
    Calculate_Again = input("Would you like to do another calculation (Y/N): </> ")
    if Calculate_Again == "Y":
        os.system('cls||clear')
        Calculator_Menu()
    if Calculate_Again == "N":
        os.system('cls||clear')
        Main_Menu()

def subtract():
    x = float(input("Enter x: </> "))
    y = float(input("Enter y: </> "))
    print("Answer: ", x - y)
    Calculate_Again = input("Would you like to do another calculation (Y/N): </> ")
    if Calculate_Again == "Y":
        os.system('cls||clear')
        Calculator_Menu()
    if Calculate_Again == "N":
        os.system('cls||clear')
        Main_Menu()

def multiply():
    x = float(input("Enter x: </> "))
    y = float(input("Enter y: </> "))
    print("Answer: ", x * y)
    Calculate_Again = input("Would you like to do another calculation (Y/N): </> ")
    if Calculate_Again == "Y":
        os.system('cls||clear')
        Calculator_Menu()
    if Calculate_Again == "N":
        os.system('cls||clear')
        Main_Menu()

def divide():
    x = float(input("Enter x: </> "))
    y = float(input("Enter y: </> "))
    print("Answer: ", x / y)
    Calculate_Again = input("Would you like to do another calculation (Y/N): </> ")
    if Calculate_Again == "Y":
        os.system('cls||clear')
        Calculator_Menu()
    if Calculate_Again == "N":
        os.system('cls||clear')
        Main_Menu()

def Calculator_Menu():

    print("""
            ===========================
                     Calculator
                 1 | Addition
                 2 | Subtraction
                 3 | Multiply
                 4 | Divide
                 M | Main Menu
            ===========================""")
    Calculator_Input = input("Choose option </> ")

    if Calculator_Input == "M":
        os.system('cls||clear')
        Main_Menu()

    if Calculator_Input == "1":
        add()

    if Calculator_Input == "2":
        subtract()

    if Calculator_Input == "3":
        multiply()

    if Calculator_Input == "4":
        divide()

    else:
        os.system("cls||clear")
        print("Please choose a correct option")
        Calculator_Menu()

# Statistics Menu

# Statistics Functions

def Descriptive():
    print("""
            ===========================
                     Descriptive

                 1 | Manual
                 2 | Data File
                 M | Main Menu
            ===========================""")
    Descriptive_Input = input("Choose an option </> ")

    if Descriptive_Input == "M":
        os.system('cls||clear')
        Main_Menu()

    if Descriptive_Input == '1':
        Manual_Input = input("Enter each number in data set seperated by a space: </> ")
        print("\n")
        Manual_List = Manual_Input.split()
        print("""
        ====================================
        Descriptive Summary of your Data Set 
        ====================================""")

        print("Data set: ", Manual_List)

        for i in range(len(Manual_List)):
            Manual_List[i] = float(Manual_List[i])

        print("Sum: ", sum(Manual_List))
        print("Mean: ", mean(Manual_List))
        print("Median: ", median(Manual_List))
        print("Mode: ", mode(Manual_List))

        User_Input = input("Enter a new data set? (Y/N) </> ")
        if User_Input == 'Y':
            os.system('cls||clear')
            Descriptive()
        if User_Input == 'N':
            os.system('cls||clear')
            Main_Menu()
        else:
            print("Incorrect Input")
            os.system('cls||clear')
            Main_Menu()


    if Descriptive_Input == '2':
        filename = input("Enter File Name (include '.txt'): </> ")
        try:
            fhand = open(filename)
            list = []
        except:
            print("File cannot be opened: ", filename)
            Descriptive()

        for line in fhand:
            values = line.split()
            for i in values:
                for number in i:
                    if(number.isdigit()):
                        list.append(number)


        for i in range(len(list)):
            list[i] = float(list[i])

        print("""
        ====================================
        Descriptive Summary of your Data Set 
        ====================================""")

        print(list)
        print("Sum: ", sum(list))
        print("Mean: ", mean(list))
        print("Median: ", median(list))
        print("Mode: ", mode(list))

        User_Input = input("Enter a new data set? (Y/N) </> ")
        if User_Input == 'Y':
            os.system('cls||clear')
            Descriptive()
        if User_Input == 'N':
            os.system('cls||clear')
            Main_Menu()
        else:
            print("Incorrect Input")
            os.system('cls||clear')
            Main_Menu()

def Standard_Deviation():
    print("""
            ===========================
                 Standard Deviation

                 1 | Manual
                 2 | Data File
                 M | Main Menu
            ===========================""")

    StandardDev_Input = input("Choose an option </> ")

    if StandardDev_Input == "M":
        os.system('cls||clear')
        Main_Menu()

    if StandardDev_Input == "1":
        Manual_Input = input("Enter each number in data set seperated by a space: </> ")
        print("\n")
        Manual_List = Manual_Input.split()
        print("""
        ===================================
        Standard Deviation of your Data Set 
        ===================================""")

        print("Data set: ", Manual_List)

        for i in range(len(Manual_List)):
            Manual_List[i] = float(Manual_List[i])

        print("Standard Deviation: ", stdev(Manual_List))

        User_Input = input("Enter a new data set? (Y/N) </> ")
        if User_Input == 'Y':
            os.system('cls||clear')
            Standard_Deviation()
        if User_Input == 'N':
            os.system('cls||clear')
            Main_Menu()
        else:
            print("Incorrect Input")
            os.system('cls||clear')
            Main_Menu()

    if StandardDev_Input == "2":
        filename = input("Enter File Name (include '.txt'): </> ")
        try:
            fhand = open(filename)
            list = []
        except:
            print("File cannot be opened: ", filename)
            Descriptive()

        for line in fhand:
            values = line.split()
            for i in values:
                for number in i:
                    if(number.isdigit()):
                        list.append(number)


        for i in range(len(list)):
            list[i] = float(list[i])

    print("""
    ===================================
    Standard Deviation of your Data Set 
    ===================================""")

    print("Data set: ", list)
    print("Standard Deviation: ", stdev(list))

    User_Input = input("Enter a new data set? (Y/N) </> ")
    if User_Input == 'Y':
        os.system('cls||clear')
        Standard_Deviation()
    if User_Input == 'N':
        os.system('cls||clear')
        Main_Menu()
    else:
        print("Incorrect Input")
        os.system('cls||clear')
        Main_Menu()

# ========================================

# T-test Functions

def Independent():
    global data1, data2
    print("""
            ==========================
                   Data Input

                 1 | Manual
                 2 | Data file
                 M | Main Menu
            ===========================""")

    Independent_Input = input("Choose how to enter data sets: </> ")

    if Independent_Input == "M":
        os.system('cls||clear')
        Main_Menu()

    if Independent_Input == "1":
        data1 = input("Enter data set 1 (numbers seperated by spaces): </>")
        data2 = input("Enter data set 2 (numbers seperated by spaces): </>")
        data1 = data1.split()
        data2 = data2.split()

        for i in range(len(data1)):
            data1[i] = float(data1[i])
        for i in range(len(data2)):
            data2[i] = float(data2[i])
        # calculate means
        mean1, mean2 = mean(data1), mean(data2)
        # calculate standard errors
        n1, n2 = len(data1), len(data2)
        se1, se2 = stats.sem(data1), stats.sem(data2)
        # standard error on the difference between the samples
        sed = np.sqrt(se1**2.0 + se2**2.0)
        # t statistic
        t_stat = (mean1 - mean2) / sed
        # degrees of freedom
        df = n1 + n2 - 2
        # calculate critical value
        alpha = 0.05
        cv = t.ppf(1.0 - alpha, df)
        # calculate the p-value
        p = (1.0 - t.cdf(abs(t_stat), df)) * 2.0
        print("t statistic: ", t_stat)
        print("Degrees of freedom: ", df)
        print("Critical value: ", cv)
        print("p-value: ", p)
        if p > alpha:
            print("Accept null hypothesis that the means are equal - no significant difference between groups")
        else:
            print("Reject the null hypothesis that the means are equal - there is significant difference between groups")

        User_Input = input("Analyse more data? (Y/N): </> ")
        if User_Input == "Y":
            Independent()
        if User_Input == "N":
            Main_Menu()

    if Independent_Input == "2":
        filename1 = input("Enter File Name for first data set (include '.txt'): </> ")
        filename2 = input("Enter File Name for second data set (include '.txt'): </> ")
        try:
            fhand1 = open(filename1)
            file1_list = []
        except:
            print("File cannot be opened: ", filename1)
            Independent()

        for line in fhand1:
            file1_values = line.split()
            for i in file1_values:
                for number in i:
                    if (number.isdigit()):
                        file1_list.append(number)

        for i in range(len(file1_list)):
            file1_list[i] = float(file1_list[i])

        try:
            fhand2 = open(filename2)
            file2_list = []
        except:
            print("File cannot be opened: ", filename2)
            Independent()

        for line in fhand2:
            file2_values = line.split()
            for i in file2_values:
                for number in i:
                    if (number.isdigit()):
                        file2_list.append(number)

        for i in range(len(file2_list)):
            file2_list[i] = float(file2_list[i])

        data1 = file1_list
        data2 = file2_list

        print(data1)
        print(data2)
        mean1, mean2 = mean(data1), mean(data2)
        # calculate standard errors
        n1, n2 = len(data1), len(data2)
        se1, se2 = stats.sem(data1), stats.sem(data2)
        # standard error on the difference between the samples
        sed = np.sqrt(se1**2.0 + se2**2.0)
        # t statistic
        t_stat = (mean1 - mean2) / sed
        # degrees of freedom
        df = n1 + n2 - 2
        # calculate critical value
        alpha = 0.05
        cv = t.ppf(1.0 - alpha, df)
        # calculate the p-value
        p = (1.0 - t.cdf(abs(t_stat), df)) * 2.0
        print("t statistic: ", t_stat)
        print("Degrees of freedom: ", df)
        print("Critical value: ", cv)
        print("p-value: ", p)
        if p > alpha:
            print("Accept null hypothesis that the means are equal - no significant difference between groups")
        if p <= alpha:
            print("Reject the null hypothesis that the means are equal - there is significant difference between groups")

        User_Input = input("Analyse more data? (Y/N): </> ")
        if User_Input == "Y":
            Independent()
        if User_Input == "N":
            Main_Menu()



def Dependent():

    print("""
            ==========================
                   Data Input

                 1 | Manual
                 2 | Data file
                 M | Main Menu
            ===========================""")

    Dependent_Input = input("Choose how to enter data sets: </> ")

    if Dependent_Input == "M":
        os.system("cls||cls")
        Main_Menu()

    if Dependent_Input == "1":
        data1 = input("Enter data set 1 (numbers seperated by spaces): </>")
        data2 = input("Enter data set 2 (numbers seperated by spaces): </>")
        data1 = data1.split()
        data2 = data2.split()

        for i in range(len(data1)):
            data1[i] = float(data1[i])
        for i in range(len(data2)):
            data2[i] = float(data2[i])

        # calculate means
        mean1, mean2 = mean(data1), mean(data2)
        #number of paired samples
        n = len(data1)
        # sum of squared difference between observations
        d1 = sum([(data1[i]-data2[i])**2 for i in range(n)])
        #sum difference between observations
        d2 = sum([data1[i]-data2[i] for i in range(n)])
        #standard deviation of the difference between means
        sd = sqrt((d1 - (d2**2 / n)) / (n-1))
        #standard error of the difference between means
        sed = sd / sqrt(n)
        # calculate the t-statistic
        alpha = 0.05
        t_stat = (mean1 - mean2) / sed
        #degrees of freedom
        df = n - 1
        # calculate the critical value
        cv = t.ppf(1.0 - alpha, df)
        # calculate the p-value
        p = (1.0 - t.cdf(abs(t_stat), df)) * 2.0
        print("t statistic: ", t_stat)
        print("Degrees of freedom: ", df)
        print("Critical value: ", cv)
        print("p-value: ", p)

        if p > alpha:
            print("Accept null hypothesis that the means are equal - there is no significant difference between the groups")
        if p <= alpha:
            print("Reject null hypothesis that the means are equal - there is significant difference between the groups")

        User_Input = input("Analyse more data? (Y/N): </> ")
        if User_Input == "Y":
            Dependent()
        if User_Input == "N":
            Main_Menu()


    if Dependent_Input == "2":
        filename1 = input("Enter File Name for first data set (include '.txt': </> ")
        filename2 = input("Enter File Name for second data set (include '.txt': </> ")
        try:
            fhand1 = open(filename1)
            file1_list = []
        except:
            print("File cannot be opened: ", filename1)
            Dependent()

        for line in fhand1:
            file1_values = line.split()
            for i in file1_values:
                for number in i:
                    if (number.isdigit()):
                        file1_list.append(number)

        for i in range(len(file1_list)):
            file1_list[i] = float(file1_list[i])

        try:
            fhand2 = open(filename2)
            file2_list = []
        except:
            print("File cannot be opened: ", filename2)
            Dependent()

        for line in fhand2:
            file2_values = line.split()
            for i in file2_values:
                for number in i:
                    if (number.isdigit()):
                        file2_list.append(number)

        for i in range(len(file2_list)):
            file2_list[i] = float(file2_list[i])

        data1 = file1_list
        data2 = file2_list

        mean1, mean2 = mean(data1), mean(data2)
        #number of paired samples
        n = len(data1)
        # sum of squared difference between observations
        d1 = sum([(data1[i]-data2[i])**2 for i in range(n)])
        #sum difference between observations
        d2 = sum([data1[i]-data2[i] for i in range(n)])
        #standard deviation of the difference between means
        sd = sqrt((d1 - (d2**2 / n)) / (n-1))
        #standard error of the difference between means
        sed = sd / sqrt(n)
        # calculate the t-statistic
        alpha = 0.05
        t_stat = (mean1 - mean2) / sed
        #degrees of freedom
        df = n - 1
        # calculate the critical value
        cv = t.ppf(1.0 - alpha, df)
        # calculate the p-value
        p = (1.0 - t.cdf(abs(t_stat), df)) * 2.0
        print("t statistic: ", t_stat)
        print("Degrees of freedom: ", df)
        print("Critical value: ", cv)
        print("p-value: ", p)

        if p > alpha:
            print("Accept null hypothesis that the means are equal - there is no significant difference between the groups")
        if p <= alpha:
            print("Reject null hypothesis that the means are equal - there is significant difference between the groups")

        User_Input = input("Analyse more data? (Y/N): </> ")
        if User_Input == "Y":
            Dependent()
        if User_Input == "N":
            Main_Menu()


def t_test_Menu():
    print("""
            ==========================
                 Student's t-test

                 1 | Independent samples
                 2 | Dependent samples
                 M | Main Menu
            ===========================""")

    T_test_Input = input("Choose option: </>")
    if T_test_Input == 'M':
        Main_Menu()

    if T_test_Input == '1':
        Independent()

    if T_test_Input == '2':
        Dependent()


#=========================================


def Statistics_Menu():
    print("""
            ===========================
                     Statistics

                 1 | Descriptive
                 2 | Standard Deviation
                 3 | Student's t-test
                 M | Main Menu
            ===========================""")
    Statistics_Input = input("Choose option </> ")
    if Statistics_Input == "M":
        os.system('cls||clear')
        Main_Menu()

    if Statistics_Input == "1":
        os.system('cls||clear')
        Descriptive()

    if Statistics_Input == "2":
        os.system('cls||clear')
        Standard_Deviation()

    if Statistics_Input == "3":
        t_test_Menu()


# Graph Menu

def Scatter_Graph():
    print("""
            =======================
                 Scatter Graph

                 1 | Manual
                 2 | Data File
                 M | Main Menu
            =======================""")

    Scatter_Input = input("Choose option </> ")
    if Scatter_Input == "M":
        os.system('cls||clear')
        Main_Menu()

    if Scatter_Input == "1":
        x_input = input("Enter x values, separated by spaces: </> ")
        y_input = input("Enter y values, separated by spaces: </> ")

        x_values = x_input.split()
        y_values = y_input.split()

        for i in range(len(x_values)):
            x_values[i] = float(x_values[i])
        for i in range(len(y_values)):
            y_values[i] = float(y_values[i])

        x_label = input("Enter x axis label: </> ")
        y_label = input("Enter y axis label: </> ")
        fig_title = input("Enter Figure Title: </> ")
        plt.scatter(x_values, y_values)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.suptitle(fig_title)
        plt.show()



def Graph_Menu():
    print("""
            ===========================
                       Graph

                 1 | Scatter Graph
                 2 | Line Graph
                 M | Main Menu
            ===========================""")
    Graph_Input = input("Choose option </> ")
    if Graph_Input == "M":
        os.system('cls||clear')
        Main_Menu()

    if Graph_Input == "1":
        Scatter_Graph()

# Main Menu Function
def Main_Menu():
    print("""
            ===========================
                     BioStat Py

                 1 | Calculator
                 2 | Statistics
                 3 | Graph
                 4 | Exit
            ===========================""")

    Menu_Input = input("What would you like to do? </> ")

    if Menu_Input == "1":
        os.system('cls||clear')
        Calculator_Menu()

    if Menu_Input == "2":
        os.system('cls||clear')
        Statistics_Menu()

    if Menu_Input == "3":
        os.system('cls||clear')
        Graph_Menu()

    if Menu_Input == "4":
        os.system('cls||clear')
        exit()


# MAIN FUNCTION =========================================================


Main_Menu()

