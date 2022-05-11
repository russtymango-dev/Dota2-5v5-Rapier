players={} #This is a dictionary that is used to generate V1 version of the balancer
team2players ={}
team1players ={}
teamsort={} #This is a dictionary that is used to generate V2 version of the balancer
teamsort2 = {} #This is a duplicate dictionary used for the second pass of the algorithim 
playerphonebook = {
  "A": "Liam",
  "B": "Russell",
  "C": "Migs",
  "D": "Sean",
  "E": "Mege",
  "F": "Mun",
  "G": "Troy",
  "H": "Jordan",
  "I": "Nugget",
  "J": "Drew", 
}

#n = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J") #All players are reduced to a letter, which corresponds to their rating in the tuple below
#m = (58.85,52.71,91.39,77.91,93.91,35.51,13.21,53.67,44.99,82.14) # tuple which has all the player ranks ordered. Hence first rank will correspond to player A
#the values of M are to be edited before running the algo

n = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J") #All players are reduced to a letter, which corresponds to their rating in the tuple below
m = (56.17,51.45,89.39,77.25,36.42,36.01,60.33,72.77,47.99,76.44) # tuple which has all the player ranks ordered. Hence first rank will correspond to player A
#actual values, stored for later use 

allpasses = 10
sumteam = 5
numPlayers = 10 #Static field, always 10 players
numPlayersJ = 10 #static field, used for the J level of the loop
numPlayersTeam = 5 #static field, used to print team at end 
numTeams = 2 #static field, always 2 teams of 5
t1 = {} #Dictionary for the final team 1
t2 = {} #Dictionary for the final team 2
n_ = 0 #value used to calculate the current MAX value within a dictionary 
dt = () #used to store the current letter that is to be removed from the teamsort dicitionary 
cr = 0 #used to store the current MMR of the checked player 
n1 =() #a tuple to store the team 1 of letters
m1 =() #a tuple to store the team 1 of ranks 
n2 =() #a tuple to store the team 2 of letters
m2 =() #a tuple to store the team 2 of tanks
t_c = ()#is a check to make sure that the right value has bene assigned before moving on in the loop
t_l = [] #temporary list to delete items for tuples
posi =() #current position of i in the loop
adds_m1 = 0 #tracks the current length of m1
adds_m2 = 0 #tracks the current length of m1
sumlist1 =[]
sumlist2 =[]
sumt1 = 0
sumt2 = 0

for i in range(numPlayers): #populates the dictionary of both players and teamsort values with the given set 
    players[n[i]] = m[i]
    teamsort[n[i]] = m[i]
    teamsort2[n[i]] = m[i]
    
for j in range(numPlayersJ):
    for i in range(numPlayers): #V2 algo, currently goes through each player and assigns values to teams based on W/R scoring.
        
         cr = teamsort [n[i]] #starts the loop process by assigning the first value in a dictoinary to CR to start checking for max value 
                  
         if adds_m1 == 1:
             sumlist1 = list(m1)
             sumt1 = sum(m1)

         if adds_m2 == 1:
             sumlist2 = list(m2)
             sumt2 = sum(m2)
             
         if adds_m1 >= 2:
             sumlist1 = list(m1)
             sumt1 = sum(m1)

         if adds_m2 >= 2:
             sumlist2 = list(m2)
             sumt2 = sum(m2)
         
         if n_ < cr: #Runs a loop that checks the max value within the dictionary and returns it 
             n_ = cr
             dt = n[i]
             posi = i

         

         if i == 1 and t_c == 9:
             n_ = m[0]
             dt = n[0]
             
         if i == 9: #since it has checked all 9 values, we know that max value has been determined so we can store the value into the new T1 dictionary and remove that value from the current dictionary
             
             n1 = n1 + (dt,)
             m1 = m1 + (n_,)
             adds_m1 = adds_m1 + 1
             
             t_l = list(n)
             t_l.pop(posi)            
             n = t_l
             t_l = list(m)
             t_l.pop(posi)            
             m = t_l
             
             
             del teamsort[dt]
             cr = 0
             t_c = 1
             n_ = 0
             numPlayers = numPlayers - 1
             
         if i == 8 and t_c == 1: #since it has checked all 9 values, we know that max value has been determined so we can store the value into the new T1 dictionary and remove that value from the current dictionary
             
             n2 = n2 + (dt,)
             m2 = m2 + (n_,)
             
             adds_m2 = adds_m2 + 1

             t_l = list(n)
             t_l.pop(posi)            
             n = t_l
             t_l = list(m)
             t_l.pop(posi)            
             m = t_l
             
             del teamsort[dt]
             cr = 0
             t_c = 2
             n_ = 0
             numPlayers = numPlayers - 1
             
             
         if i == 7 and t_c == 2: #since it has checked all 9 values, we know that max value has been determined so we can store the value into the new T1 dictionary and remove that value from the current dictionary
             
             
             if m1 >= m2:
                 
                 n2 = n2 + (dt,)
                 m2 = m2 + (n_,)
                 adds_m2 = adds_m2 + 1
                 

                 t_l = list(n)
                 t_l.pop(posi)            
                 n = t_l
                 t_l = list(m)
                 t_l.pop(posi)            
                 m = t_l
                 
                 del teamsort[dt]
                 cr = 0
                 t_c = 3
                 numPlayers = numPlayers - 1
                 n_ = 0
                 
             
             if m2 >= m1:
                 
                 n1 = n1 + (dt,)
                 m1 = m1 + (n_,)
                 adds_m1 = adds_m1 + 1
                 

                 t_l = list(n)
                 t_l.pop(posi)            
                 n = t_l
                 t_l = list(m)
                 t_l.pop(posi)            
                 m = t_l
                 
                 del teamsort[dt]
                 cr = 0
                 t_c = 3
                 numPlayers = numPlayers - 1
                 n_ = 0

         if i == 6 and t_c == 3: #since it has checked all 9 values, we know that max value has been determined so we can store the value into the new T1 dictionary and remove that value from the current dictionary
             
             
             if sumt1 >= sumt2:
                 
                 n2 = n2 + (dt,)
                 m2 = m2 + (n_,)
                 adds_m2 = adds_m2 + 1
                 

                 t_l = list(n)
                 t_l.pop(posi)            
                 n = t_l
                 t_l = list(m)
                 t_l.pop(posi)            
                 m = t_l
                 
                 del teamsort[dt]
                 cr = 0
                 t_c = 4
                 numPlayers = numPlayers - 1
                 n_ = 0
                 
             
             if sumt2 >= sumt1:
                 
                 n1 = n1 + (dt,)
                 m1 = m1 + (n_,)
                 adds_m1 = adds_m1 + 1
                 

                 t_l = list(n)
                 t_l.pop(posi)            
                 n = t_l
                 t_l = list(m)
                 t_l.pop(posi)            
                 m = t_l
                 
                 del teamsort[dt]
                 cr = 0
                 t_c = 4
                 numPlayers = numPlayers - 1
                 n_ = 0
                 
         if i == 5 and t_c == 4: #since it has checked all 9 values, we know that max value has been determined so we can store the value into the new T1 dictionary and remove that value from the current dictionary
             
             
             if sumt1 >= sumt2:
                 
                 n2 = n2 + (dt,)
                 m2 = m2 + (n_,)
                 adds_m2 = adds_m2 + 1
                 

                 t_l = list(n)
                 t_l.pop(posi)            
                 n = t_l
                 t_l = list(m)
                 t_l.pop(posi)            
                 m = t_l
                 
                 del teamsort[dt]
                 cr = 0
                 t_c = 5
                 numPlayers = numPlayers - 1
                 n_ = 0
                 
             
             if sumt2 >= sumt1:
                 
                 n1 = n1 + (dt,)
                 m1 = m1 + (n_,)
                 adds_m1 = adds_m1 + 1
                 

                 t_l = list(n)
                 t_l.pop(posi)            
                 n = t_l
                 t_l = list(m)
                 t_l.pop(posi)            
                 m = t_l
                 
                 del teamsort[dt]
                 cr = 0
                 t_c = 5
                 numPlayers = numPlayers - 1
                 n_ = 0
         if i == 4 and t_c == 5: #since it has checked all 9 values, we know that max value has been determined so we can store the value into the new T1 dictionary and remove that value from the current dictionary
             
             
             if sumt1 >= sumt2:
                 
                 n2 = n2 + (dt,)
                 m2 = m2 + (n_,)
                 adds_m2 = adds_m2 + 1
                 

                 t_l = list(n)
                 t_l.pop(posi)            
                 n = t_l
                 t_l = list(m)
                 t_l.pop(posi)            
                 m = t_l
                 
                 del teamsort[dt]
                 cr = 0
                 t_c = 6
                 numPlayers = numPlayers - 1
                 n_ = 0
                 
             
             if sumt2 >= sumt1:
                 
                 n1 = n1 + (dt,)
                 m1 = m1 + (n_,)
                 adds_m1 = adds_m1 + 1
                 

                 t_l = list(n)
                 t_l.pop(posi)            
                 n = t_l
                 t_l = list(m)
                 t_l.pop(posi)            
                 m = t_l
                 
                 del teamsort[dt]
                 cr = 0
                 t_c = 6
                 numPlayers = numPlayers - 1
                 n_ = 0


         if i == 3 and t_c == 6: #since it has checked all 9 values, we know that max value has been determined so we can store the value into the new T1 dictionary and remove that value from the current dictionary
             
             
             if sumt1 >= sumt2:
                 
                 n2 = n2 + (dt,)
                 m2 = m2 + (n_,)
                 adds_m2 = adds_m2 + 1
                 

                 t_l = list(n)
                 t_l.pop(posi)            
                 n = t_l
                 t_l = list(m)
                 t_l.pop(posi)            
                 m = t_l
                 
                 del teamsort[dt]
                 cr = 0
                 t_c = 7
                 numPlayers = numPlayers - 1
                 n_ = 0
                 
             
             if sumt2 >= sumt1:
                 
                 n1 = n1 + (dt,)
                 m1 = m1 + (n_,)
                 adds_m1 = adds_m1 + 1
                 

                 t_l = list(n)
                 t_l.pop(posi)            
                 n = t_l
                 t_l = list(m)
                 t_l.pop(posi)            
                 m = t_l
                 
                 del teamsort[dt]
                 cr = 0
                 t_c = 7
                 numPlayers = numPlayers - 1
                 n_ = 0


         if i == 2 and t_c == 7: #since it has checked all 9 values, we know that max value has been determined so we can store the value into the new T1 dictionary and remove that value from the current dictionary
             
             
             if sumt1 >= sumt2:
                 
                 n2 = n2 + (dt,)
                 m2 = m2 + (n_,)
                 adds_m2 = adds_m2 + 1
                 

                 t_l = list(n)
                 t_l.pop(posi)            
                 n = t_l
                 t_l = list(m)
                 t_l.pop(posi)            
                 m = t_l
                 
                 del teamsort[dt]
                 cr = 0
                 t_c = 8
                 numPlayers = numPlayers - 1
                 n_ = 0
                 
             
             if sumt2 >= sumt1:
                 
                 n1 = n1 + (dt,)
                 m1 = m1 + (n_,)
                 adds_m1 = adds_m1 + 1
                 

                 t_l = list(n)
                 t_l.pop(posi)            
                 n = t_l
                 t_l = list(m)
                 t_l.pop(posi)            
                 m = t_l
                 
                 del teamsort[dt]
                 cr = 0
                 t_c = 8
                 numPlayers = numPlayers - 1
                 n_ = 0

         if i == 1 and t_c == 8: #since it has checked all 9 values, we know that max value has been determined so we can store the value into the new T1 dictionary and remove that value from the current dictionary
             
             
             if sumt1 >= sumt2:
                 
                 n2 = n2 + (dt,)
                 m2 = m2 + (n_,)
                 adds_m2 = adds_m2 + 1
                

                 t_l = list(n)
                 t_l.pop(posi)            
                 n = t_l
                 t_l = list(m)
                 t_l.pop(posi)            
                 m = t_l
                 
                 del teamsort[dt]
                 
                 cr = 0
                 t_c = 9
                 numPlayers = numPlayers - 1
                 n_ = 0
                 
             
             if sumt2 >= sumt1:
                 
                 n1 = n1 + (dt,)
                 m1 = m1 + (n_,)
                 adds_m1 = adds_m1 + 1
                 

                 t_l = list(n)
                 t_l.pop(posi)            
                 n = t_l
                 t_l = list(m)
                 t_l.pop(posi)            
                 m = t_l
                 
                 del teamsort[dt]
                 
                 cr = 0
                 t_c = 9
                 numPlayers = numPlayers - 1
                 n_ = 0

         if i == 0 and t_c == 9: #since it has checked all 9 values, we know that max value has been determined so we can store the value into the new T1 dictionary and remove that value from the current dictionary
             
             
             if adds_m1 == 5 and adds_m2 != 5:
                 
                 n2 = n2 + (dt,)
                 m2 = m2 + (n_,)
                 adds_m2 = adds_m2 + 1
                                                
                 
                 cr = 0
                 t_c = 3
                 numPlayers = numPlayers - 1
                 n_ = 0
                 
             
             if adds_m2 == 5 and adds_m1 != 5:
                 
                 n1 = n1 + (dt,)
                 m1 = m1 + (n_,)
                 adds_m1 = adds_m1 + 1
                 

                 
                 
                 cr = 0
                 t_c = 3
                 numPlayers = numPlayers - 1
                 n_ = 0

sumt1 = 0
sumt2 = 0

n1pass1 =()
n2pass1 =()
m1pass1 =()
m2pass1 =()

n1pass1 =n1
n2pass1 =n2
m1pass1 =m1
m2pass1 =m2

for k in range(sumteam):
    sumt1 = sumt1 + m1[k]
    sumt2 = sumt2 + m2[k]
#final sum score
totalgamevalue = sumt1+sumt2

sumd_d = 0 

               

print(" ")
print("Results")
print(" ")
                             
print("Team 1 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n1[i]])

print(" ")
print ("Team 1 indervidual MMR rating")
print(n1)
print(m1)


print(" ")
print ("Team 1 combined MMR rating")
print (sumt1)

print(" ")
print ("Calculated chance of team 1 victory")
print ((sumt1/totalgamevalue)*100,"%")
print(" ") 
print(" ")             

print("Team 2 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n2[i]])
print(" ")
print ("Team 2 indervidual MMR rating")
print(n2)
print(m2)


print(" ")
print ("Team 2 combined MMR rating")
print (sumt2)

print(" ")
print ("Calculated chance of team 2 victory")
print ((sumt2/totalgamevalue)*100,"%")
print(" ")
if sumt1 >= sumt2:
    print ("Team 2 chooses to draft first or pick side of map")
    sumd_d = 1
else:
    print ("Team 1 chooses to draft first or pick side of map")
    sumd_d = 2

print(" ")    
print(" ")


print("Lets do a second pass")



print(" ")
print(" ")

if sumd_d == 1:
     sumd_d = sumt1 - sumt2
else:
     sumd_d = sumt2 - sumt1

print("this is the difference between the two teams")
print(sumd_d)

sumd_d_d = sumd_d/2 #this is the value that the second pass is trying to achieve

sumd_d_d = abs(sumd_d_d)

print(" ")
print(" ")

print("this is what I am looking for between differences of 2 numbers")


print(sumd_d_d)

teampass_first = 0
teampass_first = sumd_d_d

n02 = 0
cr02 = 0
n02 = 0
crn02 = 0
crncheck = 0
crnmatch = 0
localteam = 5
localteam2 = 5
localteam3 = 5
passcount = 0
savep = 0
savez = 0
saveletp = ()
saveletz = ()

t_m = []

swap1n = m1  #number for the player to swap 
swap2n = m2
swap1a = n1  #letter for the player to swap team 1 
swap2a = n2  

checker = sumd_d_d
truechecker = 0
checkper = checker/6

print(" ")
print(" ")
print("THIS IS THE FIRST PASS ")
print(" ")
print(" ")

for i in range(localteam): #populates the dictionary of both players and teamsort values with the given set 
    team1players[n1[i]] = m1[i]
    team2players[n2[i]] = m2[i]

for k in range(localteam): #okay so this is kinda cool but super ineffecient. I was originally planning on having the 2nd pass try every possible combination
                             #and then do a min on the closest one and use that as the switch value. But a better way is to have a small value slowly
                             #increment and when it finds a swap that is within the current tollarence of that check, then it breaks the loop
    if checker < 0.1:
        print("it broke")
        break                         #then it will perform the swap and provide the new teams. This way I can simply just repeat the loop if required
                            #to continue have additional passes at the loop. This also allows me to change the tolerence to a higher value
    if k>0:                          
        checker = checker+checkper
    if truechecker == 1:
        break
    
    for j in range(localteam2):
          
                  
        
          crn02 = m2[j]
                   
          if truechecker == 1:
              break 
          for i in range(localteam3):
          
               passcount = passcount + 1 
               n02 = m1[i]
               crnmatch = crn02
               crncheck = crn02
               
               
               crncheck = crncheck  - n02
               crncheck = abs(crncheck)
               

               if crncheck <= checker and crncheck != 0:
                   truechecker = 1

                 

                   for p in range(localteam):
                      
                       if m2[p] == crnmatch:
                           
                           savep = p
                           saveletp = n2[p]
                           

                           
                   for z in range(localteam):
                       
                       if m1[z] == n02:
                           
                           savez = z
                           saveletz = n1[z]

                   mmm1 = ()
                   mmm2 = ()
                   nnn1 = ()
                   nnn2 = ()
                   mmm1 = n02
                   mmm2 = crnmatch
                   nnn1 = saveletz
                   nnn2 = saveletp

                   

                   t_m = list(m1)
                   t_m.pop(savez)            
                   m1 = tuple(t_m)
                   m1 = m1 + (mmm2,)

                   t_m = list(m2)
                   t_m.pop(savep)            
                   m2 = tuple(t_m)
                   m2 = m2 + (mmm1,)

                   t_m = list(n1)
                   t_m.pop(savez)            
                   n1 = tuple(t_m)
                   n1 = n1 + (nnn2,)
                   
                   t_m = list(n2)
                   t_m.pop(savep)            
                   n2 = tuple(t_m)
                   n2 = n2 + (nnn1,)
                   break



n1pass2 =()
n2pass2 =()
m1pass2 =()
m2pass2 =()

n1pass2 =n1
n2pass2 =n2
m1pass2 =m1
m2pass2 =m2

newsumt1 = 0
newsumt2 = 0

#final sum score

sumd_d = 0

for k in range(localteam):
    newsumt1 = newsumt1 + m1[k]
    newsumt2 = newsumt2 + m2[k]

totalgamevalue = newsumt1 + newsumt2

print(" ")
print(" ")
print("pass")

print("Results")
print(" ")
                             
print("Team 1 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n1[i]])

print(" ")
print ("Team 1 indervidual MMR rating")
print(n1)
print(m1)


print(" ")
print ("Team 1 combined MMR rating")
print (newsumt1)

newsumt1 = float(newsumt1)


print(" ")
print ("Calculated chance of team 1 victory")
print ((newsumt1/totalgamevalue)*100,"%")
print(" ") 
print(" ")             

print("Team 2 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n2[i]])
print(" ")
print ("Team 2 indervidual MMR rating")
print(n2)
print(m2)




print(" ")
print ("Team 2 combined MMR rating")
print (newsumt2)

print(" ")
print ("Calculated chance of team 2 victory")
print ((newsumt2/totalgamevalue)*100,"%")
print(" ")
if newsumt1 >= newsumt2:
    print ("Team 2 chooses to draft first or pick side of map")
    sumd_d = 1
else:
    print ("Team 1 chooses to draft first or pick side of map")
    sumd_d = 2

print(" ")    
print(" ")


print("Lets do a third pass")



print(" ")
print(" ")

if sumd_d == 1:
     sumd_d = newsumt1 - newsumt2
else:
     sumd_d = newsumt2 - newsumt1

print("this is the difference between the two teams")
print(sumd_d)

sumd_d_d = sumd_d/2 #this is the value that the second pass is trying to achieve

sumd_d_d = abs(sumd_d_d)

print(" ")
print(" ")

print("this is what I am looking for between differences of 2 numbers")


print(sumd_d_d)      

teampass_second = 0
teampass_second = sumd_d_d                   

                   
n02 = 0
cr02 = 0
n02 = 0
crn02 = 0
crncheck = 0
crnmatch = 0
localteam = 5
localteam2 = 5
localteam3 = 5
localteam4 = 5
localteam5 = 5
passcount = 0
savep = 0
savez = 0
saveletp = ()
saveletz = ()

t_m = []

swap1n = m1  #number for the player to swap 
swap2n = m2
swap1a = n1  #letter for the player to swap team 1 
swap2a = n2            
                   
checker = sumd_d_d
truechecker = 0
checkper = checker/10

print(" ")
print(" ")
print("THIS IS THE SECOND PASS ")
print(" ")
print(" ")
               
for i in range(localteam): #populates the dictionary of both players and teamsort values with the given set 
    team1players[n1[i]] = m1[i]
    team2players[n2[i]] = m2[i]

for k in range(localteam): #okay so this is kinda cool but super ineffecient. I was originally planning on having the 2nd pass try every possible combination
                             #and then do a min on the closest one and use that as the switch value. But a better way is to have a small value slowly
                             #increment and when it finds a swap that is within the current tollarence of that check, then it breaks the loop
                             #then it will perform the swap and provide the new teams. This way I can simply just repeat the loop if required
    if checker < 0.1:
        print("it broke")
        break                         #to continue have additional passes at the loop. This also allows me to change the tolerence to a higher value
                             #which should discover different team combinations whilst still being within tolerance 
    if k>0:                          
        checker = checker+checkper
    if truechecker == 1:
        break
    
    for j in range(localteam2):
          
                  
        
          crn02 = m2[j]
                   
          if truechecker == 1:
              break 
          for i in range(localteam3):
          
               passcount = passcount + 1 
               n02 = m1[i]
               crnmatch = crn02
               crncheck = crn02
               
               
               crncheck = crncheck  - n02
               crncheck = abs(crncheck)
               

               if crncheck <= checker and crncheck != 0:
                   truechecker = 1

                   

                   for p in range(localteam5):
                       
                       if m2[p] == crnmatch:
                           
                           savep = p
                           saveletp = n2[p]
                           

                           
                   for z in range(localteam4):
                       
                       if m1[z] == n02:
                           
                           savez = z
                           saveletz = n1[z]

                   


                   mmm1 = ()
                   mmm2 = ()
                   nnn1 = ()
                   nnn2 = ()
                   mmm1 = n02
                   mmm2 = crnmatch
                   nnn1 = saveletz
                   nnn2 = saveletp

                   t_m = list(m1)
                   t_m.pop(savez)            
                   m1 = tuple(t_m)
                   m1 = m1 + (mmm2,)

                   t_m = list(m2)
                   t_m.pop(savep)            
                   m2 = tuple(t_m)
                   m2 = m2 + (mmm1,)

                   t_m = list(n1)
                   t_m.pop(savez)            
                   n1 = tuple(t_m)
                   n1 = n1 + (nnn2,)
                   
                   t_m = list(n2)
                   t_m.pop(savep)            
                   n2 = tuple(t_m)
                   n2 = n2 + (nnn1,)
                   break
                   


newnewsumt1 = 0
newnewsumt2 = 0

n1pass3 =()
n2pass3 =()
m1pass3 =()
m2pass3 =()

n1pass3 =n1
n2pass3 =n2
m1pass3 =m1
m2pass3 =m2

for k in range(localteam):
    newnewsumt1 = newnewsumt1 + m1[k]
    newnewsumt2 = newnewsumt2 + m2[k]


#final sum score
totalgamevalue = newnewsumt1+newnewsumt2
sumd_d = 0 

print(" ")
print(" ")
print("pass")

print("Results")
print(" ")
                             
print("Team 1 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n1[i]])

print(" ")
print ("Team 1 indervidual MMR rating")
print(n1)
print(m1)


print(" ")
print ("Team 1 combined MMR rating")
print (newnewsumt1)

print(" ")
print ("Calculated chance of team 1 victory")
print ((newnewsumt1/totalgamevalue)*100,"%")
print(" ") 
print(" ")             

print("Team 2 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n2[i]])
print(" ")
print ("Team 2 indervidual MMR rating")
print(n2)
print(m2)


print(" ")
print ("Team 2 combined MMR rating")
print (newnewsumt2)

print(" ")
print ("Calculated chance of team 2 victory")
print ((newnewsumt2/totalgamevalue)*100,"%")
print(" ")
if newnewsumt1 >= newnewsumt2:
    print ("Team 2 chooses to draft first or pick side of map")
    sumd_d = 1
else:
    print ("Team 1 chooses to draft first or pick side of map")
    sumd_d = 2

print(" ")    
print(" ")

print("Lets do a third pass")



print(" ")
print(" ")

if sumd_d == 1:
     sumd_d = newnewsumt1 - newnewsumt2
else:
     sumd_d = newnewsumt2 - newnewsumt1

print("this is the difference between the two teams")
print(sumd_d)

sumd_d_d = sumd_d/2 #this is the value that the second pass is trying to achieve

sumd_d_d = abs(sumd_d_d)

print(" ")
print(" ")

print("this is what I am looking for between differences of 2 numbers")


print(sumd_d_d) 



teampass_third = 0
teampass_third = sumd_d_d                  


n02 = 0
cr02 = 0
n02 = 0
crn02 = 0
crncheck = 0
crnmatch = 0
localteam = 5
localteam2 = 5
localteam3 = 5
localteam4 = 5
localteam5 = 5
passcount = 0
savep = 0
savez = 0
saveletp = ()
saveletz = ()

t_m = []

swap1n = m1  #number for the player to swap 
swap2n = m2
swap1a = n1  #letter for the player to swap team 1 
swap2a = n2            
                   
checker = sumd_d_d
truechecker = 0
checkper = checker/12
print(" ")
print(" ")
print("THIS IS THE THIRD PASS ")
print(" ")
print(" ")
               
for i in range(localteam): #populates the dictionary of both players and teamsort values with the given set 
    team1players[n1[i]] = m1[i]
    team2players[n2[i]] = m2[i]

for k in range(localteam): #okay so this is kinda cool but super ineffecient. I was originally planning on having the 2nd pass try every possible combination
                             #and then do a min on the closest one and use that as the switch value. But a better way is to have a small value slowly
                             #increment and when it finds a swap that is within the current tollarence of that check, then it breaks the loop
                             #then it will perform the swap and provide the new teams. This way I can simply just repeat the loop if required
    if checker < 0.1:
        print("it broke")
        break                        #to continue have additional passes at the loop. This also allows me to change the tolerence to a higher value
                             #which should discover different team combinations whilst still being within tolerance 
    if k>0:                          
        checker = checker+checkper
    if truechecker == 1:
        break
    
    for j in range(localteam2):
          
                  
        
          crn02 = m2[j]
                   
          if truechecker == 1:
              break 
          for i in range(localteam3):
          
               passcount = passcount + 1 
               n02 = m1[i]
               crnmatch = crn02
               crncheck = crn02
               
               crncheck = crncheck  - n02
               crncheck = abs(crncheck)
               

               if crncheck <= checker and crncheck != 0:
                   truechecker = 1

                   

                   for p in range(localteam5):
                       
                       if m2[p] == crnmatch:
                           
                           savep = p
                           saveletp = n2[p]
                           

                           
                   for z in range(localteam4):
                       
                       if m1[z] == n02:
                           
                           savez = z
                           saveletz = n1[z]

                   


                   mmm1 = ()
                   mmm2 = ()
                   nnn1 = ()
                   nnn2 = ()
                   mmm1 = n02
                   mmm2 = crnmatch
                   nnn1 = saveletz
                   nnn2 = saveletp

                   t_m = list(m1)
                   t_m.pop(savez)            
                   m1 = tuple(t_m)
                   m1 = m1 + (mmm2,)

                   t_m = list(m2)
                   t_m.pop(savep)            
                   m2 = tuple(t_m)
                   m2 = m2 + (mmm1,)

                   t_m = list(n1)
                   t_m.pop(savez)            
                   n1 = tuple(t_m)
                   n1 = n1 + (nnn2,)
                   
                   t_m = list(n2)
                   t_m.pop(savep)            
                   n2 = tuple(t_m)
                   n2 = n2 + (nnn1,)
                   break
                   


newnewnewsumt1 = 0
newnewnewsumt2 = 0



for k in range(localteam):
    newnewnewsumt1 = newnewnewsumt1 + m1[k]
    newnewnewsumt2 = newnewnewsumt2 + m2[k]
n1pass4 =()
n2pass4 =()
m1pass4 =()
m2pass4 =()

n1pass4 =n1
n2pass4 =n2
m1pass4 =m1
m2pass4 =m2

#final sum score
totalgamevalue = newnewnewsumt1+newnewnewsumt2
sumd_d = 0 

print(" ")
print(" ")
print("pass")

print("Results")
print(" ")
                             
print("Team 1 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n1[i]])

print(" ")
print ("Team 1 indervidual MMR rating")
print(n1)
print(m1)


print(" ")
print ("Team 1 combined MMR rating")
print (newnewnewsumt1)

print(" ")
print ("Calculated chance of team 1 victory")
print ((newnewnewsumt1/totalgamevalue)*100,"%")
print(" ") 
print(" ")             

print("Team 2 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n2[i]])
print(" ")
print ("Team 2 indervidual MMR rating")
print(n2)
print(m2)


print(" ")
print ("Team 2 combined MMR rating")
print (newnewnewsumt2)

print(" ")
print ("Calculated chance of team 2 victory")
print ((newnewnewsumt2/totalgamevalue)*100,"%")
print(" ")
if newnewnewsumt1 >= newnewnewsumt2:
    print ("Team 2 chooses to draft first or pick side of map")
    sumd_d = 1
else:
    print ("Team 1 chooses to draft first or pick side of map")
    sumd_d = 2

print(" ")    
print(" ")


print(" ")
print(" ")

if sumd_d == 1:
     sumd_d = newnewnewsumt1 - newnewnewsumt2
else:
     sumd_d = newnewnewsumt2 - newnewnewsumt1

print("this is the difference between the two teams")
print(sumd_d)

sumd_d_d = sumd_d/2 #this is the value that the second pass is trying to achieve

sumd_d_d = abs(sumd_d_d)

print(" ")
print(" ")

print("this is what I am looking for between differences of 2 numbers")


print(sumd_d_d) 



teampass_fourth = 0
teampass_fourth = sumd_d_d

n02 = 0
cr02 = 0
n02 = 0
crn02 = 0
crncheck = 0
crnmatch = 0
localteam = 5
localteam2 = 5
localteam3 = 5
localteam4 = 5
localteam5 = 5
passcount = 0
savep = 0
savez = 0
saveletp = ()
saveletz = ()

t_m = []

swap1n = m1  #number for the player to swap 
swap2n = m2
swap1a = n1  #letter for the player to swap team 1 
swap2a = n2            
                   
checker = sumd_d_d
truechecker = 0
checkper = checker/14

print(" ")
print(" ")
print("THIS IS THE fifth PASS ")
print(" ")
print(" ")
               
for i in range(localteam): #populates the dictionary of both players and teamsort values with the given set 
    team1players[n1[i]] = m1[i]
    team2players[n2[i]] = m2[i]

for k in range(localteam): #okay so this is kinda cool but super ineffecient. I was originally planning on having the 2nd pass try every possible combination
                             #and then do a min on the closest one and use that as the switch value. But a better way is to have a small value slowly
                             #increment and when it finds a swap that is within the current tollarence of that check, then it breaks the loop
                             #then it will perform the swap and provide the new teams. This way I can simply just repeat the loop if required
    if checker < 0.1:
        print("it broke")
        break                       #to continue have additional passes at the loop. This also allows me to change the tolerence to a higher value
                             #which should discover different team combinations whilst still being within tolerance 
    if k>0:                          
        checker = checker+checkper
    if truechecker == 1:
        break
    
    for j in range(localteam2):
          
                  
        
          crn02 = m2[j]
                   
          if truechecker == 1:
              break 
          for i in range(localteam3):
          
               passcount = passcount + 1 
               n02 = m1[i]
               crnmatch = crn02
               crncheck = crn02
               
               
               crncheck = crncheck  - n02
               crncheck = abs(crncheck)
               

               if crncheck <= checker and crncheck != 0:
                   truechecker = 1

                   

                   for p in range(localteam5):
                       
                       if m2[p] == crnmatch:
                           
                           savep = p
                           saveletp = n2[p]
                           

                           
                   for z in range(localteam4):
                       
                       if m1[z] == n02:
                           
                           savez = z
                           saveletz = n1[z]

                   
                   


                   mmm1 = ()
                   mmm2 = ()
                   nnn1 = ()
                   nnn2 = ()
                   mmm1 = n02
                   mmm2 = crnmatch
                   nnn1 = saveletz
                   nnn2 = saveletp

                   t_m = list(m1)
                   t_m.pop(savez)            
                   m1 = tuple(t_m)
                   m1 = m1 + (mmm2,)

                   t_m = list(m2)
                   t_m.pop(savep)            
                   m2 = tuple(t_m)
                   m2 = m2 + (mmm1,)

                   t_m = list(n1)
                   t_m.pop(savez)            
                   n1 = tuple(t_m)
                   n1 = n1 + (nnn2,)
                   
                   t_m = list(n2)
                   t_m.pop(savep)            
                   n2 = tuple(t_m)
                   n2 = n2 + (nnn1,)
                   break
                   
newnewnewnewsumt1 = 0
newnewnewnewsumt2 = 0



for k in range(localteam):
    newnewnewnewsumt1 = newnewnewnewsumt1 + m1[k]
    newnewnewnewsumt2 = newnewnewnewsumt2 + m2[k]

n1pass5 =()
n2pass5 =()
m1pass5 =()
m2pass5 =()
n1pass5 =n1
n2pass5 =n2
m1pass5 =m1
m2pass5 =m2

#final sum score
totalgamevalue = newnewnewnewsumt1+newnewnewnewsumt2
sumd_d = 0 

print(" ")
print(" ")
print("pass")

print("Results")
print(" ")
                             
print("Team 1 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n1[i]])

print(" ")
print ("Team 1 indervidual MMR rating")
print(n1)
print(m1)


print(" ")
print ("Team 1 combined MMR rating")
print (newnewnewnewsumt1)

print(" ")
print ("Calculated chance of team 1 victory")
print ((newnewnewnewsumt1/totalgamevalue)*100,"%")
print(" ") 
print(" ")             

print("Team 2 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n2[i]])
print(" ")
print ("Team 2 indervidual MMR rating")
print(n2)
print(m2)


print(" ")
print ("Team 2 combined MMR rating")
print (newnewnewnewsumt2)

print(" ")
print ("Calculated chance of team 2 victory")
print ((newnewnewnewsumt2/totalgamevalue)*100,"%")
print(" ")
if newnewnewnewsumt1 >= newnewnewnewsumt2:
    print ("Team 2 chooses to draft first or pick side of map")
    sumd_d = 1
else:
    print ("Team 1 chooses to draft first or pick side of map")
    sumd_d = 2

print(" ")    
print(" ")


print(" ")
print(" ")

if sumd_d == 1:
     sumd_d = newnewnewnewsumt1 - newnewnewnewsumt2
else:
     sumd_d = newnewnewnewsumt2 - newnewnewnewsumt1

print("this is the difference between the two teams")
print(sumd_d)

sumd_d_d = sumd_d/2 #this is the value that the second pass is trying to achieve

sumd_d_d = abs(sumd_d_d)

print(" ")
print(" ")

print("this is what I am looking for between differences of 2 numbers")


print(sumd_d_d)

teampass_fifth = 0
teampass_fifth = sumd_d_d

n02 = 0
cr02 = 0
n02 = 0
crn02 = 0
crncheck = 0
crnmatch = 0
localteam = 5
localteam2 = 5
localteam3 = 5
localteam4 = 5
localteam5 = 5
passcount = 0
savep = 0
savez = 0
saveletp = ()
saveletz = ()

t_m = []

swap1n = m1  #number for the player to swap 
swap2n = m2
swap1a = n1  #letter for the player to swap team 1 
swap2a = n2            
                   
checker = sumd_d_d
truechecker = 0
checkper = checker/15
print(" ")
print(" ")
print("THIS IS THE sixth PASS ")
print(" ")
print(" ")
               
for i in range(localteam): #populates the dictionary of both players and teamsort values with the given set 
    team1players[n1[i]] = m1[i]
    team2players[n2[i]] = m2[i]

for k in range(localteam): #okay so this is kinda cool but super ineffecient. I was originally planning on having the 2nd pass try every possible combination
                             #and then do a min on the closest one and use that as the switch value. But a better way is to have a small value slowly
                             #increment and when it finds a swap that is within the current tollarence of that check, then it breaks the loop
                             #then it will perform the swap and provide the new teams. This way I can simply just repeat the loop if required
                             #to continue have additional passes at the loop. This also allows me to change the tolerence to a higher value
    if checker < 0.1:
        print("it broke")
        break
    if k>0:                          
        checker = checker+checkper
    if truechecker == 1:
        
        break
    
    for j in range(localteam2):
          
                  
        
          crn02 = m2[j]
                   
          if truechecker == 1:
              break 
          for i in range(localteam3):
          
               passcount = passcount + 1 
               n02 = m1[i]
               crnmatch = crn02
               crncheck = crn02
               
               
               crncheck = crncheck  - n02
               crncheck = abs(crncheck)
               

               if crncheck <= checker and crncheck != 0:
                   truechecker = 1

                   

                   for p in range(localteam5):
                       
                       if m2[p] == crnmatch:
                           
                           savep = p
                           saveletp = n2[p]
                           

                           
                   for z in range(localteam4):
                       if m1[z] == n02:
                           
                           savez = z
                           saveletz = n1[z]

                   


                   
                   mmm1 = ()
                   mmm2 = ()
                   nnn1 = ()
                   nnn2 = ()
                   mmm1 = n02
                   mmm2 = crnmatch
                   nnn1 = saveletz
                   nnn2 = saveletp

                   t_m = list(m1)
                   t_m.pop(savez)            
                   m1 = tuple(t_m)
                   m1 = m1 + (mmm2,)

                   t_m = list(m2)
                   t_m.pop(savep)            
                   m2 = tuple(t_m)
                   m2 = m2 + (mmm1,)

                   t_m = list(n1)
                   t_m.pop(savez)            
                   n1 = tuple(t_m)
                   n1 = n1 + (nnn2,)
                   
                   t_m = list(n2)
                   t_m.pop(savep)            
                   n2 = tuple(t_m)
                   n2 = n2 + (nnn1,)
                   break
                   
newnewnewnewnewsumt1 = 0
newnewnewnewnewsumt2 = 0



for k in range(localteam):
    newnewnewnewnewsumt1 = newnewnewnewnewsumt1 + m1[k]
    newnewnewnewnewsumt2 = newnewnewnewnewsumt2 + m2[k]
n1pass6 =()
n2pass6 =()
m1pass6 =()
m2pass6 =()

n1pass6 =n1
n2pass6 =n2
m1pass6 =m1
m2pass6 =m2

#final sum score
totalgamevalue = newnewnewnewnewsumt1+newnewnewnewnewsumt2
sumd_d = 0 

print(" ")
print(" ")
print("pass")

print("Results")
print(" ")
                             
print("Team 1 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n1[i]])

print(" ")
print ("Team 1 indervidual MMR rating")
print(n1)
print(m1)


print(" ")
print ("Team 1 combined MMR rating")
print (newnewnewnewnewsumt1)

print(" ")
print ("Calculated chance of team 1 victory")
print ((newnewnewnewnewsumt1/totalgamevalue)*100,"%")
print(" ") 
print(" ")             

print("Team 2 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n2[i]])
print(" ")
print ("Team 2 indervidual MMR rating")
print(n2)
print(m2)


print(" ")
print ("Team 2 combined MMR rating")
print (newnewnewnewnewsumt2)

print(" ")
print ("Calculated chance of team 2 victory")
print ((newnewnewnewnewsumt2/totalgamevalue)*100,"%")
print(" ")
if newnewnewnewnewsumt1 >= newnewnewnewnewsumt2:
    print ("Team 2 chooses to draft first or pick side of map")
    sumd_d = 1
else:
    print ("Team 1 chooses to draft first or pick side of map")
    sumd_d = 2

print(" ")    
print(" ")


print(" ")
print(" ")

if sumd_d == 1:
     sumd_d = newnewnewnewnewsumt1 - newnewnewnewnewsumt2
else:
     sumd_d = newnewnewnewnewsumt2 - newnewnewnewnewsumt1

print("this is the difference between the two teams")
print(sumd_d)

sumd_d_d = sumd_d/2 #this is the value that the second pass is trying to achieve

sumd_d_d = abs(sumd_d_d)

print(" ")
print(" ")

print("this is what I am looking for between differences of 2 numbers")


print(sumd_d_d)

teampass_sixth = 0
teampass_sixth = sumd_d_d



n02 = 0
cr02 = 0
n02 = 0
crn02 = 0
crncheck = 0
crnmatch = 0
localteam = 5
localteam2 = 5
localteam3 = 5
localteam4 = 5
localteam5 = 5
passcount = 0
savep = 0
savez = 0
saveletp = ()
saveletz = ()

t_m = []

swap1n = m1  #number for the player to swap 
swap2n = m2
swap1a = n1  #letter for the player to swap team 1 
swap2a = n2            
                   
checker = sumd_d_d
truechecker = 0
checkper = checker/15
print(" ")
print(" ")
print("THIS IS THE sixth PASS ")
print(" ")
print(" ")
               
for i in range(localteam): #populates the dictionary of both players and teamsort values with the given set 
    team1players[n1[i]] = m1[i]
    team2players[n2[i]] = m2[i]

for k in range(localteam): #okay so this is kinda cool but super ineffecient. I was originally planning on having the 2nd pass try every possible combination
                             #and then do a min on the closest one and use that as the switch value. But a better way is to have a small value slowly
                             #increment and when it finds a swap that is within the current tollarence of that check, then it breaks the loop
                             #then it will perform the swap and provide the new teams. This way I can simply just repeat the loop if required
                             #to continue have additional passes at the loop. This also allows me to change the tolerence to a higher value
    if checker < 0.1:
        print("it broke")
        break
    if k>0:                          
        checker = checker+checkper
    if truechecker == 1:
        
        break
    
    for j in range(localteam2):
          
                  
        
          crn02 = m2[j]
                   
          if truechecker == 1:
              break 
          for i in range(localteam3):
          
               passcount = passcount + 1 
               n02 = m1[i]
               crnmatch = crn02
               crncheck = crn02
               
               
               crncheck = crncheck  - n02
               crncheck = abs(crncheck)
               
               
               

               if crncheck <= checker and crncheck != 0:
                   truechecker = 1

                   

                   for p in range(localteam5):
                       
                       if m2[p] == crnmatch:
                           savep = p
                           saveletp = n2[p]
                           

                           
                   for z in range(localteam4):
                       
                       if m1[z] == n02:
                           
                           savez = z
                           saveletz = n1[z]

                   


                   mmm1 = ()
                   mmm2 = ()
                   nnn1 = ()
                   nnn2 = ()
                   mmm1 = n02
                   mmm2 = crnmatch
                   nnn1 = saveletz
                   nnn2 = saveletp

                   t_m = list(m1)
                   t_m.pop(savez)            
                   m1 = tuple(t_m)
                   m1 = m1 + (mmm2,)

                   t_m = list(m2)
                   t_m.pop(savep)            
                   m2 = tuple(t_m)
                   m2 = m2 + (mmm1,)

                   t_m = list(n1)
                   t_m.pop(savez)            
                   n1 = tuple(t_m)
                   n1 = n1 + (nnn2,)
                   
                   t_m = list(n2)
                   t_m.pop(savep)            
                   n2 = tuple(t_m)
                   n2 = n2 + (nnn1,)
                   break
                   
_1newnewnewnewnewsumt1 = 0
_1newnewnewnewnewsumt2 = 0



for k in range(localteam):
    _1newnewnewnewnewsumt1 = _1newnewnewnewnewsumt1 + m1[k]
    _1newnewnewnewnewsumt2 = _1newnewnewnewnewsumt2 + m2[k]

n1pass7 =()
n2pass7 =()
m1pass7 =()
m2pass7 =()

n1pass7 =n1
n2pass7 =n2
m1pass7 =m1
m2pass7 =m2

#final sum score
totalgamevalue = _1newnewnewnewnewsumt1+_1newnewnewnewnewsumt2
sumd_d = 0 

print(" ")
print(" ")
print("pass")

print("Results")
print(" ")
                             
print("Team 1 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n1[i]])

print(" ")
print ("Team 1 indervidual MMR rating")
print(n1)
print(m1)


print(" ")
print ("Team 1 combined MMR rating")
print (_1newnewnewnewnewsumt1)

print(" ")
print ("Calculated chance of team 1 victory")
print ((_1newnewnewnewnewsumt1/totalgamevalue)*100,"%")
print(" ") 
print(" ")             

print("Team 2 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n2[i]])
print(" ")
print ("Team 2 indervidual MMR rating")
print(n2)
print(m2)


print(" ")
print ("Team 2 combined MMR rating")
print (_1newnewnewnewnewsumt2)

print(" ")
print ("Calculated chance of team 2 victory")
print ((_1newnewnewnewnewsumt2/totalgamevalue)*100,"%")
print(" ")
if _1newnewnewnewnewsumt1 >= _1newnewnewnewnewsumt2:
    print ("Team 2 chooses to draft first or pick side of map")
    sumd_d = 1
else:
    print ("Team 1 chooses to draft first or pick side of map")
    sumd_d = 2

print(" ")    
print(" ")


print(" ")
print(" ")

if sumd_d == 1:
     sumd_d = _1newnewnewnewnewsumt1 - _1newnewnewnewnewsumt2
else:
     sumd_d = _1newnewnewnewnewsumt2 - _1newnewnewnewnewsumt1

print("this is the difference between the two teams")
print(sumd_d)

sumd_d_d = sumd_d/2 #this is the value that the second pass is trying to achieve

sumd_d_d = abs(sumd_d_d)

print(" ")
print(" ")

print("this is what I am looking for between differences of 2 numbers")


print(sumd_d_d)

teampass_seventh = 0
teampass_seventh = sumd_d_d



n02 = 0
cr02 = 0
n02 = 0
crn02 = 0
crncheck = 0
crnmatch = 0
localteam = 5
localteam2 = 5
localteam3 = 5
localteam4 = 5
localteam5 = 5
passcount = 0
savep = 0
savez = 0
saveletp = ()
saveletz = ()

t_m = []

swap1n = m1  #number for the player to swap 
swap2n = m2
swap1a = n1  #letter for the player to swap team 1 
swap2a = n2            
                   
checker = sumd_d_d
truechecker = 0
checkper = checker/15
print(" ")
print(" ")
print("THIS IS THE sixth PASS ")
print(" ")
print(" ")
               
for i in range(localteam): #populates the dictionary of both players and teamsort values with the given set 
    team1players[n1[i]] = m1[i]
    team2players[n2[i]] = m2[i]

for k in range(localteam): #okay so this is kinda cool but super ineffecient. I was originally planning on having the 2nd pass try every possible combination
                             #and then do a min on the closest one and use that as the switch value. But a better way is to have a small value slowly
                             #increment and when it finds a swap that is within the current tollarence of that check, then it breaks the loop
                             #then it will perform the swap and provide the new teams. This way I can simply just repeat the loop if required
                             #to continue have additional passes at the loop. This also allows me to change the tolerence to a higher value
    if checker < 0.1:
        print("it broke")
        break
    if k>0:                          
        checker = checker+checkper
    if truechecker == 1:
        
        break
    
    for j in range(localteam2):
          
                  
        
          crn02 = m2[j]
                   
          if truechecker == 1:
              break 
          for i in range(localteam3):
          
               passcount = passcount + 1 
               n02 = m1[i]
               crnmatch = crn02
               crncheck = crn02
               
               
               crncheck = crncheck  - n02
               crncheck = abs(crncheck)
               
               
               

               if crncheck <= checker and crncheck != 0:
                   truechecker = 1

                   

                   for p in range(localteam5):
                       
                       if m2[p] == crnmatch:
                           
                           savep = p
                           saveletp = n2[p]
                           

                           
                   for z in range(localteam4):
                       
                       if m1[z] == n02:
                           
                           savez = z
                           saveletz = n1[z]

                   print(saveletp)
                   print(saveletz)


                   

                   


                   mmm1 = ()
                   mmm2 = ()
                   nnn1 = ()
                   nnn2 = ()
                   mmm1 = n02
                   mmm2 = crnmatch
                   nnn1 = saveletz
                   nnn2 = saveletp

                   t_m = list(m1)
                   t_m.pop(savez)            
                   m1 = tuple(t_m)
                   m1 = m1 + (mmm2,)

                   t_m = list(m2)
                   t_m.pop(savep)            
                   m2 = tuple(t_m)
                   m2 = m2 + (mmm1,)

                   t_m = list(n1)
                   t_m.pop(savez)            
                   n1 = tuple(t_m)
                   n1 = n1 + (nnn2,)
                   
                   t_m = list(n2)
                   t_m.pop(savep)            
                   n2 = tuple(t_m)
                   n2 = n2 + (nnn1,)
                   break
                   
_2newnewnewnewnewsumt1 = 0
_2newnewnewnewnewsumt2 = 0



for k in range(localteam):
    _2newnewnewnewnewsumt1 = _2newnewnewnewnewsumt1 + m1[k]
    _2newnewnewnewnewsumt2 = _2newnewnewnewnewsumt2 + m2[k]

n1pass8 =()
n2pass8 =()
m1pass8 =()
m2pass8 =()

n1pass8 =n1
n2pass8 =n2
m1pass8 =m1
m2pass8 =m2

#final sum score
totalgamevalue = _2newnewnewnewnewsumt1+_2newnewnewnewnewsumt2
sumd_d = 0 

print(" ")
print(" ")
print("pass")

print("Results")
print(" ")
                             
print("Team 1 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n1[i]])

print(" ")
print ("Team 1 indervidual MMR rating")
print(n1)
print(m1)


print(" ")
print ("Team 1 combined MMR rating")
print (_2newnewnewnewnewsumt1)

print(" ")
print ("Calculated chance of team 1 victory")
print ((_2newnewnewnewnewsumt1/totalgamevalue)*100,"%")
print(" ") 
print(" ")             

print("Team 2 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n2[i]])
print(" ")
print ("Team 2 indervidual MMR rating")
print(n2)
print(m2)


print(" ")
print ("Team 2 combined MMR rating")
print (_2newnewnewnewnewsumt2)

print(" ")
print ("Calculated chance of team 2 victory")
print ((_2newnewnewnewnewsumt2/totalgamevalue)*100,"%")
print(" ")
if _2newnewnewnewnewsumt1 >= _2newnewnewnewnewsumt2:
    print ("Team 2 chooses to draft first or pick side of map")
    sumd_d = 1
else:
    print ("Team 1 chooses to draft first or pick side of map")
    sumd_d = 2

print(" ")    
print(" ")


print(" ")
print(" ")

if sumd_d == 1:
     sumd_d = _2newnewnewnewnewsumt1 - _2newnewnewnewnewsumt2
else:
     sumd_d = _2newnewnewnewnewsumt2 - _2newnewnewnewnewsumt1

print("this is the difference between the two teams")
print(sumd_d)

sumd_d_d = sumd_d/2 #this is the value that the second pass is trying to achieve

sumd_d_d = abs(sumd_d_d)

print(" ")
print(" ")

print("this is what I am looking for between differences of 2 numbers")


print(sumd_d_d)

teampass_eigth = 0
teampass_eigth = sumd_d_d



n02 = 0
cr02 = 0
n02 = 0
crn02 = 0
crncheck = 0
crnmatch = 0
localteam = 5
localteam2 = 5
localteam3 = 5
localteam4 = 5
localteam5 = 5
passcount = 0
savep = 0
savez = 0
saveletp = ()
saveletz = ()

t_m = []

swap1n = m1  #number for the player to swap 
swap2n = m2
swap1a = n1  #letter for the player to swap team 1 
swap2a = n2            
                   
checker = sumd_d_d
truechecker = 0
checkper = checker/15
print(" ")
print(" ")
print("THIS IS THE sixth PASS ")
print(" ")
print(" ")
               
for i in range(localteam): #populates the dictionary of both players and teamsort values with the given set 
    team1players[n1[i]] = m1[i]
    team2players[n2[i]] = m2[i]

for k in range(localteam): #okay so this is kinda cool but super ineffecient. I was originally planning on having the 2nd pass try every possible combination
                             #and then do a min on the closest one and use that as the switch value. But a better way is to have a small value slowly
                             #increment and when it finds a swap that is within the current tollarence of that check, then it breaks the loop
                             #then it will perform the swap and provide the new teams. This way I can simply just repeat the loop if required
                             #to continue have additional passes at the loop. This also allows me to change the tolerence to a higher value
    if checker < 0.1:
        print("it broke")
        break
    if k>0:                          
        checker = checker+checkper
    if truechecker == 1:
        
        break
    
    for j in range(localteam2):
          
                  
        
          crn02 = m2[j]
                   
          if truechecker == 1:
              break 
          for i in range(localteam3):
          
               passcount = passcount + 1 
               n02 = m1[i]
               crnmatch = crn02
               crncheck = crn02
               
               
               crncheck = crncheck  - n02
               crncheck = abs(crncheck)
               
               
               

               if crncheck <= checker and crncheck != 0:
                   truechecker = 1

                   

                   

                   

                   for p in range(localteam5):
                       
                       if m2[p] == crnmatch:
                           
                           savep = p
                           saveletp = n2[p]
                           

                           
                   for z in range(localteam4):
                       
                       if m1[z] == n02:
                          
                           savez = z
                           saveletz = n1[z]

                   


                   


                   mmm1 = ()
                   mmm2 = ()
                   nnn1 = ()
                   nnn2 = ()
                   mmm1 = n02
                   mmm2 = crnmatch
                   nnn1 = saveletz
                   nnn2 = saveletp

                   t_m = list(m1)
                   t_m.pop(savez)            
                   m1 = tuple(t_m)
                   m1 = m1 + (mmm2,)

                   t_m = list(m2)
                   t_m.pop(savep)            
                   m2 = tuple(t_m)
                   m2 = m2 + (mmm1,)

                   t_m = list(n1)
                   t_m.pop(savez)            
                   n1 = tuple(t_m)
                   n1 = n1 + (nnn2,)
                   
                   t_m = list(n2)
                   t_m.pop(savep)            
                   n2 = tuple(t_m)
                   n2 = n2 + (nnn1,)
                   break
                   
_3newnewnewnewnewsumt1 = 0
_3newnewnewnewnewsumt2 = 0



for k in range(localteam):
    _3newnewnewnewnewsumt1 = _3newnewnewnewnewsumt1 + m1[k]
    _3newnewnewnewnewsumt2 = _3newnewnewnewnewsumt2 + m2[k]

n1pass9 =()
n2pass9 =()
m1pass9 =()
m2pass9 =()

n1pass9 =n1
n2pass9 =n2
m1pass9 =m1
m2pass9 =m2

#final sum score
totalgamevalue = _3newnewnewnewnewsumt1+_3newnewnewnewnewsumt2
sumd_d = 0 

print(" ")
print(" ")
print("pass")

print("Results")
print(" ")
                             
print("Team 1 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n1[i]])

print(" ")
print ("Team 1 indervidual MMR rating")
print(n1)
print(m1)


print(" ")
print ("Team 1 combined MMR rating")
print (_3newnewnewnewnewsumt1)

print(" ")
print ("Calculated chance of team 1 victory")
print ((_3newnewnewnewnewsumt1/totalgamevalue)*100,"%")
print(" ") 
print(" ")             

print("Team 2 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n2[i]])
print(" ")
print ("Team 2 indervidual MMR rating")
print(n2)
print(m2)


print(" ")
print ("Team 2 combined MMR rating")
print (_3newnewnewnewnewsumt2)

print(" ")
print ("Calculated chance of team 2 victory")
print ((_3newnewnewnewnewsumt2/totalgamevalue)*100,"%")
print(" ")
if _3newnewnewnewnewsumt1 >= _3newnewnewnewnewsumt2:
    print ("Team 2 chooses to draft first or pick side of map")
    sumd_d = 1
else:
    print ("Team 1 chooses to draft first or pick side of map")
    sumd_d = 2

print(" ")    
print(" ")


print(" ")
print(" ")

if sumd_d == 1:
     sumd_d = _3newnewnewnewnewsumt1 - _3newnewnewnewnewsumt2
else:
     sumd_d = _3newnewnewnewnewsumt2 - _3newnewnewnewnewsumt1

print("this is the difference between the two teams")
print(sumd_d)

sumd_d_d = sumd_d/2 #this is the value that the second pass is trying to achieve

sumd_d_d = abs(sumd_d_d)

print(" ")
print(" ")

print("this is what I am looking for between differences of 2 numbers")


print(sumd_d_d)

teampass_ninth = 0
teampass_ninth = sumd_d_d



n02 = 0
cr02 = 0
n02 = 0
crn02 = 0
crncheck = 0
crnmatch = 0
localteam = 5
localteam2 = 5
localteam3 = 5
localteam4 = 5
localteam5 = 5
passcount = 0
savep = 0
savez = 0
saveletp = ()
saveletz = ()

t_m = []

swap1n = m1  #number for the player to swap 
swap2n = m2
swap1a = n1  #letter for the player to swap team 1 
swap2a = n2            
                   
checker = sumd_d_d
truechecker = 0
checkper = checker/15
print(" ")
print(" ")
print("THIS IS THE sixth PASS ")
print(" ")
print(" ")
               
for i in range(localteam): #populates the dictionary of both players and teamsort values with the given set 
    team1players[n1[i]] = m1[i]
    team2players[n2[i]] = m2[i]

for k in range(localteam): #okay so this is kinda cool but super ineffecient. I was originally planning on having the 2nd pass try every possible combination
                             #and then do a min on the closest one and use that as the switch value. But a better way is to have a small value slowly
                             #increment and when it finds a swap that is within the current tollarence of that check, then it breaks the loop
                             #then it will perform the swap and provide the new teams. This way I can simply just repeat the loop if required
                             #to continue have additional passes at the loop. This also allows me to change the tolerence to a higher value
    if checker < 0.1:
        print("it broke")
        break
    if k>0:                          
        checker = checker+checkper
    if truechecker == 1:
        
        break
    
    for j in range(localteam2):
          
                  
        
          crn02 = m2[j]
                   
          if truechecker == 1:
              break 
          for i in range(localteam3):
          
               passcount = passcount + 1 
               n02 = m1[i]
               crnmatch = crn02
               crncheck = crn02
               
               
               crncheck = crncheck  - n02
               crncheck = abs(crncheck)
               

               if crncheck <= checker and crncheck != 0:
                   truechecker = 1

                   

                   for p in range(localteam5):
                       
                       if m2[p] == crnmatch:
                           
                           savep = p
                           saveletp = n2[p]
                           

                           
                   for z in range(localteam4):
                       
                       if m1[z] == n02:
                           
                           savez = z
                           saveletz = n1[z]

                   


                   mmm1 = ()
                   mmm2 = ()
                   nnn1 = ()
                   nnn2 = ()
                   mmm1 = n02
                   mmm2 = crnmatch
                   nnn1 = saveletz
                   nnn2 = saveletp

                   t_m = list(m1)
                   t_m.pop(savez)            
                   m1 = tuple(t_m)
                   m1 = m1 + (mmm2,)

                   t_m = list(m2)
                   t_m.pop(savep)            
                   m2 = tuple(t_m)
                   m2 = m2 + (mmm1,)

                   t_m = list(n1)
                   t_m.pop(savez)            
                   n1 = tuple(t_m)
                   n1 = n1 + (nnn2,)
                   
                   t_m = list(n2)
                   t_m.pop(savep)            
                   n2 = tuple(t_m)
                   n2 = n2 + (nnn1,)
                   break
                   
_4newnewnewnewnewsumt1 = 0
_4newnewnewnewnewsumt2 = 0



for k in range(localteam):
    _4newnewnewnewnewsumt1 = _4newnewnewnewnewsumt1 + m1[k]
    _4newnewnewnewnewsumt2 = _4newnewnewnewnewsumt2 + m2[k]

n1pass10 =()
n2pass10 =()
m1pass10 =()
m2pass10 =()

n1pass10 =n1
n2pass10 =n2
m1pass10 =m1
m2pass10 =m2

#final sum score
totalgamevalue = _4newnewnewnewnewsumt1+_4newnewnewnewnewsumt2
sumd_d = 0 

print(" ")
print(" ")
print("pass")

print("Results")
print(" ")
                             
print("Team 1 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n1[i]])

print(" ")
print ("Team 1 indervidual MMR rating")
print(n1)
print(m1)


print(" ")
print ("Team 1 combined MMR rating")
print (_4newnewnewnewnewsumt1)

print(" ")
print ("Calculated chance of team 1 victory")
print ((_4newnewnewnewnewsumt1/totalgamevalue)*100,"%")
print(" ") 
print(" ")             

print("Team 2 is ")
for i in range(numPlayersTeam):
    print(playerphonebook[n2[i]])
print(" ")
print ("Team 2 indervidual MMR rating")
print(n2)
print(m2)


print(" ")
print ("Team 2 combined MMR rating")
print (_4newnewnewnewnewsumt2)

print(" ")
print ("Calculated chance of team 2 victory")
print ((_4newnewnewnewnewsumt2/totalgamevalue)*100,"%")
print(" ")
if _4newnewnewnewnewsumt1 >= _4newnewnewnewnewsumt2:
    print ("Team 2 chooses to draft first or pick side of map")
    sumd_d = 1
else:
    print ("Team 1 chooses to draft first or pick side of map")
    sumd_d = 2

print(" ")    
print(" ")


print(" ")
print(" ")

if sumd_d == 1:
     sumd_d = _4newnewnewnewnewsumt1 - _4newnewnewnewnewsumt2
else:
     sumd_d = _4newnewnewnewnewsumt2 - _4newnewnewnewnewsumt1

print("this is the difference between the two teams")
print(sumd_d)

sumd_d_d = sumd_d/2 #this is the value that the second pass is trying to achieve

sumd_d_d = abs(sumd_d_d)

print(" ")
print(" ")

print("this is what I am looking for between differences of 2 numbers")


print(sumd_d_d)

teampass_tenth = 0
teampass_tenth = sumd_d_d

bestpass = ()

bestpass= (teampass_first,) + (teampass_second,) + (teampass_third,) + (teampass_fourth,) + (teampass_fifth,) + (teampass_sixth,) + (teampass_seventh,) + (teampass_eigth,) + (teampass_ninth,) +(teampass_tenth,)

print(bestpass)

lowpass = 100000
lowchk = 0
lowestchk = 0 
countlow = 0

for i in range (allpasses):
    lowchk = bestpass[i]
    countlow = countlow + 1
    if lowchk < lowpass:
        lowestchk = countlow
        lowpass = lowchk

print(" ")
print("lowest value is")

print(lowpass)

print(" ")
print("lowest chk is")
print(lowestchk)

print(" ")
print("check which pass was most accurate") #this works, just need to finish it off 
print(" ")

if lowestchk == 2:
    print(n1pass2, n2pass2, m1pass2, m2pass2)


print("check which pass was most accurate")
print(" ")

print("1st pass")
print(teampass_first)

print(" ")
print(" ")


print("2nd pass")
print(teampass_second)

print(" ")
print(" ")

print("3rd pass")
print(teampass_third)

print(" ")
print(" ")

print("4th pass")
print(teampass_fourth)

print(" ")
print(" ")

print("5th pass")
print(teampass_fifth)

print(" ")
print(" ")

print("6th pass")
print(teampass_sixth)

print(" ")
print(" ")


print("7th pass")
print(teampass_seventh)

print(" ")
print(" ")

print("8th pass")
print(teampass_eigth)

print(" ")
print(" ")

print("9th pass")
print(teampass_ninth)

print(" ")
print(" ")

print("10th pass")
print(teampass_tenth)

print(" ")
print(" ")




