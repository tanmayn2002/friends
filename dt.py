library(rpart)
library(caTools)
library(dplyr)
library(rpart.plot)
library(party)
url<-"https://raw.githubusercontent.com/ankurv343/GFG/master/Advertisement.csv"
data<-read.csv(url)
traindata<-sample.split(Y=data,SplitRatio = 0.80)
train1<-data[traindata,]
test<-data[!traindata,]
head(data)
set.seed(1234)
model=rpart(Purchased~.,d=train1,method="class")
rpart.plot(model)
pred<-predict(model,test,type = "class")
m<-table(test$Purchased,pred)
ac<- sum(diag(m)) /sum(m)
print(paste('Accuracy for test is found to be',ac))


