class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):  # so upon the initial creation this has a value of None so when first made it has a larger value?
        if value < self.value:  # here this compares what was in the init for the original root value with the to be inserted one
            if not self.left:  # starting comparison
                # makes the node if smaller
                # creates new tree which is its own tree also in the location determined by the camparison
                self.left = BinarySearchTree(value)
            else:
                # this recurses if there is a left
                # this keep looking for where it belongs if there are already values/nodes in tree
                return self.left.insert(value)
        if value >= self.value:  # repeated same as the left above
            if not self.right:
                self.right = BinarySearchTree(
                    value)  # makes the node if bigger
            else:
                # this recurses if there is a right
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target < self.value:  # this starts at the root node and then we work our way down
            # if its smaller and nothing there to compare it isnt in there (base case)
            if self.left is None:
                return False
            else:
                # creates the recursive move to the left
                return self.left.contains(target)
        if target > self.value:
            # if target is larger but there isnt a right to compare then it isnt in there (base case)
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        if target == self.value:  # this is our base case so this is where we return True once found
            return True
