import nltk
from newspaper import Article
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import random
import string



article = Article('https://www.lpu.in/')
article.download()
article.parse()
article.nlp()
f = article.text
text = f



sentencelist = nltk.sent_tokenize(text)



lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

Introduce_Ans = ["Lpu mate","My name is lpu mate you can call me your mate ;-).","Im lpumate :) ","My name is Lpumate. and my nickname is lpu and i am happy to solve your queries :) "]
GREETING_INPUTS = ("hello", "hi","hiii","hii","hiiii","hiiii", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "hii there", "hi there", "hello", "I am glad! You are talking to me",'Hello',"Hey :-)", "Hello, thanks for visiting",
        "Hi there, what can I do for you?","Hi there, how can I help?"]

bye = ["bye","see you","catch you later"]
doubt = ("help","helpme","i need a help?","query",'doubt')
answer = "Are you a student or parent ?"
stu = ["student"]
stures = ['what is your query?', 'how can i help you','Is there something through which i can help you ? ']

payres = ['what is your query?', 'how can i help you','Is there something through which i can help you ? ']
par =['parent' ]

string=['payment','acdemics','fee','result','marks','placements','scholarship','reappear','assignments','practical','administrative','attendance','exams','timetable' ]
string1=['enter student course', 'can you type student course']

thanksuser =[ 'thank you','thanks','thankyou' "That's helpful", "Thank's a lot!" ,'thank you so much']
thanksbot = ["Happy to help!", "Any time!", "My pleasure"]
noted=['your course and query are noted someone will reach you shortly and is there any other queries Y/N','done , wait till someone contacts you and is there any other queries Y/N']
course=["cse","ece","bba","mba","bpharmacy","fashiondesigning","architecture","msc","bsc"]
yoo= ['y','yes','Yes','Y']
restart = ['then type query', 'If yes type helpme','you can type doubt']
nai=['n','N','No','no']
final=['Have a Good Day buddy','I hope you enjoyed my company;-)']
# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def basic(sentence):
    for word in doubt:
        if sentence.lower() == word:
            return answer
def finall(sentence):
    for word in nai:
        if sentence.lower() == word:
            return random.choice(final)
def restarts(sentence):
    for word in yoo:
        if sentence.lower() == word:
            return random.choice(restart)






def thanks(sentence):
    for word in thanksuser:
        if sentence.lower() == word:
            return random.choice(thanksbot)
def student(sentence):
    for word in sentence.split():
        if word.lower() in stu:
            return random.choice(stures)
def parent(sentence):
    for word in sentence.split():
        if word.lower() in par:
            return random.choice(payres)
def query(sentence):
    for word in sentence.split():
        if word.lower() in string:
            return random.choice(string1)
def notes(sentence):
    for word in course:
        if sentence.lower() == word:
            return random.choice(noted)

# Checking for Introduce
def IntroduceMe(sentence):
    return random.choice(Introduce_Ans)
def byeMe(sentence):
    return random.choice(bye)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



      
# Generating response
def responseone(user_response):
    robo_response=''
    sentencelist.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sentencelist)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sentencelist[idx]
        return robo_response


def chat(user_response):
    
    
    user_response=user_response.lower()
    keyword = " student "
    keywordone = " student"
    keywordsecond = "student "
    
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            #print("ROBO: You are welcome..")
            return byeMe(user_response) 
        elif(basic(user_response)!=None):
                    return basic(user_response)
            
        else:
            if(notes(user_response)!=None):
                return notes(user_response)
            elif(finall(user_response)!=None):
                return finall(user_response)
                
            elif(restarts(user_response)!=None):
                return restarts(user_response)
         
            else:
                if(user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(keywordsecond) != -1):
                #print("ROBO: ",end="")
                #print(responseone(user_response))
                    return responseone(user_response)
                    sentencelist.remove(user_response)
                elif(greeting(user_response)!=None):
                #print("ROBO: "+greeting(user_response))
                    return greeting(user_response)
                elif(query(user_response)!=None):
                    return query(user_response)
                
                elif(student(user_response)!=None):
                    return student(user_response)
                   
                elif(parent(user_response)!=None):
                    return parent(user_response)
                
                elif(user_response.find("catch you later") != -1 or user_response.find(" catch you later") != -1 or user_response.find("catch you later ") != -1 or user_response.find("  catch you later ") != -1):
                    return byeMe(user_response)
               
                elif(user_response.find("your name") != -1 or user_response.find(" your name") != -1 or user_response.find("your name ") != -1 or user_response.find(" your name ") != -1):
                    return IntroduceMe(user_response)
                elif(basic(user_response)!=None):
                    return basic(user_response)
                
                else:
                #print("ROBO: ",end="")
                #print(response(user_response))
                    return responseone(user_response)
                    sentencelist.remove(user_response)
    
    else:
        flag=False
        #print("ROBO: Bye! take care..")
        return "Bye! take care.."