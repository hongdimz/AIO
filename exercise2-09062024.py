#câu hỏi tự luận
#câu 1
def max_kernel(num_list,k):
    if k > len(num_list): return('invalid k')
    else:
        result = []
        for i in range(0,len(num_list)-k+1):
            slide_window=num_list[i:i+k]
            max_number = slide_window[0]
            for j in slide_window:
                if j > max_number: max_number = j
            result.append(max_number)
        return result 

num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3
print(max_kernel(num_list,3))

#câu 2
def character_count(string):
    character_statistic = {}
    for i in string:
        if i in character_statistic: character_statistic[i]=character_statistic[i]+1
        else: character_statistic[i] = 1
    return character_statistic
print(character_count('Happiness'))
    
#câu 3
filename = r"C:\Users\Admin\Documents\[Diem learning]\AIO Official\AIO\P1_data.txt"

def count_word(file):
    counter = {}
    #open file
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    #word count
    for word in contents.lower().split():
        if word in counter: counter[word] = counter[word]+1
        else: counter[word] = 1
    return counter
print(count_word(filename))

#câu 4
def levenshtein_distance(source,target):
    m = len(source)
    n = len(target)
    if m == 0 or n == 0: return max(m,n)
    else:
        matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
        #hàng và cột đầu tiên
        for i in range(n+1): matrix[0][i] = i
        for j in range(m+1): matrix[j][0] = j 
        #điền các cột còn lại
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i][0]==matrix[0][j]: a = 0
                else: a = 1
                #tính matrix[i][j]
                del_cost = matrix[i-1][j]+1  
                ins_cost = matrix[i][j-1]+1
                sub_cost = matrix[i-1][j-1]+a
                matrix[i][j] = min(del_cost,ins_cost,sub_cost)
        return matrix[m][n]
    
print(levenshtein_distance('yu','you'))

#TRẮC NGHIỆM
#câu 1
assert max_kernel ([3 , 4 , 5 , 1 , -44] , 3) == [5 , 5 , 5]
num_list = [3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1]
k = 3 
print ( max_kernel ( num_list , k ) )

#câu 2
assert character_count ("Baby") == {'B': 1 , 'a': 1 , 'b': 1 , 'y': 1}
print ( character_count ('smiles') )

#câu 3
result = count_word ( filename )
assert result['who'] == 3
print ( result ['man'])

#câu 4
print(levenshtein_distance('hola', 'hello'))

#câu 5
def check_the_number(N):
    list_of_number = []
    result = ""
    for i in range(1,5):
        list_of_number.append(i)
    if N in list_of_number:
        results = "True"
    if N not in list_of_number:
        results = "False"
    return results 
N = 7
assert check_the_number ( N ) == "False"
N = 2
print(check_the_number(N))

#câu 6 
def my_function(data,max,min):
    result = []
    for i in data:
        if i < min: result.append(min)
        elif i > max: result.append(max)
        else: result.append(i)
    return result 
my_list = [5 , 2 , 5 , 0 , 1]
max = 1 
min = 0 
assert my_function (max = max , min = min , data = my_list ) == [1 , 1 , 1 , 0 , 1]
my_list = [10 , 2 , 5 , 0 , 1]
max = 2 
min = 1 
print ( my_function (max = max , min = min , data = my_list ) )

#câu 7
def my_function7(x,y):
    x.extend(y)
    return x
list_num1 = ['a', 2 , 5]
list_num2 = [1 , 1]
list_num3 = [0 , 0]

assert my_function7 ( list_num1 , my_function7 ( list_num2 , list_num3 ) ) == ['a', 2 , 5 , 1 , 1 , 0 , 0]
list_num1 = [1 , 2]
list_num2 = [3 , 4]
list_num3 = [0 , 0]

print ( my_function7 ( list_num1 , my_function7 ( list_num2 , list_num3 ) ) )

#câu 8
def my_function8(n):
    min = 999999999
    for i in n:
        if i < min: min = i 
    return min
my_list = [1 , 22 , 93 , -100]
assert my_function8 ( my_list ) == -100
my_list = [1 , 2 , 3 , -1]
print ( my_function8 ( my_list ) )

#câu 9
def my_function9(n):
    max = -999999999
    for i in n:
        if i > max: max = i 
    return max
my_list = [1001 , 9 , 100 , 0]
assert my_function9 ( my_list ) == 1001
my_list = [1 , 9 , 9 , 0]
print ( my_function9 ( my_list ) )

#câu 10
def my_function10( integers , number = 1):
    return any(
        i == number for i in integers
    )

my_list = [1 , 3 , 9 , 4]
assert my_function10 ( my_list , -1) == False
my_list = [1 , 2 , 3 , 4]
print ( my_function10 ( my_list , 2) )

# câu 11 
def my_function11(list_nums = [0,1,2]):
    var = 0
    for i in list_nums:
        var +=i 
    return var/len(list_nums)
assert my_function11 ([4 , 6 , 8]) == 6
print ( my_function11 () )

# câu 12
def my_function12(data):
    var = []
    for i in data:
        if i % 3 == 0: var.append(i)
    return var 
assert my_function12 ([3 , 9 , 4 , 5]) == [3 , 9]
print ( my_function12 ([1 , 2 , 3 , 5 , 6]) )

# câu 13
def my_function13(y):
    var = 1
    while y > 1:
        var = var*y 
        y = y-1
    return var 
assert my_function13 (8) == 40320
print ( my_function13 (4) )

# câu 14:
def my_function14(x):
    return x[::-1]
x = 'I can do it'
assert my_function14 (x ) =='ti od nac I'

x = 'apricot'
print ( my_function14 ( x ) )

# câu 15:
def function_helper(x):
    return 'T' if x > 0 else 'N'

def my_function15(data):
    res = [function_helper(x) for x in data]
    return res 

data = [10 , 0 , -10 , -1]
assert my_function15 ( data ) == ['T', 'N', 'N', 'N']
data = [2 , 3 , 5 , -1]
print ( my_function15 ( data ) )

# câu 16
def function_helper1(x, data):
    for i in data: 
        if x == i: return 0
    return 1

def my_function16(data):
    res =[]
    for i in data: 
        if function_helper1(i, res):
            res.append(i)
    return res

lst = [10 , 10 , 9 , 7 , 7]
assert my_function16 ( lst ) ==[10 , 9 , 7]

lst = [9 , 9 , 8 , 1 , 1]
print ( my_function16 ( lst ) )
