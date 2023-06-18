def midcol(a,b,r):
    return (int(a[0]+(b[0]-a[0])*r),int(a[1]+(b[1]-a[1])*r),int(a[2]+(b[2]-a[2])*r))

def ColorScheme(start=(0,0,0),middle=[],end=(255,255,255)):
    def ColFunc(pos):#0<pos<1
        if pos<0:
            return start
        elif pos>1:
            return start
        else:
            if middle:
                Next=0
                LastCol=start
                for i in middle:
                    Last=Next
                    Next=i[0]
                    if pos<Next:
                        return midcol(LastCol,i[1],(pos-Last)/(Next-Last))
                    LastCol=i[1]
                Last=Next
                Next=1
                return midcol(LastCol,end,(pos-Last)/(Next-Last))
                    
            else:
                return midcol(start,end,pos)
    return ColFunc

def draw_sample_gradient(name,ColFunc):
    from PIL import Image,ImageDraw
    im=Image.new("RGB",(640,480),(0,0,0))
    dr=ImageDraw.Draw(im)
    for i in range(640):
        dr.rectangle((i,0,i+1,480),fill=ColFunc(i/640))
    im.save(name+".png")
    
ColTest1=ColorScheme(start=(64,100,196),middle=[(.2,(255,196,196)),(.22,(64,32,164)),(.23,(255,255,255)),(.25,(0,0,0)),(.3,(100,100,64)),(.35,(0,0,0)),(.4,(64,32,164)),(.55,(255,255,255)),(.75,(0,0,0)),(.9,(32,132,96))],end=(164,64,196))
ColTest2=ColorScheme(start=(196,32,32),middle=[(.2,(0,0,0)),(.4,(64,32,164)),(.8,(255,255,255)),(.95,(0,0,0)),(.98,(128,180,200))],end=(164,64,196))
ColTest3=ColorScheme(start=(32,196,32),middle=[(.2,(255,0,0)),(.22,(64,32,164)),(.23,(255,255,255)),(.25,(0,0,0)),(.3,(255,255,0)),(.42,(64,164,32)),(.43,(255,255,255)),(.45,(0,0,0)),(.6,(64,0,196))],end=(255,255,255))
BluePurple=ColorScheme(start=(164,164,196),middle=[(.1,(164,64,164)),(.2,(64,0,64)),(.3,(0,0,100)),(.34,(70,40,90)),(.5,(80,80,255)),(.6,(180,80,255)),(.75,(255,180,255)),(.85,(200,200,255))],end=(255,255,255))
ElectricBlue=ColorScheme(start=(43,204,231),middle=[(.1,(0,164,232)),(.2,(56,255,223)),(.3,(0,0,100)),(.34,(0,0,0)),(.5,(80,80,255)),(.6,(153,217,235)),(.75,(255,255,255)),(.85,(200,200,255))],end=(0,0,0))
Fire=ColorScheme(start=(0,0,0),middle=[(.3,(64,64,0)),(.4,(200,96,64)),(.3,(255,196,100)),(.34,(255,100,0)),(.5,(255,0,0)),(.6,(255,100,100)),(.75,(166,0,194)),(.85,(96,96,255))],end=(0,0,0))
Blurple=ColorScheme(start=(0,0,0),middle=[(.3,(64,0,64)),(.4,(96,0,64)),(.5,(0,0,0)),(.6,(0,80,128)),(.8,(0,80,80))],end=(0,0,0))
BlurplePlus=ColorScheme(start=(0,0,0),middle=[(.2,(64,0,64)),(.3,(96,0,96)),(.35,(206,128,196)),(.4,(64,0,96)),(.48,(0,0,0)),(.55,(0,0,128)),(.65,(20,80,128)),(.7,(100,200,200)),(.72,(20,80,128)),(.8,(20,100,120))],end=(0,0,0))
Boundary=ColorScheme(start=(40,64,96),middle=[(.2,(100,120,164)),(.3,(100,120,96)),(.3,(96,0,96)),(.35,(206,128,196)),(.4,(64,0,96)),(.48,(0,0,0)),(.65,(0,0,128)),(.65,(20,80,128)),(.7,(100,200,200)),(.7,(20,80,128)),(.8,(20,100,120))],end=(0,0,0))

draw_sample_gradient("ElectricBlue",ElectricBlue)
draw_sample_gradient("Fire",Fire)
draw_sample_gradient("Blurple",Blurple)
draw_sample_gradient("BlurplePlus",BlurplePlus)
draw_sample_gradient("Boundary",Boundary)
#draw_sample_gradient("GreyPrimarys",ColTest2)
#draw_sample_gradient("Pastel",ColTest3)
