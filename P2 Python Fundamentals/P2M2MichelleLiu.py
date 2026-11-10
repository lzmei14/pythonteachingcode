# [] create list-o-matic as a function and call it
# [] be sure to include your spelled-out name in the welcome prompt
# [] you are welcome to use any list you like for list-o-matic, does not have to be animals 
def list_o_matic(item,trees):
    if item == "":
        popped_item = trees.pop()
        return popped_item + " popped from list."
    elif item in trees:
        trees.remove(item)
        return "1 instance of " + item + " removed from list."
    else:
        trees.append(item)
        return "1 instance of " + item + " appended to list."

trees = ["birch", "acacia", "oak", "mahogany"]

while trees:
    print("\nWelcome, Michelle Liu, Look at all the trees: ", trees)
    item = input("Enter the name of a tree or 'quit' to exit: ")
    if item.lower() == "quit":
        break
    print(list_o_matic(item,trees))

print("Goodbye!")
