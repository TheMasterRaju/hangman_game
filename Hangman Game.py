import random
words=['algorithm','function','variable','compile','iterate','recursion','binary','array','syntax','pointer']
word=words[random.randint(0,9)]
i=0
s='_'*len(word)
l=[]
while True:
    print('HANGMAN')
    print(' '*i+'^')
    if i==6:
        print('You are hanged.')
        break
    if '_' not in s:
        print('Congratulations! You guessed the word: \''+word+'\'')
        print('Phew... you are saved.')
        break
    print(s)
    c=input('Guess a letter: ')[0]
    if c in l:
        print('You already guessed that letter. Try another one.')
    elif c in word:
        print('Good guess!')
        for j in range(len(word)):
            if word[j]==c:
                s=s[:j]+c+s[(j+1):]
        l.append(c)
    else:
        print('Wrong guess!')
        i+=1
