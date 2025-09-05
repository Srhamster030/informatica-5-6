independence_stages = ["inicio", "organización", "resistencia", "consumación"]
print(independence_stages[0])
print(len(independence_stages))

#list methods
leaders = []
leaders.append("Miguel Hidalgo")
leaders.append("Vicente Guerrero")
#leaders.extend(independence_stages) //Mix lists together
leaders.insert(1, "José María Morelos y Pavón")
#leaders.remove("Vicente Guerrero") //to delete specific first match of specific items 
leaders.append(input("Type a leader: "))
#leaders.pop(1) //the same as remove but funciona with index instead of specific.
#leaders.clear()//para quitar todos los argumentos de la lista.
print(leaders.index("Miguel Hidalgo"))# para contar el número exacto donde está.
print(leaders.count("Vicente Guerrero"))
#leaders.sort() //change the order of the elements
#leaders.reverse() //puts the elements in the contrary order... -_-
new_leader = leaders.copy()
    
print(leaders)
print(new_leader)
