s = input("Nhập chuỗi: ")
k  = t = 0
for e in "TRẺTRÂU":
	k = s.find(e, k) + 1
	if k == 0:
		break
else: t = 1
print("Answer:", ("Không TRẺ TRÂU", "TRẺ TRÂU")[t])