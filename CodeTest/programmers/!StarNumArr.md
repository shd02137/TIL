# 월간코드챌린지 / 스타수열

## 첫번째 시도

```python
def solution(a):
    answer = 0
    
    a = compress_dup(a)    
    if len(a)<= 1:
        return answer
        
    a_max_num = max_num(a)  
    
    while len(a)>1:
        a_max_num_count = 0
        a_stararray_partner = 0
        
        pre_value = None
        dup_value = 0
        for i,value in enumerate(a):
            if pre_value == value:
                dup_value += 1
            pre_value = value          
            a_stararray_partner += 1
            if value == a_max_num:
                if a_max_num_count == 1:
                    a_stararray_partner-= 1
                else:
                    a_max_num_count += 1             
            if a_max_num_count >= 1 and a_stararray_partner >=2:
                a = a[i+1:]
                answer += 2
                break
                
        if a_max_num_count == 0:
            break       
        if dup_value == len(a)-1:
            break
             
        # print(a,"answer : ", answer) 
    
    return answer

def compress_dup(a):
    result = []
    pre_pre_value = None
    pre_value = None
    for value in a:
        if pre_pre_value == pre_value == value:
            continue
        pre_pre_value = pre_value
        pre_value = value
        result.append(value)
        
    return result


def max_num(a):
    temp_dict = dict()
    
    for value in a:
        if value in temp_dict:
            temp_dict[value] += 1
        else:
            temp_dict[value] = 1         
    num,_ = max(temp_dict.items(),key = (lambda x :x[1]))
    
    return num
```

우선 숫자의 반복이 3번이상 반복되는 것이 없도록 리스트를 다시 만든다.

이후 가장 많이 나온 숫자가 무엇인지 찾아낸뒤 그 숫자를 기준으로 스타수열의 최대 길이를 찾아내었다.

결과는 테스트케이스 28번 오답과 시간초과 2문항

첫결과가 나오기까지는 40분정도 걸렸지만 오류탐색으로 30분정도를 더 사용했고,

다른사람의 질문과 개인적인 코드 분석을 통해 문제점을 찾아내었다.

그 결과는 다음과 같다.

우선 위에서 가장 많이 나온 숫자를 기준으로 스타수열의 최대 길이를 찾아내었는데, 다른 사람의 질문을 보고 이것에서 오답이 발생했음을 알아내었다.

그리고 시간초과가 나는 문제는 아마 a = a[i+1] 이라는 구문에서 발생했을 것이라고 판단했다. 

다음번에 다시 풀때에는 슬라이싱이 아닌 index_start 지점을 int로 저장해서 시간을 줄일 수 있을 것이라고 생각한다. 또한 앞으로 a = a[i+1:] 과 같은 식을 사용하는 버릇을 고쳐야 겠다고 생각했다.



## 다른 사람의 풀이

```python
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
 
int Max(int A, int B) { return A > B ? A : B; }
bool Cmp(int A, int B) { return A > B ? true : false; }
 
int solution(vector<int> a)
{
    int answer = -1;
    vector<int> Cnt(a.size() + 1, 0);
    for (int i = 0; i < a.size(); i++) Cnt[a[i]]++;
 
    for (int i = 0; i < Cnt.size(); i++)
    {
        if (Cnt[i] == 0) continue;
        if (Cnt[i] <= answer) continue;
        int Result = 0;
 
        for (int j = 0; j < a.size() - 1; j++)
        {
            if (a[j] != i && a[j + 1] != i) continue;
            if (a[j] == a[j + 1]) continue;
            
            Result++;
            j++;
        }
        answer = Max(answer, Result);
    }
    return answer * 2;
}


출처: https://yabmoons.tistory.com/610 [얍문's Coding World..]
```

보지는 않고 일단 기록용으로 가져왔다.





## 다시 풀어보기

```python

```

