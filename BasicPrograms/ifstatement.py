def max_number(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        output=n1
        return output
    elif n2>=n1 and n2>=n1:
        output=n2
        return output
    else:
        output=n3
        return output


output=max_number(608,850,504)
print("Maximum number is:",output)