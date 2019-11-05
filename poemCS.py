import random
#4. TITLE: ---- MASKS (Every Thing On It)
poem = '''She had blue skin.
And so did he.
He kept it hid
And so did she.
They searched for blue
Their whole life through,
Then passed right by—
And never knew.'''

def lines_printed_backwards(poem): #will pring lines in reverse
    splits = poem.split("\n") #will split at every line break
    splits = splits[-1::-1] #reversing

    i=8 #setting number of lines
    for sentence in splits: #creating for loop through sentences
        print(f"{i} {sentence}") #formatting number then sentence
        i-=1 #going backwards

#lines_printed_backwards(poem) #calling backwards function

def lines_printed_random(poem):
    for i in range(0,8): #total lines in poem is 8
        print(random.choice(poem.split("\n"))) #prints the random line
#lines_printed_random(poem) #calling random function

def line_only(poem): #function to only print a random line in poem
    print(random.choice(poem.split("\n"))) #chooses random line and prints

line_only(poem) #everytime called will give a different line
