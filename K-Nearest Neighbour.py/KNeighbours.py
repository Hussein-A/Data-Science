import csv
import math

data_1 = open('data1.csv')
data_2 = open('data2.csv')
data_3 = open('data3.csv')
data_4 = open('data4.csv')
data_5 = open('data5.csv')
data_6 = open('data6.csv')
data_7 = open('data7.csv')
data_8 = open('data8.csv')
data_9 = open('data9.csv')
data_10 = open('data10.csv')

labels_1 = open('labels1.csv')
labels_2 = open('labels2.csv')
labels_3 = open('labels3.csv')
labels_4 = open('labels4.csv')
labels_5 = open('labels5.csv')
labels_6 = open('labels6.csv')
labels_7 = open('labels7.csv')
labels_8 = open('labels8.csv')
labels_9 = open('labels9.csv')
labels_10 = open('labels10.csv')

closing_list = [data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10]



csv_data_1 = csv.reader(data_1)
csv_data_2 = csv.reader(data_2)
csv_data_3 = csv.reader(data_3)
csv_data_4 = csv.reader(data_4)
csv_data_5 = csv.reader(data_5)
csv_data_6 = csv.reader(data_6)
csv_data_7 = csv.reader(data_7)
csv_data_8 = csv.reader(data_8)
csv_data_9 = csv.reader(data_9)
csv_data_10 = csv.reader(data_10)



csv_labels_1 = csv.reader(labels_1)
csv_labels_2 = csv.reader(labels_2)
csv_labels_3 = csv.reader(labels_3)
csv_labels_4 = csv.reader(labels_4)
csv_labels_5 = csv.reader(labels_5)
csv_labels_6 = csv.reader(labels_6)
csv_labels_7 = csv.reader(labels_7)
csv_labels_8 = csv.reader(labels_8)
csv_labels_9 = csv.reader(labels_9)
csv_labels_10 = csv.reader(labels_10)

list_of_data = [csv_data_1, csv_data_2, csv_data_3, csv_data_4, csv_data_5, csv_data_6, csv_data_7, data_8, data_9, data_10]

list_labels_1 = []
list_labels_2 = []
list_labels_3 = []
list_labels_4 = []
list_labels_5 = []
list_labels_6 = []
list_labels_7 = []
list_labels_8 = []
list_labels_9 = []
list_labels_10 = []


for row in csv_labels_3:
    list_labels_3 =  list_labels_3+[int(row[0])]
##list_of_labels_2 = [list_labels_1, list_labels_2,list_labels_3,list_labels_4,list_labels_5,list_labels_6,list_labels_7,list_labels_8,list_labels_9,list_labels_10]

list_of_labels= []
csv_list_of_labels = [csv_labels_1, csv_labels_2,csv_labels_3,csv_labels_4,csv_labels_5,csv_labels_6,csv_labels_7,csv_labels_8,csv_labels_9,csv_labels_10]
for label_set in csv_list_of_labels:
    for row in label_set:
        list_of_labels = list_of_labels + [int(row[0])]

master_list = []
master_list_2 = []

second_list = ()
j=0


j = 0
x=0
for item in list_of_data[:7]:
    for row in (item): ## here i am converting each element of the row into an integer and forming a tuple of the row

        i = 0
        second_list = ()
        while i < len(row):
            second_list = second_list + (int(row[i]),)
            i = i + 1
        master_list = master_list + [[]]
        master_list[j] = [second_list]
        j = j+1
i = 0
while i < 777:
    master_list[i] = master_list[i] + [list_of_labels[i]]
    i = i+1
#I have now formed my list of data.


def distance(row,x): ## this is my distance function in Euclidean L_2 norm, takes a row vector and an x vector both of the same length
    i = 0
    sum = 0
    while i < len(row):
        sum = sum + pow(abs(row[i] - x[0][i]),2)
        i = i+1
    sum = math.sqrt(sum)
    return sum


k=0



i=0
## this part checks if all the data is matching up as it should be!
while i < 777:
    if not master_list[i][1] == list_of_labels[i]:
        print ("false at", i)

    i=i+1

##just making a vector from unused data for testing
j=0
for row in (csv_data_8): ## here i am converting each element of the row into an integer and forming a tuple of the row
    i = 0
    second_list = ()
    while i < len(row):
            second_list = second_list + (int(row[i]),)
            i = i + 1
    master_list_2 = master_list_2 + [[]]
    master_list_2[j] = [second_list]
    j = j+1

i=0

for label in list_of_labels[777:888]:
    master_list_2[i] = master_list_2[i] + [label]
    i = i+1
## a function to measure accuracy

def accuracy(prediction, reality):
    i = 0
    counter = 0
    while i < len(prediction):
        if prediction[i] == reality[i]:
            counter = counter +1
        i = i +1
    return 'only %', float(counter)/float(len(prediction_list)), 'were correct'

list= [1,2,3,4,5]


## now i will write the n-fold cross validation
j=1
newlist= []
data_set=[]





def k_nearest_neighbours(k,x,data_set):
    i =0
    list_of_distances = []
    list_of_nearest = []
    nearest_label = []
    for row in data_set:
        list_of_distances = list_of_distances +  [distance(row[0],x[0])]

    #list ofnearest not only returns numerical value of the distance to closest, but also what label it's attached to.
    while i < k:
        list_of_nearest = list_of_nearest+ [(list_of_distances[list_of_distances.index(min(list_of_distances))],data_set[list_of_distances.index(min(list_of_distances))][1],)]
        list_of_distances[list_of_distances.index(min(list_of_distances))] = max(list_of_distances)
        i = i +1
    for item in list_of_nearest:
        nearest_label = nearest_label + [item[1]]
# finding which label occurs the most.

    #print(nearest_label.count(5), nearest_label.count(6))
    if nearest_label.count(5) < nearest_label.count(6):
        return list_of_nearest, 6

    else:
        return list_of_nearest,5

prediction_list = []
reality = []
for i in range(1,8,1):
    j=i*111
    newlist = master_list[:j-111]+ master_list[j:]
    for item in master_list[j - 111:j][0]:
        print(k_nearest_neighbours(3,master_list[j-111:j],newlist))
        prediction_list = prediction_list + [k_nearest_neighbours(3,master_list[j-111:j],newlist)[1]]
    #accuracy(prediction_list, )
#print k_nearest_neighbours(30, master_list_2[1][0])

#accuracy(k_nearest_neighbours(7, master_list_2[0][0]), master_list_2[0][1])


#for i in range(0,111):
    #prediction_list = prediction_list + [k_nearest_neighbours(23, master_list_2[i][0])[1]]
    #2reality = reality + [master_list_2[i][1]]



#print(prediction_list)
#print(reality)

#print(accuracy(prediction_list, reality))

for item in closing_list:
    item.close()
