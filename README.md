GCP Modules
======================

# 1. 개요
## 1.1. GCP Modules
- GCP 서비스의 데이터를 보다 더 직관적인 동작으로 가져오기 위함

## 1.2. 구동 환경
- Python 3.6
- 가상환경 사용 권장(anaconda, virtualenv, venv 등)

## 1.3. Prerequisite
- gcp 플랫폼의 서비스 계정 정보 필요 (service_account)

## 1.3. 기능
#### 1.3.1 Cloud Storage
- storage bucket 선언
- exists   : 스토리지에 파일 존재 여부 반환
- list     : 스토리지 파일 리스트 반환, prefix, nested 키워드로 제한하여 검색 가능
- download : 파일 또는 파일 리스트 다운로드, 성공과 실패 리스트 반환
- read     : 파일 다운로드 및 읽기 (json, csv 지원)

#### 1.3.2 BigQuery
- estimate : 쿼리 실행 전 소요 예상 cost 반환(단위: gb)
- query    : 쿼리 실행, limit 키워드로 cost 제한 가능

# 2. 설치
- pip를 최신 버전으로 업그레이드
```
(env_name) (project_directory)$ pip install --upgrade pip
```
- 다음 명령어 사용하여 설치
```
(env_name) (project_directory)$ pip install git+https://github.com/sandboxnetwork/data-datalake-gcpModules.git
```

# 3. 사용법
- 프로젝트 내에 존재하는 sample.py 확인

# 4. 기본 사용 시나리오
- 프로젝트 내에 존재하는 sample.py 확인
