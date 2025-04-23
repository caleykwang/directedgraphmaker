import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

class GraphMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("DFA/NFA Graph Maker")

        self.G = nx.DiGraph()

        self.node_entry = tk.Entry(root, width=10)
        self.node_entry.grid(row=0, column=1, padx=10, pady=10)
        self.add_node_button = tk.Button(root, text="Add Node", command=self.add_node)
        self.add_node_button.grid(row=0, column=2, padx=10, pady=10)

        self.edge_entry = tk.Entry(root, width=10)
        self.edge_entry.grid(row=1, column=1, padx=10, pady=10)
        self.edge_label_entry = tk.Entry(root, width=10)
        self.edge_label_entry.grid(row=1, column=2, padx=10, pady=10)
        self.add_edge_button = tk.Button(root, text="Add Edge", command=self.add_edge)
        self.add_edge_button.grid(row=1, column=3, padx=10, pady=10)

        self.draw_button = tk.Button(root, text="Draw Graph", command=self.draw_graph)
        self.draw_button.grid(row=2, column=1, columnspan=2, pady=20)

    def add_node(self):
        node = self.node_entry.get()
        if node:
            self.G.add_node(node)
            messagebox.showinfo("Success", f"Node {node} added!")
            self.node_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a node name.")

    def add_edge(self):
        edge = self.edge_entry.get()
        label = self.edge_label_entry.get()
        if edge and label:
            source, target = edge.split('->')
            self.G.add_edge(source.strip(), target.strip(), label=label.strip())
            messagebox.showinfo("Success", f"Edge {edge} with label {label} added!")
            self.edge_entry.delete(0, tk.END)
            self.edge_label_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter edge and label.")

    def draw_graph(self):
        pos = nx.spring_layout(self.G)
        plt.figure(figsize=(6, 4))
        nx.draw(self.G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=16, font_weight='bold', arrowsize=20)
        labels = nx.get_edge_attributes(self.G, 'label')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels, font_size=14)
        plt.title("DFA/NFA Directed Graph")
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphMaker(root)
    root.mainloop()
