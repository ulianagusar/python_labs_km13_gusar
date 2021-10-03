print("enter the magnitude value")
mag =float(input())
if(mag<2):
    print("earthquake type: micro")
elif((mag>=2)&(mag<3)):
    print("earthquake type: very minor")
elif((mag>=3)&(mag<4)):
    print("earthquake type: minor")
elif((mag>=4)&(mag<5)):
    print("earthquake type: light")
elif((mag>=5)&(mag<6)):
    print("earthquake type: moderate")
elif((mag>=6)&(mag<7)):
    print("earthquake type: strong")
elif((mag>=7)&(mag<8)):
    print("earthquake type: major")
elif((mag>=8)&(mag<10)):
    print("earthquake type: great")
elif(mag>=10):
    print("earthquake type: meteoric")