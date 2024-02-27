import numpy as np
import pandas as pd

'''
VERY VERY IMPORTANT 
WHEN CLEANING THE TEXT FILE MAKE SURE THERE ARE NO NEW LINES AT THE END 
NO EMPTY LINES IN THE TEXT FILE


and no empty lines in the begining
'''




content = open('modified.txt','r' ).read() 
size_content = len(content) 
prices= [ "bid" , "ask" , " oct 95 " , "oct 98" , "diesel","gas","crude" , "omt", "sayrafa" ] 
counter_category = 0;
category = prices[counter_category]
index = ''
value = ''
volume = ''

data = {} # Final data stored in this dict 
precedente_rupture = 0
counter_rupture = 0 #BINARY NUMBER THAT CHANGES WHENEVR THERE IS A RUPTURE BETWEEN INDEX AND VALUE  
for i in range(size_content):
    if ord(content[i]) == 10:  # ASCII 10 corresponds to char: new line
        counter_category +=1 
        category = prices[counter_category]
    if category!= "sayrafa":
        if (48 <= ord(content[i]) <= 57) or ( ord(content[i]) == 46): #if digit 
            if counter_rupture == 0:
                index += content[i]
                #print(index,"this is index       ",i )
            else:
                value += content[i]           
                #print(value,"this is value" , i)

            if( (ord(content[i+1]) < 48) or (ord(content[i+1]) > 57 )) and ord(content[i+1])!= 46  :  #if SUCCEEDING non digit 
                precedente_rupture = counter_rupture

                counter_rupture = (counter_rupture + 1 )% 2 	#equal to one when there is a sepation : used in ordet to add to  value which comes after 
        couple_rupture = counter_rupture - precedente_rupture 
        if (couple_rupture) ==-1 : 
            #print("we have here a couple rupture")
            if category not in data:
                data[category] = {}
            if index != "" and value != "":
                data[category][(index)] = (value)

            index = ""
            value = "" 
            precedente_rupture = 0 
            counter_rupture = 0
    else:
        if (48 <= ord(content[i]) <= 57) or ( ord(content[i]) == 46): #if digit 
            if counter_rupture == 0:
                index += content[i]
                #print(index,"this is index       ",i )
            elif counter_rupture == 1 :
                value += content[i]           
                #print(value,"this is value" , i)
            else:
                volume += content[i]
            if( (ord(content[i+1]) < 48) or (ord(content[i+1]) > 57 )) and ord(content[i+1])!= 46  :  #if SUCCEEDING non digit 
                precedente_rupture = counter_rupture
                counter_rupture = (counter_rupture + 1 )% 3 	#equal to one when there is a sepation : used in ordet to add to  value which comes after 
        couple_rupture = counter_rupture - precedente_rupture 
        if (couple_rupture) ==-2 : 
            #print("we have here a couple rupture")
            if category not in data:
                data[category] = {}
            if index != "" and value != "":
                data[category][(index)] = (value,volume)
            index = ""
            value = "" 
            volume = ""
            precedente_rupture = 0 
            counter_rupture = 0


'''
everything above is if not sayrafa 
i need to add else (i.e. if there is sayrafa) 
the diff in sayrafa is that there are 2 values volume and value
'''
for i in data:
    print("this is :" + i)

print(data["sayrafa"])

#array_bid = np.array(data["bid"])

#df = pd.DataFrame(data)
#print(df)
