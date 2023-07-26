print(f"Digite dois numeros:")
x = int(input())
y = int(input())

while x != y:
    if x < y:
        print(f"CRESCENTE!")
    else:
        print(f"DESCRECENTE!")


    print(f"Digite outro dois numeros:")
    x = int(input())
    y = int(input())