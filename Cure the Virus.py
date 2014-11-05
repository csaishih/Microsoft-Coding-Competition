import itertools

if __name__ == "__main__":
    #read from input file
    lines = [line.strip() for line in open('PracticeInput3.txt')]

    numberOfPeople = int(lines[0].split(' ')[0])
    lengthOfPeopleDNA = int(lines[0].split(' ')[1])
    lengthOfVirusDNA = int(lines[0].split(' ')[2])

    virus = lines[len(lines) - 1]
    
    virusMutations = [] #keep track of all mutations of the virus
    people = [] #keep track of the resident's DNA and the probability of
                #of this person getting the virus

    #get the resident's DNA
    for i in range(1, len(lines) - 1):
        people.append([lines[i], 0]); #initially everyone has 0% chance
                                      #to get the virus
        
    for i in range(0, lengthOfVirusDNA):
        for item in list(itertools.combinations(virus, i+1)):
            a = ""
            for things in item:
                a += things
            virusMutations.append(a)
            
    #Gets rid of duplicates in the list        
    virusMutations = list(set(virusMutations))

    #find the chance that each person will get the virus
    for person in people:
        for item in virusMutations:
            if item in person[0]:
                percentage = float(len(item))/lengthOfVirusDNA
                if percentage > person[1]:
                    person[1] = percentage                

    chances = [] #keep track of the different possibilities of getting the virus
    
    for person in people:
        if person[1] not in chances:
            chances.append(person[1])

    chances.sort()
    counter = 0
    
    for person in people:
        print("Person #" + str(counter) + ": " + str(list(reversed(chances)).index(person[1]) + 1) + ".")
        counter += 1
    
