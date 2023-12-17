def longest_prefix(word):
    if len(word) == 0:
        return ""
    else:
        prefix = word[0]
        for i in range(1, len(word)):
            while word[i].find(prefix) != 0:
                prefix = prefix[:-1]
        return prefix
    
