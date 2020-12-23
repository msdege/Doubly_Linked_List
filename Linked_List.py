class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      #construct node,prev, and next (must be public so python can
      #actually access them). Make next and prev point to None.
      self.val=val
      self.next=None
      self.prev=None

  def __init__(self):
    #Initialize header and trailer and self.__size=0 (make them private).
    #Make header and trailer point to each other.
    self.__header=Linked_List.__Node(None)
    self.__trailer=Linked_List.__Node(None)
    self.__header.next=self.__trailer
    self.__trailer.prev=self.__header
    self.__size=0

  def __len__(self):
    return self.__size

  def append_element(self, val):
    #create new node, and using trailer Node, make proper links
    #so the new node is added at the end. Increase size by one.
    new_node=Linked_List.__Node(val)
    new_node.next=self.__trailer
    new_node.prev=self.__trailer.prev
    self.__trailer.prev=new_node
    new_node.prev.next=new_node
    self.__size+=1

  def insert_element_at(self, val, index):
    #raise index error if index is out of bounds or invalid
    if index<0 or index>self.__size-1 or isinstance(index, int)==False:
      raise IndexError
    new_node=Linked_List.__Node(val)   #create new node
    #split list into two halves
    if index<(self.__size/2):              #start at header, then walk 
      cur=self.__header                    #through to node just before
      for i in range(0,index):             #index. Link new node.
        cur=cur.next
      new_node.prev=cur
      new_node.next=cur.next
      cur.next=new_node
      new_node.next.prev=new_node
    elif index>=(self.__size/2):           #start at trailer, walk 
      cur=self.__trailer                   #backwards to node currently
      for i in range(0,self.__size-index): #at index you want to insert
        cur=cur.prev                       #at, then link new node.
      new_node.next=cur
      new_node.prev=cur.prev
      cur.prev=new_node
      new_node.prev.next=new_node
    self.__size+=1

  def remove_element_at(self, index):
    #raise index error if index is out of bounds or invalid
    if index<0 or index>self.__size-1 or isinstance(index, int)==False:
      raise IndexError
    #split list into two halves
    if index<(self.__size/2):         #start at header, then walk through
      cur=self.__header               #to node before one you want to
      for i in range(0,index):        #remove. Unlink and return node.
        cur=cur.next
      value=cur.next.val
      cur.next=cur.next.next
      cur.next.prev=cur
    elif index>=(self.__size/2):      #start at trailer, then walk
      cur=self.__trailer              #backwards to node just after 
      for i in range(1,self.__size-index):    #node you want to
        cur=cur.prev                          #remove. Unlink and 
      value=cur.prev.val                      #return node
      cur.prev=cur.prev.prev
      cur.prev.next=cur
    self.__size-=1
    return value

  def get_element_at(self, index):
    #raise index error if index is out of bounds or invalid
    if index<0 or index>self.__size-1 or isinstance(index, int)==False:
      raise IndexError
    #split list into two halves
    if index<(self.__size/2):         #start at header
      cur=self.__header.next
      for i in range(0,index):
        cur=cur.next
    elif index>=(self.__size/2):      #start at trailer
      cur=self.__trailer.prev
      for i in range(1,self.__size-index):
        cur=cur.prev
    return cur.val

  def rotate_left(self):
    if self.__size==0 or self.__size==1: #return if size is 0 or 1 since
      return                             #rotating does nothing
    cur=self.__header.next
    cur.prev=self.__trailer.prev         #rotate left by unlinking first
    self.__header.next=cur.next          #node and linking it between
    cur.next.prev=self.__header          #the last node and trailer,
    cur.next=self.__trailer              #and link header to new first
    self.__trailer.prev.next=cur         #node
    self.__trailer.prev=cur
    
  def __str__(self):
    #this method returns a string representation of list's contents
    if self.__size==0:
      return '[ ]'
    else:
      #initiate walk through list while appending value stored in each 
      #node to string
      cur=self.__header.next
      string='[ '
      for i in range(0,self.__size):  
        string+=(str(cur.val)+', ')
        cur=cur.next
      string=string[0:-2]               #remove extra comma and space.
    return string+' ]'                  #add final space and bracket

  def __iter__(self):
    #Create new attribute (self.__current) for walking through the list.
    #Make it point to first node with actual value.
    self.__current=self.__header.next
    return self

  def __next__(self):
    #Iteration must stop once the self.__current is pointing to Trailer.
    if self.__current.next is None:
      raise StopIteration
    return_this=self.__current.val         #return value stored in
    self.__current=self.__current.next     #current node, and update
    return return_this                     #pointer to point to next node

if __name__ == '__main__':
  test=Linked_List()
  print(test)
  #len() function should properly return self.__size without error.
  #current length should be 0.
  print('The current size of the list is '+str(len(test))+'.')

  #test insert, remove, get, and rotate_left methods on empty list
  try:
    test.insert_element_at(222,0)
  except IndexError:
    print('Caught attempt to insert on empty list. No crash!')
  try:
    test.remove_element_at(4)
  except IndexError:
    print('Caught attempt to remove from empty list. No crash!')
  try:
    test.get_element_at(0)
  except IndexError:
    print('Caught attempt to get element from empty list. No crash!')
  try:
    print('Rotating empty list left. Should result in no errors...')
    test.rotate_left()
    print('No errors occurred while rotating empty list')
  except:
    print('Error occurred while rotating empty list left.')
  print(test)
  
  #append 5 new elements to the list
  try:          #should append new elements without error
    print('Appending elements...')
    test.append_element(10)
    test.append_element(20)
    test.append_element(30)
    test.append_element(40)
    test.append_element(50)
  except:
    print('An unexpected error occurred while appending.')
  print(test)
  print('The length of the list should be 5. The current length is: '\
    +str(len(test)))
  
  #test insert_element_at() method with valid and invalid indices
  try:   
    print("Inserting elements at valid indices...")
    test.insert_element_at(5,0)           #valid indices, should work
    test.insert_element_at(15,2)
    test.insert_element_at(25,4)
  except IndexError:
    print('Error: Invalid index given for insertion.')
  print(test)
  print('The length of the list should be 8. The current length is: '\
    +str(len(test)))
  try:
    print('Attempting to insert element at invalid index...')
    test.insert_element_at(5,-4)           #invalid index, should crash
  except IndexError:
    print('Correctly caught IndexError exception: No crash occurred.')
  print(test)
  print('The length of the list should still be 8. The current length '\
    'is: '+str(len(test)))
  
  #test remove_element_at() method at valid and invalid indices
  try:
    print('Removing elements at valid indices...')
    test.remove_element_at(4)              #valid indices, should work
    test.remove_element_at(2)
    test.remove_element_at(0)
    print(test.remove_element_at(0)) #test if removed element is returned
  except IndexError:
    print('Error: Invalid index given for removal.')
  print(test)
  print('The returned element printed out on terminal should be 10.')
  print('The length of the list should be 4. The current length is: '\
    +str(len(test)))
  try:
    print('Attempting to remove at invalid index...')
    test.remove_element_at(5)              #invalid index, should crash
  except IndexError:
    print('Correctly caught IndexError exception: No crash occurred.')
  print(test)
  print('The length of the list should still be 4. The current length '\
    'is: '+str(len(test)))

  #test get_element_at() method with invalid and valid indices
  try:
    print('Getting first and last element in list...')
    print(test.get_element_at(0))         #valid indices, no error 
    print(test.get_element_at(3))         #should occur
  except IndexError:
    print('Unexpected error occurred. Invalid index.')
  print(test)
  print('Correctly got first and last elements in list. List should'\
    ' still be the same. Length should still be 4. The current '\
      'length is: '+str(len(test)))
  try:
    print('Attempting to get element at invalid index...')
    test.get_element_at(5)                #invalid index
  except IndexError:
    print('Correctly caught IndexError exception: No crash occurred.')
  print(test)
  print('The length of the list should still be 4. The current length' \
    ' is: '+str(len(test)))
  
  #test rotate_left() method on list of length 1 and greater
  try:
    print('Rotating list left...')
    test.rotate_left()
  except:
    print('Unexpected error occurred while rotating list left.')
  print(test)
  print('Previous first element should now be at the end of the list.'\
    ' The list length should still be 4. Current length is: '\
      +str(len(test)))

  #test __iter__ and __next__ by printing out each value contained in
  #the list using a for loop
  print('Appending some elements to list...')
  test.append_element(60)
  test.append_element(70)
  test.append_element(80)         #add some extra elements to the list
  test.append_element(90)
  test.append_element(100)
  print(test)
  print('Current size of list is: '+str(len(test)))
  #should successfully walk through list while printing out value
  #contained in each node (excluding header and trailer).
  try:
    print("Iterating through list using 'for' loop...")
    for i in test:
      print(i)
    print('Successfully iterated through list.')
  except:
    print('Unexpected error occcurred while iterating.')
  

  #test methods on list of size one
  test2=Linked_List()
  test2.append_element(123454321)
  print('New list of size 1 created to test methods on list of size 1.')
  print(test2,'Length of new list is: '+str(len(test2)))

  #test insert_element_at() method on list of size 1
  try:
    print('Inserting on list of size 1...')
    test2.insert_element_at(0.5, 0)        #only valid index is zero
  except IndexError:
    print('Invalid index given.')
  except:
    print('Error occurred while inserting on list of size 1.')
  print(test2)
  print('List should be length 2. Current length is: '+str(len(test2)))

  #test remove_element_at() method on list of size 1
  print('First, remove element just added in last case...')
  test2.remove_element_at(0)
  print(test2)
  try:
    print('Removing only element in the list...')
    test2.remove_element_at(0)            #only valid index is zero
  except IndexError:
    print('Invalid index given')
  except:
    print('Error occurred while removing from list of size 1.')
  print(test2)
  print('List is now empty. Length should be 0. Current length is: '\
    +str(len(test2)))

  #test get_element_at() on list of size 1
  test2.append_element(123454321)
  print('Add element to list so we can test get_element_at() on list' \
    ' of size zero.')
  try:
    print('Getting element in list of size zero...')
    print(test2.get_element_at(0))        #only valid index
  except IndexError:
    print('Invalid index given.')
  except:
    print('Unexpected error occurred while getting element')
  print(test2)
  print('List should remain unchanged. Length should still be 1.'\
    ' Current length is: '+str(len(test2)))
  
  #test rotate_left method on list of size 1
  try:
    print('Rotating list of size 1 left. List should be unchanged...')
    test2.rotate_left()
  except:
    print('Error occurred while rotating left on list of length 1.')
  print(test2)


  