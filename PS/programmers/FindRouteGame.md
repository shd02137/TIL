#  2019 카카오 블라인드 / 길찾기게임

## 첫번째 시도

```python
import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    answer = []
    
    nodeinfo = make_tree(nodeinfo)
    
    answer.append(pre_order(nodeinfo))
    answer.append(post_order(nodeinfo))
    
    return answer

def make_tree(nodeinfo):
    for i,info in enumerate(nodeinfo,1):
        nodeinfo[i-1].append(i)
    
    nodeinfo = sorted(nodeinfo,key = lambda x : (x[1] , -x[0]) ,reverse = True)
    
    return nodeinfo


def split_node(nodeinfo):
    left_nodeinfo = []
    right_nodeinfo = []
    for node in nodeinfo:
        if nodeinfo[0][1] > node[1] and nodeinfo[0][0] > node [0]:
            left_nodeinfo.append(node)
        elif nodeinfo[0][1] > node[1] and nodeinfo[0][0] < node[0]:
            right_nodeinfo.append(node)
    
    return left_nodeinfo,right_nodeinfo

def pre_order(nodeinfo):
    answer = []
    
    left_nodeinfo ,right_nodeinfo = split_node(nodeinfo)
    #print(nodeinfo[0][2],"="*20)
    #print("node" , nodeinfo)
    # print("left" , left_nodeinfo)
    # print("right", right_nodeinfo)
    
    answer.append(nodeinfo[0][2])
    if left_nodeinfo:
        answer.extend(pre_order(left_nodeinfo))
    if right_nodeinfo:
        answer.extend(pre_order(right_nodeinfo))
        
    #print(answer)
    return answer

def post_order(nodeinfo):
    answer = []
    
    left_nodeinfo ,right_nodeinfo = split_node(nodeinfo)
    # print(nodeinfo[0][2],"="*20)
    # print("node" , nodeinfo)
    # print("left" , left_nodeinfo)
    # print("right", right_nodeinfo)
    
    if left_nodeinfo:
        answer.extend(post_order(left_nodeinfo))
    if right_nodeinfo:
        answer.extend(post_order(right_nodeinfo))
    answer.append(nodeinfo[0][2])
    
    #print(answer)
    return answer
```

문제는 익숙한 전위 후위 노드 계산이어서 쉬웠다.

풀이시간도 40분 안으로 끝났고, 크게 생각하기 어려운 부분이 없었다.

하지만 재귀로풀어서 런타임 에러가 나는 부분이 있어서 재귀가 아닌 다른 방법으로 푸는 방법을 생각해 봐야겠다.



## 다른 사람의 풀이

```python

```





## 다시 풀어보기

```python

```

