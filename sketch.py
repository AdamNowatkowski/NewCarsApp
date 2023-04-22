A = [1,2,5,9]
B = [1,3,5,11]

while len(B) > 0:
    for num1 in B:
        for index, num2 in enumerate(A):
            if index + 1 == len(A):
                if num1 >= num2:
                    A.insert(index, num1)
                    B.remove(num1)
                break
            else:
                if num1 >= num2 and num1 <= A[index + 1]:
                    A.insert(index+1, num1)
                    B.remove(num1)
                    break
print(A)