def split_and_join(line):
    # Splitting the line into a list of words
    words = line.split()
    
    # Joining the words with hyphens
    joined_line = "-".join(words)
    
    # Returning the joined line
    return joined_line

if __name__ == '__main__':
    # Reading the input line
    line = input()
    
    # Calling the split_and_join function and printing the result
    result = split_and_join(line)
    print(result)
