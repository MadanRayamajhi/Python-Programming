
# Using enumerate()

languages = ["Python", "Java", "C++", "JavaScript"]

for index, language in enumerate(languages):
    print(index, language)

print("\nStarting index from 1:")

for index, language in enumerate(languages, start=1):
    print(index, language)
