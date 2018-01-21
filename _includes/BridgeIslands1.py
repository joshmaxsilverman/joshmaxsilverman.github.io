
# We use Google's Constraint Programming solver to solve each puzzle in a few seconds.
# Find it at https://developers.google.com/optimization/cp/
from ortools.constraint_solver import pywrapcp

Width = 11
Height = 8

# Map 1 data
Islands = ((0,2),(1,4),(1,7),(2,0),(2,1),(2,3),(2,5),(2,6),(3,0),(3,2),(3,5),(3,6),(4,0),(4,1),(4,4),(4,6),(4,7),(5,1),(5,3),(5,5),(5,7),(6,0),(6,2),(6,4),(6,6),(7,0),(7,2),(7,3),(7,5),(7,7),(8,1),(8,3),(8,4),(9,0),(9,2),(9,4),(9,6),(9,7),(10,0),(10,1),(10,3),(10,5),(10,6))
Signs = {(0,5):(0,1,15,0),(1,3):(0,0,0,0),(4,2):(15,5,9,6),(5,0):(10,0,11,9),(7,1):(18,3,4,9),(8,6):(0,11,3,11),(10,4):(4,9,0,15)}

# Test whether the map is a connected graph.
def Connected(BridgesBetween):
  global Islands, Neighbors
  
  def Explore(Island):
    Remaining.remove(Island)
    if Remaining == []:
      return
    else:
      for Neighbor in Neighbors[Island]:
        if not Neighbor in Remaining:
          continue
        if (Island,Neighbor) in BridgesBetween:
          Pair = (Island,Neighbor)
        else:
          Pair = (Neighbor,Island)
        if BridgesBetween[Pair].Value() == 0:
          continue
        Explore(Neighbor)

  Remaining = list(Islands)
  Explore(Remaining[0])
  return (Remaining == [])

# Preliminaries:

## Find bridgeable neighbors of every island

Neighbors = {}
for Island in Islands:
  Neighbors[Island] = []
  x,y = Island
  for x1 in range(x+1,Width):
    if (x1,y) in Islands:
      Neighbors[Island].append((x1,y))
      break
    elif (x1,y) in Signs:
      break
  for x1 in range(x-1,-1,-1):
    if (x1,y) in Islands:
      Neighbors[Island].append((x1,y))
      break
    elif (x1,y) in Signs:
      break
  for y1 in range(y+1,Height):
    if (x,y1) in Islands:
      Neighbors[Island].append((x,y1))
      break
    elif (x,y1) in Signs:
      break
  for y1 in range(y-1,-1,-1):
    if (x,y1) in Islands:
      Neighbors[Island].append((x,y1))
      break
    elif (x,y1) in Signs:
      break

## Find 4-tuples of islands, the first above and neighboring the second,  
## the third left of and neighboring the fourth, such that bridges would cross.

CrossThreats = []
for Island1 in Islands:
  for Island2 in Islands:
    for Island3 in Islands:
      for Island4 in Islands:
        x1,y1 = Island1
        x2,y2 = Island2
        x3,y3 = Island3
        x4,y4 = Island4
        if y2>=y1 or not x1==x2 or x3>=x4 or not y3==y4:
          continue
        if x1<=x3 or x1>=x4 or y3>=y1 or y3<=y2:
          continue
        if Island2 in Neighbors[Island1] and Island4 in Neighbors[Island3]:
          CrossThreats.append((Island1,Island2,Island3,Island4))

# Create the solver.

solver = pywrapcp.Solver("")

# Create the variables.

Vars = []

## Island values (number of bridges)
Value = {}
for Island in Islands:
  Value[Island] = solver.IntVar(1,8,"IslandValue_"+str(Island[0])+"_"+str(Island[1]))
  Vars.append(Value[Island])

## Number of bridges between pairs of islands
BridgesBetween = {}
for Island in Islands:
  x,y = Island
  for Neighbor in Neighbors[Island]:
    x1,y1 = Neighbor
    if x<x1 or (x==x1 and y<y1):
      BridgesBetween[(Island,Neighbor)] = solver.IntVar(0,2,"BridgesBetween_"+str(x)+"_"+str(y)+"_"+str(x1)+"_"+str(y1))
      Vars.append(BridgesBetween[(Island,Neighbor)])

# Constraints

## Island value is number of bridges to neighbors.

for Island in Islands:
  Bridges = []
  for Neighbor in Neighbors[Island]:
    if (Island,Neighbor) in BridgesBetween:
      Bridges.append(BridgesBetween[(Island,Neighbor)])
    else:
      Bridges.append(BridgesBetween[(Neighbor,Island)])
  solver.Add(Value[Island] == sum(Bridges))

## Sign sums are correct, and all addends differ

for Sign in Signs:
  x,y = Sign
  N,S,E,W = Signs[Sign]
  if not N == 0:
    Addends = []
    for y1 in range(y+1,Height):
      if (x,y1) in Signs:
        break
      if (x,y1) in Islands:
        Addends.append(Value[(x,y1)])
    solver.Add(sum(Addends) == N)
    solver.Add(solver.AllDifferent(Addends))
  if not S == 0:
    Addends = []
    for y1 in range(y-1,-1,-1):
      if (x,y1) in Signs:
        break
      if (x,y1) in Islands:
        Addends.append(Value[(x,y1)])
    solver.Add(sum(Addends) == S)
    solver.Add(solver.AllDifferent(Addends))
  if not E == 0:
    Addends = []
    for x1 in range(x+1,Width):
      if (x1,y) in Signs:
        break
      if (x1,y) in Islands:
        Addends.append(Value[(x1,y)])
    solver.Add(sum(Addends) == E)
    solver.Add(solver.AllDifferent(Addends))
  if not W == 0:
    Addends = []
    for x1 in range(x-1,-1,-1):
      if (x1,y) in Signs:
        break
      if (x1,y) in Islands:
        Addends.append(Value[(x1,y)])
    solver.Add(sum(Addends) == W)
    solver.Add(solver.AllDifferent(Addends))

## Bridges do not cross

for Island1,Island2,Island3,Island4 in CrossThreats:
  solver.Add(BridgesBetween[(Island2,Island1)]*BridgesBetween[(Island3,Island4)] == 0)

# Create the "decision builder"

db = solver.Phase(Vars, solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)

# Call the solver and display the solution.

if solver.Solve(db):
  while solver.NextSolution():
    if Connected(BridgesBetween):
      print("Solution:")
      for Island in Islands:
        print("Island", Island, "=",Value[Island].Value())
      for B in BridgesBetween:
        print(B,BridgesBetween[B].Value(), "bridges")
      break
else:
  print("No solution found.")
