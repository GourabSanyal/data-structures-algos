# To solve it with O(n) we have to not take any values which is negative or pt thgem to zero
# If we do take negative values it will take O(n)
# https://www.youtube.com/watch?v=mXb-NPo0ldI&ab_channel=nETSETOS/


def max_sum_array(arr):
    size = len(arr)
    curr_sum = 0
    max_so_far = arr[0]
    st = 0
    end = 0
    poi = 0

    for i in range(0, size):
        curr_sum = curr_sum + arr[i]
        if max_so_far < curr_sum:
            max_so_far = curr_sum
            st = poi
            end = i
        if curr_sum < 0:
            curr_sum = 0
            poi = i

    print("max sub array is ", max_so_far)
    print("start index is ", st)
    print("end index is ", end)


arr = [1, -2, 3, -4, 5, 78, -9]
max_sum_array(arr)
