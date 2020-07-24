#Function for converting the special characters.
change_from=[]
change_to=[]
def allagi(lex,apo,se):
    for gramma in lex:
        if ord(gramma)<32:
            lex.replace(gramma,"^")
    pl=len(apo)
    for i in range(pl):
        lex=lex.replace(apo[i],se[i])
    return lex
def read_replace():
    arxeio=open("C:\PhD/aaaa.txt",'r',encoding="utf8")
    allagi_apo=[]
    allagi_se=[]
    for rec in arxeio:
        rec=rec.strip()
        pedio=rec.split(';')
        pedio[0]=pedio[0].replace('"','')
        pedio[1]=pedio[1].replace('"','')
        allagi_apo.append(pedio[0])
        allagi_se.append(pedio[1])
    arxeio.close()
    return allagi_apo, allagi_se
#Function for stemming the customer's review terms. There is a lack of resources in the NLTK library for the Greek language.
def stem(word,excep,suffixes):
    if word in excep:
        return word
    done = len(word)<=3
    if not done:
        for suffix in suffixes:
            if stemma(word, suffix):
                word = word[:len(word) - len(suffix)]
    else:
        word=word
    return word
def stemma(word, suffix):
    return word[len(word) - len(suffix):]==suffix
#Function for converting the lowercase characters to uppercase.There is a lack of resources in the NLTK library for the Greek language.
def metatr(let,antistt):
    if  let in antistt:
        gr=antistt.get(let)
    else:
        gr=let
    return gr
#Input: (1)the list of terms(le) of the examined review after the pre-processing proccedure.
#       (2)the position of the aspect that is identified by the list of customer service(thes).
#       (3)the customer’s service dictionary (DOS).
#	    (4)the list of customer’s service aspects (LF).
#	    (5)the negations’ list (NE).
#Output: the customer's evaluation for the specific customer service aspect.
def evaluate_service(le,thes,DOS,LS,NE):
#Initialization of the customer's evaluation for the specific customer service aspect.
    eval_service=0
#Τhe program searches for an adjective in DoS in the previous location (j-1) of the aspect and
#examines the following possibilities.
#the word in the first position previous the aspect is adjective and contained in the service's dictionary.
    if le[thes-1] in DOS:
        #the word in the first position after the aspect is (.) or (,) or ("").
        if le[thes+1]=='.'or le[thes+1]==',' or le[thes+1]=='':
            #the word in the second position previous the aspect is adjective and contained in the service's dictionary.
            if le[thes-2]in DOS:
                #the word in the third position previous the aspect is noun and contained in the list of service aspects.
                if le[thes-3]in LS:
                    #the polarity value is provided by the adjective in the first position previous of the aspect.
                    eval_service=DOS[le[thes-1]]
                else:
                    #the polarity value is provided by the average of adjectives in the first and second previous positions of the aspect.
                    eval_service=(DOS[le[thes-1]]+DOS[le[thes-2]])/2
                    #the word in the second position previous the aspect is contained in the negations' list.
            elif le[thes-2]in NE:
                #the polarity value is provided by the adjective's opposite polarity in the first position previous of the aspect.
                eval_service=-DOS[le[thes-1]]
            else:
                #the polarity value is provided by the adjective in the first position previous of the aspect.
                eval_service=DOS[le[thes-1]]
                #the word in the first position after the aspect is adjective and contained in the service's dictionary
        elif le[thes+1] in DOS:
            #the word in the second position after the aspect is (.) or (,) or ("").
            if le[thes+2]=='.' or le[thes+2]==',' or le[thes+2]=='':
                #the polarity value is provided by the average of adjectives in the first previous and first after positions of the aspect.
                eval_service=(DOS[le[thes-1]]+DOS[le[thes+1]])/2
                #the word in the second position after the aspect is noun and contained in the list of service aspects.
            elif le[thes+2] in LS:
                #the polarity value is provided by the adjective in the first position previous of the aspect.
                eval_service=DOS[le[thes-1]]
                #the word in the second position previous the aspect is (.) or (,) or ("").
        elif le[thes-2]=='.'or le[thes-2]==','or le[thes-2]=='':
            #the word in the second position after the aspect is adjective and contained in the service's dictionary.
            if le[thes+2] in DOS:
                #the polarity value is provided by the average of adjectives in the first previous and second after positions of the aspect.
                eval_service=(DOS[le[thes+2]]+DOS[le[thes-1]])/2
            else:
                #the polarity value is provided by the adjective in the first position previous of the aspect.
                eval_service=DOS[le[thes-1]]
                #the word in the second position previous the aspect is adjective and contained in the service's dictionary.
        elif le[thes-2] in DOS:
            #the polarity value is provided by the average of adjectives in the first and second positions previous of the aspect.
            eval_service=(DOS[le[thes-1]]+DOS[le[thes-2]])/2
        else:
            #the polarity value is provided by the adjective in the first previous position of the aspect.
            eval_service=DOS[le[thes-1]]
#Τhe program searches for an adjective in DoQl in the after location(j+1)of the aspect and examines
#the following possibilities in the case that there is no adjective in location “j-1”.
        #the word in the first position after the aspect is adjective and contained in service's dictionary
    elif le[thes+1] in DOS:
        #the word in the second poistion after the aspect is (.) or (,) or ("").
        if le[thes+2]=='.'or le[thes+2]==','or le[thes+2]=='':
            #the word in the first position previous the aspect is contained in negations' list.
            if le[thes-1] in NE:
                #the polarity value is provided by the adjective's opposite polarity in the first position after the aspect.
                eval_service=-DOS[le[thes+1]]
            else:
                #the polarity value is provided by the adjective in the first position after the aspect.
                eval_service=DOS[le[thes+1]]
                #the word in the second position after the aspect is adjective and contained in the service's dictionary.
        elif le[thes+2]in DOS:
            #the word in the third position after the aspect is noun and contained in the list of service aspects.
            if le[thes+3]in LS:
                #the polarity value is provided by the adjective in the first position after the aspect.
                eval_service=DOS[le[thes+1]]
                #the word in the third position after the aspect is (.) or (,) or ("")
            elif le[thes+3]==',' or le[thes+3]=='.'or le[thes+3]=='':
                #the polarity value is provided by the average of adjectives in the first and second positions after the aspect.
                eval_service=(DOS[le[thes+1]]+DOS[le[thes+2]])/2
                #the word in the third position after the aspect is adjective and contained in the service's dictionary.
            elif le[thes+3]in DOS:
                #the word in the fourth position after the aspect is noun and contained in the list of service aspects.
                if le [thes+4]in LS:
                    #the polarity value is provided by the average of adjectives in the first and second positions after the aspect.
                    eval_service=(DOS[le[thes+1]]+DOS[le[thes+2]])/2
                else:
                    #the polarity value is provided by the average of adjectives in the first, second and third position after the aspect.
                    eval_service=(DOS[le[thes+1]]+DOS[le[thes+2]]+DOS[le[thes+3]])/3
            else:
                #the polarity value is provided by the average of adjectives in the first and second position after the aspect.
                eval_service=(DOS[le[thes+1]]+DOS[le[thes+2]])/2
                #the word in the second position after the aspect is noun and contained in the list of service aspects.
        elif le[thes+2] in LS:
            #the polarity value is provided by the adjective in the first position after the aspect.
            eval_service=DOS[le[thes+1]]
        else:
            #the polarity value is provided by the adjective in the first position after the aspect.
            eval_service=DOS[le[thes+1]]
            #the word in the first position after the aspect is (.) or (,) or ("").
    elif le[thes+1]=='.' or le[thes+1]=='' or le[thes+1]==',':
        #the polarity value equals to zero.
        eval_service=0
#It moves to the location “j+2” and examines the following possibilities in the case that there is
#no adjective in locations “j-1”and "j+1".
    #the word in the second position previous the aspect is adjective and contained in the service's dictionary.
    elif le[thes-2] in DOS:
        #the polarity value is provided by the adjective in the second position previous the aspect.
        eval_service=DOS[le[thes-2]]
    else:
        #the polarity value equals to zero.
        eval_service=0
    return eval_service
#Input: (1)the list of terms(le) of the examined review after the pre-processing proccedure.
#       (2)the position of the aspect that is identified by the list of image of the company(thes).
#       (3)the image's dictionary (DOS).
#	    (4)the list of image's aspects (LF).
#	    (5)the negations’ list (NE).
#Output: the customer's evaluation for the specific image aspect.
def evaluate_image(le,thes,DOI,LI,NE):
    eval_image=0
#Τhe program searches for an adjective in DoI in the previous location (j-1) of the aspect and
#examines the following possibilities.
    if le[thes-1] in DOI:
        if le[thes+1]=='.'or le[thes+1]==',' or le[thes+1]=='':
            if le[thes-2]in DOI:
                if le[thes-3]in LI:
                    eval_image=DOI[le[thes-1]]
                else:
                    eval_image=(DOI[le[thes-1]]+DOI[le[thes-2]])/2
            elif le[thes-2]in NE:
                eval_image=-DOI[le[thes-1]]
            else:
                eval_image=DOI[le[thes-1]]
        elif le[thes+1] in DOI:
            if le[thes+2]=='.' or le[thes+2]==',' or le[thes+2]=='':
                eval_image=(DOI[le[thes-1]]+DOI[le[thes+1]])/2
            elif le[thes+2] in LI:
                eval_image=DOI[le[thes-1]]
        elif le[thes-2]=='.'or le[thes-2]==','or le[thes-2]=='':
            if le[thes+2] in DOI:
                eval_image=(DOI[le[thes+2]]+DOI[le[thes-1]])/2
            else:
                eval_image=DOI[le[thes-1]]
        elif le[thes-2] in DOI:
            eval_image=(DOI[le[thes-1]]+DOI[le[thes-2]])/2
        else:
            eval_image=DOI[le[thes-1]]
#Τhe program searches for an adjective in DoI in the after location(j+1)of the aspect and examines
#the following possibilities in the case that there is no adjective in location “j-1”.
    elif le[thes+1] in DOI:
        if le[thes+2]=='.'or le[thes+2]==','or le[thes+2]=='':
            if le[thes-1] in NE:
                eval_image=-DOI[le[thes+1]]
            else:
                eval_image=DOI[le[thes+1]]
        elif le[thes+2]in DOI:
            if le[thes+3]in LI:
                eval_image=DOI[le[thes+1]]
            elif le[thes+3]==',' or le[thes+3]=='.'or le[thes+3]=='':
                eval_image=(DOI[le[thes+1]]+DOI[le[thes+2]])/2
            elif le[thes+3]in DOI:
                if le [thes+4]in LI:
                    eval_image=(DOI[le[thes+1]]+DOI[le[thes+2]])/2
                else:
                    eval_image=(DOI[le[thes+1]]+DOI[le[thes+2]]+DOI[le[thes+3]])/3
            else:
                eval_image=(DOI[le[thes+1]]+DOI[le[thes+2]])/2
        elif le[thes+2] in LI:
            eval_image=DOI[le[thes+1]]
        else:
            eval_image=DOI[le[thes+1]]
    elif le[thes+1]=='.' or le[thes+1]=='' or le[thes+1]==',':
        eval_image=0
#It moves to the location “j+2” and examines the following possibilities in the case that there is
#no adjective in locations “j-1”and "j+1".
    elif le[thes+2] in DOI:
        if le [thes+3]=='.'or le[thes+3]==',' or le[thes+3]=='':
            if le[thes+1]in NE:
                eval_image=-DOI[le[thes+2]]
            else:
                eval_image=DOI[le[thes+2]]
        elif le [thes+3] in LI:
            if le[thes+4] in DOI:
                eval_image=DOI[le[thes+2]]
        else:
            eval_image=DOI[le[thes+2]]
#It moves to the location “j-2” in the case that there is no adjective
#in locations “j-1”and "j+1".
    elif le[thes-2] in DOI:
        eval_image=DOI[le[thes-2]]
    else:
        eval_image=0
    return eval_image
#Input: (1)the list of terms(le) of the examined review after the pre-processing procedure.
#       (2)the position of the aspect that is identified by the list of food(thes).
#       (3)the quality’s dictionary (DOQ).
#	    (4)the list of food aspects (LF).
#	    (5)the negations’ list (NE).
#Output: the customer's evaluation for the specific food aspect.
def evaluate_quality(le,thes,DOQ,LF,NE):
#Initialization of the customer's evaluation for the specific food aspect.
    eval_qual1=0
#Τhe program searches for an adjective in DoQl in the previous location (j-1) of the aspect and
#examines the following possibilities.
    if le[thes-1] in DOQl:
        if le[thes+1]=='.' or le[thes+1]==',' or le[thes+1]=='':
            if le[thes-2]in DOQl:
                if le[thes-3]in LF:
                    eval_qual1=DOQl[le[thes-1]]
                else:
                    eval_qual1=(DOQl[le[thes-1]]+DOQl[le[thes-2]])/2
            elif le[thes-2]in NE:
                eval_qual1=-DOQl[le[thes-1]]
            else:
                eval_qual1=DOQl[le[thes-1]]
        elif le[thes+1] in DOQl:
            if le[thes+2]=='.' or le[thes+2]==',' or le[thes+2]=='':
                eval_qual1=(DOQl[le[thes-1]]+DOQl[le[thes+1]])/2
            elif le[thes+2] in LF:
                eval_qual1=DOQl[le[thes-1]]
        elif le[thes-2]=='.'or le[thes-2]==','or le[thes-2]=='':
            if le[thes+2] in DOQl:
                eval_qual1=(DOQl[le[thes+2]]+DOQ[le[thes-1]])/2
            else:
                eval_qual1=DOQl[le[thes-1]]
        elif le[thes-2] in DOQl:
            eval_qual1=(DOQl[le[thes-1]]+DOQl[le[thes-2]])/2
        else:
            eval_qual1=DOQl[le[thes-1]]
#Τhe program searches for an adjective in DoQi in the after location(j+1)of the aspect and examines
#the following possibilities in the case that there is no adjective in location “j-1”.
    elif le[thes+1] in DOQl:
        if le[thes+2]=='.'or le[thes+2]==','or le[thes+2]=='':
            if le[thes-1] in NE:
                eval_qual1=-DOQl[le[thes+1]]
            else:
                eval_qual1=DOQl[le[thes+1]]
        elif le[thes+2]in DOQl:
            if le[thes+3]in LF:
                eval_qual1=DOQl[le[thes+1]]
            elif le[thes+3]==',' or le[thes+3]=='.'or le[thes+3]=='':
                eval_qual1=(DOQl[le[thes+1]]+DOQl[le[thes+2]])/2
            elif le[thes+3]in DOQl:
                if le [thes+4]in LF:
                    eval_qual1=(DOQl[le[thes+1]]+DOQl[le[thes+2]])/2
                else:
                    eval_qual1=(DOQl[le[thes+1]]+DOQl[le[thes+2]]+DOQl[le[thes+3]])/3
            else:
                eval_qual1=(DOQl[le[thes+1]]+DOQl[le[thes+2]])/2
        elif le[thes+2] in LF:
            eval_qual1=DOQl[le[thes+1]]
        else:
            eval_qual1=DOQl[le[thes+1]]
    elif le[thes+1]=='.' or le[thes+1]=='' or le[thes+1]==',':
        eval_qual1=0
#It moves to the location “j+2” and examines the following possibilities in the case that there is
#no adjective in locations “j-1”and "j+1".
    elif le[thes+2] in DOQ:
        if le [thes+3]=='.'or le[thes+3]==',' or le[thes+3]=='':
            if le[thes+1]in NE:
                eval_qual1=-DOQl[le[thes+2]]
            else:
                eval_qual1=DOQl[le[thes+2]]
        elif le [thes+3] in LF:
            if le[thes+4] in DOQl:
                eval_qual1=DOQl[le[thes+2]]
        else:
            eval_qual1=DOQl[le[thes+2]]
#It moves to the location “j-2” in the case that there is no adjective
#in locations “j-1”and "j+1".
    elif le[thes-2] in DOQl:
        eval_qual1=DOQl[le[thes-2]]
    else:
        eval_qual1=0
    return eval_qual1
