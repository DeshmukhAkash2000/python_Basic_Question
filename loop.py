####################### armstrong number ########################################################

# a=int(input("enter number:-- "))
# sum=0
# t=a
# s=0
# while t>0:
#     t=t//10
#     s+=1
# t=a
# while t>0:
#     c=t%10
#     sum+=c**s
#     t//=10
# if sum==a:
#     print("yes",a,"is a armstrong number")
# else:
#     print("no",a,"is not a armstrong number")



############################# progress tracking 22-09-2021 fabonacci series#########################
# a=int(input("enter number :-- "))
# x=0
# y=1
# z=0
# while z<=a:
#     print(z)
#     x=y
#     y=z
#     z=x+y 

################### pattern printing 25-09 #############################################
# for i in range(1,6):            # *
#     for j in range(1,i+1):      # **
#         print("*",end="")       # ***
#     print("\n")                 # ****
                                  # *****
        ### amulya academy
# num=int(input("enter your number of rows :-- "))   #same output
# for i in range(1,num+1):
#     print("*"*i)
##################################################################################
                              


# for i in range(5,0,-1):        # *****
#     for j in range(1,i+1):     # ****
#         print("*",end="")      # ***
#     print("\n")                # **
#                                # *


##################################################################################

# for i in range(1,6):             #     *    
#     for j in range(1,6-i):       #    **
#         print(" ",end="")        #   ***
#     for k in range(1,i+1):       #  ****
#         print("*",end="")        # *****
#     print("\n")

# num=int(input("enter your number of rows :-- "))
# for i in range(1,num+1):                         ## same output
#     print("  "*(num-i)+"* "*i)

#########################################################################################

# num=int(input("enter your number of rows :-- "))
# for i in range(1,num+1):                         ## same output
#     print(" "*(num-i)+"*"*i)

########################################################################################


# for i in range(5,0,-1):            # *****
#     for j in range(1,6-i):         #  ****
#         print(" ",end="")          #   ***
#     for k in range(1,i+1):         #    **
#         print("*",end="")          #     *
#     print("\n")
#############################################################################################
# for i in range(1,6):                 #     *
#     for j in range(1,6-i):           #    ***
#         print(" ",end="")            #   *****
#     for k in range(1,(i*2-1)+1):     #  *******
#         print("*",end="")            # *********  
#     print("\n")


# num=int(input("enter your number of rows :-- "))
# for i in range(1,num+1):                         ## same output
#     print(" "*(num-i)+"* "*i)

#############################################################################################



# a=9                                  # *********
# for i in range(1,6):                 #  *******
#     print(" "*i+"*"*a)               #   *****
#     a-=2                             #    ***
                                       #    
                                       

                                       
# num=int(input("enter your number of rows :-- "))
# for i in range(num,0,-1):                         ## same output
#     print(" "*(num-i)+"* "*i)


################# amulya's academy pattern printing ##########################

# num=int(input("enter your number of rows :-- "))  # * * * * *
# for i in range(num):                              # * * * * *
#     for j in range(num):                          # * * * * *                           
#         print("*",end=" ")                        # * * * * *
#     print()                                       # * * * * *
                                                         
                                                     
# num=int(input("enter your number of rows :-- "))        #same output
# for i in range(num):
#     print("*"*num)
##########################################################################################

# num=int(input("enter your number of rows :-- "))
# for i in range(1,num+1):                        
#     print(" "*(num-i)+"* "*i)
# for i in range(num-1,0,-1):                         ## diamond shape
#     print(" "*(num-i)+"* "*i)
  
###########################################################################
# num=int(input("enter the number of row :-- "))  # *
# for i in range(1,num+1):                        # * *
#     print("*  "*i)                              # * * *
# for i in range(num-1,0,-1):                     # * * * *
#     print("*  "*i)                              # * * * * *
                                                  # * * * *
                                                  # * * *
                                                  # * *
                                                  # *
########################################################################################
# num=int(input("enter the number of row :-- "))    
# for i in range(1,num+1):                                             
#     print("  "*(num-i)+"* "*i)              ## revrse arrow         
# for i in range(num-1,0,-1):                     
#     print("  "*(num-i)+"* "*i)
###################### A pattern #############################################################

# for row in range(6):
#     for col in range(5):
#         if row in (0,3) and col in (0,1,2,3,4):
#             print("*",end=" ")
#         elif row in (0,1,2,3,4,5) and col in (0,4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#################################### snake pattern ##############################################
# a=int(input("enter number :- "))
# b=a
# for i in range(1,b+1):
#         print(i,end=" ")
#         if i==5:
#             print("\n")
# print()
           
####################################################################################

# a=int(input("enter number :-- "))
# b=1
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(b,end=" ")
#         b+=1
#     print() 



############################ squere pattern ################################
# a=int(input("enter your number :"))
# for row in range(a):
#     for col in range(a):
#         if row in (0,a-1) and (a)>col>=0:
#             print("*",end=" ")
#         elif (a)>row>=0 and col in(0,a-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
##################################################################################   
#########################################################################################
# for row in range(7):
#     for col in range(5):

#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print() 






