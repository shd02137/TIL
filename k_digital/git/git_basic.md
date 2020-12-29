# git 기초



## What?

### vcs

git은 버전관리 시스템이다.



## Why?





## How?

### 초기화

`$ git init` 로 초기화한다.



```
$ git add new.txt
$ git commit -m "first commit"
```

```python
def myfunc():
	print("py")
```



| 명령어               | 설명                      | 추가 | 내용 |
| -------------------- | ------------------------- | ---- | ---- |
| git init             | 본 폴더를 저장소로 초기화 |      |      |
| git add < filename > | 파일을 스테이지에 올림    |      |      |
| git commit -m '내용' | 변경사항 커밋             |      |      |
| git log              |                           |      |      |



사용했던 CLI 명령어들
mkdir
touch
cd (~/./..)
ls
ls -a
rm
rm -r
mv

CLI 문서 편집기 vim
i => 편집(insert)모드
esc => 명령모드
명령모드에서
:w => 저장
:q => 종료
:wq => 저장 후 종료
:q! => 강제 종료

git 명령어
git config --global user.name "이름"
git config --global user.email "이메일"
git init
git status
git log
git add <file/dirname>
git commit -m "<message>"
git restore <file/dirname>

git 핵심 주제어들
VCS
폴더(directory)
저장소(repository)
.git/
스테이지(stage area)
commits
변경사항
untracked/tracking
unmodified
modified
staged