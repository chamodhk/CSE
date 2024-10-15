in_msg = 'EXAMPLESINPUT 4'  #replace this with ur input code
msg = in_msg.split()[0]
num = int(in_msg.split()[1])

mat = [[] for i in range(num)]
message_len = len(msg)

col = 0
idx = 0
run = True
while run:
    row = 0
    while row <num:
        if idx == message_len:
            run = False
            break
        else:
            letter = msg[idx]
            print(letter)
            mat[row].append(letter)
            idx += 1
            row += 1
    col += 1

def print_matrix(mat):
    out = ""
    for row in mat:
        for letter in row:
            out += letter

    print(out)


col_count = len(mat[0])

if col_count == len(mat[1]) == len(mat[2]):
    print_matrix(mat)
else:
    for row in mat:
        while len(row) != col_count:
            row.append("*")

    print_matrix(mat)
