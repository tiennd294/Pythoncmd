#texttospeech
import pyttsx3
engine = pyttsx3.init()
engine.say("hôm nay là thứ 3")
engine.runAndWait()

# from time import sleep
# _a = "Anh ko biet bao nhieu sao tren troi"
# for x in _a:
# 	print(x , end='', flush=True)
# 	sleep(0.1)
# print()

"""_c = 9
_d = 6
if _c < 9:
	print("demo")
else:print("NG")"""

'''for x in [1,10,6,9,4,6]:
	print(x)'''
'''print("demo") ;print("OK")'''

'''def test(_a,_b="demo"):
	print(_a+_b)
test("admin",_b="pro3")'''

'''for x in range(10):
	print(x)'''
#Ctrl+B


# import pandas as pd
# import matplotlib.pyplot as plt
# data = pd.read_csv('Advertising.csv',header = None)
# X = data.values[:,2]
# Y = data.values[:,4]
# plt.scatter(X,Y,marker='o')
# plt.show()

Các chế độ mở tệp khác nhau là
r - mở một tập tin để đọc. (mặc định)

w - Mở tệp để ghi. Nếu tệp đã tồn tại, dữ liệu của nó sẽ bị xóa trước khi mở. Nếu không, tệp mới sẽ được tạo

x - mở để tạo độc quyền, không thành công nếu tệp đã tồn tại

a - mở để ghi, nối vào cuối tệp nếu nó tồn tại

b - chế độ nhị phân

t - chế độ văn bản (mặc định)

+ r - Mở tệp để cập nhật (đọc và ghi)
tệp văn bản có thể được mở ở bất kỳ một trong các chế độ đã nói ở trên bằng cách chỉ định tùy chọn "t" cùng với "r", "w", "rw" và "a",
để các chế độ trước trở thành "rt", " wt "," rwt "và" at ". Một tệp nhị phân có thể được mở ở bất kỳ một trong các chế độ
đã nói ở trên bằng cách chỉ định tùy chọn "b" cùng với "r", "w", "rw" và "a" 
để các chế độ trước đó trở thành "rb", " wb "," rwb "," ab ".


Mode	Mô tả
r	Mở file chỉ để đọc
r+	Mở file để đọc và ghi
rb	Mở file trong chế độ đọc cho định dạng nhị phân, đây là chế độ mặc định. Con trỏ tại phần bắt đầu của file
rb+	Mở file để đọc và ghi trong định dạng nhị phân. Con trỏ tại phần bắt đầu của file
w	Tạo một file mới để ghi, nếu file đã tồn tại thì sẽ bị ghi mới
w+	Tạo một file mới để đọc và ghi, nếu file tồn tại thì sẽ bị ghi mới
wb	Mở file trong chế độ ghi trong định dạng nhị phân. Nếu file đã tồn tại, thì ghi đè nội dung của file đó, nếu không thì tạo một file mới
wb+	Mở file để đọc và ghi trong định dạng nhị phân. Nếu file tồn tại thì ghi đè nội dung của nó, nếu file không tồn tại thì tạo một file mới để đọc và ghi
a	Mở file để ghi thêm vào cuối file, nếu không tìm thấy file sẽ tạo mới một file để ghi mới
a+	Mở file để đọc và ghi thêm vào cuối file, nếu không tìm thấy file sẽ tạo mới một file để đọc và ghi mới
ab	Mở file trong chế độ append trong chế độ nhị phân. Con trỏ là ở cuối file nếu file này đã tồn tại. Nếu file không tồn tại, thì tạo một file mới để ghi
ab+	Mở file trong để đọc và append trong định dạng nhị phân. Con trỏ file tại cuối nếu file đã tồn tại. Nếu không tồn tại thì tạo một file mới để đọc và ghi