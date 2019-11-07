import sys
import re


def main():
    path = input("ファイルのパスを入力")
    with open(path) as f:
        s = f.read()
        modified = marumeru(s)

    with open(path + "_ramen.modified", mode='w') as f:
        f.write(modified)
    print("DONE!")

def marumeru(file):
    match = re.finditer(r'\)([0-9]+)', file)
    i = 1
    newfile = file
    for m in match:
        bs = int(m.group(1))
        if bs == 100:
            bs_new = bs
            newfile = rep(newfile, m, bs_new, i)
        elif bs >= 70:
            bs_new = 100
            newfile = rep(newfile, m, bs_new, i)
            i = i+1
        elif bs >= 50 and bs < 70:
            bs_new = 50
            newfile = rep(newfile, m, bs_new, i)
        elif bs < 50:
            bs_new = 0
            newfile = rep(newfile, m, bs_new, i)
            if bs >= 10:
                i = i-1
        
    return newfile

def rep(newfile, m, bs_new, i):
    #print(newfile[m.start()+i:m.end()+i-1], i)
    newfile = newfile[:m.start()+i] + str(bs_new) + newfile[m.end()+i-1:]
    return newfile

if __name__ == '__main__':
    main()