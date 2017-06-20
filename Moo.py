def cowgame():
    print "Welcome to the Cows and Bulls Game!"
    import random
    rnd=random.randint(1000,9999)
    rnd=str(rnd)
    guess=raw_input("Enter a four digit number:")
    count=0
    bull=0
    cow=0
    while guess>0:
        if guess==' ':
            print "Please enter a value"
        if guess<'1000':
            print 'CAUGHT YOU CHEATER!!! TRY AGAIN'
            guess=raw_input("Enter a four digit number:")
        else:
            count=count+1
            if len(guess)!=4:
                print'the value you gave was not a four digit number'
                guess=raw_input("Enter a four digit number:")
            else:
                if guess==rnd:
                    print "You win!",rnd,"is the number"
                    print "you made",count,"guesses"
                    break
                else:
                    for i in range(0,len(guess)):
                        for z in range(0,len(rnd)):
                            if guess[i]==rnd[z] and i==z:
                                cow=cow+1
                            elif guess[i]==rnd[z] and i!=z:
                                bull=bull+1
                                if guess.count(guess[i])>1:
                                    bull=bull-1     
                    print 'you have',cow,'cow(s)'
                    print 'you have',bull,'bull(s)'
                    bull=0
                    cow=0
                    guess=0
                    guess=raw_input("Enter a four digit number:")
    
