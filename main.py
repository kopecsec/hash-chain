import hashlib # import

text = "ecsc" # nOOB and Noob has cases reversed, so ECSC becomes ecsc

counter = 0 # initialize counter int

while text!= 'c89aa2ffb9edcc6604005196b5f0e0e4': # compare chain hashes to the one were looking for

    text = hashlib.md5(text.encode()).hexdigest() # hash the ecsc text

    counter = counter + 1 # counter

    print(text) # print hashes

print("Total Hashes = " + str(counter)) # total hashes
