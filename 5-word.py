import webbrowser

def find_word_in_video(word):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    word = word.lower().strip()
    
    if len(word) != 5 or not all(c in alphabet for c in word):
        return None
    
    word_index = 0
    for i, char in enumerate(word):
        char_value = alphabet.index(char)
        power = 4 - i
        word_index += char_value * (33 ** power)
        
    total_seconds = int(word_index // 100)
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    position_on_screen = word_index % 100
    row = (position_on_screen // 10) + 1
    col = (position_on_screen % 10) + 1
    
    domain = "https://youtube.com"
    video_path = "/watch?v=0I2-yqFVmIg"
    time_param = f"&t={total_seconds}s"
    
    video_url = domain + video_path + time_param
    
    return time_str, row, col, video_url

print("=== СУПЕР-КАЛЬКУЛЯТОР ТАЙМКОДОВ ДЛЯ МЕМНОГО ВИДЕО ===")
print("Вводите любые 5-буквенные слова на русском.")
print("После расчета нужный момент автоматически откроется в браузере!")
print("Чтобы закрыть программу, просто нажмите ENTER, оставив поле пустым.\n")

while True:
    user_input = input("Введите слово из 5 букв: ").strip()
    
    if not user_input:
        break
        
    result = find_word_in_video(user_input)
    
    if result is None:
        print("❌ Ошибка: нужно ввести ровно 5 РУССКИХ букв! Попробуйте еще раз.\n")
    else:
        time_str, row, col, video_url = result
        print(f"⏱  Таймкод: {time_str}")
        print(f"📍  Позиция: строка {row}, столбец {col}")
        print(f"🔗  Ссылка на YouTube: {video_url}")
        print("🚀 Открываю браузер...")
        print("-" * 40 + "\n")
        
        webbrowser.open(video_url)
