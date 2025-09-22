# 8 - dars
# mavzu: while sikli
# 9/22/2025

# **********misol1**************
# ism = input("ismingizni kiritng\n>>")
# savol = f"Salom, {ism.title()}. Yoshingiz nechchida ?\n>>"
# yosh = int(input(savol))
# boyi = float(input("bo'yingiz necha metr ?\n>>"))

# print(f"{ism.title()} ning ma'lumotlari \n"
#       f"Yoshi: {yosh}\n",
#       f"Boyi: {boyi}")

#*****************misol2****************
# ism = input("ismingizni kiritng\n>>")
# savol = f"Salom, {ism.title()}. tugilgan yilingizni kiriting ?\n>>"
# yosh = int(input(savol))
# boyi = float(input("bo'yingiz necha metr ?\n>>"))
# yil = 2025 - yosh

# print(f"{ism.title()} ning ma'lumotlari \n"
#       f"Yoshi: {yil}\n",
#       f"Boyi: {boyi}")



#*************while***************
# son = 1
# while son <= 5:
#     print(son)
#     son = son + 1


#*****************misol3********************

# print("kiritilgan sonlarning kvadratini qaytaruvchi dastur:")
# savol = "istalgan sonni kiriting"
# savol += "dasturni yakunlash uchun 'stop' deb yozing\n>>"
# qiymat = ' '
# while qiymat != 'stop':
#     qiymat = input(savol)
#     if qiymat != 'stop':
#         print(float(qiymat)**2)
# print("dastur tugadi.")


#************************misol4******************
# print("kiritilgan sonlarning kvadratini qaytaruvchi dastur:")
# savol = "istalgan sonni kiriting"
# savol += "dasturni yakunlash uchun 'stop' deb yozing\n>>"
# qiymat = True
# while qiymat:
#     qiymat = input(savol)
#     if qiymat == 'stop':
#         qiymat = False
#     else:
#         print(float(qiymat)**2)
# print("dastur tugadi.")

#***************************           ****************
# print("kiritilgan sonlarning kvadratini qaytaruvchi dastur:")
# savol = "istalgan sonni kiriting"
# savol += "dasturni yakunlash uchun 'stop' deb yozing\n>>"
# while True:
#     qiymat = input(savol)
#     if qiymat == 'stop':
#         break
#     else:
#         print(float(qiymat)**2)
# print("dastur tugadi.")


#***************************break in for****************
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng.")


# **********************continue*******************
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng.")


# **********************continue in while*******************

# son = 0
# while son <= 10:
#     son +=1
#     if son == 5:
#         continue
#     print(son)

# ****************royhatlar *****************
print("siz yaxshi ko'rgan dasturchilar royhati:")
ismlar = []
n = 1 # sanash uchun
while True:
    savol = f"{n} - dasturchini ismini kiriting"
    ism = input(savol)
    ismlar.append(ism)
    takror = input("yana ism kqoshasizmi ? (ha) (yoq) \n >>>")
    n+= 1
    if takror != 'ha':
        break
print(ismlar)