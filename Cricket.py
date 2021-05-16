import time
import random
Game_score = []
game1 = []
toss_opt = ["Head","Tails"]
bator = ['bat','bowl']
toss = random.choice(toss_opt)
overs = 10
wickets = 0
hits  = [1,2,3,4,6]
rnum = random.randrange(1,10)
team1 = input("Which is your Team ? : ")
team2 = input("Your opponent team ? : ")
print(f"{team1}  V.S  {team2}  {time.asctime()}")
print("Tossing")
time.sleep(2)
print("Tossed")
print("You got",toss)
if toss=='Head':
    to = input("What you want to chose bat or bowl : ")
    w = 0
    wickets = random.randint(1,10)
    if to=='bat':
        for i in range(1,10+1):
            w = int(input("What do you want to hit  1 or 2 or 3 or 4 or 6 : "))
            Game_score.append(w)
            if i==wickets:
                w+=1
        Game_score.remove(Game_score[w])
        print(team1,"Scored ",sum(Game_score),team2,"need",sum(Game_score)+1,"to win")
        time.sleep(5)
        w1 = 0
        wic = random.randint(1,10)
        opponent = False
        for i in range(1,10+1):
            hit = random.choice(hits)
            game1.append(hit)
            if i==wic:
                w1+=1
            if sum(game1) > sum(Game_score):
                print(team2,"Won by",10-w1,"Wickets")
                opponent = True
                break
        game1.remove(game1[w1])
        if not opponent:
            if sum(game1) > sum(Game_score):
                print(team2,"Won by ",10-w1,"Wickets")
            else:
                print(team2,"Lost by",sum(Game_score)-sum(game1),"runs")
    if to=='bowl':
        w3 = 0
        we = random.randint(1,10)
        for i in range(1,10+1):
            hit = random.choice(hits)
            game1.append(hit)
            if i==we:
                w3+=1
        game1.remove(game1[w3])
        print(team2,"Scored",sum(game1),"runs",team1,"need",sum(game1)+1,"to win")
        time.sleep(5)
        io = False
        for i in range(1,10+1):
            w = int(input("What do you want to hit  1 or 2 or 3 or 4 or 6 : "))
            Game_score.append(w)
            if i==we:
                w3+=1
            if sum(Game_score) > sum(game1):
                print(team1,"Won by",10-w3,"wickets")
                io = True
                break
        Game_score.remove(Game_score[w3])
        if not io:
            if sum(Game_score) > sum(game1):
                print(team1,"Won by",10-w3,"wickets")
            else:
                print(team2,"Won by",sum(game1)-sum(Game_score),"runs")
                
if toss=='Tails':
        w2 = 0
        wick = random.randint(1,10)
        o = random.choice(bator)
        if o=='bat':
            for i in range(1,10+1):
                hit1 = random.choice(hits)
                game1.append(hit1)
                if i==wick:
                    w2+=1
            game1.remove(game1[w2])
            print(team2,"Scored ",sum(game1),team1,"need ",sum(game1)+1,"to win")
            time.sleep(5)
            opponent = False
            for i in range(1,10+1):
                w = int(input("What do you want to hit  1 or 2 or 3 or 4 or 6 : "))
                Game_score.append(w)
                if i==wick:
                    w2+=1
                if sum(Game_score) > sum(game1):
                    print(team1,"Won by",10-w2,"Wickets")
                    opponent = True
                    break
            Game_score.remove(Game_score[w2])
            if not opponent:
                if sum(Game_score) > sum(game1):
                    print(team1,"Won by",10-w2,"Wickets")
                else:
                    print(team1,"Lost by",sum(Game_score)-sum(game1))
        if o=='bowl':
            w11 = 0
            w32 = random.randrange(1,10)
            op = False
            for i in range(1,10+1):
                h = int(input("What you want to hit 1 or 2 or 3 or 4 or 6 : "))
                Game_score.append(h)
                if i==w32:
                    w11+1
            Game_score.remove(Game_score[w11])
            print(team1,"Scored",sum(Game_score),team2,"need",sum(Game_score)+1,"to win")
            time.sleep(5)
            w35 = 0
            q = random.randint(1,10)
            for i in range(1,10+1):
                hit = random.choice(hits)
                game1.append(hit)
                if i==q:
                    w35+=1
                if sum(game1) > sum(Game_score):
                    print(team2,"Won by",10-w35,"wickets")
                    op = True
                    break
            game1.remove(game1[w35])
            if not op:
                if sum(game1) > sum(Game_score):
                    print(team2,"Won by",10-w35,"wickets")
                else:
                    print(team2,"Lost by",sum(Game_score)-sum(game1),"runs")
print('ENDED')
print('-----------------------------------------------------------------------------------------------------------------------')
