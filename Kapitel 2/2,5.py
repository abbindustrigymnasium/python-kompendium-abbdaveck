print("Hur många vill äta 2 vanliga korvar?")
två_vk = input()
print("Hur många vill äta 3 vanliga korvar?")
tre_vk = input()
print("Hur många vill äta 2 veganska korvar?")
två_vgk = input()
print("Hur många vill äta 3 veganska korvar?")
tre_vgk = input()
mEtt = int(två_vk)+int(tre_vk)
mTvå = mEtt/8
mTre = int(mTvå)
if mTvå == mTre:
    V_Pris= int(mTre)*20.95
    V_Korvar = int(mTre)
elif mTvå > mTre:
    V_Pris= int(mTvå+1)*20.95
    V_Korvar = int(mTvå+1)
#print(V_Korvar)
mFyra = int(två_vgk)+int(tre_vgk)
mFem = mFyra/8
mSex = int(mFem)
if mFem == mSex:
    VG_Pris = int(mSex)*34.95
elif mFem > mSex:
    VG_Pris = int(mFem+1)*34.95
Pris = V_Pris+VG_Pris
#print("Du kommer behöva köpa", V_Korvar, "och det kommer att kosta", V_Pris,"kr.")
#totala_vk = int(lall)
#print(mTre)
#print("Du behöver skaffa",int(två_vk)+int(tre_vk)+int(två_vgk)+int(tre_vgk),"korvar.")