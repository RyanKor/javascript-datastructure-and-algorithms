# def solution(words):
#     Trie = {}                                ## dictionary 형태로 Trie를 만듭니다.
#     for word in words:
#         cur_Trie = Trie
#         for w in word:
#             cur_Trie.setdefault(w,[0,{}])
#             cur_Trie[w][0] +=1               ## Trie를 만들어 가면서 하위 트리가 몇개인지 추가합니다.
#             cur_Trie = cur_Trie[w][1]
            
#     answer = 0
#     for word in words:
#         cur_Trie = Trie
#         for i in range(len(word)):
#             if cur_Trie[word[i]][0] == 1 :   ## Trie를 탐색하다가 하위트리가 한개이면 결과에 추가합니다.
#                 break
#             cur_Trie = cur_Trie[word[i]][1]
#         answer += i+1
#     return answer

class Trie():
    def __init__(self):
        self.next = dict()
        self.value = 0
 
def solution(words):
    answer = 0
    tree = Trie()
    for word in words:
        subtree = tree
        for idx, val in enumerate(word):
            subtree.value += 1
            if val not in subtree.next:
                subtree.next[val] = Trie()
            subtree = subtree.next[val]
            if (idx == len(word) - 1):
                subtree.value += 1
 
    for word in words:
        subtree = tree
        counts = 0
        for idx, val in enumerate(word):
            if (subtree.value == 1):
                answer += counts
                break
            elif idx == len(word) - 1:
                answer += counts + 1
                break
            else:
                subtree = subtree.next[val]
                counts += 1
    return answer