import pandas as pd
data=pd.read_excel('aeroflot_prices.xls')
data.columns=['Date','Open','High','Low','Close','V']
data
open_ye=[]
high_ye=[]
low_ye=[]
close_ye=[]
v_ye=[]
for i in range(1,397):
  open_ye.append(data.Open[i-1])
  high_ye.append(data.High[i-1])
  low_ye.append(data.Low[i-1])
  close_ye.append(data.Close[i-1])
  v_ye.append(data.V[i-1])
data=data[1:]
data=data.reset_index()
data=data.drop(columns=['index'])
data
indexx=[]
for i in range(396):
  indexx.append(i)
data_reg = pd.DataFrame(
{
"Open_ye": open_ye,
"Close_ye":close_ye,
"v_ye":v_ye,
'high_ye':high_ye,
 'low_ye':low_ye,
},
index=indexx,
)
result=pd.concat([data,data_reg],axis=1)
result['Weekday']=result.Date.dt.dayofweek
result
result['monthday']=result.Date.dt.daysinmonth
result['weekofyear']=result.Date.dt.weekofyear
result
result['month']=result.Date.dt.month
result.drop(columns=['Date'],inplace=True)
result = pd.get_dummies(result, columns=['Weekday','monthday','weekofyear','month'])
result.corr()
from sklearn.linear_model import LinearRegression
data_train=result

X_train = data_train.drop(columns=["Open","High","Low","Close","V"])
y_train = data_train["Open"]

LinReg = LinearRegression(normalize=False)
LinReg.fit(X_train, y_train)
prediction = LinReg.predict(X_test)
from sklearn.metrics import mean_absolute_error
print("MAE = ", mean_absolute_error(y_test, prediction))
data_predict = pd.DataFrame(
{
"Date":pd.Timestamp("2021-04-29"),
"Open_ye": 65.70,
"Close_ye":65.00,
"v_ye":9486780,
"high_ye":65.74,
"low_ye":64.60,
},index=[1]
,)
# 2021-04-29	open 65.70	high 65.74	low 64.60	close 65.00	 v 9486780
data_predict	
#Weekday	monthday	weekofyear	month
#result['Weekday']=result.Date.dt.dayofweek
#result['monthday']=result.Date.dt.daysinmonth
# result['weekofyear']=result.Date.dt.weekofyear
# result['month']=result.Date.dt.month
data_predict['Weekday']=data_predict.Date.dt.dayofweek
data_predict['monthday']=data_predict.Date.dt.daysinmonth
data_predict['weekofyear']=data_predict.Date.dt.weekofyear
data_predict['month']=data_predict.Date.dt.month
print(data_predict)
data_predict=pd.get_dummies(data=data_predict,columns=['Weekday','monthday','weekofyear','month'])
nulls=['Weekday_0',	'Weekday_1',	'Weekday_2', 'Weekday_4','Weekday_5',	'Weekday_6',	'monthday_28',	'monthday_29', 'monthday_31',	'weekofyear_1',	'weekofyear_2',	'weekofyear_3',	'weekofyear_4',	'weekofyear_5',	'weekofyear_6',	'weekofyear_7',	'weekofyear_8',	'weekofyear_9',	'weekofyear_10',	'weekofyear_11',	'weekofyear_12',	'weekofyear_13',	'weekofyear_14',	'weekofyear_15',	'weekofyear_16',	'weekofyear_18',	'weekofyear_19',	'weekofyear_20',	'weekofyear_21',	'weekofyear_22',	'weekofyear_23',	'weekofyear_24',	'weekofyear_25',	'weekofyear_26',	'weekofyear_27',	'weekofyear_28',	'weekofyear_29',	'weekofyear_30',	'weekofyear_31',	'weekofyear_32',	'weekofyear_33',	'weekofyear_34',	'weekofyear_35',	'weekofyear_36',	'weekofyear_37',	'weekofyear_38',	'weekofyear_39',	'weekofyear_40',	'weekofyear_41',	'weekofyear_42',	'weekofyear_43',	'weekofyear_44',	'weekofyear_45',	'weekofyear_46',	'weekofyear_47',	'weekofyear_48',	'weekofyear_49',	'weekofyear_50',	'weekofyear_51',	'weekofyear_52',	'weekofyear_53',	'month_1',	'month_2',	'month_3',	'month_5',	'month_6',	'month_7',	'month_8',	'month_9',	'month_10',	'month_11',	'month_12']
dictinary={}
for i in nulls:
  dictinary.update({i:0})
print(dictinary)
dictik={
 "Open_ye": 65.70,
 "Close_ye":65.00,
 "v_ye":9486780,
 "high_ye":65.74,
 "low_ye":64.60, 
 'Weekday_0': 0,
 'Weekday_1': 0,
 'Weekday_2': 0,
 'Weekday_3': 0,
 'Weekday_4': 1,
 'Weekday_5': 0,
 'Weekday_6': 0,
 'monthday_28': 0,
 'monthday_29': 0,
 'monthday_30':1,
 'monthday_31': 0,
 'weekofyear_1': 0,
 'weekofyear_2': 0,
 'weekofyear_3': 0,
 'weekofyear_4': 0,
 'weekofyear_5': 0,
 'weekofyear_6': 0,
 'weekofyear_7': 0,
 'weekofyear_8': 0,
 'weekofyear_9': 0,
 'weekofyear_10': 0,
 'weekofyear_11': 0,
 'weekofyear_12': 0,
 'weekofyear_13': 0,
 'weekofyear_14': 0,
 'weekofyear_15': 0,
 'weekofyear_16': 0,
 'weekofyear_17': 1,
 'weekofyear_18': 0,
 'weekofyear_19': 0,
 'weekofyear_20': 0,
 'weekofyear_21': 0,
 'weekofyear_22': 0,
 'weekofyear_23': 0,
 'weekofyear_24': 0,
 'weekofyear_25': 0,
 'weekofyear_26': 0,
 'weekofyear_27': 0,
 'weekofyear_28': 0,
 'weekofyear_29': 0,
 'weekofyear_30': 0,
 'weekofyear_31': 0,
 'weekofyear_32': 0,
 'weekofyear_33': 0,
 'weekofyear_34': 0,
 'weekofyear_35': 0,
 'weekofyear_36': 0,
 'weekofyear_37': 0,
 'weekofyear_38': 0,
 'weekofyear_39': 0,
 'weekofyear_40': 0,
 'weekofyear_41': 0,
 'weekofyear_42': 0,
 'weekofyear_43': 0,
 'weekofyear_44': 0,
 'weekofyear_45': 0,
 'weekofyear_46': 0,
 'weekofyear_47': 0,
 'weekofyear_48': 0,
 'weekofyear_49': 0,
 'weekofyear_50': 0,
 'weekofyear_51': 0,
 'weekofyear_52': 0,
 'weekofyear_53': 0,
 'month_1': 0,
 'month_2': 0,
 'month_3': 0,
 'month_4':1,
 'month_5': 0,
 'month_6': 0,
 'month_7': 0,
 'month_8': 0,
 'month_9': 0,
 'month_10': 0,
 'month_11': 0,
 'month_12': 0,
 }
data_pred_zavtra=pd.DataFrame(dictik,index=[1],)
predictionx=LinReg.predict(data_pred_zavtra)
print(predictionx)
