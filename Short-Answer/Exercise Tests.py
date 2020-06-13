# def test(n):
#     a = 0
#     while (a < n * n * n):
#         a = a + n * n
#         print(a)
# test(15)
#     sum = 0
#     for i in range(n):
#         j = 1
#         print(f"1st J: {j}")
#         while j < n:
#             j *= 2
#             sum += 1
#         print(sum)
# test(15)

def bunnyEars(bunnies):
    if bunnies == 0:
        return 0
    print(f"Return: {2 + bunnyEars(bunnies - 1)}")
    print(f"Bunnies: {bunnies}\n")
    return 2 + bunnyEars(bunnies - 1)

bunnyEars(4)