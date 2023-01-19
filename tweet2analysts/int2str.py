def int2str(new_begin_date):
    lis_temp = [str(new_begin_date[0])]
    for i in new_begin_date:
        if i < 10:
            temp_lis = ["0", str(i)]
            str_temp = ''.join(temp_lis)
            lis_temp.append(str_temp)
        elif i > 2000:
            pass
        else:
            lis_temp.append(str(i))
    begin_str = '-'.join(lis_temp)
    return begin_str
