
# We use Google's Constraint Programming solver to solve each puzzle in a few seconds.
# Find it at https://developers.google.com/optimization/cp/
from ortools.constraint_solver import pywrapcp

Width = 11
Height = 8

# Map 1 data
Islands = ((0,2),(1,4),(1,7),(2,0),(2,1),(2,3),(2,5),(2,6),(3,0),(3,2),(3,5),(3,6),(4,0),(4,1),(4,4),(4,6),(4,7),(5,1),(5,3),(5,5),(5,7),(6,0),(6,2),(6,4),(6,6),(7,0),(7,2),(7,3),(7,5),(7,7),(8,1),(8,3),(8,4),(9,0),(9,2),(9,4),(9,6),(9,7),(10,0),(10,1),(10,3),(10,5),(10,6))
Signs = {(0,5):(0,1,15,0),(1,3):(0,0,0,0),(4,2):(15,5,9,6),(5,0):(10,0,11,9),(7,1):(18,3,4,9),(8,6):(0,11,3,11),(10,4):(4,9,0,15)}

# Preliminaries:

## Find bridgeable neighbors of every island
Neighbors = {}
for Island in Islands:
  Neighbors[Island] = []
  x,y = Island
  for x1,x2,y1,y2,xStep,yStep in ((x+1,Width,y,y+1,1,1),(x-1,-1,y,y+1,-1,1),(x,x+1,y+1,Height,1,1),(x,x+1,y-1,-1,1,-1)):
    Done = False
    for xx in range(x1,x2,xStep):
      for yy in range(y1,y2,yStep):
        if (xx,yy) in Islands:
          if not Done:
            Neighbors[Island].append((xx,yy))
            Done = True
        elif (xx,yy) in Signs:
          Done = True

## Find 4-tuples of islands, the first above and neighboring the second,  
## the third left of and neighboring the fourth, such that bridges would cross.

CrossThreats = []
for (x1,y1) in Islands:
  for (x2,y2) in Islands:
    for (x3,y3) in Islands:
      for (x4,y4) in Islands:
        if y2>=y1 or not x1==x2 or x3>=x4 or not y3==y4 or x1<=x3 or x1>=x4 or y3>=y1 or y3<=y2:
          continue
        if (x2,y2) in Neighbors[(x1,y1)] and (x4,y4) in Neighbors[(x3,y3)]:
          CrossThreats.append(((x1,y1),(x2,y2),(x3,y3),(x4,y4)))

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

def FindAddends(x1,x2,y1,y2,xStep,yStep,Tot):
  Addends = []
  xx,yy = x1,y1
  while not (xx==x2 or yy==y2):
    if (xx,yy) in Signs:
      break
    if (xx,yy) in Islands:
      Addends.append(Value[(xx,yy)])
    xx += xStep
    yy += yStep
  solver.Add(sum(Addends) == Tot)
  solver.Add(solver.AllDifferent(Addends))

for Sign in Signs:
  x,y = Sign
  N,S,E,W = Signs[Sign]
  if not N == 0:
    FindAddends(x,x+1,y+1,Height,0,1,N)
  if not S == 0:
    FindAddends(x,x+1,y-1,-1,0,-1,S)
  if not E == 0:
    FindAddends(x+1,Width,y,y+1,1,0,E)
  if not W == 0:
    FindAddends(x-1,-1,y,y+1,-1,0,W)

## Bridges do not cross

for Island1,Island2,Island3,Island4 in CrossThreats:
  solver.Add(BridgesBetween[(Island2,Island1)]*BridgesBetween[(Island3,Island4)] == 0)

# Create the "decision builder"

db = solver.Phase(Vars, solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)

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

# Call the solver and display the solution.

if solver.Solve(db):
  while solver.NextSolution():
    if Connected(BridgesBetween):
      print("Solution:")
      for Island in Islands:
        print("Island", Island, "=",Value[Island].Value())
      for B in BridgesBetween:
        if not BridgesBetween[B].Value() == 0:
          print(B,BridgesBetween[B].Value(), "bridges")
      break
