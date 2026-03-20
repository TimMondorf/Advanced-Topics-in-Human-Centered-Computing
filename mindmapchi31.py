import numpy as np
import os
import pydot

tim_generator = np.random.default_rng()

os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'

mindmap = pydot.Dot(graph_type="digraph", rankdir="UD", beautify=True)
mindmap.set_splines("curved")
mindmap.set_overlap("false")   # reduces edge crossings
mindmap.set_nodesep("0.6")
mindmap.set_ranksep("0.8")

nodes = dict()

methodcolor = "blue"
artifactcolor = "lightblue"
empcolor = "lightgreen"
surveycolor = "burlywood"
opicolor = "yellow"
theocolor ="chartreuse"
assignmentcolor = "red"

def check_vertex(namo):
    if namo in list(nodes.keys() ):
        print(f"{namo} already exists as vertex")

def new_node(namo, coloro, shapo="box"):
    check_vertex(namo)
    nodo = pydot.Node(namo, shape=shapo, style="filled", fillcolor=coloro)
    nodes[namo] = nodo
    mindmap.add_node(nodo)

def new_node_chi(namo):
    check_vertex(namo)
    nodo = pydot.Node(namo, shape="hexagon", style="filled", fillcolor="gold")
    nodes[namo] = nodo
    mindmap.add_node(nodo)

def new_node_topical(namo):
    check_vertex(namo)
    nodo = pydot.Node(namo, shape="circle", style="filled", fillcolor="white")
    nodes[namo] = nodo
    mindmap.add_node(nodo)

def new_edge(v1, v2):
    edgo = pydot.Edge(nodes[v1], nodes[v2])
    mindmap.add_edge(edgo)

def new_edge_invis(v1, v2):
    edge = pydot.Edge(nodes[v1], nodes[v2], style="invis")
    mindmap.add_edge(edge)

new_node("Wobbrock", methodcolor)
new_node("Oulasvirta", methodcolor)
new_node("Berkel", methodcolor)
new_node_topical("HCI scientific identity")

new_edge("Wobbrock", "HCI scientific identity")
new_edge("Oulasvirta", "HCI scientific identity")
new_edge("Berkel", "HCI scientific identity")

new_node("Klemmer", methodcolor)
new_edge("HCI scientific identity", "Klemmer")

new_node("Park", artifactcolor)
new_edge("HCI scientific identity", "Park")
new_node_topical("Generative agents")
new_edge("Park", "Generative agents")
new_node("Assignment 1", assignmentcolor)
new_edge("Generative agents", "Assignment 1")

new_node("Ishii", artifactcolor)
new_edge("HCI scientific identity", "Ishii")

new_node("Shneiderman", surveycolor)
new_edge("HCI scientific identity", "Shneiderman")

new_node("Knowles", surveycolor)
new_edge("HCI scientific identity", "Knowles")

new_node("Hollan", methodcolor)
new_edge("HCI scientific identity", "Hollan")

new_node("Holz", empcolor)
new_edge("HCI scientific identity", "Holz")

new_node_topical("Nudging")
for p in ["Klemmer", "Shneiderman", "Knowles", "Park"]:
    new_edge(p, "Nudging")

new_node("Pohl", theocolor)
new_edge("Nudging", "Pohl")
new_node_topical("Creativity")
new_edge("Shneiderman", "Creativity")

new_node("Tyack", surveycolor)
new_edge("Creativity", "Tyack")
new_node_topical("Self-determination theory")
new_edge("Tyack", "Self-determination theory")

mindmap.write_jpg("mmweek2.jpg")
##os.startfile("mmweek2.jpg")

new_node("Rogers", surveycolor)
new_edge("HCI scientific identity", "Rogers")
new_edge("Rogers", "Assignment 1")

new_node("Bargas-Avila", surveycolor)
new_edge("HCI scientific identity", "Bargas-Avila")
new_node_topical("Emotions, enjoyment and aesthetics")
new_edge("Bargas-Avila", "Emotions, enjoyment and aesthetics")
new_node_topical("Context of use and anticipated use")
new_edge("Bargas-Avila", "Context of use and anticipated use")

new_node("Clark", methodcolor)
new_edge("Clark", "Assignment 1")
new_node("Cooper", methodcolor)
new_edge("Cooper", "Assignment 1")

new_node("PRISMA", artifactcolor)
new_edge("HCI scientific identity", "PRISMA")
new_edge("PRISMA", "Assignment 1")

new_node("Rasmussen", surveycolor)

new_edge_invis("Assignment 1", "Rasmussen")
new_node_topical("Shape changing")
new_edge("Rasmussen", "Shape changing")

mindmap.write_jpg("mmweek3.jpg")
##os.startfile("mmweek3.jpg")

new_node("Kim", artifactcolor)
new_edge("Emotions, enjoyment and aesthetics", "Kim")
new_edge("Context of use and anticipated use", "Kim")

new_node("Birk", empcolor)
new_edge("Emotions, enjoyment and aesthetics", "Birk")

new_node("McGrath", methodcolor)
new_node("Assignment 2", assignmentcolor)
new_edge("Park", "Assignment 2")
new_edge("McGrath", "Assignment 2")
new_node("Brown", opicolor)
new_edge_invis("Creativity", "Brown")
new_node_topical("Ethics")
new_edge("Brown", "Ethics")
new_node("Hornbæk", methodcolor)
new_edge("HCI scientific identity", "Hornbæk")
new_edge("Hornbæk", "Assignment 2")
new_node("Velloso", theocolor)
new_edge_invis("Ishii", "Velloso")
new_edge("HCI scientific identity", "Velloso")
new_edge("Velloso", "Assignment 2")
new_node("Wobbrock 2015", methodcolor)
new_edge_invis("Generative agents", "Wobbrock 2015")
new_edge("Wobbrock 2015", "Assignment 2")

mindmap.write_jpg("mmweek4.jpg")
##os.startfile("mmweek4.jpg")

new_node("Wester", empcolor)
new_edge("Generative agents", "Wester")
new_edge("Wester", "Assignment 2")
new_node("Putkonen", empcolor)
new_edge_invis("Wobbrock 2015", "Putkonen")
new_node_topical("Visual")
new_edge("Putkonen", "Visual")
mindmap.write_jpg("mmweek5.jpg")
##os.startfile("mmweek5.jpg")

new_node("Hartmann", artifactcolor)
new_edge_invis("Assignment 2", "Hartmann")
new_node("Assignment 3", "red")
new_node_topical("Prototype")
new_edge("Hartmann", "Prototype")
new_edge("Generative agents", "Assignment 3")

new_node("Ashbrook", artifactcolor)
new_edge_invis("Assignment 2", "Ashbrook")
new_edge("Ashbrook", "Prototype")
new_node("Chintalapati", artifactcolor)
new_edge_invis("Assignment 2", "Chintalapati")
new_node_topical("Dataset")
new_edge("Chintalapati", "Dataset")
new_node("Reinecke", surveycolor)
new_edge_invis("Assignment 2", "Reinecke")
new_edge("Reinecke", "Dataset")
new_edge("Reinecke", "Visual")
new_node("Savage", artifactcolor)
new_edge_invis("Assignment 2", "Savage")
new_edge("Savage", "Dataset")
new_node("Buxton", opicolor)
new_edge_invis("Assignment 2", "Buxton")
new_edge("Buxton", "Prototype")
new_node("Houde", artifactcolor)
new_edge_invis("Assignment 2", "Houde")
new_edge("Houde", "Prototype")
new_node("Olsen", artifactcolor)
new_edge_invis("Assignment 2", "Olsen")
new_edge("Olsen", "Assignment 3")
new_node_topical("Evaluation")
new_edge("Olsen", "Evaluation")
new_node("Myers", theocolor)
new_edge_invis("Assignment 2", "Myers")
new_edge("Myers", "Assignment 3")
new_node("Ledo", methodcolor)
new_edge_invis("Assignment 2", "Ledo")
new_edge("Ledo", "Evaluation")
new_edge("Ledo", "Assignment 3")
new_node("Antoine", artifactcolor)
new_edge_invis("Assignment 2", "Antoine")
new_edge("Prototype", "Assignment 3")
new_edge("Dataset", "Assignment 3")
new_edge("Evaluation", "Assignment 3")
mindmap.write_jpg("mmweek6.jpg")
##os.startfile("mmweek6.jpg")

print(len(list(nodes.keys() )))

print("Now building CHI32-mind map")

new_node_topical("Understand how AI assists humans")
new_edge("Park", "Understand how AI assists humans")
new_node_chi("Hyeji Kim")
new_edge("Hyeji Kim", "Understand how AI assists humans")
new_node_chi("Ho")

new_edge("Ho", "Understand how AI assists humans")
new_node_chi("Xiao")
new_edge("Xiao", "Understand how AI assists humans")
new_node_chi("Cunningham")
new_edge("Cunningham", "Understand how AI assists humans")
new_node_chi("Schoembs")
new_edge("Schoembs", "Understand how AI assists humans")
new_node_chi("Bird")
new_edge("Bird", "Understand how AI assists humans")
new_node_chi("Schmude")
new_edge("Schmude", "Understand how AI assists humans")
new_node_chi("Danry")
new_edge("Danry", "Understand how AI assists humans")
new_node_chi("Harden")
new_edge("Harden", "Understand how AI assists humans")
new_node_chi("Bucinca")
new_edge("Bucinca", "Understand how AI assists humans")
new_node_chi("Carmichael")
new_edge("Carmichael", "Understand how AI assists humans")
new_node_chi("Freire")
new_edge("Freire", "Understand how AI assists humans")
new_node_chi("Arakawa")
new_edge("Arakawa", "Understand how AI assists humans")
new_edge("Hyeji Kim", "Ethics")
new_edge("Bird", "Creativity")
new_edge("Ho", "Prototype")
new_node_topical("Explainability")
new_edge("Schmude", "Explainability")
new_edge("Danry", "Explainability")
new_edge("Schmude", "Assignment 3")
new_edge("Arakawa", "Nudging")

new_node_topical("Understand how AI assists human-human-interaction")
new_node_chi("Brenna Li")
new_edge("Brenna Li", "Understand how AI assists human-human-interaction")
new_node_chi("Pereira")
new_edge("Pereira", "Understand how AI assists human-human-interaction")
new_edge("Hyeji Kim", "Understand how AI assists human-human-interaction")
new_edge("Ho", "Understand how AI assists human-human-interaction")

new_node_chi("Suzuki")
new_edge("Suzuki", "Context of use and anticipated use")

new_node_topical("Trust")
new_edge("Pohl", "Trust")
new_node_chi("Tae Soo Kim")
new_edge("Tae Soo Kim", "Trust")
new_node_chi("Ashktorab")
new_edge("Ashktorab", "Trust")
new_node_chi("Bansal")
new_edge("Bansal", "Trust")
new_node_chi("Chang")
new_edge("Chang", "Trust")
new_node_chi("Chamorro")
new_edge("Chamorro", "Trust")

new_edge("Explainability", "Trust")
new_node_chi("Sunnie Kim")
new_edge("Sunnie Kim", "Explainability")
new_node_chi("Yakura")
new_edge("Yakura", "Explainability")

new_node_chi("Lee")
new_edge("Lee", "Context of use and anticipated use")
new_edge("Lee", "Assignment 3")

new_node_chi("Muller")
new_edge("Muller", "HCI scientific identity")

new_node_chi("Hyanghee Park")
new_edge("Hyanghee Park", "Nudging")
new_edge("Hyanghee Park", "Emotions, enjoyment and aesthetics")
new_node_chi("Atabey")
new_edge("Atabey", "Ethics")
new_node_chi("Ge Wang")
new_edge("Ge Wang", "Ethics")
new_node_chi("Bhattacarya")
new_edge("Bhattacarya", "Explainability")
new_edge("Bhattacarya", "Visual")
new_node_chi("Liu")
new_edge("Liu", "Visual")
new_edge("Liu", "Creativity")
new_node_chi("Kuang")
new_edge("Kuang", "Evaluation")
new_edge("Kuang", "Assignment 3")
new_node_chi("Lehmann")
new_edge("Lehmann", "Nudging")
new_node_chi("Laschke")
new_edge("Laschke", "Ethics")
new_node_chi("Roemmich")
new_edge("Roemmich", "Emotions, enjoyment and aesthetics")


mindmap.write_jpg("mmchi31.jpg")
os.startfile("mmchi31.jpg")



















