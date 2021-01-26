# MariaDB

ORM







## RDBS

 관계기반 데이터베이스 시스템의 약자이다. 데이터가 엄격한 데이터 스키마를 따라 데이터베이스 테이블에 저장되며, SQL을 사용하여 데이터를 관리하고, 모든 데이터를 2차원 테이블로 표현한다. 과거 주로 사용하던 DB의 형태로 oracle,MSSQL,MySQL,MariaDB 등이 있다.

데이터가 자주 수정되는 애플리케이션일 경우, 혹은 수정될 여지가 없고, 명확한 스키마가 사용자와 데이터에게 중요한 경우 사용한다.


## NOSQL

 데이터 사이의 관계가 없고 RDBS에 비해 훨신 더 대용량의 데이터를 저장할 수 있다. 스키마가 없고 데이터의 구조가 JSON과 유사하다.새롭게 떠오른 DB의 운영방식으로 MongoDB,레디스등이 있다.

정확한 데이터 구조를 알수 없거나 변경 확장 될 수 있는 경우 사용한다.



## UML

 통합 모델링 언어의 약자로 표준화된 범용 모델링 언어이다.
다음과같은 3가지의 목적을 위해 만들어진다.

* 의사소통 또는 설계 논의를 위해
* 전체 시스템의 구조 및 클래스의 의존성 파악을 위해
* 유지 보수를  위한 설계의 back-end문서 제작을 위해



## ERD

개체 관계 모델(Enity Relationship Diagram)의 약자로 관리하고자하는 정보의 실체(Entitiy), Entitiy를 구성하고 있는 구성요소(Attribute), Entitiy간의 관계(Relationship)로 데이터 모델링 단계에서 작성하는 다이어그램이다.
관계의 표현 방법은 여러가지가 있다 점선은 선택, 실선은 필수 사항을 의미하고 ,삼지창 형태는 하나이상, 단선은 하나 고리는 0을 의미한다.



## 정규화

1원칙 : 한가지 행을 특정할 수 있는 정보가 있어야한다.

2원칙 : 데이터의 중복이 존재하면 안된다

3원칙 :



## DB 구축의 일반적인 절차

1. DB 설치
2. CRUD(생성,읽기,업데이트,삭제) 작업
3. Data 활용



## SQL 기본 활용

### 주석

* -- : 한줄 주석문을 작성할 때 사용한다.
* /* */ : 여러줄 주석문을 작성할 때 사용한다.



### 테이블 구조 출력

테이블의 구조를 출력한다.

```mysql
> desc table_name;
or
> describe table_name;
```



### 샘플 데이터 베이스 구축

* 샘플 데이터 베이스 생성

  ``` mysql
  > C:\User\user > mysqldump -u [user] -p databasename > [경로]
  >mysqldump -u root -p sqldb > C:\User\user\Desktop\db_dumb.sql
  ```

  



* 샘플 데이터 베이스로 구축

  ``` mysql
  > source db_dumb.sql
  ```

  

### select

```mysql
> select [필드목록] from [테이블명];
-- 추가 가능 
-- (where [조건] , group by [컬럼명], having [조건], order by [컬럼명]);
```

 처럼 사용된다.



#### where 절

And, Or, Between A and B,IN(A,B,C), Like등이 사용 가능하다.

```mysql
-- And 예시
> select * from userTbl where birth_date >= '1970-01-01' and birth_date <= '1970-12-31'

-- Between 예시
> select * from userTbl where birth_date between '1970-01-01' and '1970-12-31';

-- IN 예시
> select * from userTbl where name IN("홍길동","둘리","도우너");

-- NOT IN 예시
> select * from userTbl where name Not IN("홍길동","둘리","도우너");


-- Like 예시
-- 홍으로 시작하는 모든이름
> select Name from userTbl where name Like '홍%';

-- 길동으로 끝나며 한글자가 앞에 들어가는 모든 이름
> select Name from userTbl where name Like '_길동'; 

-- null을 찾을경우
> select name from userTbl where name is null;
```



#### 서브 쿼리

from 절이나 where 절에 select 문을 넣을 수 있고 이것을 서브쿼리라고 한다.
서브 쿼리를 작성할 때 반드시 ()안에 작성 해야한다.

```mysql
> select name from userTbl 
where height > (select height from userTbl where name = "홍길동")
```

서브쿼리의 결과에 상황에 맞게 Any/ All /Some을 사용할 수 있다.

* Any는 결과값중 어떤것 하나에만 조건이 충족되면 된다.

  ```mysql
  > select name from userTbl 
  where birth_date > all(select birth_date from userTbl where address ="서울" )
  ```

  

* All은 모든 결과값에 조건이 충족되면 된다.

  ```mysql
  > select name from userTbl 
  where birth_date > all(select birth_date from userTbl where address ="서울" )
  ```

  

* Some가지고 있는 결과값과 조건이 같으면 된다.(In 과 동일한 동작을 한다.)

  ```mysql
  >select name from userTbl 
  where birth_date = some(select birth_date from userTbl where address ="서울" )
  ```



#### 중복제외

중복된것을 하나만 남기기 위해 Distinct를 사용한다.

```mysql
> select distinct name from userTbl;
```



#### 출력 개수 제한

출력 개수를 제한하기 위해 Limit를 사용한다.

```mysql
-- 0번째부터 10개를 출력하는 쿼리문
> select name from usertbl limit 0,10;
```



#### 테이블을 복사할경우

테이블을 생성할때와 동일한 구조로 테이블을 생성하지만 제약조건은 복사되지 않는다.(ex>primary key)

```mysql
> create table newtable 
(select name,birth_date from usertbl);
```



#### 그룹을 나누는 경우

특정 컬럼을 중심으로 그룹을 나누는 경우는 group by를 사용한다.

* group by의 결과를 일정한 조건으로 필터링하고싶은경우 having을 사용한다.

  ```mysql
  -- userid를 기준으로 price와 amout 곱의 합이 1000초과인 사람의 이름과 합만 출력한다.
  > SELECT userID, SUM(price*amount) FROM buyTbl
  GROUP BY userID HAVING SUM(price*amount) > 1000 ;
  ```

  

* Rollup

  중간 합계와 총 합을 출력한다.

  ```mysql
  > SELECT userID, SUM(price*amount) FROM buyTbl
  GROUP BY userID with rollup;
  ```

  

### insert

데이터 삽입시 사용한다.

```mysql
> insert into table(칼럼명...) values (들어갈 값...)
> insert into tb1(id, name) values (1,'홍길동');
```

다중 입력시에는 다음과 같이 사용할 수 있다.

```mysql
-- 직접 입력시
> insert into tbl values
(NULL, 1,'홍길동'),
(NULL, 2,'둘리'),
(NULL, 3,'도우너');

-- 다른 테이블의 값들을 활용할 시
> insert into tbl select index, num, name from usertbl;

```



### update

데이터를 수정할 때 사용한다.

```mysql
UPDATE 테이블이름 SET 열1=값1, 열2=값2 ... [WHERE 조건]; 
-- where이 없으면 테이블의 값을 전부 수정한다.
> UPDATE buyTBL2 SET price = price * 1.5 ;
```



### delete

데이터를 삭제할 때 사용한다.

```mysql
> DELETE FROM 테이블 이름 [WHERE 조건]; -- where이 없으면 테이블의 값을 전부 삭제한다.
> DELETE FROM testTBL4 WHERE Fname = 'Aamer';

```



## SQL 내장함수

### 데이터 형 변환

* cast(표현식 as 데이터형식)

  cast를 사용해서 표현식을 특정한 데이터 형식으로 바꿀수 있다.

  ```mysql
  > SELECT CAST('2020-10-19 12:35:29.123' AS DATE) AS 'DATE';
  > SELECT CAST('2020-10-19 12:35:29.123' AS TIME) AS 'TIME';
  > SELECT CAST('2020-10-19 12:35:29.123' AS DATETIME) AS 'DATETIME'; 
  > SELECT CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 개수' FROM buyTBL;
  ```

* Convert(표현식, 데이터 형식)

  convert를 사용해서 표현식을 특정한 데이터 형식으로 바꿀수 있다.

  ```mysql
  > SELECT CONVERT(AVG(amount),SIGNED INTEGER) AS '평균 구매 개수' FROM buyTBL;
  ```



### 제어 흐름 함수

* If(조건, 참, 거짓)

  ```mysql
  > select if (100>200, '참','거짓');
  -- 거짓
  ```



* IfNull(수식1,수식2)

  수식 1이 Null이 아니면 수식 1을 리턴하고,  Null이면 수식 2 리턴

  ```mysql
  > SELECT IFNULL(NULL, '널이군요'), IFNULL(100, '널이군요');
  -- 널이군요, 100
  ```



* NullIf(수식1, 수식2)

  수식1과 수식2가 같으면 NULL 반환, 다르면 수식1 반환

  ```mysql
  > Select NullIf(100,100), Nullif(200,100);
  -- NULL, 200
  ```




#### Case ~ when ~ else ~ end

```mysql
> SELECT NAME, CASE WHEN SEX LIKE 'male' THEN 'M' ELSE 'F' END FROM userTbl;
```



### 문자열 결합

* concat(문자열 ...)

  concat에 결합을 원하는 문자열을 넣어서 결합할 수 있다.

  ```mysql
  > SELECT CONCAT('이것이', SPACE(10), 'MariaDB다'); 
  -- space(10)으로 공백을 만들 수 있다.
  ```

* concat_ws(구분자,문자열 ...)

  결합할때 문자열 사이에 구분자를 넣고 싶다면 concat_ws를 사용할 수 있다.

  ```mysql
  > SELECT CONCAT_WS('/', '2022', '01', '01');
  ```

  

###   문자열 길이

* Bit_length(문자열), char_length(문자열),length(문자열)

  ```mysql
  > SELECT BIT_LENGTH('abc'), CHAR_LENGTH('abc'), LENGTH('abc');
  --24, 3 ,3
  > SELECT BIT_LENGTH('가나다'), CHAR_LENGTH('가나다'), LENGTH('가나다');
  --72, 3 , 9(utf-8 기준)
  --48, 3 , 6(euc-kr 기준)
  ```

  

### 문자열 탐색

* INSTR(기준 문자열,찾울문자열)

  이때 시작점이 1이란 점에 유의하자(시작점이 0이 아니다.)

  ```mysql
  > SELECT INSTR('하나둘셋', '둘');
  -- 3 
  ```



### 문자열 변환

* Format(숫자, 소수점 자리수)

  소수점 자리수에서 반올림해준다.(0이하의 수는 0과 동일하게 취급한다.)

  ```mysql
  > SELECT FORMAT(123456.123456, 4);
  -- 123456.1235
  > SELECT FORMAT(123456.123456, -4);
  -- 123456
  ```



* insert(기준 문자열, 위치, 길이 ,삽입할 문자열)

  ```mysql
  > SELECT INSERT('abcdefghi', 3, 4, '@@@@');
  -- ab@@@@ghi
  > SELECT INSERT('abcdefghi', 3, 2, '@@@@');
  -- ab@@@@efghi
  ```



* left(문자열, 길이), right(문자열, 길이)

  ```mysql
  > SELECT LEFT('abcdefghi', 3);
  -- abc
  > SELECT RIGHT('abcdefghi', 3);
  -- ghi
  ```



* upper(문자열),lower(문자열)

  ```mysql
  > SELECT LOWER('abcdEFGH')
  -- abcdefgh
  > SELECT UPPER('abcdEFGH');
  -- ABCDEFGH
  ```

  

### 문자열 공백 지우기

* LPAD(문자열, 길이, 공백문자), RPAD(문자열,길이,공백문자)

  문자열을 채우고 길이가 남는만큼 공백문자를 채운다.



* LTRIM(문자열), RTRIM(문자열), TRIM(문자열)

  문자열 양 끝에서 부터 공백 문자를 지운다.
  TRIM(BOTH 'A' FROM "ASTRA")처럼 사용할 수도 있다.

  ```mysql
  > SELECT TRIM(' 나머지 '), TRIM(BOTH 'ㅋ' FROM 'ㅋㅋㅋ가운데ㅋ글자.ㅋㅋㅋ');
  -- 나머지 , 가운데ㅋ글자
  ```

  



### 문자열 자르기

* substring(문자열, 시작위치, 길이)

  ```mysql
  > SELECT SUBSTRING('대한민국만세', 3, 2);
  -- 민국
  ```



* substring_index(문자열, 구분자, 횟수)

  ```mysql
  > SELECT SUBSTRING_INDEX('cafe.naver.com', '.', 2);
  -- cafe.naver
  > SELECT SUBSTRING_INDEX('cafe.naver.com', '.', -2);
  -- naver.com
  ```

  

### 날짜 및 시간

* 날짜와 시간을 가져오는 내장 함수는 다음과 같다.

  현재시간 : CURDATE(), CURTIME(), NOW(), SYSDATE() 

  특정 시간값 추출 : 
  YEAR(날짜), MONTH(날짜), DAY(날짜) , HOUR(시간), MINUTE(시간), SECOND(시간), MICROSECOND(시간)

* DateDiff(날짜1, 날짜2), TimeDiff(날짜1, 날짜2)

  두 날짜 혹은 시간 사이의 차이를 출력한다.

  ```mysql
  > SELECT DATEDIFF('2022-01-01', NOW()), TIMEDIFF('23:23:59', '12:11:10');
  ```

  

## 조인

 관계형 테이블의 가장 큰 특징으로 두개 이상의 테이블을 서로 묶어서 하나의 결과 집합으로 만들어 내는 것을 조인(join)이라고 한다.

### INNER Join

공통된 컬럼을 기반으로 결합시간다. 사용 방법은 다음과 같다.

```mysql
> SELECT [칼럼 목록] FROM [주 테이블]
INNER JOIN [서브 테이블] ON [조인 조건]
(WHERE [검색 조건]);

> SELECT * FROM buyTBL 
INNER JOIN userTBL ON buyTBL.userID = userTBL.userID
WHERE buyTBL.userID = "JYP" (ORDER BY userTBL.userID);
```



3개 이상의 테이블을 조인할수도 있다.

```mysql
SELECT S.stdName, S.addr, C.clubName, C.roomNo FROM stdTBL S
INNER JOIN stdclubTBL SC ON S.stdName = SC.stdName
INNER JOIN clubTBL C ON SC.clubName = C.clubName
ORDER BY S.stdName;
```



### OUTER Join

값이 없는 경우에도 기준 테이블의 모든 행에 대해 조인한다.
outer join은 총 3가지가 존재한다.(left, right, full)
사용법은 다음과 같다.

```mysql
> SELECT [컽럼 목록] FROM [메인 테이블(LEFT)]
(LEFT | RIGHT | FULL) JOIN [서브 테이블(RIGHT)] ON [조인될 조건]
[WHERE 검색 조건];

> SELECT U.userID, B.prodName FROM userTBL U
LEFT OUTER JOIN buyTBL B ON U.userID = B.userID
ORDER BY U.userID;
```



### CROSS JOIN

두테이블의 가능한 모든 조합을 반환한다.



### SELF Join

한 개의 테이블을 두개의 테이블로 생각하여 자체적으로 조인을 수행한다.



## 제약조건설정







제약조건



foreign key => primary key나 unique 제약조건 참조가능

check = 조건 달성 확인

default 기본값



constranint 제약조건 , 제약조건_별명(컬럼명)

제약조건 타임 관례 : 제약조건 타입(PK | U | C)_테이블명 _ 컬럼명



foreign key



## 사용자생성

create user 'iot'@'%' identified by '0000';

iot를 %(모든 아이피에서) 접근가능하게 만든다.(비밀번호는 0000)

이후 계정 설정을 바꾸고 싶으면 alter을 사용한다.



## 권한 부여

grant all privileges on sqldb.* to 'iot'@'%';

_*은 테이블 명이고 ' * '처럼  ''같은건 붙이지 않는다._

























