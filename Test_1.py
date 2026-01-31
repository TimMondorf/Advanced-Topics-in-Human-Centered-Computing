import pydot
import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'

##First define a graph based purely on which articles refer to which

coloros = ["salmon",
    "lightblue",
    "lightgreen",
    "aquamarine4",
    "blue2",
    "blueviolet",
    "brown",
    "burlywood",
    "cadetblue",
    "chartreuse",
    "chocolate",
    "cornflowerblue",
    "darkgreen",
    "darkslategrey4",
    "deeppink2"]

coloros.reverse()

print("Themes are boxes and articles are circles")
themecolor = "white"
print(f"Colorcode of themes is {themecolor}")
metacolor = coloros.pop()
print(f"Colorcode of Meta papers is {metacolor}")
artcolor = coloros.pop()
print(f"Colorcode of articles is {artcolor}")
print("Assigning color codes to attributes")
empcolor = coloros.pop()
print(f"Empirical color is {empcolor}")
artifactcolor = coloros.pop()
print(f"Artifact color is {artifactcolor}")
methodcolor = coloros.pop()
print(f"Methodological color is {methodcolor}")
theocolor = coloros.pop()
print(f"Theoretical color is {theocolor}")
datacolor = coloros.pop()
print(f"Dataset color is {datacolor}")
surveycolor = coloros.pop()
print(f"Survey color is {surveycolor}")
opinioncolor = coloros.pop()
print(f"Opinion color is {opinioncolor}")
nocolor = coloros.pop()
print(f"No contribution color is {nocolor}")

refs = pydot.Dot(graph_type="digraph", rankdir="UD")
refs.set_splines("curved")
refs.set_overlap("false")   # reduces edge crossings
refs.set_nodesep("0.6")
refs.set_ranksep("0.8")

w1_articles = dict()
for a in ["Wobbrock",
    "Oulasvirta",
    "Berkel",
    "Klemmer",
    "Park",
    "Shneiderman",
    "Knowles",
    "Hollan",
    "Holz",
    "Ishii"]:
    nodo = pydot.Node(a, style="filled", fillcolor=artcolor)
    refs.add_node(nodo)
    w1_articles[a] = nodo

edge = pydot.Edge(w1_articles["Oulasvirta"], w1_articles["Wobbrock"]) ##Wobbrock refers to Oulasvirta
refs.add_edge(edge)

edge = pydot.Edge(w1_articles["Ishii"], w1_articles["Wobbrock"]) ##Wobbrock refers to Ishii
refs.add_edge(edge)

edge = pydot.Edge(w1_articles["Ishii"], w1_articles["Oulasvirta"]) ##Oulasvirta refers to Ishii
refs.add_edge(edge)

edge = pydot.Edge(w1_articles["Wobbrock"], w1_articles["Berkel"]) ##Berkel refers to Wobbrock and even acknowledges them in the tex
refs.add_edge(edge)

edge = pydot.Edge(w1_articles["Hollan"], w1_articles["Klemmer"]) ##Klemmer refers to Hollan
refs.add_edge(edge)

refs.write_jpg("refs.jpg")

mmcur = pydot.Dot(graph_type="digraph", rankdir="UD")
mmcur.set_splines("curved")
mmcur.set_overlap("false")   # reduces edge crossings
mmcur.set_nodesep("0.6")
mmcur.set_ranksep("0.8")

themes = dict()
for t in ["Human-centered Computing",
    "Meta papers",
    "WHAT",
    "WHY",
    "HOW"]:
    nodo = pydot.Node(t, shape="box", style="filled", fillcolor="white")
    mmcur.add_node(nodo)
    themes[t] = nodo

for k in list(w1_articles.keys()):
    mmcur.add_node(w1_articles[k])

edge = pydot.Edge(themes["Human-centered Computing"], themes["Meta papers"])
mmcur.add_edge(edge)

for arr in ["Wobbrock",
    "Oulasvirta",
    "Berkel"]:
    edge = pydot.Edge(themes["Meta papers"], arr)
    mmcur.add_edge(edge)

w1_articles["Wobbrock"].set_fillcolor(theocolor) ##Wobbrock provides a theoretical contribution
edge = pydot.Edge(w1_articles["Wobbrock"], themes["HOW"]) ##Wobbrock relates primarily to how
mmcur.add_edge(edge)

w1_articles["Oulasvirta"].set_fillcolor(theocolor) ##Oulasvirta provides a theoretical contribution
edge = pydot.Edge(w1_articles["Oulasvirta"], themes["WHAT"]) ##Oulasvirta relates to what
mmcur.add_edge(edge)

w1_articles["Berkel"].set_fillcolor(theocolor) ##Berkel is a theoretical contribution
edge = pydot.Edge(w1_articles["Berkel"], themes["WHY"]) ##Berkel relates to why
mmcur.add_edge(edge)

##Berkel also defines 7 implications that I define as additional themes

for t in ["COMMUNITY",
    "DESIGN",
    "PRACTICE",
    "POLICY",
    "SOCIETY"]:
    nodo = pydot.Node(t, shape="box", style="filled", fillcolor = "white")
    themes[t] = nodo
    mmcur.add_node(nodo)

for art in ["Wobbrock", "Oulasvirta", "Berkel"]:
    edge = pydot.Edge(w1_articles[art], themes["COMMUNITY"])
    mmcur.add_edge(edge)
    
w1_articles["Klemmer"].set_fillcolor(methodcolor)
edge = pydot.Edge(themes["HOW"], w1_articles["Klemmer"])
mmcur.add_edge(edge)
edge = pydot.Edge(w1_articles["Klemmer"], themes["DESIGN"])
mmcur.add_edge(edge)

w1_articles["Park"].set_fillcolor(artifactcolor)
edge = pydot.Edge(themes["WHAT"], w1_articles["Park"])
mmcur.add_edge(edge)
edge = pydot.Edge(w1_articles["Park"], themes["DESIGN"])
mmcur.add_edge(edge)
edge = pydot.Edge(w1_articles["Park"], themes["PRACTICE"])
mmcur.add_edge(edge)

w1_articles["Ishii"].set_fillcolor(artifactcolor)
edge = pydot.Edge(themes["HOW"], w1_articles["Ishii"])
mmcur.add_edge(edge)
edge = pydot.Edge(w1_articles["Ishii"], themes["DESIGN"])
mmcur.add_edge(edge)
edge = pydot.Edge(w1_articles["Ishii"], themes["PRACTICE"])
mmcur.add_edge(edge)

w1_articles["Shneiderman"].set_fillcolor(surveycolor)
edge = pydot.Edge(themes["WHAT"], w1_articles["Shneiderman"])
mmcur.add_edge(edge)
edge = pydot.Edge(themes["WHY"], w1_articles["Shneiderman"])
mmcur.add_edge(edge)
edge = pydot.Edge(w1_articles["Shneiderman"], themes["SOCIETY"])
mmcur.add_edge(edge)

w1_articles["Knowles"].set_fillcolor(surveycolor)
edge = pydot.Edge(themes["WHAT"], w1_articles["Knowles"])
mmcur.add_edge(edge)
edge = pydot.Edge(w1_articles["Knowles"], themes["SOCIETY"])
mmcur.add_edge(edge)
edge = pydot.Edge(w1_articles["Knowles"], themes["COMMUNITY"])
mmcur.add_edge(edge)

w1_articles["Hollan"].set_fillcolor(methodcolor)
edge = pydot.Edge(themes["HOW"], w1_articles["Hollan"])
mmcur.add_edge(edge)
edge = pydot.Edge(w1_articles["Hollan"], themes["DESIGN"])
mmcur.add_edge(edge)
edge = pydot.Edge(w1_articles["Hollan"], themes["PRACTICE"])
mmcur.add_edge(edge)

w1_articles["Holz"].set_fillcolor(empcolor)
edge = pydot.Edge(themes["HOW"], w1_articles["Holz"])
mmcur.add_edge(edge)
edge = pydot.Edge(w1_articles["Holz"], themes["DESIGN"])
mmcur.add_edge(edge)
edge = pydot.Edge(w1_articles["Holz"], themes["PRACTICE"])

print()

mmcur.write_jpg("mmcur.jpg")
os.startfile("mmcur.jpg")