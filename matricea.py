x=[[1,2,3,4,5],
[2,5,4,7,8],
[1,3,5,7,9],
[2,4,6,8,10],
[2,2,7,5,1]]
print('suma primei linii este',sum(x[0]))
print('suma primei linii este',sum(x[1]))
print('suma primei linii este',sum(x[2]))
print('suma primei linii este',sum(x[3]))
print('suma primei linii este',sum(x[4]))
a=[]
b=[]
c=[]
d=[]
e=[]
for i in x:
 a.append(i[0])
 b.append(i[1])
 c.append(i[2])
 d.append(i[3])
 e.append(i[4])
 print('suma primei coloane este',sum(a))
 print('suma coloanei 2 este',sum(b))
 print('suma coloanei 3 este',sum(c))
 print('suma coloanei 4 este',sum(d))
 print('suma coloanei 5 este',sum(e))
 f=[]
 for i in range(len(x)):
  for j in range(len(x[0])):
      if i==j:
          f.append(x[i][j])
print('diagonala principala este',f)
g=[]
for i in range(len(x)):
    for j in range(len(x[0])):
        if i+j==4:    #n=5, n-1=4
           
            g.append(x[i][j])
print('diagonala secundara este',g)