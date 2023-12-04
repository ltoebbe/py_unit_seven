word = 'word'


def half_slice(word):
    halfpoint = len(word)/2
    first_half = word[0:int(halfpoint)]
    last_half = word[int(halfpoint):]
    print(last_half, first_half)


half_slice(word)

# __________________________________________________________
str = 'there sat the brown barbaloots in their barbaloot suits'


def no_first_last(str):
    new_str = str[1:-1]
    print(new_str)


no_first_last(str)

# ___________________________________________________________
phrase1 = 'there is no I in team, however there are six Is in screw it I dont care how big the room is I cast fireball'
phrase2 = 'the opposite of finger licking good is toe sucking evil'


def longest(phrase):
    p1len = len(phrase1.split(' '))
    p2len = len(phrase2.split(' '))
    if p1len > p2len:
        print(p1len)
    elif p1len < p2len:
        print(p2len)


longest(phrase1)

# ___________________________________________________________
sentence = "that's rough buddy"


def title_case(sentence):
    senlist = sentence.split(' ')

