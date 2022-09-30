import gcpModules

if __name__ == '__main__':
    
    """
    0. Service account settings
    GCP에서 제공받은 서비스 계정을 입력
    """
    service_account = {}
    service_account_path = ""

    """
    1. Cloud Storage
    1-0. Cloud Storage Handler

    Args:
        credentials       : GCP에서 제공받은 서비스 계정
        credential_path   : GCP에서 제공받은 서비스 계정이 저장된 로컬 경로
        bucket[option]    : storage bucket 이름
        file_path[option] : 다운로드 시 필요한 로컬 파일 경로
    """
    handler = gcpModules.StorageHandler(credentials=service_account)
    handler = gcpModules.StorageHandler(credential_path=service_account_path)
    handler = gcpModules.StorageHandler(credential_path=service_account_path, bucket="bucket_name", file_path="file_path")
    
    # storage bucket 이름을 지정 (추후 매번 버킷명을 입력하지 않도록)
    handler.set_bucket("bucket_name")
    # 다운로드 시 필요한 로컬 파일 경로를 지정 (추후 매번 경로를 지정하지 않도록)
    handler.set_file_path("file_path")

    """
    1-1. exists
    파일 존재 유무 확인
    
    Args:
        name              : 스토리지 파일명 or 파일경로
        bucket[option]    : storage bucket 이름

    Return:
        bool
    """
    # 파일명으로 조회
    file_exists = handler.exists("file_name.json")
    # 파일 경로로 조회
    file_exists = handler.exists("folder_name/file_name.json")
    # 파일 경로 + 버킷 설정
    file_exists = handler.exists("folder_name/file_name.json", bucket="bucket_name")

    """
    1-2. list
    파일 검색
    
    Args:
        bucket[option]    : storage bucket 이름
        prefix[option]    : 접두사로 검색, (*폴더명도 접두사에 포함)
        nested[option]    : 하위 디렉토리 포함 여부 (default True)

    Return:
        blob object list
    """
    # 설정된 버킷의 모든 파일 검색
    blob      = handler.list()
    blob_list = handler.list()
    # 새로 설정하는 버킷의 모든 파일 검색
    blob_list = handler.list(bucket="bucket_name")
    # 접두사로 폴더명을 넣어 해당 폴더 내의 모든 파일 검색
    blob_list = handler.list(prefix="folder_name")
    # 접두사로 폴더명을 넣어 해당 폴더 내의 모든 파일 검색, 하위 폴더 제외
    blob_list = handler.list(prefix="folder_name", nested=False)
    # 접두사로 파일명을 가진 모든 파일 검색, 하위 폴더 제외
    blob_list = handler.list(prefix="filename_prefix", nested=False)

    # 반환된 blob 객체에서 파일 명을 얻고자 하는 경우
    file_list = [blob.name for blob in blob_list]

    """
    1-3. download
    파일 다운로드, progress bar를 사용하여 진행률 표시
    
    Args:
        blob or blob_list : list()를 통해 검색한 blob 객체 결과
        file_path[option] : 파일을 다운로드할 로컬 경로

    Return:
        다운로드 완료된 로컬 경로 리스트
    """
    # 파일 다운로드
    downloaded_paths = handler.download(blob)
    # 파일 리스트 다운로드
    downloaded_paths = handler.download(blob_list)
    # 파일 리스트 다운로드, file_path 경로
    downloaded_paths = handler.download(blob_list, file_path="file_path")

    """
    1-4. read
    파일 다운로드 및 읽기 (*json, csv 지원, 단일 객체)
    
    Args:
        blob              : list()를 통해 검색한 blob 객체 결과, *단일 객체만 가능
        file_path[option] : 파일을 다운로드할 로컬 경로

    Return:
        파일 내용
    """
    result = handler.read(blob)
    result = handler.read(blob, file_path="file_path")

    
    """
    2. BigQuery
    2-0. BigQuery Handler

    Args:
        credentials       : GCP에서 제공받은 서비스 계정
        credential_path   : GCP에서 제공받은 서비스 계정이 저장된 로컬 경로
    """
    handler = gcpModules.BigQueryHandler(credentials=service_account)
    handler = gcpModules.BigQueryHandler(credential_path=service_account_path)
    # 조회를 원하는 쿼리문
    # **From절은 dataset가 항상 포함되어 있어야 함
    q = '''
    SELECT *
    FROM dataset.table_name
    WHERE date = '2022.01.01'
    '''

    """
    2-1. estimate
    소비 용량 예측 (gb 단위)
    
    Args:
        q : 조회를 원하는 쿼리문

    Return:
        예측된 소비 용량 (gb)
    """
    cost = handler.estimate(q)

    """
    2-2. query
    쿼리문 조회
    
    Args:
        q                    : 조회를 원하는 쿼리문
        cost_limit[optional] : 소비 용량 제한 (default 50)

    Return:
        쿼리 결과값
    """
    rst = handler.query(q)
    rst = handler.query(q, cost_limit=1)


    """
    기본 사용 시나리오 (storage)
    """
    handler = gcpModules.StorageHandler(credential_path=service_account_path, bucket="bucket_name", file_path="file_path")

    # 시나리오 1
    blob_list        = handler.list()
    downloaded_paths = handler.download(blob_list)

    # 시나리오 2
    blob_list        = handler.list()
    for blob in blob_list:
        result = handler.read(blob)
        # modify result here

    """
    기본 사용 시나리오 (Bigquery)
    """
    handler = gcpModules.BigQueryHandler(credential_path=service_account_path)
    q       = ""
    rst     = handler.query(q)
