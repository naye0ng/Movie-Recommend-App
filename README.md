# Movie Flex

최신 영화에 대한 데이터를 수집하여, 유저에게 영화 정보를 제공하는 서비스



## I. 프로젝트 기능

- TMDb 페이지에 api요청을 하여 최신 영화 정보를 수집
- 수집된 영화 정보를 사용자에게 제공
- 가입한 유저에 대해 기능 제공
  - 유저간 follow
  - 영화에 대한 review 작성
  - 작성한 review를 기반으로 사용자에게 영화 추천
- 영화 예고편을 modal창으로 제공





## II. 개발 및 배포

### (1) 개발 환경

- 개발 언어: python(3.6.8), html, css, javascript
- framework: django(2.1.8), Vue.js, django rest framework
- requirements.txt : package lit
```shell
# package 설치
pip install -r requirements.txt
```

### (2) 배포 환경

- 배포 플랫폼: c9





## III. 진행 과정

### (1) 팀원 정보 및 업무 분담 내역

#### 🙋‍♀️ 김나영 [Github](https://github.com/naye0ng)

- 유저 가입, 로그인 기능 구현
- 관리자 페이지 구성 
  - 유저 관리 기능
  - 영화 정보 등록
- 영화 리뷰 관련 기능
- 페이지 디자인



####  🙆‍♂ ️염희돈 [Github](https://github.com/don2101)

- 영화 정보 제공
- 유저 상세페이지 
  - 선호 장르 선택
- 영화 추천 기능
- 리뷰 관련 기능





### (2) 목표 구현 서비스

#### 1. 유저 가입, 로그인 기능

- django modelform 사용



#### 2. 관리자 페이지 구성 🤟

- 관리자 페이지에서 유저 권한 관리
- 관리자 권한을 가진 유저는 영화 등록 가능


#### 3. 영화 정보 제공

- api 요청으로 영화 정보를 수집
- 수집한 영화 정보를 영화 상세페이지에서 제공



#### 4. 사용자 페이지 🤟

- 사용자가 직접 선호하는 장르를 설정
- 선호하는 장르를 기반으로 영화 추천
- 유저간 follow 가능



#### 5. 리뷰 관련

- 영화에 대한 리뷰 조회, 작성, 수정, 삭제 기능





### (3) 핵심 기능

#### 1. 영화 추천

- 유저가 설정한 장르에 따라 영화 추천
- **추가 구현**: 유저가 follow하는 유저가 높게 평가한 순으로 정렬


#### 2. 예고편 제공

- **추가 구현**: youtube api 사용하여 구현 예정



### (4) 배포 서버 URL

[don2101 메인페이지](https://movie-recommendator-don2101.c9users.io/)

[naye0ng 메인페이지](https://movie-recommend-app-naye0ng.c9users.io/)


