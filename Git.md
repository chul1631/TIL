# Git이란?

- 분산버전관리시스템 버전을 관리하는 도구

  


## 명령어 - log



### $ git log 

- 현재 저장소에 기록된 커밋을 조회

- 다양한 옵션을 통해 로그를 조회할 수 있음 

  `$ git log -1` `$ git log --oneline`  `$ git log -2 --oneline`



### $ git status

- Git 저장소에 있는 파일의 상태를 확인하기 위하여 활용



## 파일 라이프사이클

- status로 확인할 수 있는 파일의 상태 
- Tracked : 이전부터 버전으로 관리되고 있는 파일 
- Unmodified : git status에 나타나지 않음 
- Modified : 파일이 수정된 상태 (add 명령어를 통하여 staging area로)
- Staged : 수정한 파일을 곧 커밋할 것이라고 표시한 상태 (commit 명령어로 저장소)

![2433203557690E1012](Git.assets/2433203557690E1012-16570948359717.png)

|         명령어         |              내용               |
| :--------------------: | :-----------------------------: |
|        git init        |        로컬 저장소 생성         |
|    git add '파일명'    | 특정파일 / 폴더의 변경사항 추가 |
|       git add .        |              전체               |
| git commit -m '메세지' |         커밋(버전 기록)         |
|       git status       |            상태 확인            |
|        git log         |            버전 확인            |



## 원격 저장소 흐름

![img](https://blog.axosoft.com/wp-content/uploads/2018/05/push-and-pull.png)



## Git Hub에서 원격 저장소 제작 및 활용

1. New Repositiory

2. 저장소 설정하기

3. 주소 확인 http:://github.com/username/저장소 이름

4. 저장소 경로 설정 $git remote add origin http:://github.com/username/저장소 이름

5. $ git remote -v   원격 저장소의 정보를 확인함

6. $ git push <원격저장소이름> <브랜치이름>

   - 원격 저장소로 로컬 저장소 변경 사항(커밋)을 올림(push) 
   - 로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)이 올라감

7. $ git pull <원격저장소이름> <브랜치이름> • 원격 저장소로부터 변경된 내역을 받아와서 이력을 병합함

   
   
   

## 원격저장소 설정 기본 명령어

|              명령어               |                내용                 |
| :-------------------------------: | :---------------------------------: |
|          git clone <url>          |           원격저장소 복제           |
|           git remote -v           |        원격저장소 정보 확인         |
| git remote add <원격저장소> <url> | 원격저장소 추가 (일반적으로 origin) |
|    git remote rm <원격저장소>     |           원격저장소 삭제           |
|  git push <원격저장소> <브랜치>   |          원격저장소에 push          |
|  git pull <원격저장소> <브랜치>   |        원격저정소로부터 pull        |



##  gitignore 

- Git 저장소에 .gitignore 파일을 생성하고 해당 내용을 관리한다.
- 일반적인 개발 프로젝트에서 버전 관리를 별도로 하지 않는 파일/디렉토리가 발생한다.

❗ **주의** ❗ `이미 커밋된 파일은 반드시 삭제를 하여야 .gitignore로 적용 , 프로젝트 시작전에 미리 설정`

