import random
def shuffle(list):
    for i in range(len(list)-1):
        index = random.randint(i+1, len(list)-1)
        while (index == i):
            index = random.randint(i+1, len(list)-1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list

givers = ['anne','andrew','ben','bwohan','ivan','susannah']
receivers = ['anne','andrew','ben','bwohan','ivan','susannah']
print(givers)
# result: ['ben', 'bwohan', 'susannah', 'anne', 'andrew', 'ivan']
#print(shuffle(givers))
'''RESULTS: anne gives to ben
andrew gives to bwohan
ben gives to susannah
bwohan gives to anne
ivan gives to andrew
susannah gives to ivan'''

def probabilitycounting(list):
    counters = [0,0,0,0,0,0]
    for i in range(1000):
        l = shuffle(list)
        for j in range(len(l)):
            if (givers[j] == l[j]):
                counters[j] += 1
    return counters

print(probabilitycounting(receivers))