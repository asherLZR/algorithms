"""
The cost function here tells us how added spaces we have per line.
Cost function is (page_width - total_width)**3.

Running time is O(N^2) as we have N sub-problems and we do dp(i) for each one.
Sub-problem statement: dp(i) = min(dp(j) + cost(i, j) for each j in range(i+1, n+1)) # this is O(N)
Sub-problems are each suffix [i:]; there are N suffixes.
"""


def justified_table(text, page_len):
    """
    The following function builds the cost table for each possible suffix starting at each word in the
    input text. The table is filled in with the cost if the suffix fits within the page_width given,
    float('inf') otherwise.

    :param text: the list of words to justify
    :param page_len: the maximum width of the page
    :return: memoisation table containing the costs of each suffix
    """
    n_words = len(text)
    memo = [[0] * n_words for _ in range(n_words)]
    for i in range(n_words):
        running_cost = 0
        for j in range(i, n_words):
            # compute the running cost of adding one more word from i to j to that line
            # float('inf') indicates words[i:j+1] exceeds the line width limit
            running_cost += len(text[j])
            if j > i:
                running_cost += 1
            memo[i][j] = cost(page_len, running_cost)
    return memo


def justified_solution(text, memo):
    """
    Takes in the memoisation table, working our way back from the suffix of the last word alone
    towards the first word. At each step, we take the minimum cost of memo[i] = min[memo[j] +
    cost[i, j] for each j in range(i+1, n+1)). In essence, what we are doing is figuring out the
    minimum possible cost of adding in the new word, given that we already know the minimum cost
    of the rest of the words in the suffix. Whenever we find a minimum, we add that jth value to
    our parent pointers list, which allows us to return to the point optimal for each line break.
    :param text: the list of words to be justified
    :param memo: our memoisation table with the costs of each suffix
    :return: None
    """
    n_words = len(text)
    # cost list to compute the minimum cost required, which will be at cost_memo[0]
    cost_memo = [float('inf')] * n_words
    # parent pointer list to store the optimal point for each line break
    parent_pointer = [0] * n_words
    # initialise the value of the cost list with the value for only the last word
    cost_memo[-1] = memo[-1][-1]
    # initialise the parent pointer list with the last break of the paragraph - the last word
    parent_pointer[-1] = len(text)
    i = n_words - 2
    # working backwards for each word in our word list
    while i >= 0:
        # start by assuming the minimum cost from that ith suffix onwards is from i to n+1
        # in most cases this will yield float('inf') and be replaced later on
        cost_memo[i] = memo[i][n_words-1]
        # assume the parent pointer is the last of all the words; similar to cost list, this
        # is most often going to be replaced as well
        parent_pointer[i] = n_words
        j = i
        # for each possible position to break the line from i to a running value of j,
        # we take the minimum for all of these combinations, adjusting the cost list and
        # parent pointer list along the way
        while j+1 < n_words:
            line_cost = memo[i][j] + cost_memo[j+1]
            cost_memo[i] = min(cost_memo[i], line_cost)
            if line_cost == cost_memo[i]:
                # the parent pointer for this word will be j+1 where the cost is minimised
                parent_pointer[i] = j + 1
            j += 1
        i -= 1
    # printing our solutions
    print("Minimum cost for paragraph:", cost_memo[0])
    print()
    for row in memo:
        print(row)
    return parent_pointer


def cost(page_len, suffix_len):
    """
    The cost function, returning the cost of the suffix if it were all on one line.
    :param page_len: width of the page specified
    :param suffix_len: the width of the suffix
    :return: the cost of the suffix if it fits, float('inf') otherwise
    """
    if page_len - suffix_len >= 0:
        return (page_len - suffix_len) ** 3
    else:
        return float('inf')


def tidy_text(text, parent_pointer, page_len):
    """
    Prints the text in justified format. We retrace the steps with parent pointers; we start at 0 for our first
    word, where we find the optimal line break then we navigate to the element of the line break. At each line, we
    compute the spaces required in between the text, taking into account edge cases where the last space is one more
    than the rest of the spaces in the line.
    :param text: the justified text to be printed
    :param parent_pointer: the parent pointer list from our justified_solution function
    :param page_len: the length of the page specified
    :return:
    """
    i = 0
    while i < len(parent_pointer):
        # calculate the number of spaces required by the words in the line
        n_spaces = parent_pointer[i] - 1 - i
        # add up the lengths of each word and their spaces
        line_len = sum([len(x) for x in text[i:parent_pointer[i]]]) + n_spaces
        # the number of spaces remaining
        excess = page_len - line_len
        # if there are no spaces remaining, we only need to print that line, avoiding potentially
        # integer dividing or modulo by 0
        if n_spaces == 0:
            print(' '.join(text[i:parent_pointer[i]]))
            i = parent_pointer[i]
            continue
        # calculate the average number of spaces required between words, and the potential case where
        # the last space is one more than the rest
        even_spacing = excess//n_spaces + 1
        last_spacing = even_spacing
        if excess % n_spaces != 0:
            last_spacing += 1
        # build up the line with the required number of spaces
        line = text[i]
        for j in range(i+1, parent_pointer[i]):
            if j == parent_pointer[i]-1:
                line += " " * last_spacing
                # line += " " * (line_len - len(line) - len(text[j]))
            else:
                line += " " * even_spacing
            line += text[j]
        print(line)
        i = parent_pointer[i]


def main():
    # text_to_justify = "you can use dynamic programming to justify text and I learnt that in FIT1008"
    text_to_justify = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus suscipit pharetra " \
                      "libero interdum gravida. Nunc nec sem semper purus dignissim semper. Nullam rutrum nunc" \
                      " a quam commodo pulvinar. Sed lobortis dui eu arcu consectetur molestie. Proin maximus " \
                      "arcu in mauris condimentum vestibulum. Morbi erat leo, mollis nec elit nec, tincidunt " \
                      "lobortis dui. Quisque et odio odio. Praesent ut nisl dui. Maecenas vitae nisl viverra, " \
                      "congue sem in, ultrices dui. In nisi eros, blandit ac felis ut, accumsan blandit est."
    text_to_justify = text_to_justify.split(" ")
    page_len = 50
    memo = justified_table(text_to_justify, page_len)
    parent_pointer = justified_solution(text_to_justify, memo)
    tidy_text(text_to_justify, parent_pointer, page_len)


if __name__ == '__main__':
    main()
