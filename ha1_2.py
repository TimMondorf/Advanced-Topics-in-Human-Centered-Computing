import numpy as np
import os
import pydot

tim_generator = np.random.default_rng()

os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'

mindmap = pydot.Dot(graph_type="digraph", rankdir="LR")
mindmap.set_splines("curved")
mindmap.set_overlap("false")   # reduces edge crossings
mindmap.set_nodesep("0.6")
mindmap.set_ranksep("0.8")

nodes = dict()

artempcolor = "blue"
artifactcolor = "lightblue"
empcolor = "lightgreen"
surveycolor = "burlywood"
opicolor = "yellow"

def new_node(namo, shapo, coloro):
    nodo = pydot.Node(namo, shape=shapo, style="filled", fillcolor=coloro)
    nodes[namo] = nodo
    mindmap.add_node(nodo)

def new_edge(v1, v2):
    edgo = pydot.Edge(nodes[v1], nodes[v2])
    mindmap.add_edge(edgo)

themes = ["Architectures",
    "Experiments",
    "In silico",
    "HCI",
    "Frameworks",
    "Software"]

for t in themes:
    new_node(t, "circle", "white")

new_node("Park", "box", artempcolor)

##new_edge("Believable proxy of human behavior", "Park")
new_edge("Park", "Architectures")
new_edge("Architectures", "Frameworks")
new_edge("Architectures", "Software")
new_edge("Park", "Experiments")
new_edge("Experiments", "HCI")
new_edge("Experiments", "In silico")

new_node("Bill Lin", "box", artempcolor)
new_edge("Software", "Bill Lin")
new_edge("Frameworks", "Bill Lin")
new_edge("In silico", "Bill Lin")

new_node("He", "box", empcolor)
new_edge("HCI", "He")

new_node("Hutson", "box", artifactcolor)
new_edge("Frameworks", "Hutson")

new_node("Stark", "box", opicolor)
new_edge("Frameworks", "Stark")

new_node("Jaber", "box", empcolor)
new_edge("HCI", "Jaber")

new_node("Xu", "box", artempcolor)
new_edge("Software", "Xu")
new_edge("Frameworks", "Xu")
new_edge("HCI", "Xu")
new_edge("In silico", "Xu")

new_node("Zheng", "box", artempcolor)
new_edge("Software", "Zheng")
new_edge("Frameworks", "Zheng")
new_edge("HCI", "Zheng")

new_node("Naik", "box", empcolor)
new_edge("HCI", "Naik")

new_node("Adornetto", "box", surveycolor)
new_edge("Frameworks", "Adornetto")

new_node("Guimares", "box", artempcolor)
new_edge("Frameworks", "Guimares")
new_edge("Software", "Guimares")
new_edge("HCI", "Guimares")

new_node("Sai Zhang", "box", artempcolor)
new_edge("Frameworks", "Sai Zhang")
new_edge("Software", "Sai Zhang")
new_edge("HCI", "Sai Zhang")
new_edge("In silico", "Sai Zhang")

new_node("Zhihuai Lin", "box", empcolor)
new_edge("HCI", "Zhihuai Lin")

new_node("Mao", "box", artempcolor)
new_edge("Frameworks", "Mao")
new_edge("Software", "Mao")
new_edge("In silico", "Mao")

mindmap.write_jpg("mindmap.jpg")

##os.startfile("mindmap.jpg")

listo = list(nodes.keys())
i = tim_generator.integers(low=0, high=len(listo)-1, size=1)[0]
print(listo[i])

