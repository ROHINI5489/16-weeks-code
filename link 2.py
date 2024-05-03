if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
# Removing duplicates by converting the list to a set and back to a list
    unique_scores = list(set(arr))
    # Sorting the list of scores in descending order
    unique_scores.sort(reverse=True)

    # Retrieving the second element in the sorted list, which represents the runner-up score
    runner_up_score = unique_scores[1]

    # Printing the runner-up score
    print(runner_up_score)