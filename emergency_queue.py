class Patient:
    def __init__(self, name, urgency):
        """
        A class to represent a node in the priority queue.
            Attributes:
                name (str): The name of the patient.
                urgency (int): An integer from 1 to 10, where 1 is the most urgent.
        """
        self.name = name
        self.urgency = urgency

class MinHeap:
    """
    A class to represent a patient queue.
        Attributes:
            data (list): A list of patient objects. Index 0 is the root of the heap and the patient with the lowest urgency score (highest priority patient)
    """
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        """ Starts at the last index and sorts the heap by comparing the urgency scores of nodes  """
        while index > 0:
            #Get parent index for current child index
            parent_index = (index - 1) // 2

            #Assign patients
            current_patient = self.data[index]
            parent_patient = self.data[parent_index]

            #Check if current patient's urgency attribute is smaller than its parent
            if current_patient.urgency < parent_patient.urgency:
                #if it's smaller, move the current patient up the list
                temp = self.data[index]
                self.data[index] = self.data[parent_index]
                self.data[parent_index] = temp

                #Move up heap
                index = parent_index
            else:
                #Stop if the current patient's urgency attribute is higher than its parent 
                break

    def heapify_down(self, index):
        """ Starts at index 0 and sorts the heap by comparing the urgency scores of nodes """
        #Calculate the index of the left and right child nodes
        left = 2 * index + 1
        right = 2 * index + 2

        #Assume current index has lowest urgency
        lowest = index

        #Check if left child exists and has a lower urgency than current lowest
        if left < len(self.data) and self.data[left].urgency < self.data[lowest].urgency:
            lowest = left

        #Check if right child exists and has a lower urgency than current lowest
        if right < len(self.data) and self.data[right].urgency < self.data[lowest].urgency:
            lowest = right

        #If the lowest is not the current index, swap and continue. Otherwise, stop the function
        if lowest != index:

            #Swap the current patient with the patient that was a lower urgency value
            temp = self.data[index]
            self.data[index] = self.data[lowest]
            self.data[lowest] = temp

            #Recursively heapify the affected subtree
            self.heapify_down(lowest)

    def insert(self, patient):
        """ Adds a new patient to the heap """

        #Add the patient to the end of the queue
        self.data.append(patient)

        #Call heapify_up and start at the end of the queue where the new patient was added
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        """ Print each patient's name and urgency score """
        print("\nCurrent Patients:")
        for patient in self.data:
            print(f"-{patient.name} (Priority: {patient.urgency})")
    
    def peek(self):
        """ Returns the patient object at index 0 """
        if not self.data:
            print("The heap is empty.")
            return
        
        next_patient = self.data[0]
        
        print(f"\nNext patient: {next_patient.name} (Priority: {next_patient.urgency})")    
        
        return next_patient
    
    def remove_min(self):
        """ Removes and returns the patient with the lowest urgency score (highest priority patient)"""
        #Check if the list is empty
        if not self.data:
            return None

        #Length of 1 indicates the last value, no reordering needed
        if len(self.data) == 1:
            return self.data.pop()

        #Get the value to return
        min_value = self.data[0]

        #Place last item as root
        self.data[0] = self.data.pop()

        #Restore heap order
        self.heapify_down(0)

        #Return most urgent patient
        print(f"{min_value.name} (Priority: {min_value.urgency}) removed from queue.")
        return min_value

# Test your MinHeap class here including edge cases
heap = MinHeap()

#Add some patients to start out
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))
heap.insert(Patient("Joe", 5))
heap.insert(Patient("Sue", 3))
heap.insert(Patient("Stu", 1))
heap.insert(Patient("Bob", 2))

heap.print_heap()
heap.peek()

#Remove 2 patients
heap.remove_min()
heap.peek()
heap.remove_min()
heap.peek()
heap.print_heap()

#Demonstrate that heap is working correctly by removing remaining patients from queue
print("\nRemoving remaining patients from queue")
while heap.data:
    current_patient = heap.remove_min()

heap.peek()  #try to peek when heap is empty