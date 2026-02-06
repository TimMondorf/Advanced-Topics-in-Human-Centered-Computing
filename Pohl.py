import pydot
import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'

mindmap = pydot.Dot(graph_type="digraph", rankdir="UD")
refs.set_splines("curved")
refs.set_overlap("false")   # reduces edge crossings
refs.set_nodesep("0.6")
refs.set_ranksep("0.8")

nodes = dict()

articles = ["POHL subtle",
    "Klemmer human body",
    "Wobbrock 2011 disabilities",
    "Ishii combine physical and virtual world",
    "Park generative agents",
    "Shneiderman creativity",
    "Knowles sustainability",
    "Hollan: face-to-face real-time interaction is not the only goal of HCI",
    "Holz touch devices"]

flowdowns = ["Deception",
    "Do less",
    "Nudging"]

links = ["Visibility (pictograms)",
    "Thinking through doing (lane assist)",
    "Eye tracker as input device",
    "Ambient display media",
    "Invitation spreads autonomously",
    "Inspirationalist view of creativity",
    "Subtly encourage self-transcendent values",
    "Humans are subtle, computers are not",
    "Smaller touch devices"
]

for a in articles:
    nodo = pydot.Node(a, shape="box", style="filled", fillcolor="white")
    mindmap.add_node(nodo)
    nodes[a] = nodo

for a in flowdowns+links:
    nodo = pydot.Node(a)
    mindmap.add_node(nodo)
    nodes[a] = nodo

for b in flowdowns:
    edge = pydot.Edge(nodes["Pohl subtle"], nodes[b])
    mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Do less"], nodes["Visibility (pictograms)"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Visibility (pictograms)"], nodes["Klemmer human body"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Nudging"], nodes["Thinking through doing (lane assist)"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Do less"], nodes["Ambient display media"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Ambient display media"], nodes["Ishii combine physical and virtual world"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Do less"], nodes["Eye tracker as input device"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Eye tracker as input device"], nodes["Wobbrock 2011 disabilities"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Nudging"], Nodes["Invitation spreads autonomously"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Invitation spreads autonomously"], nodes["Park generative agents"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Nudging"], nodes["Humans are subtle, computers are not"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Humans are subtle, computers are not"], nodes["Park generative agents"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Nudging"], nodes["Inspirationalist view of creativity"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Inspirationalist view of creativity"], nodes["Shneiderman creativity"]),
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Nudging"], nodes["Subtly encourage self-transcendent values"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Subtly encourage self-transcendent values"], nodes["Knowles sustainability"]),
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Pohl subtle"], nodes["Humans are subtle, computers are not"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Do less"], nodes["Smaller touch devices"])
mindmap.add_edge(edge)

edge = pydot.Edge(nodes["Smaller touch devices"], nodes["Holz touch devices"])
mindmap.add_edge(edge)

mindmap.write_jpg("mindmap.jpg")

os.startfile("mindmap.jpg")
