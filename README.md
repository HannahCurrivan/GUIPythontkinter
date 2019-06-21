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

The following is how to create a button using ``` Button``` (make sure it is capital B) within a GUI which you can name and give a command, in this example the command is to print out hello.

```python
button = tk.Button(r, text = 'Reliability', width=25, command= 'hello')
button.pack()
```

## Call a function using a button

First make a function: 

```python
def flower():
  white = 5
  blue = 8
  green = 2
  total number of flowers = 15 
  print('How many of the flowers will be blue =', (blue/total number of  flowers)*100)
```

and then to call it using the button use ```command = flower```. 
The result for this function comes out of the python console as ``` How many of the flowers will be blue = 53.333333333333336 ```

# Result to appear in GUI using a Label 


