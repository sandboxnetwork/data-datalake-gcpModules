GCP Modules
======================

# 1. 개요
## 1.1. GCP Modules
- GCP 서비스의 데이터를 보다 더 직관적인 동작으로 가져오기 위함

## 1.2. 구동 환경
- Python 3.6
- 가상환경 사용 권장(anaconda, virtualenv, venv 등)

## 1.3. Prerequisite
- 프로젝트의 루트 디렉토리에 `settings.json.template` 파일명 뒤에 `.template`를 제거
- 포멧에 맞추어 gcp 플랫폼의 서비스 계정 정보를 입력

## 1.3. 기능
#### 1.3.1 Cloud Storage
- storage bucket 선언
- exists   : 스토리지에 파일 존재 여부 반환
- list     : 스토리지 파일 리스트 반환, prefix, nested 키워드로 제한하여 검색 가능
- download : 파일 또는 파일 리스트 다운로드, 성공과 실패 리스트 반환

#### 1.3.2 BigQuery
- estimate : 쿼리 실행 전 소요 예상 cost 반환(단위: gb)
- query    : 쿼리 실행, limit 키워드로 cost 제한 가능


# 2. 설치
- 다음 명령어 사용하여 설치
```
(env_name) (project_directory)$ pip install dist/gcpModules-1.0.0.tar.gz
```

# 3. 배포
- 코드 수정 후 로컬에 재설치 시에는 다음 명령어를 사용하여 build 후 재설치
```
(env_name) (project_directory)$ pip uninstall gcpModules
(env_name) (project_directory)$ python setup.py build
(env_name) (project_directory)$ python setup.py install
```

- 코드 수정 후 배포 시에는 다음 명령어를 사용하여 tar.gz 파일 생성 후 push
```
(env_name) (project_directory)$ rm -rf dist/gcpModules-1.0.0.tar.gz
(env_name) (project_directory)$ python setup.py sdist
```

# 4. 사용
- 프로젝트 내에 존재하는 sample.py 확인
- 각 메소드의 주석 확인