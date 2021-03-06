# Shell, Scripts and the Juypter Notebook

we'll walk through all of the methods of launching and interacting with Python in class. Here's a summary:


From your system taskbar, lauch a shell terminal. 

The terminal enables you to interact with your computer using a command line interface (CLI) rather than a graphical user interface (GUI). Once you're familiar with a CLI, it's usually faster to drive your computer from this than a GUI.

If you don't want to launch terminals or jupyter notebooks as show below, on a Windows machine you can use the Anaconda Navigator to launch the apps for jupyter, IPython, Spyder etc. that are refered to below.



## Launch a system command prompt or shell

On a windows machine, type this in the search box within the Start menu: 

``` dos

cmd

```


Alternatively hunt around for the Command Prompt shortcut on the Start menu bar!



Mac and Linux have similar shells.



From the shell you can interact with the filesystem. You might want to explore the [SWC Unix Shell lesson](http://swcarpentry.github.io/shell-novice/) for some ideas on how to use the shell.



The place where you type commands is called the prompt, and looks something like this on a windows machine:

```dos

C:\Users\username\>

```


or on a linux box:

```bash

/usr/usrname/home$

```



## Getting python up and running

To launch python in the terminal, type at the prompt:

```dos

> python

```



You should see some text telling you which python version and distribution is running. You'll also see the prompt change from > to >>> or something similar to signify your now at a python prompt.



A better CLI for python is provided by IPython:


```dos

> ipython

```



We'll explore basic python using the command line, and also use a notebook system for interactively sharing code. This is called the Juypter notebook.

You can quit the python session, and get dropped back to a system shell, by typing:


```python

>>> exit()
```

## Running code from the CLI
Once in python or IPython you can run python commands. For example, at the IPython prompt you might try the following statements:

``` python
>>> print('Hello World!')
>>> 2+3
>>> print?
``` 

We'll be building longer sequences of analysis steps and it's most convenient to put these into scripts. A script is a text file of python code, with the extension .py. To make them run them from the command line:

``` bash
> python ./my_python_script.py
```

or from within IPython (using a 'cell magic' function):

``` python
>>> %run my_python_script.py
```  

## Launching the Juypter Notebook:

The Juypter notebook is a nice format for sharing python code and text, for example the write up of an analysis you've done alongside the code to re-generate that analysis.

Using your system taskbar shortcut or at the command line, launch the Juypter notebook:

```bash

juypter notebook

```

This launches a server which you can connect to use a web-browser using the local url http://127.0.0.1:8888.

We'll explore the nuances of the notebook together in class. Here's a [simple example notebook](1_example_notebook.ipynb) that shows you how some elements work. Feel free to explore! To interact with it and explore executing cells you'll need to download a copy to your local machine and run a juypter notebook server.

If you're coming from Matlab, there's also a fully featured development environment for python programming called Spyder which might be worth checking out.






