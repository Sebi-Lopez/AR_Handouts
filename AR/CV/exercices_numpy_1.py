
import numpy as np 

def ex1(): 
    print("Exercice 1")
    arr = np.zeros(10)
    print(arr)

# ex1()

def ex2(): 
    print("Exercice 2")
    arr = np.zeros(10)
    arr[5] = 1
    print(arr)

# ex2()

def ex3(): 
    print("Exercice 3")
    arr = np.arange(10, 50)
    print(arr)

# ex3()

def ex4(): 
    print("Exercice 4")
    arr = np.arange(1, 10)
    arr = arr.reshape(3,3)
    print(arr)

# ex4()

def ex5(): 
    print("Exercice 5")
    arr = np.arange(1, 10)
    arr = arr.reshape(3,3)
    arr = np.flip(arr)
    print(arr)

# ex5()

def ex6(): 
    print("Exercice 6")
    arr = np.arange(1, 10)
    arr = arr.reshape(3,3)
    arr = np.flip(arr, 1)
    print(arr)

# ex6()


def ex7(): 
    print("Exercice 7")
    arr = np.identity(3)
    print(arr)

ex7()