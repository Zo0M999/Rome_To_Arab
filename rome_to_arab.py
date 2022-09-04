import json

dct = json.load(open('rome_dict.json'))


def rome_to_arab(nums):
    nums = list(nums.upper())
    lst = []
    for i in nums:
        for j in dct.keys():
            if i == j:
                lst.append(dct[j])

    lst_sort = sorted(lst)
    if len(lst) == 1:
        return lst[0]
    else:
        if lst == lst_sort:
            if sum(lst)/len(lst) == lst[1]:
                return sum(lst)
            else:
                return lst_sort[-1] - sum(lst_sort[0:-1])
        else:
            return sum(lst_sort)


rome_to_arab = rome_to_arab(input('Enter rome number: '))
print(rome_to_arab)
