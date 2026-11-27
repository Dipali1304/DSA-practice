#Q.1 Online Examination Result Management- An examination department
#stores student examination scores in a BST. Each score is inserted as a node.
#Tasks:
#1. Insert the following examination scores out of 100 into the BST.
# 45, 78, 32, 89, 56, 92, 67, 34, 85, 73, 61, 98
# 2. Display scores in ascending order.
# 3. Find the highest and lowest scores.
# 4. Count the number of students scoring above 50.
# 5. Search for a particular score.
# 6. Find the average of all scores.


class Node:
    def __init__(self, score):
        self.score = score
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # 1. Insert score into BST
    def insert(self, score):
        if self.root is None:
            self.root = Node(score)
        else:
            self._insert(self.root, score)

    def _insert(self, root, score):
        if score < root.score:
            if root.left is None:
                root.left = Node(score)
            else:
                self._insert(root.left, score)

        elif score > root.score:
            if root.right is None:
                root.right = Node(score)
            else:
                self._insert(root.right, score)

    # 2. Display scores in ascending order
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.score, end=" ")
            self.inorder(root.right)

    # 3. Find lowest score
    def find_min(self):
        current = self.root

        if current is None:
            return None

        while current.left:
            current = current.left

        return current.score

    # 3. Find highest score
    def find_max(self):
        current = self.root

        if current is None:
            return None

        while current.right:
            current = current.right

        return current.score

    # 4. Count students scoring above 50
    def count_above_50(self, root):
        if root is None:
            return 0

        count = 1 if root.score > 50 else 0

        return (count +
                self.count_above_50(root.left) +
                self.count_above_50(root.right))

    # 5. Search for a particular score
    def search(self, root, key):
        if root is None:
            return False

        if root.score == key:
            return True

        if key < root.score:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # 6. Find average of all scores
    def calculate_sum(self, root):
        if root is None:
            return 0

        return (root.score +
                self.calculate_sum(root.left) +
                self.calculate_sum(root.right))

    def count_nodes(self, root):
        if root is None:
            return 0

        return (1 +
                self.count_nodes(root.left) +
                self.count_nodes(root.right))

    def average(self):
        total = self.calculate_sum(self.root)
        count = self.count_nodes(self.root)

        if count == 0:
            return 0

        return total / count


# Main Program
bst = BST()

scores = [45, 78, 32, 89, 56, 92,
          67, 34, 85, 73, 61, 98]

# Insert all scores
for score in scores:
    bst.insert(score)

# Display results
print("Scores in Ascending Order:")
bst.inorder(bst.root)

print("\n\nLowest Score:", bst.find_min())
print("Highest Score:", bst.find_max())

print("Students Scoring Above 50:",
      bst.count_above_50(bst.root))

# Search for a score
key = int(input("\nEnter score to search: "))

if bst.search(bst.root, key):
    print(key, "is found in the BST.")
else:
    print(key, "is not found in the BST.")

# Display average
print("Average Score:", bst.average())
