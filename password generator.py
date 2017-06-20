def password():
    import string
    import random
    password=[]
    char="!@$%^&*=+."
    while len(password)<3:
        password.append(random.choice(char))
        password.append(random.choice(string.digits))
    while len(password)<8:
        password.append(random.choice(string.ascii_letters))
    random.shuffle(password,random=random.random)
    password=''.join(password)
    print password

password()

    
            
    
