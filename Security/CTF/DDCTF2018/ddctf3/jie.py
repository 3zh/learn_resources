mod_res=0x2BF5B02AC9500
mod=0x1E75BF5AB47900
for i in range(150000,550000):
    if (2**i) %mod==mod_res:
        print(i)
        break
print("stop..")
