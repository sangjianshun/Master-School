# 500G, 特殊，一行，有分隔符
def myreadlines(f,newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos +len(newline):]
        chunk = f.read(10)
        if not chunk:
            yield buf
            break
        buf += chunk
with open("input.txt") as f:
    for line in myreadlines(f,"<SEP>"):
        print(line)
