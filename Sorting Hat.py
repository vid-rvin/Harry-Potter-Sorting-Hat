print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
ans1 = int(input("answer:"))

if ans1 == 1:
  g = 1
  r = 1
  h = 0
  s = 0

elif ans1 == 2:
  h = 1
  s = 1
  g = 0
  r = 0

else:
  print("wrong input")
  exit()

print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
ans2 = int(input("answer:"))

if ans2 == 1:
    h = h + 2
  
elif ans2 == 2:
    s = s + 2
  
elif ans2 == 3:
    r = r + 2
  
elif ans2 == 4:
    g = g + 2
  
else:
    print("wrong input")
    exit()


print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
ans3 = int(input("answer:"))
  
if ans3 == 1:
    s = s + 4
  
elif ans3 == 2:
    h = h + 4
  
elif ans3 == 3:
    r = r + 4
  
elif ans3 == 4:
    g = g + 4
  
else:
    print("wrong input")
    exit()

print(f"Gryffindor has {g} points")
print(f"Ravenclaw has {r} points")
print(f"Slytherin has {s} points")
print(f"Hufflepuff has {h} points")

if g > r and g > s and g > h:
  print("Gryffindor has the most points!")

elif r > g and r > s and r > h:
  print("Ravenclaw has the most points!")

elif s > g and s > r and s > h:
  print("Slytherin has the most poins!")

elif h > s and h > g and h > r:
  print("Hufflepuff has the most points!")