# your code goes 
def print_rangoli(size):
    import string
    
    # Create a list of alphabets from 'a' to 'z'
    alphabets = string.ascii_lowercase
    
    # Slice the list to include only the required alphabets for the rangoli pattern
    required_alphabets = alphabets[:size]
    
    # Build the top half of the rangoli
    for i in range(size-1, 0, -1):
        row = ['-'] * (2*size-1)
        for j in range(size-i):
            row[size-1-j] = row[size-1+j] = required_alphabets[j+i]
        print('-'.join(row))

    # Build the center line
    center_row = '-'.join(required_alphabets[::-1] + required_alphabets[1:])
    print(center_row)

    # Build the bottom half of the rangoli
    for i in range(1, size):
        row = ['-'] * (2*size-1)
        for j in range(size-i):
            row[size-1-j] = row[size-1+j] = required_alphabets[j+i]
        print('-'.join(row))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)