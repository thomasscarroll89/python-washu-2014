"""Data Structures
Working with Graphs/Networks"""

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

# Ring Network
ring = {} # empty graph 

n = 5 # number of nodes 

# Add in edges
for i in range(n):
  ring = makeLink(ring, i, (i+1)%n)

# How many nodes?
print len(ring)

# How many edges?
print sum([len(ring[node]) for node in ring.keys()])/2 


# Grid Network
# TODO: create a square graph with 256 nodes and count the edges 
# TODO: define a function countEdges

square = {}
n = 16
for i in range(1, (n**2)+1):
	if (i%n)!=0:
		square = makeLink(square, i, i+1)
	if ((i+n)%(n))!=1:
		square = makeLink(square, i, i-1)
	if (i not in range(n**2 - n, n**2+1)):
		square = makeLink(square, i, i+n)
	if (i not in range(1, n+1)): 
		square = makeLink(square, i, i-n)

#print square
	
def countEdges(dictionary):
	output = []
	for i in dictionary.keys():
		connected_nodes = dictionary[i].keys()
		for j in connected_nodes:
			if ((i, j) not in output):
				output.append((i, j))
				output.append((j, i))
	return (len(output)/2)

#print countEdges(square)
	
# Social Network
class Actor(object):
  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return self.name 

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DiNero")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day

# How many nodes in movies?
def countNodes(dictionary):
	return len(dictionary.keys())

print countNodes(movies)
# How many edges in movies?
print countEdges(movies)

def tour(graph, nodes):
  for i in range(len(nodes)):
    node = nodes[i] 
    if node in graph.keys():
      print node 
    else:
      print "Node not found!"
      break 
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass 
        else:
          print "Can't get there from here!"
          break 

# TODO: find an Eulerian tour of the movie network and check it 
movie_tour = [ms, rd, dh, ss, jr, dh, kb, ms, ah, jr, kb] 
tour(movies, movie_tour)


def findPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = findPath(graph, node, end, path)
                if newpath: return newpath
        return None

print findPath(movies, jr, ms)
print type(findPath(movies, ms, ss))

# TODO: implement findShortestPath()
def findShortestPath(graph, start, end, path=[]):
	if path == []:
		initial_path = findPath(graph=graph, start=start, end=end, path=[])
		length_initial_path = len(initial_path)
	new_path = path + [start]
	# if type(start)=="Actor":
		# potential_moves = graph[start] #we want potential moves to be a function of whichever node we are currently on, which is indexed by the last element of start
	# else:
	potential_moves = graph[start[-1]]

	if (end in potential_moves and (length_initial_path > (len(new_path) + 1))): #IF we can move to the end node in the next move
		new_path.append(end)
		return new_path
	for next_move in potential_moves:
		new_path_temp = new_path.append(next_move)
		if len(new_path_temp) >= length_initial_path:
			break
		else:
			findShortestPath(graph=graph, start=new_path_temp, end=end, path=new_path_temp)

print findShortestPath(movies, ms, ss)

# TODO: implement findAllPaths() to find all paths between two nodes
# allPaths = findAllPaths(movies, jr, ms)
# for path in allPaths:
#   print path