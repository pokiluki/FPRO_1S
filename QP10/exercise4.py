def union_with(combine, dict1:dict, dict2:dict): return {**{x: combine(dict1[x], dict2[x]) for x in dict1 if dict2.get(x) != None}, **{x: dict1[x] for x in dict1 if x not in dict2}, **{x:dict2[x] for x in dict2 if x not in dict1}}

