class Wynagrodzenie:
 suma=0
 def __init__(self,imie,brutto):
  self.imie=imie
  self.brutto=int(brutto)
 
 def wynagrodzenie_netto(self):
  if self.brutto > 1599:
   skladki=round(round(self.brutto*0.0976,2)+round(self.brutto*0.015,2)+round(self.brutto*0.0245,2),2)
   a=round(self.brutto-skladki,2)
   zdrow=round(a*0.09,2)
   b=round(a*0.0775,2)
   poz=round(self.brutto-139.25-skladki,0)
   zpdpo=round((poz*0.18)-46.33,2)
   zpddp=round(zpdpo-b,0)
   n=round(self.brutto-skladki-zdrow-zpddp,2)
   netto='%.2f' %n

   skp=round(self.brutto*0.0976,2)+round(self.brutto*0.065,2)+round(self.brutto*0.0193,2)+round(self.brutto*0.0245,2)+round(self.brutto*0.001,2)
   koszty=round(self.brutto+skp,2)
   obciazprac='%.2f' %skp
   kosztypracodawcy='%.2f' %koszty
   self.suma=self.suma+koszty
   print(self.imie,netto,obciazprac,kosztypracodawcy)
  else:
   print(self.imie,0)

pracownicy=int(input())
k=[]
for i in range(pracownicy):
 pracownik=input().split()
 k.append(pracownik)
s=0
for j in k:
 c=Wynagrodzenie(j[0],int(j[1]))
 c.wynagrodzenie_netto()
 s=(s+c.suma)
 zaokr='%.2f' %s
print(zaokr)