from time import time

# part one of the project

def tperror (prompt) :
    global inwords

    words = prompt.split()
    error = 0

    for i in range (len(inwords)) :
        if i in ( 0 , len(inwords) - 1) :
            if inwords[i] == words[i] : 
                continue
            else : 
                error = error + 1
        else :
            if inwords[i] == words[i] :
                if(inwords[i + 1] == words[i + 1]) & (inwords[i - 1] == words[i - 1]) :
                    continue
                else :
                    error += 1 
            else :
                error += 1
    return error

 # part two of the project

def speed ( inprompt , stime , etime) :
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time

    return speed

# part three of the project

def elapsedtime (stime , etime) : 
    time = etime - stime 
    return time

if __name__ == "__main__":
    prompt = "Hello there are you the fastets one in the world or no hell oin my python project good bye nice to meet you"
    print ("Type This :- " , prompt , " ")

    input ("Prees Enter When You Are Ready To Chek Your Typing Speed")
    print ( "Hello there are you the fastets one in the world or no hell oin my python project good bye nice to meet you" )

    stime = time()
    inprompt = input()
    etime = time()

    time = round (elapsedtime(stime , etime ), 2)
    speed = speed
    error= tperror(prompt)


    print ( "###########################################################################################################################################################################" )
    print ( "Total Time Elapsed: ", time ,"Seconds" )
    print ( "Your Average Typing Speed Was " , speed , "Words Per Minute (w/m)")
    print ( "With Total " , error , "errors" )

    print ( "###########################################################################################################################################################################" )
