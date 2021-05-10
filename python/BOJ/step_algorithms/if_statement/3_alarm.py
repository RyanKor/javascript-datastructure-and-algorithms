H, M = map(int, input().split())

# 내가 짠 코드는 몇 개의 테스트 케이스 통과를 못했다.
# if (H == 0 and M < 45):
#     print(23, 60 - (45-M))
# elif (H == 0 and M >= 45):
#     print(H, M-45)
# elif (H != 0 and M < 45):
#     print(H-1, 60 - (45-M))
# else:
#     print(H-1, M-45)


# 누군가의 파이썬 알고리즘 답

if M > 44:
    print(H, M-45)
elif M < 45 and H > 0:
    print(H-1, M+15)
else:
    print(23, M+15)
