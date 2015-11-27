**Python script to convert structural VHDL code to a dot graph.**

**News:**
vhdl-dot-beta3 is the latest version

Fixes:
Logical expressions can now contain literals.
Literals are now correctly graphed.


---


**Windows:**

Either download the source code and run vhdl-dot.py through a Python interpreter, or download vhdl-dot-windows and run the executable.

The executable version should 'just work' and shouldn't require a python interpreter, or any python dependencies.

**Linux:**

Download the source code and run vhdl-dot.py through a Python interpreter. You will need to have PLY installed and some way to render DOT files (details below).
Requirements:

**A Python interpreter**
http://www.python.org/

**PLY**
http://www.dabeaz.com/ply/

**Graphviz** (Windows and Linux)
http://www.graphviz.org/

Note:
This is an early build that is still in development and is not entirely error free.

Sample output:

![http://i304.photobucket.com/albums/nn168/Destroyer229/test.png](http://i304.photobucket.com/albums/nn168/Destroyer229/test.png)