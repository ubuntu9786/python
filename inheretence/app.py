from cook import Chef
from italian import italian

mychef = Chef()
mychef.chicken()

italian_chef = italian()
if italian_chef.salad(): 
    print('the italian has made the salad')
else:
    print('no salada for you')
print(italian.exp)
