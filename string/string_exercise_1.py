word = "Python is one of the fastest-growing programming languages"
#จงเขียนคำสั่งเพื่อแสดงความยาวของตัวอักษร "Python is one of the fastest-growing programming languages"
print(len(word))
#จงเขียนคำสั่งเพื่อแสดงอักษรแรกของข้อความ "Python is one of the fastest-growing programming languages"
print(word[0])
#จงเขียนคำสั่งเพื่อแสดง "fastest" ของข้อความ "Python is one of the fastest-growing programming languages"
print(word[21:28])
#จงเขียนคำสั่งเพื่อแสดข้อความ "Python is one of the fastest-growing programming languages" ที่ไม่มี space
print(word.strip())
#จงเขียนคำสั่งเพื่อแสดข้อความ "Python is one of the fastest-growing programming languages" ให้เป็นตัวพิมใหญ่ทั้งหมด
print(word.upper())
#จงเขียนคำสั่งเพื่อแสดข้อความ "Python is one of the fastest-growing programming languages" ให้เป็นตัวพิมเล็กทั้งหมด
print(word.lower())
#จงเขียนคำสั่งเพื่อแสดข้อความ "Python is one of the fastest-growing programming languages" ที่ถูกแทนที่อักษร r ด้วย x ทั้งหมด
print(word.replace("r", "x"))
#จงเติมคำในช่องว่าเพื่อแสดงอายุ
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))