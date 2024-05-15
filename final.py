from sktime.forecasting.base import ForecastingHorizon
from sktime.forecasting.model_selection import temporal_train_test_split
from sktime.forecasting.theta import ThetaForecaster
import pandas as pd
import matplotlib.pyplot as plt

f1 = "C:/Users/sansk/OneDrive/Desktop/data/B0005.xlsx"
f2 = "C:/Users/sansk/OneDrive/Desktop/data/B0006.xlsx"
f3 = "C:/Users/sansk/OneDrive/Desktop/data/B0018.xlsx"
file ="C:/Users/sansk/OneDrive/Desktop/data/B0007.xlsx"
df1 = pd.read_excel(f1)
df2 = pd.read_excel(f2)
df3 = pd.read_excel(f3)
df = pd.concat([df1,df2,df3])
x = pd.read_excel(file)
#print(x)
df.to_excel("C:/Users/sansk/OneDrive/Desktop/data/try.xlsx")
df = df['capacity'].values
df = pd.DataFrame(df)

x_train,x_test= temporal_train_test_split(x,train_size=0.25)
fh = ForecastingHorizon(x_test.index,is_relative=False) #index as we are not giving model the actual values but only the index to be predicted
forecaster = ThetaForecaster(sp=167)
forecaster.fit(df)
pred = forecaster.predict(fh)
pred.to_excel("C:/Users/sansk/OneDrive/Desktop/data/try.xlsx")

plt.plot(x_test, c='red')
plt.plot(pred, c='blue')
plt.ylim(0, 4)  # Set the x-axis limits from 0 to 10


plt.xlabel("Cycle")
plt.ylabel("Capacity")
plt.legend(["Actual Data", "Predicted Data"], loc="lower left")

plt.show()



for i in x.index:
    # print(i)

    if x.iloc[i,0]<=1.5:
        print("Actual EOL =",x.iloc[i,0])
        print("At ", i,end="")
        print("th Cycle")
        break

for k in pred.index:

    if pred.iloc[(k-len(x_train)),0]<=1.5:
        print("Predicted EOL =" , pred.iloc[(k-len(x_train)), 0])
        print("At " ,k , end="",)
        print("th Cycle")
        exit()

pred.to_excel("C:/Users/sansk/OneDrive/Desktop/data/try.xlsx")
