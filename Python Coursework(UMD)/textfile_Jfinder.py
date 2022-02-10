# Julio Claros
# 114153234
# 2018-17-9
# Assignment: P4E 7


def read_txt(text_file):
    """
    Function stores a path to txt file in parameter in "read mode" and interates through every line to check if it
    contains the character J. If it does, it counts the line and stores integer value in variable.

    Arg :
        text_file (Path to text file): contains lyrics of a song

    Return:
        counter (integer): every line counted that contains character J.
    """
    counter = 0
    with open(text_file, "r") as file:
        for line in file:
            sentence = line.find("j")
            if sentence == -1:
                continue
            else:
                counter = counter + 1
    return counter


def write_txt(text_file, counter):
    """
    Functions opens a separate text file in "write mode" and write counter value within its confines

    Args:
        text_file (Path to text file): contains text file to write in or overwrite
        counter (integer): counter variable passed from read_text function. Contains count int of total lines that had
        a character J in.

    Returns:
        None or N/a
     """
    statement = str(counter)
    with open(text_file, "w") as file:
        file.write("Total Counter: " + statement)


if __name__ == '__main__':
    print("Enter a file name (.txt): ")
    write = (input())
    counter = read_txt(write)
    print("Enter file to write in (.txt): ")
    write_txt(input(), counter)
