# # Problem-8 Write a python function that receives a list of integers and prints out a histogram of bin size 10

# # Input:
# # [13,42,15,37,22,39,41,50]


# # Output:
# # {11-20:2,21-30:1,31-40:2,41-50:3}


# def histrogram(l,d):
#     c11,c21,c31,c41,c51=0,0,0,0,0
#     for i in l:
#         if i>=11 and i<=20:
#             c11+=1
#             d['11-20']=c11
#         elif i>=21 and i<=30:
#             c21+=1
#             d['21-30']=c21
#         elif i>=31 and i<=40:
#             c31+=1
#             d['31-40']=c31
#         elif i>=41 and i<=50:
#             c41+=1
#             d['41-50']=c41
#         elif i>=51 and i<=60:
#             c51+=1
#             d['51-60']=c51
#     return d


# dic={}
# histrogram([13,42,15,37,22,39,41,50],dic)
# print(histrogram([13,42,15,37,22,39,41,50],sorted(dic.keys())))

def histogram(l):
    d = {
        '11-20': 0,
        '21-30': 0,
        '31-40': 0,
        '41-50': 0,
        '51-60': 0
    }

    for i in l:
        if 11 <= i <= 20:
            d['11-20'] += 1
        elif 21 <= i <= 30:
            d['21-30'] += 1
        elif 31 <= i <= 40:
            d['31-40'] += 1
        elif 41 <= i <= 50:
            d['41-50'] += 1
        elif 51 <= i <= 60:
            d['51-60'] += 1

    return d

print(histogram([13,42,15,37,22,39,41,50]))