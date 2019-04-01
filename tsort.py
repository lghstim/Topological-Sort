from sys import argv
from pythonds import *

# dictionary format:
''' {'v1': [0, 'v2'], 'v2': [1, 'v3'], 'v3': [1, 'v5', 'v4'], 'v5': [1, 'v6'], 'v4': [1], 'v6': [1]}'''
# dictionary[vertex][0] is the in-degree of the vertex which is the key
# dictionary[vertex][1:] is the vertices adjacent to dictionary[vertex] 
def tsort(vertices):
   dictionary = {}
   order_list = []
   string = '' 
   if len(vertices) == 0:
       raise ValueError("input contains no edges")
   if len(vertices) % 2 != 0:
       raise ValueError("input contains an odd number of tokens")

   # creating dictionary.
   for index in range(0, len(vertices), 2):
      if vertices[index] not in order_list:
         order_list.append(vertices[index])
      if vertices[index] in dictionary:
         # add vertex2 adj. to vertex1 to the list
         dictionary[vertices[index]].append(vertices[index+1]) # append vertex2 to end
      else: # vertices[index] not in dictionary.
         # if it is the first time we see vertex in graph, set its initial in-degree to 0.
         dictionary[vertices[index]] = [0, vertices[index + 1]] # form: [in-degree, ..., adj. vertex]
      # add 1 to in-degree of adj. vertex
      if vertices[index + 1] not in dictionary: # vertex2 dne in dictionary yet.
         dictionary[vertices[index + 1]] = [1] # add this vertex & in-deg. into adj. list
      else: # vertex2 exists
         dictionary[vertices[index + 1]][0] += 1

   stack = Stack()
   for vertex in order_list: # traverse vertices in order they were seen.
      if dictionary[vertex][0] == 0: # only push those with in-degree of 0. 
         stack.push(vertex)

   while stack.size() != 0:
      vertex = stack.pop()
      string += str(vertex) + '\n'
      adj_list = dictionary[vertex][1:]
      for u in adj_list: # processed in order edges were added.
         dictionary[u][0] -= 1
         if dictionary[u][0] == 0:
            stack.push(u)

   # in an acyclic graph, a vertex isn't visited more than once.
   if len(string.split()) != len(dictionary):
      raise ValueError("input contains a cycle")

   return string.strip()

def main():
   ''' Entry point for tsort utility, allowing user to specify a file containing the edges of DAG'''
   if len(argv) != 2:
      print("Usage: python3 tsort.py <filename>")
      exit()
   try:
      f = open(argv[1], 'r')
   except FileNotFoundError as e:
      print(argv[1], 'could not be found or opened')
      exit()

   vertices = []
   for line in f:
      vertices += line.split()
 
   try:
      result = tsort(vertices)
      print(result)
   except Exception as e:
      print(e)

#main()
