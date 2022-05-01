scorelist = [37.21, 37.21, 37.2, 41.0, 39.0]
Result = [['Harry', 37.21],
 ['Berry', 37.21],
 ['Tina', 37.2],
 ['Akriti', 41.0],
 ['Harsh', 39.0]]
b=sorted(list(set(scorelist)))[1] 

for a,c in sorted(Result):
    if c==b:
        print(a)