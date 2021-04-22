
data <- read.csv("./1_new_train.csv")
print (dim(data))

print ("Removing all NA values")
train = data[complete.cases(data), ]
print (dim(train))

train_new = subset(train, train$fagerec11 != 11)
print (unique(train_new$fagerec11))
print (dim(train_new))

write.csv(train_new, "./clean_training_data.csv", row.names = TRUE)