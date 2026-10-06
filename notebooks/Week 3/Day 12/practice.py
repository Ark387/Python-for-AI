

# # # def num(user):
# # #         while True:
# # #             try:
# # #                 if 0>=user<=120:
# # #                     pass
            
# # #             except ValueError:
# # #                 print()
                 
                 
# # # try:
# # #     user = int(input("Enter a number: "))
# # #     num(user)
# # # except ValueError:
# # #     print("Enter a valid Number")
 
# import numpy as np

# # a = np.arange(12)
# # print(a)
# # print(a.reshape(3, 4)) 
# # print(a.reshape(4, -1))  

# marks = np.array([80, 72, 91])
# print(marks.dtype)
# # WRONG ON PURPOSE. We put 85.7 in a whole-number array:

# marks[0] = 85.7
# print(marks)
# # We wrote 85.7. We got 85. The .7 was lost.

# # Mixing text and numbers:

# mixed = np.array([1, 2, "3"])
# print(mixed, mixed.dtype)
# # Fix: use dtype=float.

# marks = np.array([80, 72, 91], dtype=float)
# marks[0] = 85.7
# print(marks)



marks=["91","100","82"]
print(max(marks))
