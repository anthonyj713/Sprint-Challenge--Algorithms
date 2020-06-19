'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
   #Base Case, checks if theres 2 letters remaining in word
   if len(word) < 2:
      return 0
   #Check next 2 letters for 'th'
   if word[:2] == 'th':
      # increment count 1 and move to next letter
      return 1 + count_th(word[1:])
   else:
      #move to next letter
      return count_th(word[1:])
