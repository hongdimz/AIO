#câu hỏi 1
import math 
def calc_f1_score(tp,fp,fn):
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    return 2*(precision*recall)/(precision+recall)

assert round(calc_f1_score(tp=2,fp=3,fn=5),2) == 0.33
print(round(calc_f1_score(tp=2,fp=4,fn=5),2))

#câu hỏi 2 
def is_number(n):
    try:
        float(n) 
    except ValueError:
        return False 
    return True 
assert is_number (3) == 1.0
assert is_number ('-2a') == 0.0
print ( is_number (1) )
print ( is_number ('n') )

#câu hỏi 4
def calc_sig(x):
    return 1/(1+math.exp(-x))

assert round(calc_sig(3),2)==0.95
print ( round ( calc_sig (2) , 2) )

#câu hỏi 5 
def calc_elu(x):
    if x <= 0: return 0.01*(math.exp(x)-1)
    elif x > 0: return x 
assert round ( calc_elu (1) ) == 1
print ( round ( calc_elu ( -1) , 2) )

#câu hỏi 6
def calc_activation_func(x,act_name):
    if act_name == 'elu': return calc_elu(x)
    elif act_name == 'sigmoid': return calc_sig(x)
    elif act_name == 'relu':
        if x <=0: return 0 
        elif x >0: return x 
    else: return('sai tên activation function')

assert calc_activation_func ( x = 1 , act_name ='relu') == 1
print ( round ( calc_activation_func (x = 3 , act_name ='sigmoid') , 2) )

#câu hỏi 7
def calc_ae(y,y_hat):
    return abs(y-y_hat)

y = 1
y_hat = 6
assert calc_ae (y , y_hat ) ==5
y = 2
y_hat = 9
print ( calc_ae (y , y_hat ) )

#câu hỏi 8
def calc_se(y,y_hat):
    return abs(y-y_hat)**2

y=4
y_hat=2
assert calc_se (y , y_hat ) == 4
print ( calc_se (2 , 1) )

#câu hỏi 9 
def giai_thua(n):
    a = 1
    for i in range (1,n+1):
        a = a*i
    return a 

def approx_cos(x,n):
    sum = 0
    for i in range(n+1):
        sign = (-1)**i 
        term = sign*(x**(2*i)/giai_thua(2*i))
        sum = sum + term
    return sum 
assert round ( approx_cos ( x =1 , n =10) , 2) ==0.54
print ( round ( approx_cos ( x =3.14 , n =10) , 2) )

#câu hỏi 10
def approx_sin (x , n ):
    sum = 0
    for i in range(n+1):
        sign = (-1)**i 
        term = sign*(x**(2*i+1)/giai_thua(2*i+1))
        sum = sum + term
    return sum 
assert round ( approx_sin ( x =1 , n =10) , 4) ==0.8415
print ( round ( approx_sin ( x =3.14 , n =10) , 4) )

#câu hỏi 11
def approx_sinh (x , n ) :
    sum = 0
    for i in range(n+1):
        term = (x**(2*i+1)/giai_thua(2*i+1))
        sum = sum + term
    return sum 
assert round ( approx_sinh ( x =1 , n =10) , 2) ==1.18
print ( round ( approx_sinh ( x =3.14 , n =10) , 2) )

#câu hỏi 12
def approx_cosh (x , n ) :
    sum = 0
    for i in range(n+1):
        term = (x**(2*i)/giai_thua(2*i))
        sum = sum + term
    return sum 
assert round ( approx_cosh ( x =1 , n =10) , 2) ==1.54
print ( round ( approx_cosh ( x =3.14 , n =10) , 2) )