print("Let's play the Quiz Game ")

print ('Do you want to continue for  yes(y) and no (n)')
playing = input('')
if playing != 'y':
    quit()
score = 0
answer = input('what does CPU stand for :')
if(answer == "central processing unit "):
    print('correct answer ')
    score += 1
else:
    print ('Incorect answer ')
        
answer = input('what does GPU stand for :')
if(answer == "graphic  processing unit "):
    print('correct answer ')
    score += 1
else:
    print ('Incorect answer ')

answer = input('what does RAM stand for :')
if(answer == "random acess memory  "):
    print('correct answer ')
    score += 1
else:
    print ('Incorect answer ')

print (f'SCORE {score}')
