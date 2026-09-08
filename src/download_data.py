%pip install kaggle
# dowload kaggle credential file
download_path = "/Workspace/Users/xarisban@gmail.com/Anti-Money-Laundering-Transaction/kaggle"

# create the download path
dbutils.fs.mkdirs(download_path)

import os 

os.environ["KAGGLE_USERNAME"] = "xaris"
os.environ["KAGGLE_KEY"] = "KGAT_3738965802e64f87ac26505d4df27300"

!kaggle datasets download -d berkanoztas/synthetic-transaction-monitoring-dataset-aml -p {dowmload_path} --unzip