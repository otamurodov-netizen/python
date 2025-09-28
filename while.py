# Mavzu: while

# juft va toq sonlarni aniqlovchi dastur
# sonlar = []
# i = 1
# while i <= 10:
#     son = input(f"{i} - sonni kiriting\n>>")
#     sonlar.append(son)
#     i += 1
# i = 0
# while i < len(sonlar):
#     if int(sonlar[i]) % 2 == 0:
#         print(sonlar[i], " - bu juft son")
#     else:
#         print(sonlar[i], " - bu toq son")
#     i += 1



# from 1 to 10 numbers
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# from 1 to 100 numbers
# i = 1
# while i <= 100:
#     print(i)
#     i += 1



# faktorialni topish
# son = int(input("son kiriting\n>>"))
# i = 1
# faktorial = 1
# while i <= son:
#     faktorial *= i
#     i += 1
# print("kiritilgan sonning faktoriali:", faktorial)




def bubble(nums):
    nums = [8,5,2,4,3]
    n = len(nums)
    for f in range(1,4):
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    print(nums)


print(bubble(nums=[8,5,2,4,3]))

