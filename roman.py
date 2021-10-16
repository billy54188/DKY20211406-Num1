def transform_alabo2_roman_num(one_num):
  '''''
  将阿拉伯数字转化为罗马数字
  '''
  num_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  str_list=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
  res=''
  for i in range(len(num_list)):
    while one_num>=num_list[i]:
      one_num-=num_list[i]
      res+=str_list[i]
  return print(res)
transform_alabo2_roman_num(int(input('输入数字')))