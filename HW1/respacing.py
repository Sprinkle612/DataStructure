# TODO: Rain Liang, XL778
# TODO: Thomas Kennedy Shanahan, TKS46

# DO NOT CHANGE THIS CLASS


class RespaceTableCell:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.validate()

    # This function allows Python to print a representation of a RespaceTableCell
    def __repr__(self):
        return "(%s,%s)" % (str(self.value), str(self.index))

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.value) ==
               bool), "Values in the respacing table should be booleans."
        assert(self.index == None or type(self.index) ==
               int), "Indices in the respacing table should be None or int"

# Inputs: the dynamic programming table, indices i, j into the dynamic programming table, the string being respaced, and an "is_word" function.
# Returns a RespaceTableCell to put at position (i,j)


def fill_cell(T, i, j, string, is_word):
    # check wether sub string from i to j is a valid word

    test = is_word(string[i:j+1])
    if test:
        # if itself is a word
        return RespaceTableCell(test, None)
    else:
        # if itself is a word
        c = 1
        for x in range(i, j):
            if T.get(i, x).value and T.get(i+c, j).value:
                return RespaceTableCell(True, x)
            c += 1

    return RespaceTableCell(False, None)

# Inputs: N, the size of the list being respaced
# Outputs: a list of (i,j) tuples indicating the order in which the table should be filled.


def cell_ordering(N):
    # the order goes in diagonal
    order = []
    for x in range(N):
        for i in range(N-x):
            order.append((i, i+x))

    return order

# Input: a filled dynamic programming table.
# (See instructions.pdf for more on the dynamic programming skeleton)
# Return the respaced string, or None if there is no respacing.


def respace_from_table(s, table):
    result = ""
    space = []

    i, j = 0, len(s) - 1
    # check whether it's a valid word
    if not table.get(i, j).value:
        return None
    #-- Top Down --#
    while i < len(s):
        if table.get(i, j).value:
            space.append(table.get(i, j).index)
            if table.get(i, j).index != None:
                i = table.get(i, j).index + 1
            else:
                i += 1
        else:
            i += 1
    # Insert space
    for c in range(len(s)):
        result += s[c]
        if c in space:
            result += ' '

    return result


if __name__ == "__main__":
    # Example usage.
    from dynamic_programming import DynamicProgramTable
    s = "itwasthebestoftimes"
    wordlist = ["of", "it", "the", "best", "times", "was"]

    D = DynamicProgramTable(len(s) + 1, len(s) + 1,
                            cell_ordering(len(s)), fill_cell)
    D.fill(string=s, is_word=lambda w: w in wordlist)

    print(respace_from_table(s, D))
