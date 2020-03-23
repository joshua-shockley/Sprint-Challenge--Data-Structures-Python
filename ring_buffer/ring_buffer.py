from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # self.current must be for saving where to add in list_buffer_contents[iteration] so that it keeps rotating from index:0-2
        self.current = None
        self.storage = DoublyLinkedList()

    def __str__(self):
        if self.storage.length == 0:
            return f"nothing to print yet... add some shit!"
        else:
            curr_node = self.storage.head
            output = ""
            output += f"{curr_node.value} <-> "
            while curr_node.next is not None:
                curr_node = curr_node.next
                output += f"{curr_node.value} <-> "
            return f" lru size: {self.storage.length} \n Nodes: {output}"

    def append(self, item):
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = 0
            # print('added:', item)
            return
        elif self.storage.length >= 1 and self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current += 1
            return
        else:
            # print(self.capacity - self.current - 1)
            print("current:", self.current)
            if self.current == self.capacity-1:
                self.current = 0
            if self.current == 0:
                node = self.storage.head
                node.value = item
                print('should hit this if current is 2 or 0')
                print("new self.current:", self.current)
                # return

            if self.current < self.capacity and self.current >= 1:
                tmp_current = self.current
                change_node = self.storage.head
                while tmp_current >= 1:
                    tmp_current -= 1
                    print("tmp_current:", tmp_current)
                    change_node = change_node.next
                    print(change_node.value)

                print("adding new value to existing node", change_node.value)
                change_node.value = item
                print("self.current is:", self.current)
            self.current += 1
            print("just before end of main fn.. self.current:", self.current)
            return

            # self.storage.add_to_tail(item)
            # self.current += 1
            # print(self.current)
            # return

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        if self.storage.head is None and self.storage.tail is None:
            return None
        else:
            node = self.storage.head
            while node is not None:
                list_buffer_contents.append(node.value)
                if node.next is None:
                    break
                else:
                    node = node.next

        print('getting rb list')
        return list_buffer_contents


rb = RingBuffer(3)
print("capacity:", rb.capacity)
rb.append('f')
rb.append('q')
rb.append('turd')
print(rb.get())

print(rb)
rb.append('new')
print(rb.get())
print(rb)
rb.append('another')
print(rb.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
