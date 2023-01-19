# %%
#Initializing All Weights And Biases to 0
weights = [0, 0]
bias = 0
#Input Training Vector
x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
#Target Output Vector
y = [1, -1, -1, -1]
print("x1\tx2\tb\ty\tdw1\tdw2\tdb\tw1\tw2\tB")
for i in range(4):
    print(x1[i], "\t", x2[i], "\t1\t", y[i], "\t", end="")
    cw1 = x1[i] * y[i]
    cw2 = x2[i] * y[i]
    #wi(new) = wi(old) + XiY ( i= 1 to n)
    weights[0] = weights[0] + cw1
    weights[1] = weights[1] + cw2
    #Adjust the bias: b(new) = b(old) + Y
    bias = bias + y[i]
    print(cw1,"\t",cw2,"\t",bias,"\t",weights[0],"\t",weights[1],"\t",bias)


# %%



