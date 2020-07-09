# - *- coding: utf- 8 - *-
import pypyodbc
import modul as m
F=[] #Initialization of the list F which contains nouns that referred to the quality's function.
S=[] #Initialization of the list S which contains nouns that referred to the customer's service function.
I=[] #Initialization of the list I which contains nouns that referred to the company's image function.
suf=[] #Initialization of the list of suffixes.
DQ={} #Initialization of the quality's dictionary that contains adjectives that describe the function of quality.
DC={} #Initialization of the customer's service dictionary that contains adjectives that describe the function of service.
DI={} #Initialization of the images's dictionary that contains adjectives that describe the function of image.
excepti=[] #Initialization of the exception list of stemming.
asimantes=[] #Initialization of the stop words list.
antist={}#Initialization of the dictionary for converting lowercase characters to uppercase.
neg=[] #Initialization of the negations' list.
food=open("C:/modules/food.txt",'r',encoding="utf8")
service=open("C:/modules/service.txt",'r',encoding="utf8")
image=open("C:/modules/image.txt",'r',encoding="utf8")
antistixies=open("C:/modules/kef-2.txt",encoding="utf8")
asiman=open("C:/modules/asimantes.txt",'r',encoding="utf8")
dicq=open("C:/modules/DQ.txt",'r',encoding="utf8")
dics=open("C:/modules/DS.txt",'r',encoding="utf8")
dici=open("C:/modules/DI.txt",'r',encoding="utf8")
suff=open("C:/modules/suffix.txt",'r',encoding="utf8")
exceptions=open("C:/modules/stemming_exceptions.txt",'r',encoding="utf8")
negative=open("C:/modules/negative.txt",'r',encoding="utf8")
#Creating a dictionary for converting the lowercase characters to uppercase.
for rec in antistixies:
    gramma=rec.split(',')
    kleidi=gramma[0]
    timi=gramma[1]
    timi=timi.strip('\n')
    antist[kleidi]=timi
antistixies.close()
#Creating a stop words list.
for rec in asiman:
    tim=rec.strip('/n')
    tim=tim.strip()
    asimantes.append(tim)
asiman.close()
asimantes.sort()
#Creating an exception list of stemming.
for rec in exceptions:
    tim=rec.strip('/n')
    tim=tim.strip()
    excepti.append(tim)
exceptions.close()
excepti.sort
#Creating a negation's list.
for rec in negative:
    tim=rec.strip('/n')
    tim=tim.strip()
    neg.append(tim)
negative.close()
neg.sort
#Creating a list for the aspects of food (list F).
for rec in food:
    timiq=rec.strip('/n')
    timiq=timiq.strip()
    F.append(timiq)
food.close()
#Creating a list for the aspects of customer service (List S).
for rec in service:
    timis=rec.strip('/n')
    timis=timis.strip()
    S.append(timis)
service.close()
#Creating a list for the aspects of image of the company (List I).
for rec in image:
    timii=rec.strip('/n')
    timii=timii.strip()
    I.append(timii)
image.close()
#Creating a list for removing the suffixes.
for rec in suff:
    timisuf=rec.strip('/n')
    timisuf=timisuf.strip()
    suf.append(timisuf)
suff.close()
#Creating the quality's dictionary (DoQi).
for line in dicq:
    polar=line.split(',')
    kleidi=polar[0]
    timiq=polar[1]
    timiq=timiq.strip('\n')
    DQ[kleidi]=float(timiq)
dicq.close()
#Creating the customer's service dictionary (DoS).
for line in dics:
    polari=line.split(',')
    kleidi=polari[0]
    timis=polari[1]
    timis=timis.strip('\n')
    DC[kleidi]=float(timis)
dics.close()
#Creating the image's dictionary (DoQi).
for line in dici:
    polarit=line.split(',')
    kleidi=polarit[0]
    timiI=polarit[1]
    timiI=timiI.strip('\n')
    DI[kleidi]=float(timiI)
dici.close()
#Access to the data base that contains the customers' evaluations and useful information for analysis (data set or training set or annotated set).
db_file = "C:/Users/Anastasios LIapakis/Dropbox/Phd/tasos_bigdata/PhD data/Code/Code_PhD/Final_program/modules/Annotated1.accdb"
user = 'admin'
password = ''

odbc_conn_str1 = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
odbc_conn_str2="DBQ={};UID={};PWD={}".format(db_file, user, password)
conn=odbc_conn_str1+odbc_conn_str2

#odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;UID=%s;PWD=%s' %\
#               (db_file, user, password)
conn = pypyodbc.connect(conn)
rev = conn.cursor()
sql="select * from Reviews"

rev.execute(sql)
x=rev.fetchall()
#Retrieving the customers' reviews.
for pedio in x:
    frasi= str(pedio[3])
    kwd=str(pedio[0])
#Initialization of: (1) the number of aspects in each customer's review.
#                   (2) the overall evaluation of the quality, customer service and image functions in each customer's review.
    sall=0;ns=0;nq=0;ni=0;sq=0;ss=0;si=0
#Conerting the special characters. There is a lack of resources in the NLTK library for the Greek language.
    change_from=[]
    change_to=[]
    change_from,change_to=m.read_replace()
    frasii=m.allagi(frasi,change_from,change_to)
    print(frasii)
#Converting the lowercase characters to uppercase in the review.
    n_frasi= ""
    for gra in frasii:
        neo=m.metatr(gra,antist)
        n_frasi= n_frasi + neo
#Splitting the customer's review into terms.
    n_frasi=" ".join([word for word in n_frasi.split() if word not in (asimantes)])
    lex=n_frasi.split(" ")
    teliko=""
#Stemming the review's terms.There is a lack of resources in the NLTK library for the Greek language.
    for lexii in lex:
        new=m.stem(lexii,excepti,suf)
        teliko=teliko+" "+new
    teliko=teliko.split(' ')
    print('Το review προς αξιολόγηση έπειτα από την προεπεξεργασία είναι:',teliko,kwd)
    thesi=-1
#Determining the terms' position.
    for lexi in teliko:
        thesi=thesi+1
#Identifying a specific aspect from the list of Food (List F).
        if lexi in F:
            print('Θέση φαγητού:',thesi,'//','Λέξη προς αξιολόγηση ποιότητας:',lexi)
#Evaluating the specific food aspect.
            axiolq=m.evaluate_quality(teliko,thesi,DQ,F,neg)
#Identifying the number of food's aspects in the review.
            if axiolq!=0:
                nq=nq+1
#Computing the overall sentiment score of the review for the function of food's quality.
            sq=sq+axiolq
#Identifying a specific aspect from the list of customer service (List S).
        if lexi in S:
            print('Θέση εξυπηρέτησης:',thesi,'//''Λέξη προς αξιολόγηση εξυπηρέτησης:',lexi)
#Evaluating the specific customer service aspect.
            axiols=m.evaluate_service(teliko,thesi,DC,S,neg)
            if axiols!=0:
#Identifying the number of custome'r service aspects in the review.
                ns=ns+1
#Computing the overall sentiment score of the review for the function of customer's service.
            ss=ss+axiols
#Identifying a specific aspect from the list of image (List I).
        if lexi in I:
            print('Θέση εικόνας:',thesi,'//''Λέξη προς αξιολόγηση εικόνας:',lexi)
#Evaluating the specific image aspect.
            axioli=m.evaluate_image(teliko,thesi,DI,I,neg)
            if axioli!=0:
#Identifying the number of image aspects in the review.
                ni=ni+1
#Computing the overall sentiment score of the review for the function of company's image.
            si=si+axioli
#Computing the average sentiment score of the review for the function of food's quality.
    if nq!=0:
        overalll_quality=(sq/nq)
        print("Η ΑΞΙΟΛΟΓΗΣΗ ΤΗΣ ΕΞΥΠΗΡΕΤΗΣΗΣ ΕΙΝΑΙ:",overalll_quality)
#Saving the average sentiment score of the review for the function of food's quality in the database.
        if overalll_quality!=0:
            entoli="update reviews set quality={} where kleidi={}".format(overalll_quality,kwd)
            rev.execute(entoli)
            conn.commit()
#Computing the average sentiment score of the review for the function of customer's service.
    if ns!=0:
        overalll_service=(ss/ns)
        print("Η ΑΞΙΟΛΟΓΗΣΗ ΤΗΣ ΕΞΥΠΗΡΕΤΗΣΗΣ ΕΙΝΑΙ:", overalll_service)
#Saving the average sentiment score of the review for the function of customer's service in the database.
        if overalll_service!=0:
            entoli="update reviews set service={} where kleidi={}".format(overalll_service,kwd)
            rev.execute(entoli)
            conn.commit()
#Computing the average sentiment score of the review for the function of company's image.
    if ni!=0:
        overalll_image=(si/ni)
        print("Η ΑΞΙΟΛΟΓΗΣΗ ΤΗΣ ΕΙΚΟΝΑΣ ΤΟΥ ΚΑΤΑΣΤΗΜΑΤΟΣ ΕΙΝΑΙ:", overalll_image)
#Saving the average sentiment score of the review for the function of company's image in the database.
        if overalll_image!=0:
            entoli="update reviews set image={} where kleidi={}".format(overalll_image,kwd)
            rev.execute(entoli)
            conn.commit()
