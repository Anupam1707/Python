#To create a tuple containing letters of alphabets in that multiple time as of there order number
#abbccctup.py
#27-11-22
#By Anupam Kanoongo

print("Welcome to the Alphabet in Tuple Generator")
print()
tup = ()
ch = 97

for i in range(1,26+1):
    tup += (chr(ch)*i,)
    ch += 1

print(tup, end="\n")

# Output
# Welcome to the Alphabet in Tuple Generator

# ('A', 'BB', 'CCC', 'DDDD', 'EEEEE', 'FFFFFF', 'GGGGGGG', 'HHHHHHHH', 'IIIIIIIII', 'JJJJJJJJJJ', 
# 'KKKKKKKKKKK', 'LLLLLLLLLLLL', 'MMMMMMMMMMMMM', 'NNNNNNNNNNNNNN', 'OOOOOOOOOOOOOOO', 'PPPPPPPPPPPPPPPP', 
# 'QQQQQQQQQQQQQQQQQ', 'RRRRRRRRRRRRRRRRRR', 'SSSSSSSSSSSSSSSSSSS', 'TTTTTTTTTTTTTTTTTTTT', 'UUUUUUUUUUUUUUUUUUUUU', 
# 'VVVVVVVVVVVVVVVVVVVVVV', 'WWWWWWWWWWWWWWWWWWWWWWW', 'XXXXXXXXXXXXXXXXXXXXXXXX', 'YYYYYYYYYYYYYYYYYYYYYYYYY', 
# 'ZZZZZZZZZZZZZZZZZZZZZZZZZZ')

#OR when ch = 97

# Output
# Welcome to the Alphabet in Tuple Generator

# ('a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg', 'hhhhhhhh', 'iiiiiiiii', 'jjjjjjjjjj', 
# 'kkkkkkkkkkk', 'llllllllllll', 'mmmmmmmmmmmmm', 'nnnnnnnnnnnnnn', 'ooooooooooooooo', 'pppppppppppppppp', 
# 'qqqqqqqqqqqqqqqqq', 'rrrrrrrrrrrrrrrrrr', 'sssssssssssssssssss', 'tttttttttttttttttttt', 'uuuuuuuuuuuuuuuuuuuuu', 
# 'vvvvvvvvvvvvvvvvvvvvvv', 'wwwwwwwwwwwwwwwwwwwwwww', 'xxxxxxxxxxxxxxxxxxxxxxxx', 'yyyyyyyyyyyyyyyyyyyyyyyyy', 
# 'zzzzzzzzzzzzzzzzzzzzzzzzzz')