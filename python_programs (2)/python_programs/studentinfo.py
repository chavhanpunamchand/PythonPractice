
values = {22,33,44,0,5,55,66,666}    # set -->
v1 = values.pop()    # will remove --> first element --> after placing it inside hashtable --> jo first- will removed
print(v1)



import sys
sys.exit(0)









#list -- 10     --> 0-9 --> 0 - len(list)-1
#list - complex type ne -->

#complex types ->
        #properties read -->
        # methods -- list out -->

#excel sheet -->    sheet1 --> list --> all methods -->
                    #sheet2 --> set --> all methods -->
                    #and so on
#list -> append,extend,index,pop,remove,insert,count,sort,copy*,reverse
#tuple --> index,count
#set -->
#dict-->


values =(1,2,3,4)
values= [2,11,2,11,33,11,55]        # append --> will increment by 1
values.pop(0)        #remove specified index element +ve --> 0 to len-1
values.pop(-8)      # 7-1--> error --> 7-8-- -1 ??   -ve --> -len to -1

values.index(11) # find out index position of the given element --> first found cha index-->
values.insert(3,44) # insert 44 element at 3rd index position --> 3rd index position -- shift by +1index


values= [2,11,2,11,33,11,55]        # append --> will increment by 1
print(values)
ind1 = values.index(11)  # 1        #index(11,0,7)-->
print(ind1)
ind2 = values.index(11,ind1+1,len(values))   # index(11,2,7) -->    3
print(ind2)
values.pop(ind2)    # remove--> 2nd 11 -->

print(values)

#v1 = values[2:5] #--> give a list ---> started from zero index--> till 5th index
#print(v1)# --> 2,11,2,11,33
import sys
sys.exit(0)


index = values.index(11)    # 11 cha index -- 1
print(index)

import sys
sys.exit(0)

#values.reverse()        # rev -- desc-->        [1,2,5,4,3]
                                              # [3,4,5,2,1] --> [5,4,3,2,1] --> [1,2,3,4,5]
values.insert(3,111)    # 2  1  2 111 55

print(values)

import sys
sys.exit(0)

                                #extend will increment it by --> no of elements inside complex type
print('Before -->',values)
values.sort(reverse=True)   # asc order --> desc

print('After -->',values)

import sys
sys.exit(0) # after line num ur code will stop-->

values.append(1)    # will add the element at last --> len index la add karel
values.pop(33)   # will remove the element of --> 3rd index -- 44    --> pop --> 0 to len-1
values.remove(3)    # will remove first matching element -->3 absent --> error
values.extend([]) #
values.count(22)    # count the no of times element present--> no of occurenences
values.clear()  # will remove all elements , list will be empty

print('Original List-->',values)
values.append(22)   #append - simple-- complex type pn --> size + 1
values.append(22)   #extend la --> only complex type --> size + len of complex type
values.append([1,2,3,4,5])   # error     # extend la--> complex type --> simple type
print('Change zaleli list   -->',values)    #[10,22,33,44,55,22,22,1,2,3,4,5]
                                     #0  1  2   3  4  5  6  7 8 9 10 11

#values.pop(10)  # pop la index--> 10th index -- value will be remove    ---> 0 - len(list)-1


values.remove(22) # first matching 22

print('Change zaleli list',values)

             #extent             append
#complex       yes                  yes     --> size --> extend [depends on num of element] --> append by 1
#simple         error               yes     --> NA                                          --> by 1

# how to sort-- list- incase of hetro elements*

