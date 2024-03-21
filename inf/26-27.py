
#
# f = open("27_B (1).txt", encoding="utf-8")
# k = int(f.readline())
# n = int(f.readline())
# mx2=0
# mx1=0
# mx3 = 0
# a = [int(x) for x in f.readlines()]           весрия егэ 2024 27
# for i in range(2*k, n):
#     mx1 = max(mx1, a[i-2*k])
#     mx2 = max(mx2, mx1+a[i-k])
#     mx3 = max(mx3, mx2+a[i])
# print(mx3)


# f = open("107_27_A.txt")
# n = int(f.readline())
# a = [int(x) for x in f.readlines()]
# res = []
# sto = r = l = 0
# for i in range(1, n//2):
#     sto+= a[i]*i+a[-i]*i
#     res.append(sto-r+l)               егэ досрок 2022 27
#     r+=a[i]
#     l+=a[-i]
# l+=a[0]
# r+=a[n//2]
# res = [sto]
# print(res)
# for i in range(1, n):
#     res.append(res[-1]-r+l)
#     r=r-a[i]+a[(i+n//2)%n]
#     l=l+a[i]-a[(i+n//2)%n]
# print(min(res))









# 308 333 7626 7930
# 440 442 7890 7666


# m = sorted([[i, int(j)] for i, j in enumerate(f.readlines())], key=lambda x: x[1], reverse=True)[1:1000]
# for x in range(len(m)):
#     for y in range(x+1, len(m)):
#         for z in range(y+1, len(m)):
#             if abs(m[y][0]-m[x][0])>=k and abs(m[z][0]-m[y][0])>=k and abs(m[z][0]-m[x][0])>=k:
#                 mx = max(mx, m[y][1]+m[x][1]+m[z][1])
# print(mx)
#




# f = open("26 (5).txt")
# n = int(f.readline())
# a = []
# for i in range(n):
#     st, end = map(int, f.readline().split())
#     a.append([st, end])
# a.sort(key=lambda x: x[1])
#
# t = [a.pop(0)]
# for j in range(13):
#     st, end = 0, 10**6
#     for i in range(n-1):
#         if a[i][0]>=t[-1][1] and a[i][1] <= end:    2024 апробация 26
#             st, end = a[i]
#     if st!=0:
#         t.append([st, end])
#     else:
#         break
# print(len(t))
# t = t[-1]
# mx = 0
# for k in a:
#     if k[0]>=t[0] and k[1]>=t[1]: mx = max(mx, k[1])
# print(mx)


# f = open("107_26.txt")
# n = int(f.readline())
# s = [list(map(int, x.split())) for x in f.readlines()]    досрок егэ 2022 26
# a = []
# p = 0
# for i in range(n):
#     m = []
#     inde = s[i][0]
#     for j in s:
#         if j[0]==inde: m+=[j[1]]
#     if m!=p:
#         a.append([inde, m])
#         p=m
#     else:
#         continue
# a.sort(reverse=True)
# for i1 in a:
#     a1 = sorted(i1[1])
#     if len(a1)>1:
#         for i2 in range(len(a1)-1):
#             if a1[i2+1]-a1[i2]-1==13:
#                 print(f"Наибольший номер ряда: {i1[0]}", f"Наименьший номер места: {a1[i2]+1}")
#                 exit()



#
#
# f = open("107_27_A (1).txt")
# n = int(f.readline())
# a = [int(x) for x in f.readlines()]
#
# sm = []
# for i in range(len(a)):
#     s=0
#     for j in range(len(a)):
#         m = min(abs(j-i), len(a)-abs(j-i))                  досрок  егэ 2022 27А
#         s+=a[j]*m
#     sm.append([s, i+1])
# print(min(sm))



# f = open("27A_4605.txt")
# n = int(f.readline())
# sm = []
# def f1(n):
#     c = 0
#     sa = n                        егэ2022 27А
#     while sa>=36:
#         sa-=36
#         c+=1
#     if n%36==0:
#         return c
#     else:
#         return c+1
# print(f1(5))
# a = [list(map(int, x.split())) for x in f.readlines()]
# for i in range(n):
#     s = 0
#     for j in range(n):
#         m = abs(a[i][0]-a[j][0])
#         s+=f1(a[j][1])*m
#     sm.append(s)
# print(min(sm))