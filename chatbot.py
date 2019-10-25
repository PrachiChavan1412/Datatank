import sqlite3
import nltk
import os 
#import pytd.pandas_td as td
nltk.download('stopwords')
from nltk.corpus import stopwords 
#from nltk.stem.porter import PorterStemmer 
#import pytd



cacheStopWords = stopwords.words("english")

###Code to get the data from TD using the pytd 

# os.environ['TD_API_KEY'] = '10419/3c0963c6b2dce58101f54303b283ac837896077f'
# os.environ['TD_API_SERVER'] = 'https://api.treasuredata.com'


# engine = td.create_engine('presto:cdp_audience_27721')
# query = 'select first_name,last_name,email from customers'

# df = td.read_td_query(query,engine)
# df.set_index('email',inplace = True)

# print(df.head(5))

con = sqlite3.connect("chatbot.db")

# df.to_sql('customers',con,if_exists='replace',index = True)

c = con.cursor()
c.execute('select * from customers')
col_names = list(map(lambda x: x[0], c.description))
# print(col_names)
c.close()



chatbot_email = 'How are you ,Please provide your email address?'
print('chatbot: ' + chatbot_email)
Email = input('Me: ').strip() 




chatbot = 'How can we help you ?'
while True:
    #Chatbot first response
    print('chatbot: ' + chatbot)
    #Input from the user , if no input exit from the loop 
    H = input('Me: ').strip()
    if H == '':
        break

    H = H.lower()
    H = H.split()


    #Removed the Stemming code , not needed
    #ps = PorterStemmer()  
    #review = [ps.stem(word) for word in H
                #if not word in set(stopwords.words('english'))]  

    review = [word for word in H if word not in cacheStopWords]
    print(review)


    c = con.cursor()
    for item in review:
        for value in col_names:
            if (value == item):
                c.execute("select "+value+" from customers where email= '"+Email+"'")
                rows = c.fetchone()
                #print(rows)
                print('chatbot: ' + ''.join(rows))
                c.close()
                
    
    

    
   
    



