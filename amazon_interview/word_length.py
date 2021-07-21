test = input()

# input : aaaabbbcccca
# expected output : 4a3b4c1a


def word_length(test):
    idx = 0
    result = ''
    cnt = 1
    if len(test) == 1 or len(test) == 0:
        result = str(len(test)) + test
    else:
        prev = test[idx]
        for i in range(1, len(test)):
            # 방법 1 : 카운트 방식의 접근
            # if test[idx] == test[i]:
            #     cnt += 1
            #     idx += 1
            #     if i == len(test) - 1:
            #         result += str(cnt) + test[idx]
            #         break
            # else:
            #     result += str(cnt) + test[idx]
            #     cnt = 1
            #     idx += 1
            # if i == len(test) - 1:
            #     # 이 예외처리가 적용되는 상황 : aaaabbbcccca같은 상황임. aabcc같이 마지막 2개가 같은 경우가 포함이 안된다.
            #     if test[i] == test[-2]:
            #         result[-2].replace(result[-2], str(int(result[-2]) + 1))
            #     else:
            #         result += str(1) + test[i]
            # 방법 2 : 포인터 형식의 접근
            if prev == test[i]:
                cnt += 1
                if i == len(test) - 1:
                    result += str(cnt) + test[i]
                    break
            else:
                result += str(cnt) + prev
                prev = test[i]
                cnt = 1
            if i == len(test) - 1:
                # 이 예외처리가 적용되는 상황 : aaaabbbcccca같은 상황임. aabcc같이 마지막 2개가 같은 경우가 포함이 안된다.
                if test[i] == test[-2]:
                    result[-2].replace(result[-2], str(int(result[-2]) + 1))
                else:
                    result += str(1) + test[i]
    return result


print(word_length(test))