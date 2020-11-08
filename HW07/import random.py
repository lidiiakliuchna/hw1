import random

d = {}
f = open("noun.txt", "r", encoding="utf-8")
s = f.read()
words = s.split()
def noun():
   
    nouns = words
    return random.choice(nouns)
 

    
f_3 = open("adj.txt", "r", encoding="utf-8")
s_3 = f_3.read()
words_3 = s_3.split() 
def adjective(word):
    
    adjectives = words_3
    return random.choice(adjectives) + ' ' + word
 
    
f_4 = open("verb.txt", "r", encoding="utf-8")
s_4 = f_4.read()
words_4 = s_4.split() 
def verb():
    
    verbs = words_4
    return random.choice(verbs)
 
f_5 = open("question.txt", "r", encoding="utf-8")
s_5 = f_5.read()
words_5 = s_5.split() 
def question():
 
    question = words_5
    return random.choice(question)

f_6 = open("imperative.txt", "r", encoding="utf-8")
s_6 = f_6.read()
words_6 = s_6.split() 
def imperative():

    imperative = words_6
    return random.choice(imperative)

f_7 = open("nounimperative.txt", "r", encoding="utf-8")
s_7 = f_7.read()
words_7 = s_7.split() 
def noun_imperative():

    noun_imperative = words_7
    return random.choice(noun_imperative) 
 
def random_sentence():

    sentence = adjective(noun()) + ' ' + verb() +'.'+\
        ' ' + question() + ' ' + adjective(noun()) + ' ' + verb() + '?'+\
        ' ' + adjective(noun()) + ' ' + 'не' + ' ' +verb()+'.'+\
        ' ' + 'если' + ' ' + adjective(noun())  + ' ' +verb()+ ',то'+ ' ' + adjective(noun()) + ' ' + 'не' + ' ' +verb()+'.'+\
        ' ' + imperative() + ' ' + noun_imperative() + '.'

    return sentence
 
def main():

    print(random_sentence())
    return 0
 

if __name__ == '__main__':
    main()