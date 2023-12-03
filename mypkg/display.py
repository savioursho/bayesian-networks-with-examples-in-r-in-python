import pygraphviz
from pathlib import Path
from IPython.display import SVG, display


def display_graph(g: pygraphviz.AGraph, filename=None):
    filename = filename or f"graphs/graph_{hash(g)}.svg"
    Path(filename).parent.mkdir(exist_ok=True)
    g.draw(filename, prog="dot")
    display(SVG(filename))
