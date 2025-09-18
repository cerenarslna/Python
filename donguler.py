# listeler ile for döngüsü
# liste = [1,2,3,4,5,6]
# for rakam in liste:
#     print(rakam)


# isim = "Ceren"
# for harf in isim:
#     print(harf)


# for i in range(0,10):
#     print(i) 
# #range:belirlediğim iki sayı arasındaki değerleri veriyor --> 0 dan 9 a kadar İlk sınırı dahil eder ancak ikinci sınırı dahil etmez 



# for i in range (1,15,2):
#     print(i)
#     #ilk parametre: baslangıc degeri
#     ikinci parametre : bitis degeri (Kendisi dahil değil)
#     ücüncü parametre : aralık (örekteki 2 ser 2 ser gidiyor)




# 2 üzeri 10 hesaplama
# sonuc =1 
# for i in range (0,10):
#     sonuc *= 2
# print(sonuc)


# liste1 = ["a","b","c"]
# liste2 = [1,2,3]

# for harf in liste1:
#     for rakam in liste2:
#         print(harf,rakam)



#     3 haric hepsini yazdır
# liste = [1,2,3,4,5,6,7]
# for i in liste:
#     if i == 3:
#         continue
#     print(i)

# continue burda dur ve döngüyü basa al demek Atla demek 

# liste = [1,2,3,4,5,6,7]
# for i in liste:
#      if i == 3:
#          break
#      print(i)

#      break döngüyü sonlandır demek 


# 100 ün sadece 3 e böünen sayılarını yazdırma 

# liste = range(100)
# for i in liste:
#     if i % 3 != 0 :
#         continue
#     print(i)


# liste = range(50)
# for i in liste:
#     if i % 2 != 0 :
#         continue
#     if i == 46 :
#         break
#     print(i)



# WHİLE DÖNGÜSÜ
# x = 2
# while x < 10:
#     print(x)
#     x += 1
# print("x = " ,x)



# x = 2
# y = 3
# while x * y < 1000:
#     print(x,y)
#     x += 2
#     y += 2



#     while true ile sonsuz döngü olusturabilirisn
# i = 1
# while True:
#     i += 1
#     print(i) 
#     if i == 10000:
#         break



# 1000 e kadar olan tek sayıları yazdırma 
# i = 1 
# while True:
#     if i % 2== 0:
#         i += 1
#         continue
#     print(i)
#     i += 1
#     if i == 1000:
#         break