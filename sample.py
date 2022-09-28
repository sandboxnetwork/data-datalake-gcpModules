import gcpModules

if __name__ == '__main__':
    ########## 1. Cloud Storage #########
    handler = gcpModules.StorageHandler(storage="storage_name", path="download_file_path")

    # check file exists
    file_exists = handler.exists("file_name.json")

    # check file list
    file_list = handler.list()

    # search file by name and by folder
    search_list = handler.list(prefix="prefix", nested=True)

    # download file by name
    downloaded, failed = handler.download("file_name.json")

    # search multiple files and download multiple files
    file_list = handler.list(prefix="prefix")
    downloaded, failed = handler.download(file_list)

    ########## 2. BigQuery #########
    handler = gcpModules.BigQueryHandler()
    q = '''
    SELECT *
    FROM table_name
    WHERE date = '2022.01.01'
    '''

    # estimate cost of query
    cost = handler.estimate(q)

    # query 
    rst = handler.query(q, limit=1)
