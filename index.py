#Sets - blazingly fast unordered Lists 
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}

my_friends_set = {'Reg','Tery','hanna','Neil','Eric'}
# print(friends)
# print(friends_tuple)
# print(friends_set)

# cheking , remeber no space

print(friends_set.intersection(my_friends_set))
# you can combine
print(friends_set.union(my_friends_set))

#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set() #should always be with set()

#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

print ('Eric' in friends)
print ('John' in friends)
print ('Eric' in friends and 'John' in friends)
print(friends.union(my_friends))
# or you can dwo other way: 
print (friends | my_friends)

#3. Find names that are in both sets
print(friends.intersection(my_friends))
print(friends & my_friends)

#4. find names that are only in friends
print(friends - my_friends)
print(my_friends.difference(friends))
#5. Show only the names who only appear in one of the lists
print(my_friends.symmetric_difference(friends))
# or 
print(my_friends ^ friends)
#6. Create a new cars-list without duplicates
cars_no_dupl = set(cars)
print(cars_no_dupl)
# list 
cars_no_dupl = list(set(cars)) 
print(cars_no_dupl)