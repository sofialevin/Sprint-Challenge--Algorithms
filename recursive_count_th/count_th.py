'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, total = 0):
    if len(word) <= 1:
        return total
    elif word[0:2] == "th":
        total += 1
    return count_th(word[1:], total)
