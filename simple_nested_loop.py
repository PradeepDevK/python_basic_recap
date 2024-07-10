for i in range(1,3):
    print(f"Week {i}")
    for j in range(1, 4):
        print(f"Day {j}")
        
for i in range(1, 6):
    for j in range(1, i):
        print('*', end="")
    print()
    
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()