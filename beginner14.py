s=input()
list=[]
list.append(s.count("q"))
list.append(s.count("w"))
list.append(s.count("e"))
list.append(s.count("r"))
list.append(s.count("t"))
list.append(s.count("y"))
list.append(s.count("u"))
list.append(s.count("i"))
list.append(s.count("o"))
list.append(s.count("p"))
list.append(s.count("a"))
list.append(s.count("s"))
list.append(s.count("d"))
list.append(s.count("f"))
list.append(s.count("g"))
list.append(s.count("h"))
list.append(s.count("j"))
list.append(s.count("k"))
list.append(s.count("l"))
list.append(s.count("z"))
list.append(s.count("x"))
list.append(s.count("c"))
list.append(s.count("v"))
list.append(s.count("b"))
list.append(s.count("n"))
list.append(s.count("m"))
list.append(s.count(" "))
a=list.count(0)
if a==0:
    print("pangram")
else:
    print("pangram emas")