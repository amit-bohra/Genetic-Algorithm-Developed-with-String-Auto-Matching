import random

population='abcdefghijklmnopqrstuvwxyz 1234567890ABCDEFGHIJKLMNOPQRSTUVWX'  #initial population 
popu=list(population)   #initial population list
inp=input('Enter Target ')  #string to be generated or searched
target=list(inp)    #converting string into list
length=len(target)  #length of given target list
fit_count=0     #total number of fitness checked
cross_count=0   #total number of crossover happend
mut_count=0     #total number of mutation happend




def cgen():     #chromosome generating function
    chrome1=[]  #chromosome will be list
    for i in range(length):
        a=random.choice(popu)   #randomly selecting from population list
        chrome1.append(a)
    return chrome1      #returning chromosome

def fitcal(chrome1): #fitness calculating function
    ind=[]          #index list of the indexes of character matched
    fit=0           #fit counter
    for i in range(length):
        if(chrome1[i]==target[i]):  #checking chromose index value with target index value respectively
            fit+=1                  #if found then fitness is increased by 1
            ind.append(i)           #and matched value's index is appended on list
    return fit,ind                  #return fitness and index list

def cross(chrome1,chrome2):         #cross over function takes two chromosomes
    for i in range(1,length):       #swap all elements of the chromosomes after 1st element
        temp=chrome1[i]
        chrome1[i]=chrome2[i]
        chrome2[i]=temp
    return chrome1,chrome2          #returns two chromosomes after crossover


def mutate(chrome1,inde):           #mutates a single chromosomes and also takes list of index at which fitness was found
    listy=list(range(0,length))     #list of indexes from 0 to length of target string
    while(True):
        a=random.choice(listy)      #randomly chooses a index
        if a not in inde:
            r=random.choice(population) #if index is incorrect or not matched in fitness it mutates
            chrome1[a]=r            #change the value from random population at index that not matched and break
            break
        else:
            continue
    return chrome1              #return mutated chromosome

chr1=cgen()         #generate first chromosome
chr2=cgen()         #generate second chromosome
print('initial',chr1)
print('initial',chr2)
final1=[]
final2=[]
fit1,inde1=fitcal(chr1)
fit2,inde2=fitcal(chr2)
fit_count+=1
print('initially',fit1)  #print fitness
print('initial',fit2)
if(fit1==length or fit2==length):       #if fitness==length of given string then chromosome found and break
    final1=chr1
    final2=chr2
else:
    while(True):
        chr1,chr2=cross(chr1,chr2)
        print('cross chr1 ',chr1)
        print('cross chr2 ',chr2)
        cross_count+=1
        fit1,inde1=fitcal(chr1)
        fit2,inde2=fitcal(chr2)
        fit_count+=1
        print('')
        print('cross fitval 1 ',fit1)
        print('cross fitval 2 ',fit2)
        if(fit1==length or fit2==length):
            final1=chr1
            final2=chr2
            break
        else:
            chr1=mutate(chr1,inde1)
            chr2=mutate(chr2,inde2)
            print('mutate chr1 ',chr1)
            print('mutate chr2 ',chr2)
            mut_count+=1
            fit1,inde1=fitcal(chr1)
            fit2,inde2=fitcal(chr2)
            fit_count+=1
            print('mutate fit 1 ',fit1)
            print('mutate fit 2 ',fit2)
            if(fit1==length or fit2==length):
                final1=chr1
                final2=chr2
                break
            else:
                continue
print('final chr1 ',final1)
print('final chr2 ',final2)

new1=''
new2=''
for i in final1:
    new1+=i
for j in final2:
    new2+=j

print('')
print('Entered string ',inp)
print('')
print('string1 ',new1)
print('string2 ',new2)
print('')
print('total time fitness calculated ',fit_count)
print('total time crossover occured ',cross_count)
print('total time mutation occured ',mut_count)
    
    
            
        
        
        
    
        


    

    
