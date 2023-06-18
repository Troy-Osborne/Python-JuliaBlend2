from __future__ import division
from math import cos,sin,pi,sqrt,e,atan
from PIL import Image,ImageDraw
from Colors import *
def normalize_infinity(val):
    return abs(atan(val)/pi*2)
def julia(c,d,iterations=30,frame=0,colscheme=ColTest1):
    c=c+d*1j
    def inner(x,y): 
        z=x+y*1j
        thresholdpoint=.6
        thresholditeration=None
        #new test for coloring
        for i in range(iterations):
            try:
                #z=(z**2+(c*z)**6)/(1-z**2)-z**4+c
                #z=z**3/(1-z)+((z-c)**5)/10+c #really nice at drawpath(2,2,.32,.38,-.018,.045)
                #z=z**2/(1-z)+((z-c)**c)/10+c
                #z=1/(1-z**2)+c
                #z=z**z-c/(1-z**2)
                z=1/((z**2+c1)/(z**4+c2))+c1**c2
            except:
                return (1,1,1)
            #z=z**b+c
            absol=abs(z)
            if absol>2:
                #return (0,0,0)
                #absol=min(absol,4)
                return colscheme(.4+normalize_infinity((absol-2)*10+((i/iterations)*10)**1.6)*.6)
                #return ((64+((1+(i+sin(frame/100*pi)*2)/10)**1.4)%4)*30,60+(i/5%3)*70,64+(i/iterations+sin(frame/100*pi))*100)
                #return (256-(60+(i/5%3)*40),256-(64+(i/iterations)*140),256-((64+((1+i/10)**1.4)%4)*40))
            if absol<=thresholdpoint and thresholditeration==None:
                threshholditeration=i
        if thresholditeration==None:
            thresholditeration=0
        return colscheme(min(2,absol)/4)
        #return (96+min(((1+absol+thresholditeration/10)**2*60),256),min(((1+absol)**3*20),256),(255-min((1+absol+(frame/40+thresholditeration/10)%3)**3*54,196)))
    return inner

def doublejulia(a,b,c,d,iterations=20,frame=0,colscheme=Boundary,func=None):
    c1=a+b*1j
    c2=c+d*1j
    def inner(x,y): 
        z=x+y*1j
        thresholdpoint=.6
        thresholditeration=None
        #new test for coloring
        for i in range(iterations):
            try:
                #z=z**4/(z+c1)/(z+c2)+(c1+c2)/2 ###Main First Double Func
                #z=(z**5+c1)/(z**3+c2)
                #z=(c1)/(1-z**2)+c2
                #Still untested                #z=(z**2+c1)*(z**2+c2)/z**2
                #z=z**((c2+c1)/2)-c1/(1-z**2)*c2
                #z=(z**2+(c1*z)**6)/(1-z**2)-z**4+c2
                if func==None:
                    z=1/((z**2+c1)/(z**4+c2))+c1**c2
                else:
                    z=func(z,c1,c2)
            except:
                return (251,251,251)
            absol=abs(z)
            if absol>2:
                #return colscheme(.1+normalize_infinity(abs((absol-2)*5-i))**4*.9)
                #col=min(1,((i/iterations)**.34*.5+normalize_infinity((absol-1)**.3))**1.9)
                col=min(1,((i/iterations)**.34*.5+normalize_infinity(abs((absol-2)*5-i))**8*.3)**1.2)
                #print(col)
                return colscheme(col)
            if absol<=thresholdpoint and thresholditeration==None:
                threshholditeration=i
        if thresholditeration==None:
            thresholditeration=0
        return colscheme(.75-((min(20,absol*15)/26)**2)*.08)
        #return colscheme(.5+sin(absol*10)*.5)
        #return (0,0,0)
    return inner

def drawfunc(f,resolution=(1080,720),view=(-1,-1,1,1),frame=0,name="Test"):
    resolution=(int(resolution[0]),int(resolution[1]))
    im=Image.new("RGB",resolution,(0,0,0))
    for i in range(resolution[0]):
        for j in range(resolution[1]):
            x=view[0]+(view[2]-view[0])*i/resolution[0]
            y=view[1]+(view[3]-view[1])*j/resolution[1]
            col=f(x,y)
            #col=tuple([int(min(255,max(0,i))) for i in col])
            im.putpixel((i,j),col)
    im.save(name+"%04d.png"%frame)


def midpoint(a,b,r):
    return a+(b-a)*r

fourK=(3840,2160)
ten80=(1920,1080)
lowres=(600,400)

def drawrandoms(resolution=(640,480),iterations=18,steps=1000):
    from random import random
    n=0
    for frame in range(0,steps):
        r=frame/steps
        r1,r2=(random()*3-1.5,random()*3-1.5)
        c=r1+r2*1j
        print("frame %04d:c= %s"%(n,str(c)))
        drawfunc(julia(r1,r2,iterations,n),resolution=resolution,frame=n)
        n+=1

def drawdoublerandoms(resolution=lowres,iterations=26,steps=5000):
    from random import random
    n=0
    for frame in range(0,steps):
        r=frame/steps
        r1,r2=(random()*4-2,random()*4-2)
        r3,r4=(random()*4-2,random()*4-2)
        c1=r1+r2*1j
        c2=r3+r4*1j
        print("frame %04d:\n\tc1= %s \n\tc2= %s"%(n,str(c1),str(c2)))
        name="c=%s d=%s"%(c1,c2)
        drawfunc(doublejulia(r1,r2,r3,r4,iterations,n,func=lambda z,c1,c2:1/((z+c1)*(z+c2))**2),resolution=resolution,frame=0,name=name)
        n+=1

def drawpath(c1,c2,d1,d2,resolution=fourK,iterations=35,steps=10):
    n=0
    for frame in range(0,steps):
        r=frame/steps
        c=midpoint(c1,c2,r)+midpoint(d1,d2,r)*1j
        print("frame %04d:c= %s"%(n,str(c)))
        drawfunc(julia(midpoint(c1,c2,r),midpoint(d1,d2,r),iterations,n),resolution=resolution,frame=n)
        n+=1

def drawdouble(a,b,c,d,resolution=(600,320),iterations=ten80,func=None,view=(-.2,-.2,.2,.2),frame=0,name="individual"):
    drawfunc(doublejulia(a,b,c,d,iterations,0,func=func),resolution=resolution,frame=frame,name=name,view=view)

fps=60
def drawdoublepath(a1,a2,b1,b2,c1,c2,d1,d2,resolution=ten80,iterations=40,steps=int(fps*36),view=(-1,-1,1,1),name="AA",func=None):
    n=0
    for frame in range(0,steps+1):
        r=(frame)/steps
        jc1=midpoint(a1,a2,r)+midpoint(b1,b2,r)*1j
        jc2=midpoint(c1,c2,r)+midpoint(d1,d2,r)*1j
        print("frame %04d:\n\tc1= %s\n\tc2=%s"%(n,str(jc1),str(jc2)))
        drawfunc(doublejulia(midpoint(a1,a2,r),midpoint(b1,b2,r),midpoint(c1,c2,r),midpoint(d1,d2,r),iterations,n,func=func),resolution=resolution,view=view,frame=n,name=name)
        n+=1

while True:
    drawdoublerandoms(resolution=lowres,iterations=26,steps=5000)
    
def from_to(origin,destination,func,steps=int(40*fps),view=(-.55,-.1,.45,.5),name="new"):
    return drawdoublepath(origin[0],destination[0],origin[1],destination[1],origin[2],destination[2],origin[3],destination[3],steps=steps,view=view,name=name,func=func)
from random import random
#from_to([i*1.05 for i in [0.6617158962245103,0.931301477201842,0.7937245259542852,0.7621161687235718]],
#        [i*.9 for i in [0.6617158962245103,0.931301477201842,0.7937245259542852,0.7621161687235718]],
#        func=lambda z,c1,c2:1/(z+c1)/(z+c2)**3)

