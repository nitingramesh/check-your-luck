import random
print('whats your name:')
name=input()
points=0
strings=['gold','silver']
secretguess = random.choice(strings)
print('well'+name+'choose btw 2 GOLD OR SILVER')
for guesstaken in 'gold':
    print('take a guess')
    guess=input()
    if guesstaken =='gold':
        print('you win:')
        
    elif guesstaken =='silver':
        print('you loose')
    else:
        break
if guess==secretguess:
    print('goodjob you win;')
    print('you get 50 points')
    points=50
    print('do you want to continue the game')
    gameplay=['yes','no']
    gameplay=input()
    if gameplay=='yes':
        play=['ruby','diamond']
        secretguess2=random.choice(play)
        for guesstaken2 in 'ruby':
            print('your choice among DIAMOND AND RUBY :')
        guesstaken2=input()
        if guesstaken2=='ruby':
             points=points+50
             print('you win the game ')
             print(points)
        elif guesstaken2=='diamond':
               print('you loose')
               print(points)
    else:
            print('GAME OVER')
            print(points)
   
    
  
    
else:
    print('you loose')
    print('do you want to continue')
    choice2=['yes','no']
    choice2=input()
    if choice2=='yes':    
        gameplay=['diamond','ruby']
        secretchoice2=random.choice(gameplay)
        for gameplay in 'diamond':
            print('what is ur choice among PLATINUM and DIAMOND')
        gameplay=input()
        if gameplay=='diamond':
            points=points+50
            print('you get 50 points')
            print(points)
        elif gameplay=='platinum':
            print('you get 50 point')
            print(points)
        
    else:
        print('tq for playing this game')
        print(points)
   
if points>=100:
    print('you have a good choice')
else:
    print('better luck next tym')

   
