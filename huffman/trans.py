import io

a = open("ans.txt", "r");
b = open("ans.out", "wb");
while True:
    c = a.read(8)
    if not c:
        break
    c = int(c, 2)
    b.write(c.to_bytes(1, byteorder='big', signed = False))
a.close()
b.close()
