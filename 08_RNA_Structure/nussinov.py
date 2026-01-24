def nussinov_table(seq, gamma, ell=0):
    table = [[0 for _ in range(len(seq))] for _ in range(len(seq))]
    for diff in range(1+ell, len(seq)):
        for i in range(len(seq)-diff):
            j = i + diff
            opt = -1
            # case 1: if matches
            if (seq[i], seq[j]) in gamma:
                curr_opt = table[i+1][j-1] + gamma[(seq[i], seq[j])]
                if curr_opt > opt:
                    opt = curr_opt
            # case 2: skip head
            curr_opt = table[i+1][j]
            if curr_opt > opt:
                opt = curr_opt
            # case 3: skip tail
            curr_opt = table[i][j-1]
            if curr_opt > opt:
                opt = curr_opt
            # case 4: bifurcation
            for k in range(i+1+ell, j):
                curr_opt = table[i][k] + table[k+1][j]
                if curr_opt > opt:
                    opt = curr_opt
            table[i][j] = opt

    ans = table[0][-1]
    return ans, table

def reconstruction(seq, table, gamma, ell=0):
    n = len(seq)
    stack = [(0,n-1)]
    record = []
    while len(stack) > 0:
        i,j = stack.pop()
        # print(i, j)
        if i + ell >= j:
            continue
        elif table[i+1][j] == table[i][j]:
            stack.append((i+1, j))
        elif table[i][j-1] == table[i][j]:
            stack.append((i, j-1))
        elif (seq[i], seq[j]) in gamma and table[i+1][j-1] + gamma[(seq[i], seq[j])] == table[i][j]:
            record.append((i, j))
            stack.append((i+1, j-1))
        else:
            for k in range(i+1+ell, j):
                if table[i][k] + table[k+1][j] == table[i][j]:
                    stack.append((k+1, j))
                    stack.append((i, k))
                    break

    return record

def reconstruction_helper(seq, i, j, table, gamma, ell=0):
    solutions = []
    if i + ell >= j:
        return solutions
    if table[i+1][j] == table[i][j]:
        solutions += reconstruction_helper(seq, i+1, j, table, gamma, ell)
    if table[i][j-1] == table[i][j]:
        solutions += reconstruction_helper(seq, i, j-1, table, gamma, ell)
    if (seq[i], seq[j]) in gamma and table[i+1][j-1] + gamma[(seq[i], seq[j])] == table[i][j]:
        prev_sols = reconstruction_helper(seq, i+1, j-1, table, gamma, ell)
        if len(prev_sols) == 0:
            prev_sols = [[(i, j)]]
        else:
            prev_sols = [w+[(i,j)] for w in prev_sols]
        solutions += prev_sols
    for k in range(i+1+ell, j):
        if table[i][k] + table[k+1][j] == table[i][j]:
            left_sols = reconstruction_helper(seq, i, k, table, gamma, ell)
            right_sols = reconstruction_helper(seq, k+1, j, table, gamma, ell)
            combined_sols = []
            for lsol in left_sols:
                for rsol in right_sols:
                    csol = lsol + rsol
                    if len(csol) > 0:
                        combined_sols.append(csol)
            solutions += combined_sols
    return solutions

def to_dot_bracket(seq, record):
    representation = ['.' for w in seq]
    for (i, j) in record:
        representation[i] = '('
        representation[j] = ')'
    representation = ''.join(representation)
    return representation

GAMMA_SCORING = {('G', 'C'): 3, ('C', 'G'): 3, ('A', 'U'): 2, ('U', 'A'): 2, ('G', 'U'): 1, ('U', 'G'): 1}

string = 'AUUAACCGCGGUUAAUCGCG'
ell = 3

max_score, table = nussinov_table(string, GAMMA_SCORING, ell)
record = reconstruction(string, table, GAMMA_SCORING, ell)
dot_bracket = to_dot_bracket(string, record)

print(f"Sekwencja: {string}")
print(f"Struktura: {dot_bracket}")