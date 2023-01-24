import os.path

import matplotlib.pyplot as plt
import numpy as np
import paddlehub as hub
import pandas as pd


def is_empty(df):
    if df.empty:
        return True
    else:
        return False


def anal(filepath, save_dir_name):
    senta = hub.Module(name="senta_lstm")

    data = pd.read_csv(filepath)

    if is_empty(data):
        return 0

    filename = os.path.basename(filepath)

    test_text = list(data['Embedded_text'])
    df = pd.DataFrame(senta.sentiment_classify(data={"text": test_text}))

    df.to_excel("%s\\%s.xlsx" % (save_dir_name, filename))
    df.to_csv("%s\\%s.csv" % (save_dir_name, filename))

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    bins = np.arange(0, 1.1, 0.01)

    plt.hist(df['positive_probs'], bins, color='#4F94CD', alpha=0.9)
    plt.xlim(0, 1)
    plt.xlabel('情感分')
    plt.ylabel('数量')
    plt.title('情感分直方图')
    plt.savefig("%s\\%s.png" % (save_dir_name, filename))

    df.rename(columns={'positive_probs': filename}, inplace=True)
    df1 = df[filename].describe()

    return df1


if __name__ == '__main__':
    print("Hello, World!")
