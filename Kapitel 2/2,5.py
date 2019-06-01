print("Hur många vill äta 2 vanliga korvar?")
två_vk = input()
print("Hur många vill äta 3 vanliga korvar?")
tre_vk = input()
print("Hur många vill äta 2 veganska korvar?")
två_vgk = input()
print("Hur många vill äta 3 veganska korvar?")
tre_vgk = input()
print("Hur många elever vill ha en dricka")
dricka = input()
D_Pris = int(dricka)*13.95  #antalet drickor är dricka tar det gånger priset per dricka
mEtt = int(två_vk)+int(tre_vk)
mTvå = mEtt/8
mTre = int(mTvå)
if mTvå == mTre:    #om  det är lika ska koden under köras
    V_Pris= int(mTre)*20.95
    V_Korvar = int(mTre)
elif mTvå > mTre:   #annars ska denna kod köras
    V_Pris= int(mTvå+1)*20.95
    V_Korvar = int(mTvå+1)
mFyra = int(två_vgk)+int(tre_vgk)
mFem = mFyra/4
mSex = int(mFem)
if mFem == mSex:
    VG_Pris = int(mSex)*34.95
    VG_Korvar = int(mSex)
elif mFem > mSex:
    VG_Pris = int(mFem+1)*34.95
    VG_Korvar = int(mFem+1)
Pris = V_Pris+VG_Pris+D_Pris
print("Du kommer behöva köpa", V_Korvar, "paket med vanliga korvar och det kommer att kosta", round(V_Pris,2),"kr. Du kommer även att behöva köpa", VG_Korvar, 
"paket med veganska korvar och det kommer att kosta", round(VG_Pris,2), "kr. Sist kommer du behöva köpa", dricka, "drickor och det kommer att kosta",round(D_Pris,2), "kr."
"Totalt kommer det att kosta",round(Pris,2),"kr."   #round avrundar talet
)
