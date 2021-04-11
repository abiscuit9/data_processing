import pandas as pd
data = pd.read_csv("data.csv")#读取源dataframe
res = pd.DataFrame(columns=['id','utc','stald','satld','xSta','ySta','zSta','lonSta','latSta','xSat','ySat','zSat','lonSat','latSat','stec','el','topstec'])#建立结果dataframe
a = int(input(['请输入测试参数']))#输入测试参数
b = int(50)#定义比较参数，可以自己改
c = 1
for index,row in data.iterrows():#遍历源dataframe取值
    rowData = data.iloc[row[0],:]
    xSatDate = rowData.loc['xSat']#取特定值xSat，可以自己改
    distance = int(abs(xSatDate - a))#计算距离
    if distance <= b:#判断数值大小
        res = res.append(row)#成功则添加进结果dataframe    
res = res.reset_index(drop=False)#重建索引序号
res.to_csv("res" + "_input" + str(a) + ".csv")#输出