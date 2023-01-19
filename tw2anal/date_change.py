from time_convert import month_add


def date_change(start_date_lis, end_date_lis, pos_int):
    global lis_temp, start_date_str, end_date_str, op
    op = 0
    lis = [start_date_lis, end_date_lis]
    for j in lis:
        j[pos_int] += 1
        j = month_add(j)
        lis_temp = [str(j[0])]
        for i in j:
            if i < 10:
                temp_lis = ["0", str(i)]
                str_temp = ''.join(temp_lis)
                lis_temp.append(str_temp)
            elif i > 2000:
                pass
            else:
                lis_temp.append(str(i))
        if op == 0:
            start_date_str = '-'.join(lis_temp)
            op = 1
        else:
            end_date_str = '-'.join(lis_temp)
    new_date = [start_date_str, end_date_str]
    return new_date


if __name__ == '__main__':
    print("Hello, World!")
