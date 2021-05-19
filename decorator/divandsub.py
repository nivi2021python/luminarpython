def dec_divsub(func):
    def wrapper(no1,no2):
        if no1<no2:
            (no1,no2)=(no2,no1)
        return func(no1,no2)
    return wrapper

@dec_divsub
def div(no1,no2):
    return no1/no2
@dec_divsub
def sub(no1,no2):
    return no1-no2

print(div(2,6))
print(sub(6,11))