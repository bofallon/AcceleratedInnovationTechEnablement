# select a block of code and comment/uncomment with command + / (or control+/ on windows)

#lambda approach
sign = lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'zero')

# traditional function
def check_sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'