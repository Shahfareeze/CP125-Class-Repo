# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """
    # TODO: Implement this function

    list1 = open (file1, "r")
    list2 = open (file2, "r")
    output = open (output_file, "w")

    first = set(list1.readlines())
    second = set(list2.readlines())

    result = first | second
    name = sorted(set(result))
    for element in name:
        output.write(element)

    list1.close()
    list2.close()
    output.close()

    return len(name)


# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
