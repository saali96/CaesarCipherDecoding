#!/usr/bin/env python
# coding: utf-8

# In[204]:


def decrypt(encryptedMessage):
    #Extracting all the numbers form the encrypted message
    keys = ([int(s) for s in encryptedMessage.split() if s.isdigit()])
    
    #Defining the listy of alphabets
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    
    #Converting the string to lowercase because the alphabet list is also lowercase
    encryptedMessage=encryptedMessage.lower()
    decryptedMessage = ""
    
    #iterating over each extracted numbers which we will use to shift letters
    for j in range(len(keys)):
        #checking for only numbers below than 200 because the original string contains 10000 which is not a key
        if keys[j] < 200:
            #iterating over each letter in the original string
            for i in encryptedMessage:
                #checking for current letter, if it is in our list of alphabets then proceed
                if i in alphabets:
                    #finding the index of current letter in our list of alphabets then subtracting the index by the shift key
                    #and using modulus for number of letter in our list I.e. 26. This will return us the decrypted letter index
                    letter_index = (alphabets.find(i) - keys[j]) % len(alphabets)
                    
                    #Adding the decrpted letter index to our string variable
                    decryptedMessage = decryptedMessage + alphabets[letter_index]
                else:
                    #if current alphabet is not found on the list of lphabets then add the letter as it is
                    decryptedMessage = decryptedMessage + i
    #returning the decrypted string
    return decryptedMessage


# In[205]:


#Original encrypted String
encryptedMessage = "28 03 99 vjg ugetgvu hqt dgkpi iqqf cv etarvqitcrja ku vq rtcvkeg cp kpetgfkdng coqwpv qh jqwtu vtblqj ghfubswlqj brxu rzq fbskhuwhaw zlwk udqgrp qxpehuv dv nhbv. brx frxog xvh udqgrp nhb bzizmvodji vgbjmdochn. oj wz xjindyzmzy vn v hvnozm, v ojovg ja 10000 cjpmn dn mzlpdmzy"

#Decrypt function returns the decrypted string
a=decrypt(encryptedMessage)
print(a)


# In[206]:


#Since we're iterating over thr number of keys, we're getting unencrypted plus some gibberish words as well.
#After Filtering manually, we found this message.
FinalMessage = 'the secrets for being good at cryptography is to pratice an incredible amount of hours decrypting your own cyphertext with random numbers as keys. you could use random key generation algorithms. to be considered as a master, a total of 10000 hours is required.'
FinalMessage
print("")
print("CLEANED MESSAGE",FinalMessage)

# In[ ]:




