import matplotlib.pyplot as plt
import pandas as pd

def result():
    sh = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0,
          0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
          1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0,
          0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0,
          0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1]
    pel = [None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, None, 1, None, 1, None, 1, None, 1, None, 0,
           None, 1, None, None, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1,
           1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1,
           1, 1, 1, 1, 1]
    eye = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, None, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
           None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0,
           0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, None, 0, None, 0,
           None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           None, None, 0, 0, None, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None]

    sh_count = pd.Series(sh, name='sh_count', dtype='float64')
    pel_count = pd.Series(pel, name='pel_count', dtype='float64')
    eye_count = pd.Series(eye, name='eye_count', dtype='float64')
    all_count = pd.concat([sh_count, pel_count, eye_count], axis=1)
    pose_count = []
    for i in range(len(all_count)):
        if 1 in all_count.iloc[[i]].values:
            pose_count.append(1.0)
        elif 1 not in all_count.iloc[[i]].values and 0 in all_count.iloc[[i]].values:
            pose_count.append(0.0)
        elif all_count.iloc[[i]].all(None):
            pose_count.append(None)
    pose_count = pd.Series(pose_count, name='pose_count', dtype='float64')
    all_count = pd.concat([all_count, pose_count], axis=1)
    return all_count

def Visualization(all_count):
    # 흐트러진 자세 비율 구하기
    sh_count = all_count['sh_count'].sum()
    pel_count = all_count['pel_count'].sum()
    eye_count = all_count['eye_count'].sum()
    pose_count = all_count['pose_count'].sum()
    sh_none_count = all_count['sh_count'].isnull().sum()
    pel_none_count = all_count['pel_count'].isnull().sum()
    eye_none_count = all_count['eye_count'].isnull().sum()
    pose_none_count = all_count['pose_count'].isnull().sum()
    autopct = '%.1f%%'
    colors = ['lightgray', 'darkgray', '#8fd9b6']
    explode = [0, 0, 0.1]
    plt.rc('font', family='Malgun Gothic')
    plt.figure(figsize=(12, 8))
    plt.subplot(221), plt.pie([len(all_count) - (sh_count + sh_none_count), sh_none_count, sh_count],
                              labels=['전체(100%)', 'None', '어깨 흐트러짐'], autopct=autopct, explode=explode,
                              colors=colors, startangle=90), plt.title("어깨 흐트러짐 비율", fontsize=10)
    plt.subplot(222), plt.pie([len(all_count) - (pel_count + pel_none_count), pel_none_count, pel_count],
                              labels=['전체(100%)', 'None', '골반 흐트러짐'], autopct=autopct, explode=explode,
                              colors=colors, startangle=90), plt.title("골반 흐트러짐 비율", fontsize=10)
    plt.subplot(223), plt.pie([len(all_count) - (eye_count + eye_none_count), eye_none_count, eye_count],
                              labels=['전체(100%)', 'None', '얼굴 흐트러짐'], autopct=autopct, explode=explode,
                              colors=colors, startangle=90), plt.title("얼굴 흐트러짐 비율", fontsize=10)
    plt.subplot(224), plt.pie([len(all_count) - (pose_count + pose_none_count), pose_none_count, pose_count],
                              labels=['전체(100%)', 'None', '자세 흐트러짐'], autopct=autopct, explode=explode,
                              colors=colors, startangle=90), plt.title("자세 흐트러짐 비율", fontsize=10)
    plt.savefig('static/images/pose/pose_check.png', dpi=300, bbox_inches='tight')

if __name__ == '__main__':
    all = result()
    Visualization(all)