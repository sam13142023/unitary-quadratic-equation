import math
def qua(a, b, c):
	a1 = -b - math.sqrt(b * b - 4 * a * c)
	a2 = -b + math.sqrt(b * b - 4 * a * c)
	x1 = a1 / (2 * a)
	x2 = a2 / (2 * a)
	return x2, x1
a1, b1, c1 = map(int, input("☆一元二次方程计算器☆，请输入a,b,c系数，以空格隔开！\n☆输入0 0 0可退出程序☆\n\n").split())
while(a1 != 0 or b1 != 0):
	if b1 * b1 - 4 * a1 * c1 >= 0 :
		x, y = qua(a1, b1, c1)
		x1 = str(x)
		x2 = str(y)
		print("x1 = %s, x2 = %s \n" % (x1, x2))
	else :
		print("此方程无实数解\n")
	a1, b1, c1 = map(int, input("☆请输入a,b,c系数，以空格隔开☆\n☆输入0 0 0可退出程序☆\n\n").split())