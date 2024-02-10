#importing sys module
import sys

#defining function 1
def keystrokes1(keyboard,text):
    strokes = 0
    count_key,count_enter = 0,0
    rows, columns = 4,7

    # for loop to calculate minimum strokes for characters
    for char in text:
        count1 = []
        for i in range(rows):
            for j in range(columns):
                if keyboard[i][j] == char:
                    count1.append(count_key)
                    count_key += 1
                    
        strokes += min(count1) + 1
    count2 = []

    #for loop to calculate minimum strokes for enter key
    for i in range(rows):
        for j in range(columns):
            if keyboard[i][j] == '*':
                count_enter += 1
                count2.append(count_enter)
    strokes += min(count2) + 1
    return strokes


#defining function 2
def keystrokes2(keyboard,text):
    strokes = 0
    count_key,count_enter = 0,0
    rows,columns = 5,20
    iterate_count = 1707

    # for loop to calculate minimum strokes for characters
    for char in text:
        count1 = []
        for i in range(rows):
            for j in range(columns):
                if keyboard[i][j] == char:
                    count1.append(count_key)
                    count_key += 1
                    
        strokes += min(count1) + 1
    count2 = []

    # for loop to calculate minimum strokes for enter key
    for i in range(rows):
        for j in range(columns):
                if keyboard[i][j] == '*':
                    count_enter += 1
                    count2.append(count_enter - iterate_count)
    strokes += min(count2) + 1
    return strokes


#virtual keyboard 1
keyboard1 = [['A','B','C','D','E','F','G'],
            ['H','I','J','K','L','M','N'],
            ['O','P','Q','R','S','T','U'],
            ['V','W','X','Y','Z','*','*']]

#virtual keyboard 2
keyboard2 = [['1','2','2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','0','0','0'],
             ['Q','Q','W','W','E','E','R','R','T','T','Y','Y','U','U','I','I','O','O','P','P'],
             ['_','A','A','S','S','D','D','F','F','G','G','H','H','J','J','K','K','L','L','*'],
             ['-','-','Z','Z','X','X','C','C','V','V','B','B','N','N','M','M','-','-','*','*'],
             ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']]


#calling function 1
print(keystrokes1(keyboard1,'CONTEST'))
#calling function 2
print(keystrokes2(keyboard2,'ACM-ICPC-WORLD-FINALS-2015'))
