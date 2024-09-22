import pickle
x,y,z=1,2,3
s="FishC"
l=['小甲鱼',520,3.14]
d={'one':1,'two':2}
with open('data.pkl', 'wb') as f:
    pickle.dump(x,f)
    pickle.dump(y,f)
    pickle.dump(z,f)
    pickle.dump(s,f)
    pickle.dump(l,f)
    pickle.dump(d,f)
    # pickle.dump((x,y,z,s,l,d),f) # 简化写法，可以传入一个元组
    