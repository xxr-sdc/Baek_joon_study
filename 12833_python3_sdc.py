MAX_LEN = 0

def xor(a:str, b:str)-> bool:
    tmpl = ""
    if len(a) > len(b):   b = b.zfill(MAX_LEN)
    elif len(a) < len(b): a = a.zfill(MAX_LEN)
    for idx in range(MAX_LEN):
        if a[idx] == b[idx]: tmpl += "0"
        else:                tmpl += "1"
    return tmpl

def convert_binary(_decimal:int)->str:
    global MAX_LEN
    _bin = bin(_decimal)[2:]
    if MAX_LEN < len(_bin): MAX_LEN = len(_bin)
    return _bin   # bin은 str

if __name__ == "__main__":
    #01. Input * Sort
    inputs = list(map(int, input().split(' ')))

    #02. Convert binary and Match format
    a = convert_binary(inputs[0])
    b = convert_binary(inputs[1])
    c = inputs[2]

    #03. XOR
    # c가 짝수면 a를 홀수면 연산한 결과를 출력 <-- 이문제의 핵심
    if c % 2 == 0:
        print(int(a, 2))        
    else:
        a = xor(a,b)
        print(int(a, 2))