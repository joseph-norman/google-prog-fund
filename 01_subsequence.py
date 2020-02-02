# 01_subsequence.py
# 
# Given a string S and a set of words D, find the longest word in D 
# that is a 'subsequence' of S.
# 
# Word W is a subsequence of S if some number of characters, possibly zero,
# can be deleted from S to form W, without reordering the remaining characters.

# From S: iteratively remove non-matching characters and do an equality check at each step.
# Retain a swap value for current and previously matching word until we're done going through W.
# 
# Note: D can appear in any format (list, hash table, prefix tree, etc.)
# 
# For example, given the input of S = "abpppleee";
# and D = { "able", "ale", "apple", "bale", "kangaroo" }
# 
# The words 'able' and 'ale' are both subsequences of S, but they are shorter than
# 'apple'.
# 
# The word 'bale' is not a subsequence of S because even though S has all the right
# letters, they are not in the right order.
# 
# The word 'kangaraoo' is the longest word in D, but it isnt a subsequence of S.
# 
# Learning objectives
# 
# This question gives you the chance to practice with algorithms and data structures.
# It's also a good example of why careful analysis for Big-O performance is often
# worthwhile, as is careful exploration of common and worst-case input conditions.
# 

# From S: iteratively remove non-matching characters and do an equality check at each step.
# Retain a swap value for current and previously matching word until we're done going through W.

def subsequence(words):
    subsequence = "abpppleee"
    guesses = set()

    # For each word
    for ind, word in enumerate(words):
        guess = ""

        # Check we can actually compare before iterating through subseq.
        for i in word:
            if i not in subsequence:
                print("No point even checking this one (should be kangaroo)", word)

        # for each char in subsequence
        for char in subsequence:

            # If it does not exist in word
            if char not in word:
                # Remove it in its current pos.
                guess = subsequence.replace(char, "")

            for j in guess:
                # Count the chars
                # If the count of j in guess is > count of j in word
                # Remove the number of chars based on diff
                charDiff = guess.count(j) - word.count(j)
                # print(j, charDiff, word)

                # Remove occurrences that are extraneous.
                guess = guess.replace(j, "", charDiff)

            if guess == word:
                # Store count of words.
                guesses.add(guess)
    
    enumerable = list(guesses)
    longest = ""
    # Finally, get the longest
    for idx, val in enumerate(list(guesses)):
       print(idx, val)
       if len(val) > len(enumerable[idx-1]):
           longest = val
    
    print("Longest subsequence possible in", subsequence, " is", longest)


def main():
    subsequence(["able", "ale", "apple", "bale", "kangaroo"])

if __name__ == "__main__":
    main()
