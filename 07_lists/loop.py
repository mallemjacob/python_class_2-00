# def missing_char(str, n):
#     new_str = ''
#     for i in range(len(str)):
#         if i == n:
#             continue
#         else:
#             new_str = new_str + str[i]

#     return new_str

def missing_char(str, n):
    return str[0:n] + str[n+1:]


print(missing_char('kitten', 1))
