regex = r'\b[Aa]\b|\b[Aa]n\b'

'''# INPUT DATA:

# TEST_1:
A cow is an animal.

# TEST_2:
I have been reading this text for aN hour. Сan you give me this book? AN or an apple

# TEST_3:
An acle, a Ancle, A antarktida, an Any

# TEST_4:
can, hA, ban, OpAn

# TEST_5:
an uianio, ofaoj, poAnfu,  hAk

# TEST_6:
---a---an---A

# TEST_7:
na Na NA AN AAA aaa ana naa aan n Annn ann'''


'''# OUTPUT DATA:
# TEST_1:
A an

# TEST_2:
an

# TEST_3:
An a A an

# TEST_4:


# TEST_5:
an

# TEST_6:
a an A

# TEST_7:'''