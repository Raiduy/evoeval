def strange_sort_list(lst, lst2):
    merged_list = list(set(lst + lst2))
    part1 = [x for x in lst if x % 2 != 0] + [x for x in lst2 if x % 2 == 0]
    part1 = list(set(part1))
    part2 = [x for x in merged_list if x not in part1]

    def strange_sort(nums):
        result = []
        while nums:
            if nums:
                result.append(min(nums))
                nums.remove(min(nums))
            if nums:
                result.append(max(nums))
                nums.remove(max(nums))
        return result
    sorted_part1 = strange_sort(part1)
    sorted_part2 = strange_sort(part2)
    return sorted_part1 + sorted_part2