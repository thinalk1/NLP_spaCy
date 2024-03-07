import spacy

nlp = spacy.load("en_core_web_lg")
description = "I would like the weather to be warm , where the cost of living would be around 100000 rupees and the WIFI connectivity around 50mbps"
weather=""
cost_of_living=""
connectivity=""
descriptionList=[]
descriptionList=description.split(" ")
cost_of_living = nlp("50000") #converts the string "50,000" to a NLP object
connectivity = nlp("50mbps")
weather = nlp("cold tropical warm windy")
wifi=""
weathertype=""
costOfLiving=""

    
for word in descriptionList: #iterates through the array
    word_similarity1 = nlp(word).similarity(cost_of_living) #checks the word similarity
    word_similarity2 = nlp(word).similarity(connectivity)
    word_similarity3 = nlp(word).similarity(weather)

    if word_similarity1 > 0.8:
        print("cost of living: " + word)
        if (int(word)>=100000 and int(word)<500000):
            costOfLiving="average"

        if (int(word)<100000 and int(word)>0):
            costOfLiving="low"

        if (int(word)>500000):
            costOfLiving="high"

    if word_similarity2 > 0.8:
        print("connectivity: " + word)
        word =word[:-4]
        if (int(word)>50 and int(word)<100):
            wifi="average"

        if (int(word)<=50 and int(word)>0):
            wifi="low"

        if (int(word)>100):
            wifi="high"
        
    if word_similarity3 > 0.8 and word != "weather":
        print("weather: " + word)
        if (word.lower()=="tropical"):
            weathertype="tropical"

        if (word.lower()=="cold"):
            weathertype="cold"

        if (word.lower()=="warm"):
            weathertype="warm"
        
        if (word.lower()=="sunny"):
            weathertype="sunny"
            

if (costOfLiving=="average" and wifi=="low" and weathertype=="warm"):
    print("colombo")

else:
    print("no location")