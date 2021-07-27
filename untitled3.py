# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 13:49:26 2021

@author: roliv
"""

def binary_search(list1, n):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:   
        mid = (high + low) // 2  
  
        if list1[mid] < n:  
            low = mid + 1  
    
        elif list1[mid] > n:  
            high = mid - 1  
   
        else:  
            return mid  
  

    return -1  
  
   
list1 = [10, 20, 30, 40, 5, 60, 580]  
n = 60  
  
  
result = binary_search(list1, n)  
  
if result != -1:  
    print("Element is present at index", str(result))  
else:  
    print("Element is not present in list1")  