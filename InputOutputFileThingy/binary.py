# with open("binary", 'bw') as bin_file:
#     for i in range(17):
#         bin_file.write(bytes([i])) # passing a list [i]
#         # the reason we passed a list is because if we pass a integer to it
#         # it creates a byte sequence with that many bytes all set to 0
#         # by passing each integer as one element in a list the byes function then correctly converted to a single byte
#
#         # we can just do :
#         # bin_file.write(bytes(range(17)))  # range returns a list
#
# with open("binary", 'br') as binFile:
#     for b in binFile:
#         print(b)

a = 65534   # FF FE
b = 65535   # FF FF
c = 65536   # 00 01 00 00
x = 2998302     # 00 2D C0 1E

with open("binary2", 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))    # first argument is number bytes we want ,
    # Second : whether to return the result as big endian or little endian
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little'))

with open("binary2", 'br') as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'big')
    print(i)



