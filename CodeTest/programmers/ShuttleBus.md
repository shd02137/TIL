# 2018 카카오코테 / 셔틀버스

## 첫번째 시도

```python
def solution(n, t, m, timetable):

    waiting_person = len(timetable)
    persontime_values = [ int(time.split(":")[0])*60 + int(time.split(":")[1])  for time in timetable]
    persontime_values.sort()
    bus_arrivetime = [9*60+i*t for i in range(n) ]


    for time_now in bus_arrivetime:
        persontime_values,fullbus = take_person(time_now,m,persontime_values)

        
    if not fullbus:
        answer_value =  bus_arrivetime[-1]
    else:
        answer_value = fullbus - 1
        
    answer = change_value_to_time(answer_value)

    return answer

#시간 변환
def change_value_to_time(value):

    HH = value//60
    MM = value%60
    result = f"{HH:0>2}:{MM:0>2}"
    
    return result

def take_person(time_now,ride_person_per_bus,persontime_values):
    fullbus = False
    while ride_person_per_bus:
        if not persontime_values:
            break
        if time_now>=persontime_values[0]:
            if ride_person_per_bus ==1:
                fullbus = persontime_values[0]
            persontime_values = persontime_values[1:]
            ride_person_per_bus -= 1
        else:
            break
    
    return persontime_values,fullbus
```

우선 사람들이 오는 시간과  버스가 오는 시간을 순서대로 모두 구한다.

그리고 마지막 셔틀버스가 올때까지 사람들을 계속 가능한 많이 태워서 보낸다.

셔틀버스는 출발하면서 자신의 버스가 만치이면 마지막에 탑승한 사람의 도착시간을 반환해준다.

마지막 셔틀버스를 보내고 버스가 만차인지 아닌지에따라 정답을 구한다.



(목표시간 40분, 풀이 시간 50분)

늦은 이유: 

1. 문제 이해하는데만 10분넘게 써버렸다.그러고도 처음에 풀이 방법을 잘못 생각해서 5분정도 날렸다.  
2. 시간을 값으로 변환하고, 값을 시간으로 돌려주는데 시간이 조금 지체되었다.

아쉬운점 :

1. 시간을 값으로 변환하는걸 함수를 만들어서 쓰면 깔끔하고 관리가 편할텐데 너무 한줄로 끝내려고 욕심부렸다.

```python
#시간 변환
def change_value_to_time(value):
    HH = value//60
    MM = value%60
    result = f"{HH:0>2}:{MM:0>2}"
        
    return result

def change_time_to_value(time):
    HH,MM = time.split(":")
    value = int(HH)*60 + int(MM)
    
    return value

def change_time(timetable):
    persontime_values = []
    for time in timetable:
        persontime_values.append(change_time_to_value(time))
    
    return sorted(persontime_values)

def make_bus_timetable(n,t):
    bus_timetable = []
    for i in range(n):
        time = 9*60+i*t
        bus_timetable.append(time)
    
    return bus_timetable

#셔틀에 사람 태우는 함수
def take_person(time_now,ride_person_per_bus,persontime_values):
    fullbus = False
    while ride_person_per_bus:
        if not persontime_values:
            break
        if time_now>=persontime_values[0]:
            if ride_person_per_bus ==1:
                fullbus = persontime_values[0]
            persontime_values = persontime_values[1:]
            ride_person_per_bus -= 1
        else:
            break
    
    return persontime_values,fullbus

def solution(n, t, m, timetable):
    persontime_values = change_time(timetable)
    bus_arrivetime = make_bus_timetable(n,t)

    for time_now in bus_arrivetime:
        persontime_values,fullbus = take_person(time_now,m,persontime_values)
        
    if not fullbus:
        answer_value =  bus_arrivetime[-1]
    else:
        answer_value = fullbus - 1        
    answer = change_value_to_time(answer_value)

    return answer
```



## 다른 사람의 풀이

```python
def solution(n, t, m, timetable):
    answer = ''
    timetable = [ int(time[:2])*60 + int(time[3:5]) for time in timetable ]

    timetable.sort()

    for i in range(n):
        last_time = 540 + (n - 1) * t
        if len(timetable) < m:
            return '%02d:%02d' % (last_time // 60, last_time % 60)
        if i == n - 1:
            if timetable[0] > last_time:
                return '%02d:%02d' % (last_time // 60, last_time % 60)
            time = timetable[m - 1] - 1
            return '%02d:%02d' % (time // 60, time % 60)
        for j in range(m-1, -1, -1):
            bus_arrive = 540 + i * t
            if timetable[j] <= bus_arrive:
                del timetable[j]
```

방법자체는 유사하다. 

어짜피 버스도착시간을 기준으로 계산을 하므로 한번에 계산해서 저장해두는 것보다 이 풀이처럼 그때그때 하나씩 만들어가는게 저장공간이나 속도면에서 이득일것 같다. 

다음에 list를 지울때 del이 존재한다는것을 기억해 두어야 겠다.

## 다시 풀어보기

```python

```

