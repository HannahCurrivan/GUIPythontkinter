# GUIPythontkinter
# How to make a GUI using Python Tkinter:
## How to start:
First you need to import tkinter as this is the standard GUI library for Python.

```python
import tkinter as tk 
```

Next you want to give a title using ``` title``` to the GUI and maybe a icon using ``` iconbitmap ```. 
You can also set the size of your GUI using the ``` geometry ``` this is done like the following:

```python
r = tk.Tk() 
r.iconbitmap('flower.ico') # This gives the icon to the GUI 
r.title('Flowers') # This is the title to the GUI 
r.geometry("500x700")
```
## Make an Entry box in a GUI

If you want to have an entry book you use ```Entry```, and it you want to enter a variable you us ```Intvar, StringVar```. 
When a label wants to be used in a GUI you us the command ```Label```. 

```python
v = tk.IntVar() # I am looking for an integer.
u = tk.Label(r, text = 'Blue Flowers').pack()
e = tk.Entry(r, textvariable=v).pack() # Within a text book you expect an integer to be inserted.
```

Also the term ``` pack() ``` used above is a term for geometry on the GUI. 

## Make a Button 

The following is how to create a button using ``` Button``` (make sure it is capital B) within a GUI which you can name and give a command, in this example the command is to call a function which is descibed below and is called ```flower```.

```python
button = tk.Button(r, text = 'Flowers', width=25, command= flower)
button.pack()
```

## Call a function using a button

First make a function: 

```python
def flower():
  white = 5
  blue = v.get()
  green = 2
  total_number_of_flowers = 15 
  F =  (blue/total_number_of_flowers)*100
  output.insert(END, F)
```

and then to call it using the button use ```command = flower```. 
The result for this function comes out of the python console as ``` How many of the flowers will be blue : 53.333333333333336 ```
The command ```output.insert``` is calling the ```output``` command which can be seen below in this example, is passing what is inserted to the ```Text``` command so it can appear on the GUI.

## Result to appear in GUI using a Label 
To label you can use the simple command of ```Label``` make sure it is a captial L. Then Insert the text you want to see appear. 
Then to make the reult of the function you have just run from the button you can us the command of ```Text``` again make sure you use captial T. Using ```Text``` you can state the size of your text box you want to appair in your GUI. 
```python
lab = tk.Label(r, text = 'How many of the flowers will be blue (percentage):').pack()
output = tk.Text(r, width=40, height=2)
output.pack()
```

## How to close the GUI loop
You use a command called ```mainloop```
```python
r.mainloop() 
```

## Outcome of the code

![alt text](C:\Users\hcurrivan\Desktop\Hannah_Currivan\Python\gui.png)
