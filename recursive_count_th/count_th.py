'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, total = 0):
    # if word has 1 character or less it returns the total, which starts off as 0
    if len(word) <= 1:
        return total
    # slice of the first two letters in word 
    elif word[0:2] == "th":
        # increase total
        total += 1
    # pass word minus the first character to next function call along with current total
    return count_th(word[1:], total)
