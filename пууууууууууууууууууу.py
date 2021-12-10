# 1 ЕДИНИЧКИ И НУЛИ

# c = int(input())
# r = int(input())
# a = [1]*r
# for i in range (r):
#     a[i] = [1]*c
#     for j in range (c):
#         if i == j:
#             a[i][j] = 0
#         else:
#             a[i][j]=1
# for row in a :
#     for elem in row:
#         print(elem, end=' ')
#     print()

# 2 ЕДИНИЧКИ ДВОЙКИ ТРОЙКИ

# c = int(input())
# r = int(input())
# a = [1]*r
# for i in range (r):
#     a[i] = [1]*c
#     for j in range (c):
#         if i == 0:
#             a[i][j] = 1
#         if i == 1:
#             a[i][j] = 2
#         if i == 2:
#                 a[i][j] = 3
# for row in a :
#     for elem in row:
#         print(elem, end=' ')
#     print()

# 3 один два три четыре пять шесть ......  ПЯТНАДЦАДЬ!

# n = int(input())
# m = int(input())
# s=1
# r=[[i+1]*m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         r[i][j]=s
#         s+=1
# print()
# for i in r:
#     print(*i)

# 4 НУЛИ ЕДИНИЧКИ НУЛИ ДВОЙКИ НУЛИ ТРОЙКИ

# c = int(input())
# r = int(input())
# a = [1]*r
# for i in range (r):
#     a[i] = [1]*c
#     for j in range (c):
#         if j == 0:
#             a[i][j] = 0
#         if j == 1:
#             a[i][j] = 1
#         if j == 2:
#             a[i][j] = 0
#         if j == 3:
#             a[i][j] = 2
#         if j == 4:
#             a[i][j] = 0
#         if j == 5:
#             a[i][j] = 3
# for row in a :
#     for elem in row:
#         print(elem, end=' ')
#     print()