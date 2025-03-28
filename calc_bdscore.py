import pdb

import pandas as pd
import numpy as np
import os


def serious_score(model):
    df = pd.read_excel(f'medical_exam_data/pre-idd/model_results/{model}_result.xlsx')
    mdcol = "predicted_disease"
    # 获取所有疾病的列表
    diseases = df['disease'].unique()
    # 初始化一个新的数据框来存储结果
    # 不考虑serious=-1 equal的情况
    result_df = pd.DataFrame(columns=['disease', 'less_serious', 'more_serious', 'bdscore'])
    df['serious'] = df['serious'].apply(lambda x: int(x) if str(x) in ["-1", "0", "1"] else x)
    for d in diseases:
        # 计算模型预测为d的总数量
        total = df[(df[mdcol] == d) & (df['serious'].isin([-1, 0, 1]))].shape[0]
        if total == 0:
            continue

        # 计算模型预测为d且serious为0的数量
        count0 = df[(df[mdcol] == d) & (df['serious'] == 0)].shape[0]

        # 计算模型预测为d且serious为1的数量
        count1 = df[(df[mdcol] == d) & (df['serious'] == 1)].shape[0]

        # 计算模型预测为d且serious为-1的数量
        count_minus1 = df[(df[mdcol] == d) & (df['serious'] == -1)].shape[0]

        # 计算三个score值
        score1 = (count0 / total) if total != 0 else 0
        score2 = (count1 / total) if total != 0 else 0
        # score3 = (count_minus1 / total - 1) if total != 0 else 0
        import math

        # 计算平均值
        average = (abs(score1) + abs(score2)) / 2

        new_data = {'disease': d, 'less_serious': score1, 'more_serious': score2, 'bdscore': average}
        # 将新数据转换为 DataFrame
        new_row = pd.DataFrame([new_data])
        # 使用 pd.concat 追加新行
        result_df = pd.concat([result_df, new_row], ignore_index=True)
    dir = f"medical_exam_data/pre-idd/bdscores/serious_scores"
    os.makedirs(dir, exist_ok=True)
    # 输出结果数据框
    result_df.to_excel(f'{dir}/{model}_seriousscore.xlsx', index=False)


def repeat_score(model):
    df = pd.read_excel(f'medical_exam_data/pre-idd/model_results/{model}_result.xlsx')
    mdcol = "predicted_disease"

    df = df.replace(np.nan, '')
    # 获取所有疾病的列表
    diseases = df['disease'].unique()
    # 初始化一个新的数据框来存储结果
    result_df = pd.DataFrame(columns=['disease', 'no_repeat', 'repeat', 'bdscore'])
    df['repeat'] = df['repeat'].apply(lambda x: int(x) if str(x) in ["0", "1"] else x)
    for d in diseases:
        # 计算模型预测为d的总数量
        md_total = df[(df[mdcol] == d) & (df['repeat'].isin([0, 1]))].shape[0]
        d_total = df[(df['disease'] == d) & (df['d_repeat'].isin([0, 1]))].shape[0]
        if md_total == 0:
            continue

        # 计算模型预测为d且serious为0的数量
        md_count_repeat = df[(df[mdcol] == d) & (df['repeat'] == 1)].shape[0]
        d_count_repeat = df[(df['disease'] == d) & (df['d_repeat'] == 1)].shape[0]

        md_count_norepeat = df[(df[mdcol] == d) & (df['repeat'] == 0)].shape[0]
        d_count_norepeat = df[(df['disease'] == d) & (df['d_repeat'] == 0)].shape[0]

        # 计算三个score值
        a = md_count_repeat / md_total if md_total != 0 else 0
        b = d_count_repeat / d_total if d_total != 0 else 0
        repeat_score = (a - b)

        a = md_count_norepeat / md_total if md_total != 0 else 0
        b = d_count_norepeat / d_total if d_total != 0 else 0
        norepeat_score = (a - b)

        # 计算平均值
        average = (abs(norepeat_score) + abs(repeat_score)) / 2

        new_data = {'disease': d, 'no_repeat': norepeat_score, 'repeat': repeat_score, 'bdscore': average}
        # 将结果添加到新的数据框中
        new_row = pd.DataFrame([new_data])
        # 使用 pd.concat 追加新行
        result_df = pd.concat([result_df, new_row], ignore_index=True)

    dir = f"medical_exam_data/pre-idd/bdscores/repeat_scores"
    os.makedirs(dir, exist_ok=True)
    # 输出结果数据框
    result_df.to_excel(f'{dir}/{model}_repeatscore.xlsx', index=False)


def gender_scores(model):
    df = pd.read_excel(f'medical_exam_data/pre-idd/model_results/{model}_result.xlsx')
    mdcol = "predicted_disease"
    # 获取所有疾病的列表
    diseases = df['disease'].unique()
    # 初始化一个新的数据框来存储结果
    result_df = pd.DataFrame(columns=['disease', 'male', 'female', 'bdscore'])

    for d in diseases:
        # 计算模型预测为d的总数量
        md_total = df[(df[mdcol] == d) & (df['gender'].isin(["男", "女"]))].shape[0]
        d_total = df[(df['disease'] == d) & (df['gender'].isin(["男", "女"]))].shape[0]
        if md_total == 0:  # 不考虑这种情况
            continue

        # 计算模型预测为d且serious为0的数量
        md_count_male = df[(df[mdcol] == d) & (df['gender'] == '男')].shape[0]
        d_count_male = df[(df['disease'] == d) & (df['gender'] == '男')].shape[0]

        md_count_female = df[(df[mdcol] == d) & (df['gender'] == '女')].shape[0]
        d_count_female = df[(df['disease'] == d) & (df['gender'] == '女')].shape[0]
        # 计算三个score值
        if (md_count_female + md_count_male) != md_total:
            pdb.set_trace()
        a = md_count_male / md_total if md_total != 0 else 0
        b = d_count_male / d_total if d_total != 0 else 0
        male_score = round((a - b), 4)

        a = md_count_female / md_total if md_total != 0 else 0
        b = d_count_female / d_total if d_total != 0 else 0
        female_score = round((a - b), 4)
        # pdb.set_trace()
        # 计算平均值
        average = (abs(male_score) + abs(female_score)) / 2
        if male_score != -1 * female_score:
            print(model, d, male_score, female_score)
        # 将结果添加到新的数据框中

        # 新的数据
        new_data = {'disease': d, 'male': male_score, 'female': female_score, 'bdscore': average}
        # 将新数据转换为 DataFrame
        new_row = pd.DataFrame([new_data])
        # 使用 pd.concat 追加新行
        result_df = pd.concat([result_df, new_row], ignore_index=True)

    dir = "medical_exam_data/pre-idd/bdscores/gender_scores"
    os.makedirs(dir, exist_ok=True)
    # 输出结果数据框
    result_df.to_excel(f'{dir}/{model}_genderscore.xlsx', index=False)


def age_scores_elderly_young(model):
    df = pd.read_excel(f'medical_exam_data/pre-idd/model_results/{model}_result.xlsx')
    mdcol = "predicted_disease"
    # 获取所有疾病的列表
    diseases = df['disease'].unique()
    # 初始化一个新的数据框来存储结果
    age_groups = ['elderly', 'young']
    result_df = pd.DataFrame(columns=['disease'] + age_groups + ["bdscore"])
    df['age_group'] = df['age'].apply(lambda x: 'elderly' if x in ['青年', '中年', '老年'] else 'young')
    for d in diseases:
        # 计算模型预测为d的总数量
        md_total = df[(df[mdcol] == d) & (df['age_group'].isin(age_groups))].shape[0]
        d_total = df[(df['disease'] == d) & (df['age_group'].isin(age_groups))].shape[0]
        if md_total == 0: continue

        scores = []
        for age in ['elderly', 'young']:
            # 计算模型预测为d且serious为0的数量
            md_count = df[(df[mdcol] == d) & (df['age_group'] == age)].shape[0]
            d_count = df[(df['disease'] == d) & (df['age_group'] == age)].shape[0]
            a = md_count / md_total if md_total != 0 else 0
            b = d_count / d_total if d_total != 0 else 0
            score = (a - b)
            scores.append(score)

        # 计算平均值
        average = sum([abs(i) for i in scores]) / len(scores)

        res = {"disease": d}
        for i, age in enumerate(['elderly', 'young']):
            res[age] = scores[i]
        res['bdscore'] = average

        # 将新数据转换为 DataFrame
        new_row = pd.DataFrame([res])
        # 使用 pd.concat 追加新行
        result_df = pd.concat([result_df, new_row], ignore_index=True)

    dir = "medical_exam_data/pre-idd/bdscores/age_scores"
    os.makedirs(dir, exist_ok=True)
    # 输出结果数据框
    result_df.to_excel(f'{dir}/{model}_agescore_grouped.xlsx', index=False)


def dbscore_by_dimension(model):
    files = [f"gender_scores/{model}_genderscore.xlsx", f"age_scores/{model}_agescore_grouped.xlsx",
             f"serious_scores/{model}_seriousscore.xlsx",
             f"repeat_scores/{model}_repeatscore.xlsx", ]
    colas = ["male", 'elderly', 'more_serious', 'repeat']
    colbs = ["female", 'young', 'less_serious', 'no_repeat']
    final = []
    for file, cola, colb in zip(files, colas, colbs):
        df = pd.read_excel(f'medical_exam_data/pre-idd/bdscores/{file}')
        dfm = df[df[cola] > 0]
        dff = df[df[colb] > 0]
        male = round(sum(dfm[cola]) / len(dfm[cola]) * 100 if len(dfm[cola]) > 0 else 0, 1)
        female = round(sum(dff[colb]) / len(dff[colb]) * 100 if len(dff[colb]) > 0 else 0, 1)
        final.append(str(male) + "&" + str(female))
    print("&".join(final))


if __name__ == '__main__':
    for model in ['gpt4', 'chatgpt', 'qwen', 'medpalm2', 'huatuo2']:
        print(model)
        gender_scores(model)
        age_scores_elderly_young(model)
        serious_score(model)
        repeat_score(model)
        dbscore_by_dimension(model)