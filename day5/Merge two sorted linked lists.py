

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):

    new_list = []
    
    while(head1!=None and head2!=None):
        if(head1.data < head2.data):
            new_list.append(head1.data)
            head1 = head1.next
        else:
            new_list.append(head2.data)
            head2 = head2.next
    if head1 == None:
        while(head2!=None):
            new_list.append(head2.data)
            head2 = head2.next
    else:
        while(head1!=None):
            new_list.append(head1.data)
            head1 = head1.next 
            
    linked_list = SinglyLinkedList()
    for item in new_list:
        linked_list.insert_node(item)
        
    return linked_list.head

