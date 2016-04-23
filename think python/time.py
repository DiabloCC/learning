s = input().split(' ')
cur_time = eval(s[0][0:-2]) * 60 + eval(s[0][-2:])
diff = eval(s[1])
then_time = cur_time + diff
r = str(then_time // 60) + '{0:0^2}'.format(then_time % 60)
print(r)