# From Stage 2 Webcasts
# https://discussions.udacity.com/t/stage-2-webcasts/16001/8

# Problem 1

# Define a procedure, find_last, that takes as input two strings, a search string and a target string, and returns the last position in the search string where the target string appears, or -1 if there are no occurrences. Example: find_last('aaaa', 'a') returns 3. Make sure your procedure has a return statement.

# MY ANSWER

def find_last(s,t): # s for search, t for target
  start = 0
  end = len(s) - 1
  if t == "":
      return 0
  if t in s:
    if s.find(t,end) == -1:
      end -= 1
    if s.find(t,end) != -1:
      return end
  else:
      return -1
# This is close, but not giving me all the correct test cast answers...

# Test cases provided:

print find_last('aaaa', 'a') # 3

print find_last('aaaaa', 'aa') # 3

print find_last('aaaa', 'b') # -1

print find_last("111111111", "1") # 8

print find_last("222222222", "") # 9

print find_last("", "3") # -1

print find_last("", "") # 0

# PROVIDED ANSWER

def find_last(search_string, target_string):
	 # First check to see whether the target string is even inside the search string
    if search_string.find(target_string) == -1:
        return -1
    current_location = 0
    # While the current_location is greater than -1 
    while current_location >= 0:
        last_location = current_location
        # Continue to search for the next target string
        current_location = search_string.find(target_string, current_location + 1)
    return last_location

print find_last('aaaa', 'a') # 3

print find_last('aaaaa', 'aa') # 3

print find_last('aaaa', 'b') # -1

print find_last("111111111", "1") # 8

print find_last("222222222", "") # 9

print find_last("", "3") # -1

print find_last("", "") # 0

# Problem 2

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# The answer is 21124

# this is stil beyond the scope of this course...
