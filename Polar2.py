import matplotlib.pyplot as plt
import numpy as np
import os

tim_generator = np.random.default_rng(123456)

# Fixing random state for reproducibility

# Compute areas and colors

fig = plt.figure()
ax = fig.add_subplot(projection='polar')

class Arr:
    def __init__(self, namo, batch, category, chi=False):
        self.namo = namo
        self.batch = batch
        self.category = category
        self.theta = None
        self.r = None
        self.chi = chi

category_list = ["Field experiment",
    "Experimental simulation",
    "Literature survey",
    "Interview survey",
    "Formal theory",
    "Computer simulation",
    "Field study"]

arrs = []
arrs.append(Arr("Rapp", "ha2", "Literature survey"))
arrs.append(Arr("Chaves", "ha2", "Literature survey"))
arrs.append(Arr("Delgado", "ha2", "Literature survey"))
arrs.append(Arr("Brynjolfsson", "ha2", "Interview survey"))
arrs.append(Arr("Chen", "ha2", "Field experiment"))
arrs.append(Arr("DeVito", "ha2", "Field study", True))
arrs.append(Arr("Duarte", "ha2", "Field experiment"))
arrs.append(Arr("Forlizzi", "ha2", "Formal theory"))
arrs.append(Arr("Al Haque", "ha2", "Interview survey"))
arrs.append(Arr("Khadpe", "ha2", "Experimental simulation"))
arrs.append(Arr("Muresan", "ha2", "Experimental simulation", True))
arrs.append(Arr("Silva", "ha2", "Interview survey"))
arrs.append(Arr("Skjuve", "ha2", "Experimental simulation"))
arrs.append(Arr("Storey", "ha2", "Formal theory"))
arrs.append(Arr("Ziegler", "ha2", "Field study"))

arrs.append(Arr("Park", "ha1", "Computer simulation"))
arrs.append(Arr("Bill Lin", "ha1", "Computer simulation"))
arrs.append(Arr("He", "ha1", "Interview survey"))
arrs.append(Arr("Hutson", "ha1", "Formal theory"))
arrs.append(Arr("Stark", "ha1", "Formal theory"))
arrs.append(Arr("Jaber", "ha1", "Experimental simulation"))
arrs.append(Arr("Xu", "ha1", "Experimental simulation", True))
arrs.append(Arr("Zheng", "ha1", "Field experiment", True))
arrs.append(Arr("Naik", "ha1", "Interview survey", True))
arrs.append(Arr("Adornetto", "ha1", "Formal theory"))
arrs.append(Arr("Guimares", "ha1", "Field experiment"))
arrs.append(Arr("Zhihuai Lin", "ha1", "Field study"))

np.random.shuffle(arrs)

def plotto(arr):
    if arr.batch == "ha1":
        colo = "lightgreen"
    elif arr.batch == "ha2":
        colo = "darkblue"
    if arr.chi:
        ax.scatter(arr.theta, arr.r, c=colo, s=200, marker="*")
    else:
        ax.scatter(arr.theta, arr.r, c=colo)
    ax.text(arr.theta, arr.r, arr.namo)

def count_category(category, arrs):
    n = 0
    for arr in arrs:
        if arr.category == category:
            n += 1
    next_n = 1
    for arr in arrs:
        if arr.category == category:
            arr.r = next_n
            next_n -= 1/n 

for arr in arrs:
    cat = category_list.index(arr.category)
    arr.theta = 2*np.pi/len(category_list) * cat  
    if arr.category == "Field experiment":
        arr.theta += 2*np.pi/len(category_list) * 0.25

for category in category_list:
    count_category(category, arrs)

for arr in arrs:
    plotto(arr)

for cat in range(len(category_list)):
    theta = cat*2*np.pi/len(category_list)
    ax.text(theta, 1.2, category_list[cat])

for arr in arrs:
    if arr.category == "Experimental simulation" or arr.category == "Field experiment":
        print(arr.namo)

plt.savefig("polar.jpg")
os.startfile("polar.jpg")