# Remove Duplicates from Linked List

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # initialize left and right pointers
    leftPtr = linkedList
    rightPtr = linkedList.next

    while rightPtr is not None:
        # compare the values at left and right pointers
        if leftPtr.value == rightPtr.value:
        # if the values are the same, then
            # while (leftPtr.value == rightPtr.value) and rightPtr is not None:
            while rightPtr is not None and (leftPtr.value == rightPtr.value):
            # advance right pointer until the values at left and right are different (or the right pointer is None)
                rightPtr = rightPtr.next
            # At that point assign leftPtr.next to rightPtr
            leftPtr.next = rightPtr
        # advance both pointers
        leftPtr = leftPtr.next
        if rightPtr is not None:
            rightPtr = rightPtr.next

    return linkedList
