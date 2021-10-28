def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    boolean = False

    for number in nums:
        if number == 7:
            boolean = True
            break

    return(boolean, nums)


print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))
