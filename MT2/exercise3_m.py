def total_distance(dist,cities):
    resul = 0
    for i in range(len(cities)-1):
        c = (cities[i],cities[i+1])
        d = (cities[i+1],cities[i]) 
        
        if not c in dist and not d in dist:
            return -1

        elif c in dist:
            resul += dist[c]
        else:
            
            resul += dist[d]
    
    return resul

    

#print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Coimbra','Viseu','Coimbra']))
#print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Lisboa', 'Coimbra']))
