class Man:
   def __init__(self,name,preference):
      self.name=name
      self.status=False
      self.preference=preference
      self.partner=""
      self.proposed=[]
   def  hopeleft(self):
      if len(self.proposed)==len(Women):  #THERE WONT BE ANY HOPE IF the  GUY HAS already PROPOSED TO EVERYONE.
         return False
      return True

class Woman:
   def __init__(self,name,preference):
      self.name=name
      self.status=False
      self.preference=preference
      self.partner=""
def objectfromname(w):
   for i in Women+Men:       #TAKE THE OBJECT NAME AS a STRING and RETURN THE OBJECT be it a Man or WOman
      if i.name==w:
         return i

def loveyoumore(m,w):
   if w.preference.index(m.name)<w.preference.index(w.partner): #Check if this guy's better than ur partner.
      return True
   return False
def thereissomeone():
   for i in Men:              #There's a man left who is SINGLE and hasn't proposed to every woman
      if i.hopeleft() and i.status==False:
         return i

a=Man("A",['y=Woman("Y",['C','D','A','B'])W','X','Y','Z'])
b=Man("B",['X','Y','Z','W'])
c=Man("C",['Y','Z','W','X'])
d=Man("D",['Z','W','X','Y'])
w=Woman("W",['A','B','C','D'])
x=Woman("X",['B','C','D','A'])
y=Woman("Y",['C','D','A','B'])
z=Woman("Z",['D','A','B','C'])
Men=[a,b,c,d]
Women=[w,x,y,z]
while thereissomeone():
   i=thereissomeone()     #Choose the single man who hasnt proposed to every girl
   wname=i.preference[len(i.proposed):] #UNPROPOSED WOMEN list
   wname=wname[0] #MOST PREFERRED WOMAN in UNPROPOSED.
   w=objectfromname(wname)  #You have her name as a string get her as an Object, to use operations.
   i.proposed.append(w.name) #This guy just proposed to woman w OMG
   if w.status==False:     #if the girl is single then mingle
      i.partner=w.name
      w.partner=i.name
      i.status=True
      w.status=True
   else:
      if loveyoumore(i,w):
         k=objectfromname(w.partner) #GET HER EX
         k.status=False #AXE HER EX, DUMP HIM.
         k.partner=""   #MAKE HIM SINGLE
         i.partner=w.name   #GET ENGAGED
         w.partner=i.name
         i.status=True       #CHANGE RELATIONSHIP STATUS
         w.status=True

for i in Men:
   print(i.name,i.partner)