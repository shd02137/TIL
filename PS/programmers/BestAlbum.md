# 해시 / 베스트앨범

## 첫번째 시도

```python
def solution(genres, plays):
    #genres =  ["classic", "pop", "classic","house", "classic", "pop", "pop","house","house"]
    #plays = [150, 500, 150, 2500, 800, 2500 ,500, 800, 2500]
    answer = []
    total_genres = list(set(genres))
    total_play = []
    for i in total_genres:
        sum =0
        for g,p in zip(genres, plays):
            if g==i:
                sum+=p
        total_play.append(sum)
    total = list(zip(total_play,total_genres))
    total.sort(reverse = True)
    print(total)

    for tot_p,tot_g in total:
        temp =[]
        for g,p in zip(genres, plays):
            if tot_g==g:
                temp.append(p)
        temp.sort()
        print(temp)
        k=0
        while temp:
            i=0
            for g,p in zip(genres,plays):
                if g==tot_g and temp[-1]==p:
                    try:
                        answer.index(i)
                    except:
                        answer.append(i)
                        temp.pop()
                        break
                i+=1
            k+=1
            if k==2:
                break



    return answer
```

리스트만 가지고 풀이를해서 구현이 복잡하게 되었다.



## 다시 풀어보기



```python
def solution(genres, plays):
    answer = []
    plays = list(map(int,plays))
    album = list(zip(genres,plays))
    order = 0
    best_album={}
    best_genre={}
    for genre,play in album:
        if genre in best_album:
            best_album[genre].append([play,order])
            best_genre[genre] += play
        else:
            best_album[genre] = []
            best_album[genre].append([play,order])
            best_genre[genre] = play
        order += 1
    
    best_genre = dict(sorted(best_genre.items(),key=(lambda x : x[1]),reverse=True))

    
    for genre in best_genre:
        temp_album = best_album.get(genre)
        temp_album = sorted(temp_album,key = lambda x : x[0], reverse=True)
        music_count = 0
        for _,music_id in temp_album:
            answer.append(music_id)
            music_count += 1
            if music_count == 2: 
                break
        
    return answer
```





## 다른 사람의 풀이

```python
def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)



    while len(dic) > 0:
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play


```

앨범을 클래스화 시켜서 해결하였다.

lt,le,gt,ge등을 처음으로 알게되었다.

init,str등을 잘 사용하지 않는데 이후 응용시 좋은 결과가 기대 된다.

