from math import pi
##this is question 1
class Print3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def coord(self):
        xyz=(self.x,self.y,self.z)
        return xyz

a=Print3D(3,4,5)
print(a.coord())
##this is question 2
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        self.aire=self.length*self.width
        return (self.aire)
    def perimeter(self):
        self.perimeter=(self.length+self.width)*2
        return (self.perimeter)

rectangle=rectangle(2,3)
print('area of rectangle is approximately = to ',rectangle.area(),'and','perimeter of rectangle is approximatly = to ',rectangle.perimeter())


##this is question 3       
class circle:
    def __init__(self,xycoord_center,r):
        self.xycoord_center=xycoord_center
        self.r=r
    def area(self):
        self.area=(self.r**2)*pi
        return (self.area)
    def perimeter(self):
        self.perimeter=self.r*2*pi
        return (self.perimeter)
    def isinside(self,point_coord):
        a=self.a=self.xycoord_center[0]
        b=self.b=self.xycoord_center[1]
        x=point_coord[0]
        y=point_coord[1]
        distance_center_point=((x-a)**2+(y-b)**2)**0.5
        if distance_center_point<self.r:
            return('the point with your ccordinates is inside the circle')
        elif distance_center_point==self.r:
            return('the point with your ccordinates is on the circumference of the circle')
        else:
            return('the point with your ccordinates is outside of the circle')

circle=circle([0,0],4)
print('area of circle is approximately = to ',circle.area(),'and','perimeter of circle is approximatly = to ',circle.perimeter())
print(circle.isinside([3,0]))


##this is question 3 
class Bank_account:
    def __init__(self,account_money):
        self.account_money=account_money
    def deposit(self,deposit):
        self.deposit=deposit
        self.account_money=self.account_money+self.deposit
        return(self.account_money)
    def withdraw(self,withdraw):
        self.withdraw=withdraw
        self.account_money=self.account_money-self.withdraw
        return(self.account_money)
        

