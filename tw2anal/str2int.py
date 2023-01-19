def str2int(st):
    new_begin_date = []
    temp_list = st.split("-")
    for i in temp_list:
        j = int(i)
        new_begin_date.append(j)
    return new_begin_date
