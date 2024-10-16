in_ = " 1 4 7 2 3 5 8 9 10 12 15 -1 "

in_ = [int(i) for i in in_.split()[:-1]]
tmp_in = in_[:]

tmp_in = sorted(tmp_in)

min_locs = []
max_locs = []


for i in range(3):
    loc1 = in_.index(tmp_in[i])
    min_locs.append(loc1)

for i in range(-1,-4,-1):
    loc1 = in_.index(tmp_in[i])
    max_locs.append(loc1)


swap_pairs = []

for i in range(3):
    pos1 = min_locs[i]
    pos2 = max_locs[i]

    swap_pairs.append((pos1,pos2))


def swap(pair):
    pos1, pos2 = pair
    tmp = in_[pos1]
    in_[pos1] = in_[pos2]
    in_[pos2] = tmp

for pair in swap_pairs:
    swap(pair)

print(*in_)
    



