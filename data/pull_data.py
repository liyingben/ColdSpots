import pandas as pd
import boto3

bucket = 'dl-training-data'


session = boto3.Session()
s3 = session.resource('s3')

#first download the training data
Q = pd.read_json('training_data.json')
Q = Q['image_path']
for k in range(0,Q.shape[0]):
	a = Q[k]
	w = a.split("/")[2]
	w = str(w)
	s3.Bucket(bucket).download_file(a,w)
	print(k)





#second download the validation data
Q = pd.read_json('val_data.json')
Q = Q['image_path']
for k in range(0,Q.shape[0]):
        a = Q[k]
        w = a.split("/")[2]
        w = str(w)
        s3.Bucket(bucket).download_file(a,w)
	print(k)