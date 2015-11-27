# Tutorial #

Basic tutorial on running vhdl-dot


# Basics #

Note: You must have PLY installed!
http://www.dabeaz.com/ply/

Simply run the vhdl-dot.py file with a python interpreter, and when prompted, specify the VHDL file you would like to analyze.

The script will notify you of its success or failure.
Upon completion two files will be created, a log file, which is primarily for debugging purposes, and a dot file.

If you're on windows you'll have to open the dot file in a dot renderer such as Graphviz.
http://graphviz.org/

If you're on Linux and have the dot library installed, you can compile the dot file to a png with a command similar to...
dot -Tpng -Ooutput output1.dot