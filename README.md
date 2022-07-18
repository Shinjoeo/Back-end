# Shinjoeo__Back-end

### 1) 가상환경 생성 및 실행

```
% python3 -m venv 가상환경이름
% source 가상환경이름/Scripts/activate
% cd Shinjoeo

```

### 2) 최상위 폴더의 requirements.txt로 필요한 package 설치

```
% pip3 install -r requirements.txt
```

# 2. MysqlDB 설정

### 1) MysqlDB 터미널에서 database 생성

```
MysqlDB [(none)]> create database Shinjoeo;
MysqlDB [(none)]> use Shinjoeo;
Database changed
MysqlDB [Billage]> grant all privileges on Billage.* to 'root'@'%' identified by '최초실행시생성한비밀번호';
```

### 2) secreats.json 생성 후 자신의 MysqlDB 정보로 수정해줍니다

```
{
    "SECRET_KEY":"따로 제공",
    "DB_PASSWORD": "최초실행시생성한비밀번호"
}

```

# 3. Migrate

### 1) 터미널에서 실행 후에 table이 생성되는지 확인해주세요 ~

```
% python manage.py makemigrations
% python manage.py migrate 
```


# 4. Django 초기 설정

```
% python manage.py runserver 
```
