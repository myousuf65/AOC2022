#! /Users/ypathan/Dev/AOC2022/env/bin/python


# if all characters in words 2 are present in a string of words1
# then print that word
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]


# def check(word, list):
#     # will return True , False
#     return all(char in word for char in list)
#
#
# for w in words1:
#     if check(w, words2):
#         print(w)

def wordSubsets(words1, words2):
    li = []
    for w in words1:
        if all(char in w for char in words2):
            li.append(w)

    print(li)


if __name__ == "__main__":
    wordSubsets(words1, words2)
