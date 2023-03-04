List1=["How I Met Your Mother","Friends","Silicon Valley"]
List2=["Family Guy","South Park","Rick and Morty"]
List3=["Breaking Bad","Game of Thrones","The Wire"]
AllList=[List1,List2,List3]
for i in AllList:
    for j in i:
        print("The title",j,"is",len(j),"characters long")
