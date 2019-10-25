#!flask/bin/python
from flask import Flask
import sqlite3
# import nltk
# import os 
# import pytd.pandas_td as td
# nltk.download('stopwords')
from nltk.corpus import stopwords 
# from nltk.stem.porter import PorterStemmer 
# import pytd



app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     cacheStopWords = stopwords.words("english")

#     ###Code to get the data from TD using the pytd 

#     # os.environ['TD_API_KEY'] = '10419/3c0963c6b2dce58101f54303b283ac837896077f'
#     # os.environ['TD_API_SERVER'] = 'https://api.treasuredata.com'


#     # engine = td.create_engine('presto:cdp_audience_27721')
#     # query = 'select first_name,last_name,cdp_customer_id,email,street, city ,state from customers'

#     # df = td.read_td_query(query,engine)
#     # df.set_index('email',inplace = True)

#     #print(df.head(5))

#     con = sqlite3.connect("chatbot.db")

#     # df.to_sql('customers',con,if_exists='replace',index = True)

#     c = con.cursor()
#     c.execute('select * from customers')
#     col_names = list(map(lambda x: x[0], c.description))
#     #print(col_names)
#     c.close()



#     chatbot_email = 'How are you ,Please provide your email address?'
#     return('chatbot: ' + chatbot_email)
#     Email = input('Me: ').strip() 
#     return(Email)





@app.route('/', methods=['GET'])
def email():
    chatbot_email = 'How are you ,Please provide your email address?'
    return('chatbot:  ' + chatbot_email)


if __name__ == '__main__':
    app.run(debug=True)