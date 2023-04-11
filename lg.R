df<-read.csv("C:\\Users\\Tanmay\\Downloads\\income.data_\\income.data.csv")

plot(happiness~income,data=income.data)
lr<-lm(happiness~income,data=income.data)
summary(lr)
plot(lr)

plot(happiness~income,data=income.data)
