import time
###############计算当前时间
time1=time.time()
print("欢迎使用圆周率计算小程序，使用前请合理估计电脑性能再输入位数！！！避免不必要的死机")
number = int(input('请输入想要计算到小数点后的位数n:'))
# 多计算10位，防止尾数取舍的影响
number1 = number+10
# 算到小数点后number1位
b = 10**number1
# 求含4/5的首项
x1 = b*4//5
# 求含1/239的首项
x2 = b// -239
# 求第一大项
he = x1+x2
#设置下面循环的终点，即共计算n项
number *= 2
#循环初值=3，末值2n,步长=2
for i in range(3,number,2):
  # 求每个含1/5的项及符号
  x1 //= -25
  # 求每个含1/239的项及符号
  x2 //= -57121
  # 求两项之和
  x = (x1+x2) // i
  # 求总和
  he += x
# 求出π
pai = he*4
#舍掉后十位
pai //= 10**10
paistring=str(pai)
result=paistring[0]+str('.')+paistring[1:len(paistring)]
print("计算完成，结果已经存入同目录下pi文件夹的'PI.txt'")
os.makedirs(/PI, mode=0o777)
file_handle=open('PI.txt',mode='w')
file_handle.write('计算结果为：'+result+"\n")
time2=time.time()
file_handle.write('总共耗时：' + str(time2 - time1) + '秒\n')
file_handle.write('作者Sam1314，联系方式：tg:https://t.me/samwang1314')
file_handle.close()

