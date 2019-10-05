# TODO: Rain Liang, XL778
# TODO: Thomas Kennedy Shanahan, TKS46


import dynamic_programming

# DO NOT CHANGE THIS CLASS


class DiffingCell:
    def __init__(self, s_char, t_char, cost):
        self.cost = cost
        self.s_char = s_char
        self.t_char = t_char
        self.validate()

    # Helper function so Python can print out objects of this type.
    def __repr__(self):
        return "(%d,%s,%s)" % (self.cost, self.s_char, self.t_char)

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.cost) == int), "cost should be an integer"
        assert(type(self.s_char) == str), "s_char should be a string"
        assert(type(self.t_char) == str), "t_char should be a string"
        assert(len(self.s_char) == 1), "s_char should be length 1"
        assert(len(self.t_char) == 1), "t_char should be length 1"

# Input: a dynamic programming table,  cell index i and j, the input strings s and t, and a cost function cost.
# Should return a DiffingCell which we will place at (i,j) for you.


def fill_cell(table, i, j, s, t, cost):
    if (i == -1 & j == -1):
        return DiffingCell('-', '-', 0)
    # Find All Combinations
    s_dash = cost(s[i], '-')
    t_dash = cost('-', t[j])
    s_t = cost(s[i], t[j])
    # Fill up the first row
    if (i == -1):
        return DiffingCell('-', t[j], table.get(i, j-1).cost + t_dash)

    # Fill up the first column
    if (j == -1):
        return DiffingCell(s[i], '-', table.get(i-1, j).cost + s_dash)

    # Cost from three directions
    cost1 = table.get(i-1, j-1).cost + s_t
    cost2 = table.get(i-1, j).cost + s_dash
    cost3 = table.get(i, j-1).cost + t_dash

    # Min cost
    cost = min(cost1, cost2, cost3)

    if cost == cost1:
        return DiffingCell(s[i], t[j], cost)
    elif cost == cost2:
        return DiffingCell(s[i], '-', cost)
    else:
        return DiffingCell('-', t[j], cost)

# Input: n and m, represents the sizes of s and t respectively.
# Should return a list of (i,j) tuples, in the order you would like fill_cell to be called


def cell_ordering(n, m):
    # Go in row by row
    order = []
    for i in range(-1, n):
        for j in range(-1, m):
            order.append((i, j))
    return order

# Returns a size-3 tuple (cost, align_s, align_t).
# cost is an integer cost.
# align_s and align_t are strings of the same length demonstrating the alignment.
# See instructions.pdf for more information on align_s and align_t.


def diff_from_table(s, t, table):
    i = len(s) - 1
    j = len(t) - 1
    aligned_s = []
    aligned_t = []
    # Trace back from the bottom corner
    while i+j > -2:
        cur_cell = table.get(i, j)
        if cur_cell.s_char != '-' and cur_cell.t_char != '-':
            i += -1
            j += -1
        elif cur_cell.s_char == '-':
            j += -1
        else:
            i += -1
        aligned_s.insert(0, cur_cell.s_char)
        aligned_t.insert(0, cur_cell.t_char)

    return (table.get(len(s)-1, len(t)-1).cost, ''.join(aligned_s), ''.join(aligned_t))


# Example usage
if __name__ == "__main__":
    # Example cost function from instructions.pdf
    def costfunc(s_char, t_char):
        if s_char == t_char:
            return 0
        if s_char == 'a':
            if t_char == 'b':
                return 5
            if t_char == 'c':
                return 3
            if t_char == '-':
                return 2
        if s_char == 'b':
            if t_char == 'a':
                return 1
            if t_char == 'c':
                return 4
            if t_char == '-':
                return 2
        if s_char == 'c':
            if t_char == 'a':
                return 5
            if t_char == 'b':
                return 5
            if t_char == '-':
                return 1
        if s_char == '-':
            if t_char == 'a':
                return 3
            if t_char == 'b':
                return 3
            if t_char == 'c':
                return 3

    import dynamic_programming
    s = "acbbbbb"
    t = "baa"
    D = dynamic_programming.DynamicProgramTable(
        len(s) + 1, len(t) + 1, cell_ordering(len(s), len(t)), fill_cell)
    D.fill(s=s, t=t, cost=costfunc)
    (cost, align_s, align_t) = diff_from_table(s, t, D)
    print(align_s)
    print(align_t)
    print("cost was %d" % cost)
