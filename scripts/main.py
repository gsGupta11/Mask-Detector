import vedioInput
import predict

n=int(input("Mask Detection in \n 1.Image \n 2.Live Vedio \n 3.Recorded vedio\nChoice: "))

if n==1:
    print("hello World")
elif n==2:
    vedioInput.vedioPredict(0)
elif n==3:
    add = input("Enter Address of the file")
    vedioInput.vedioPredict(add)
else:
    add = input("Enter Address of the file")
    m = predict.mask(add)
    print(m)
