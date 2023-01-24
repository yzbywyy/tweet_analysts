import os
from copy import deepcopy

import pandas as pd

from tweet2analysts.date_change import date_change
from tweet2analysts.emo_paddle import anal
from tweet2analysts.int2str import int2str
from tweet2analysts.move import move
from tweet2analysts.str2int import str2int
from tweet2analysts.tweet import sctweet

if __name__ == '__main__':
    print(
        "欢迎使用本程序！本程序包基于Scweet、paddle及其他开源软件包开发，请勿用于非法用途！请在位于中国大陆境外的服务器或者其他设备运行此程序！")
    print("由于Scweet的设计问题，如果您使用代理，结果可能会大幅度减少，该问题暂时没有实用的解决方案。")
    print("请输入您的搜索模式，输入0则为关键词查找模式，输入1则为tag查找模式")
    search_mode = int(input())

    target_list = []
    hash_tag = "null"
    if search_mode == 0:
        print("请输入您所需要抓取的推文的关键词，输入完一个后回车，不输入直接回车则进入下一步：")
        while True:
            temp_tar = input()
            if temp_tar != "":
                target_list.append(temp_tar)
            else:
                break
    else:
        print("请输入您所需要抓取的推文的tag，只能输入一个，输完后回车：")
        hash_tag = input()

    print("请依次输入查询时间上限：")

    print("请输入查询开始的年份（大于2005的四位数字）：")
    year = input()

    print("请输入查询开始的月份（介于1-12之间的两位数字，例如01、04、10）：")
    month = input()

    print("请输入查询开始的日期（介于1-31之间的两位数字，例如01、04、10）：")
    day = input()

    lis_temp = [year, month, day]
    begin_date = [int(year), int(month), int(day)]
    begin_str = '-'.join(lis_temp)

    print("请依次输入查询时间下限：")

    print("请输入查询结束的年份（大于等于开始时间年份的四位数字）：")
    year = input()

    print("请输入查询结束的月份（介于1-12之间的两位数字，例如01、04、10）：")
    month = input()

    print("请输入查询结束的日期（介于1-31之间的两位数字，例如01、04、10）：")
    day = input()

    lis_temp = [year, month, day]
    end_date = [int(year), int(month), int(day)]
    end_str = '-'.join(lis_temp)

    print("请指定您需要的查找模式，如果需要按时间查找推文请输入0，按热度查找请输入1：")
    mode = int(input())
    if mode == 0:
        mode_str = "Latest"
    else:
        mode_str = "Top"

    print("请输入您需要的数据分段方式：")
    print("如果您需要每年生成一个文件，请输入0；每月生成一个文件输入1，每日生成一个文件输入2，不分段请输入3：")
    operation_mode = int(input())

    print(
        "是否需要为了大幅度降低搜索时间而减少搜索的次数？注意，此功能为测试功能，可能存在bug，请谨慎使用，需要最快请输入1，一般提速请输入2，否则请输入0：")
    test = int(input())
    if test == 1:
        if operation_mode == 0:
            interval_day = 365
        elif operation_mode == 1:
            interval_day = 30
        else:
            interval_day = 1
    elif test == 0:
        interval_day = 1
    else:
        interval_day = 7
    output_lis = []

    if target_list:
        name = deepcopy(target_list)
    else:
        name = [hash_tag]
    name.append(begin_str)
    name.append(end_str)
    save_dir_name = "-".join(name)

    save_dir_name = "Outputs\\" + save_dir_name

    if operation_mode == 3:
        output_lis = sctweet(interval_day, search_mode, target_list, hash_tag, mode_str,
                             begin_str, end_str, save_dir_name)
    else:
        new_begin_date = []
        temp_list = begin_str.split("-")
        for i in temp_list:
            j = int(i)
            new_begin_date.append(j)
        new_end_date = deepcopy(new_begin_date)
        new_end_date[operation_mode] += 1

        while True:
            if int(new_begin_date[0]) > int(end_date[0]):
                break
            elif int(new_begin_date[0]) == int(end_date[0]) and int(new_begin_date[1]) > int(end_date[1]):
                break
            elif int(new_begin_date[0]) == int(end_date[0]) and int(new_begin_date[1]) == int(end_date[1]) and int(
                    new_begin_date[2]) >= int(end_date[2]):
                break
            else:
                begin_date = deepcopy(new_begin_date)

                begin_str = int2str(new_begin_date)
                end_str = int2str(new_end_date)

                output_lis = sctweet(interval_day, search_mode, target_list, hash_tag, mode_str,
                                     begin_str, end_str, save_dir_name)
                lis_new_date = date_change(
                    new_begin_date, new_end_date, operation_mode)
                new_begin_date = str2int(lis_new_date[0])
                new_end_date = str2int(lis_new_date[1])

    df_outputs = pd.DataFrame()
    for filenames in os.walk(save_dir_name):
        for filename in filenames:
            if isinstance(filename, list):
                for h in filename:
                    path_name = [save_dir_name, h]
                    path = "\\".join(path_name)
                    df_temp = anal(path, save_dir_name)
                    if isinstance(df_temp, int):
                        pass
                    else:
                        df_outputs = pd.concat([df_outputs, df_temp], axis=1)

    df_outputs.to_csv("Outputs.csv")
    df_outputs.to_excel("Outputs.xlsx")
    move("Outputs.csv", save_dir_name)
    move("Outputs.xlsx", save_dir_name)

    print("All assignments have been done!")
