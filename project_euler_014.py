def collatz_sequence_num_of_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        steps += 1

    return steps

longest_chain = (0, 0)
for i in range(1, 10**6):
    chain_length = collatz_sequence_num_of_steps(i)
    if chain_length > longest_chain[1]:
        longest_chain = (i, chain_length)

print(longest_chain)
