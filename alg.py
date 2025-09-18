# önce bunu denedim ama index bulma kısmı yanlış buldu. bulduğu ilk indexi döndürdüğü için 
# def is_repeating(arr, k):                      #arr = [1,2,3,1,5,6]
#      for number in arr:                        #number = 1 ilk turda 
#           for i in range(1,k+1):               #i = 3
#                 if arr.index(number)+i < len(arr):
#                                                     #number = 0.eleman   sırayla 1, 2, 3, 4
#                     if arr[arr.index(number)+i] == number:
#                      return True 
#      return False

               
def is_repeating(arr, k):                      
    for idx, number in enumerate(arr):        # enumerate ile indeks + eleman
        for i in range(1, k+1):               
            if idx + i < len(arr):            
                if arr[idx + i] == number:    # arr.index(number) yerine idx kullandık
                    return True 
    return False

                       
          
     
     


liste =[1, 2, 1]
print(is_repeating(liste, 1))  #f


     
     
