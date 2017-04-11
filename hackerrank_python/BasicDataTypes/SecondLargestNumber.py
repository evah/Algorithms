#http://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    new = [x for x in arr if x < max(arr)]
    print(max(new))
