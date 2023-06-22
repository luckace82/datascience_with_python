# q={"apple":"ca","ball":"dog"}
# print (q)
# for i in q:
#     if i =="apple":
#        print (i)




# for i in range(1,221):
#     if i%5==0:
#         print("fizzbuz",end="")
#     if i%3==0:
#         print("fizz",end="")
#     else:
#         print( i,end="")       






n=int(input("enter anyn nmber"))

x=0
def cal(n):
    sum=0
    for i in range(1,n+1):
       
       sum=sum+i*i*i
    print(sum)
cal(n)