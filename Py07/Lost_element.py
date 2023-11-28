def lost_element(s1,s2):
    s1= list(s1)
    s2= list(s2)
    s1.sort()
    s2.sort()
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return s1[i]
    return s2[-1]

print(lost_element({2,3,4,5},{2,3,4,5,6}))