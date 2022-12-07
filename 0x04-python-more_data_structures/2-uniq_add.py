def uniq_add(my_list=[]):
    un_set = set(my_list)
    my_list = list(un_set)
    sum_all = 0
    for i in range(len(my_list)):
        sum_all += my_list[i]
    return sum_all
