immutable_var = 5, 7, 15, False, 'Forest'
tuple_ = immutable_var
print(tuple_)
#tuple_[0] = 23
try:
    tuple_[0] = 23
except:
    print("нельзя изменять элементы в кортеже, тк кортеж хранит ссылку на список, а не сам список")
mutable_list = ['5', '8', '32', True, 'Bomba']
print(mutable_list)
mutable_list [2] = 'Bomba'
print(mutable_list)
mutable_list [-1] = 'Greece'
print(mutable_list)
mutable_list [0] = 'Love'
print(mutable_list)


