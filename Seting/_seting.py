python -V

python -m pip install --upgrade pip

pip install pydub

# import os,sys
# from os import path
# from pydub import AudioSegment                                                                     
# src = sys.path[0] + "\\TestAudio\\CuTheRoiXa_Yentatoo.mp3"
# dst = src.replace(".mp3",".wav")                                                       
# sound = AudioSegment.from_mp3(src)
# sound.export(dst, format="wav")
# print("Convert Successfuly!")

pip install pyttsx3
# //Text to speech English
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("hôm nay là thứ 3")
# engine.runAndWait()

pip install speechrecognition

# import speech_recognition as sr
# from os import path
# AUDIO_FILE = "transcript.wav"                                     
# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#         audio = r.record(source)                
#         print("Transcription: " + r.recognize_google(audio))

pip install gTTS

# tts = gTTS("phat am thanh nay ra file mp3", 'vi')
# tts.save("file.mp3")

-m pip install PyAudio

# import playsound
# playsound.playsound('output.mp3', True)

pip install subprocess.run

pip install mpg123

# import os
# os.system("mpg123 " + "file.mp3")

pip install mpyg321 #False

# from mpyg321.mpyg321 import MPyg321Player()
# player = MPyg321Player()
# player.play_song("/path/to/some_mp3.mp3")

pip install playsound

# from playsound import playsound
# playsound('/path/to/a/sound/file/you/want/to/play.mp3')


pip install tensorflow

# python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

pip install numpy
# Được tạo bởi Travis Oliphant, NumPy là một “ngựa kéo” phân tích thực sự của Python. Nó cung cấp cho người dùng cách làm việc với các mảng nhiều chiều, cùng một số lượng lớn các hàm để xử lý trên các toán tử toán học nhiều chiều trên các mảng đó. Mảng là các khối dữ liệu được sắp xếp theo nhiều chiều dựa trên các véc tơ và ma trận trong toán học. Mảng thường hữu ích không chỉ trong việc lưu dữ liệu mà cả việc tính toán nhanh các ma trận, điều không thể thiếu khi giải quyết các vấn đề liên quan đến khoa học dữ liệu.
pip install scipy
# Là một dự án gốc bởi Travis Oliphant, Pearu Peterson, and Eric Jones, SciPy hoàn thiện các tính năng của NumPy, nhằm cung cấp các thuật toán cho đại số tuyến tính, không gian ma trận, xử lý tín hiệu và xử lý ảnh, tối ưu, biến đổi Fourier,…
pip install pandas
# pandas là thư viện thực hiện mọi thứ mà NymPy và SciPy không thể làm. Nó làm việc với các đối tượng cấu trúc dữ liệu, DataFrames và Chuỗi (Series). pandas cho phép bạn có thể xử lý các bảng dữ liệu phức tạp của nhiều loại khác nhau (điều mà các mảng của NumPy thông thể làm được) và chuỗi thời gian. Bạn sẽ dễ dàng tải dữ liệu từ nhiều nguồn khác nhau, sau đó slide, dice, xử lý các thành phần còn thiếu, thêm, đổi tên, tổng hợp (aggregate), reshape và cuối cùng là trực quan dữ liệu theo ý của bạn.
pip install scikit-learn
# Bắt đầu như một phần của SciKits, Scikit-learn là lõi hoạt động của khoa học dữ liệu trên Python. Nó cung cấp tất cả những gì bạn cần để tiền xử lý dữ liệu, học giám sát và không giám sát, lựa chọn mô hình, validate và error metrics.
pip install "ipython[notebook]"
# Một cách tiếp cận khoa học yêu cầu thử nghiệm nhanh các giả thuyết khác nhau trong một khoảng thời gian. IPython được tạo bởi Fernando Perez để giải quyết việc cần thiết một lệnh Shell Python (dựa trên shell, trình duyệt web, và giao diện ứng dụng) với đồ họa tích hợp, các lệnh có thể tùy chỉnh, lịch sử phong phú (dưới định dạng JSON) và khả năng tính toán song song để cải thiện hiểu năng tính toán.
pip install matplotlib
# Được phát triển bởi John Hunte, matplotlib là một thư viện xây dựng các khối cần thiết để tạo các biểu đồ chất lượng từ mảng và trực quan và tương tác với chúng.

pip install pillow
pip install matplotlib

pip install opencv-python 

ImageAI
pip install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.1/imageai-2.0.1-py3-none-any.whl
