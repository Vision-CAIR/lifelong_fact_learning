# Generated with SMOP  0.41
# from libsmop import *
from GetResults_exact_metric1 import *
import os
import scipy.io
import json
from pprint import pprint

root='../'
model_names = os.listdir(root + '/outputs/CV_feat')
model_names = sorted(model_names)
tembedding_path= root + 'eval/eval_files/TEmbeddings/mid_scale/semantic/'

for model_name in model_names:
    results = []
    if '4tasks_semantic' in model_name:
        if not all([os.path.exists(CV_dir + model_name + '/T4' + '/B' + str(b) + 'XEmbeddings.mat') for b in range(1, 5)]):
            continue
        print(model_name)
        for b in range(1, 5):
            X_embedding=scipy.io.loadmat(root + 'outputs/CV_feat/' + model_name + '/T4/B' + str(b) + 'XEmbeddings.mat')
            X_embedding=X_embedding['XE']
            T_embedding=scipy.io.loadmat(tembedding_path + '/TEmbedding_seen_B' + str(b) + '_test.mat')
            T_embedding=T_embedding['B_T']
            TestData=scipy.io.loadmat(tembedding_path +'/TestData_seen_B' + str(b) + '_test.mat')
            TestData=TestData['BTestData']
            res_name= root + 'eval/results/mds_results/semantic/' + model_name + '_batch' + str(b) + '_m1_nodup.mat'
            Result_exact=GetResults_exact_metric1(X_embedding,T_embedding,TestData,T_embedding,flag_nodup=True)
            # pprint(Result_exact['mAP'])
            results.append('{:.2f}%'.format(Result_exact['KnowledgeMeanDetRatio_K5'] * 100.))
            # print('T{}:'.format(b), '{:.2f}%'.format(Result_exact['KnowledgeMeanDetRatio_K5'] * 100.))
            # exit()
            # save(res_name,'Result_exact') # Todo: save as json
        print('T1, T2, T3, T4, mean:')
        print(*results, sep='\t')
