my_data <- read.csv('C:/Users/Enoch/Desktop/pj/HDCGAN-TF/logs/loss_log.csv')
my_data2 <- read.csv('C:/Users/Enoch/Desktop/selu results/loss_log.csv')
plot(my_data$iterations,my_data$d_loss/max(my_data$d_loss),type='n',ylim=c(0,1),xlim=c(0,10000),xlab='iterations',ylab='discriminator loss')
lines(my_data$iterations,my_data$d_loss/max(my_data$d_loss),col="red")
plot(my_data2$iterations,my_data2$d_loss/max(my_data2$d_loss),type='n',ylim=c(0,1),xlim=c(0,10000),xlab='iterations',ylab='discriminator loss')
lines(my_data2$iterations,my_data2$d_loss/max(my_data2$d_loss),col="red")
#plot(my_data$iterations,my_data$g_loss,type='n',ylim=c(min(my_data$g_loss)*.8,max(my_data$g_loss)*1.2),xlab='iterations',ylab='generator los/s')
#lines(my_data$iterations,my_data$g_loss,col="blue")


