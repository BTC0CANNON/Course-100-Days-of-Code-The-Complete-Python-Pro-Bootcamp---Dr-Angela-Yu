# file = open("high_score.txt")
# contents = file.read()
# print(contents)
# file.close()
"""Always close a file when you're done with it! OR ⬇ """

"""Open it in a way that closes when done"""
# with open("high_score.txt") as file:
#     contents = file.read()
#     print(contents)

"""Overwrite file"""
# with open("high_score.txt", mode="w") as file:
#     file.write("13")

"""Append file"""
# with open("high_score.txt", mode="a") as file:
#     file.write("\n15")

"""Create a new file"""
with open("new_file.txt", mode="w") as file:
    file.write("New text.")
