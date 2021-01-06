# Python 기초

알고있는 기본적인 부분은 넘어가지만 그날그날 새롭게 알게 된것을 정리하기위해 만들었습니다.

## 함수

### 인수

def function(일반변수,*가변변수,**키워드 변수):

​	return 0

ex) functions("계산기",88,77,44,55,66,method = "plus")

* 일반 변수

  일반 변수는 항상 가변변수나 키워드 변수보다 앞에 있어야한다.

* 가변변수 ex)print("asdf", "asdf")

  인수의 수가 고정되지 않아 원하는 만큼 인수를 지정할 수 있다.

  함수에서 이를 튜플로 받고 하나만 사용이 가능하다.

  이런식으로도 사용이 가능하다.

  ```python
  a = [1,2,3,4,5]
  
  def func(*list):
  	return list
  
  func(*a)
  ```

  

  

* 키워드 변수

  키워드 인수를 가변 개수로 전달 할 때 사용한다.

  dictionary 타입으로 전달이 된다.
  
  이런식으로도 사용이 가능하다.
  
  ```python
  dict = {
  
  "a" : "1"
  
  }
  
  def func(**option):
  	print(option)
  	return 0
  
  func(**dict)
  ```
  
  
  
  
  
  

 ## docstring

함수의 도움말으로 함수 코드블록 맨앞에 문자열로 작성한다.

""함수의 도움말""" 형식으로 도움말을 넣어주면 

help(함수명) 으로 호출이 가능하다.



## 문자열

### 매서드

* str.find("str")

  왼쪽에서부터 "str"을 찾는다.

* str.rfind("str")

  오른쪽에서부터 "str"을 찾는다.

* str.endswith("str")

  "str"로 시작하는지 확인한다. return bool

* str.startswith("str")

  "str"로 끝나는지 확인한다. return bool

  

 ### 포맷팅

* print(f"이름:{name:4s}, 나이: {age:3d}, 키: {height:.2f}")

  print("")의 ""앞에 f를 넣어 .format을 대신할 수 있다.

   