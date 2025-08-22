# นำเข้าไลบรารีที่จำเป็น
from microbit import *
import music
import utime
import random

# --- การตั้งค่าความเร็ว WPM ---
WPM = 8
# ----> ค่าความแรงในการเขย่าเพื่อสลับโหมด ปุ่ม/เชื่อมต่อคันเคาะ <----
SHAKE_THRESHOLD = 3500

DIT_PIN = pin1
DAH_PIN = pin2
SPEAKER_PIN = pin0
# ----> คำนวณระยะเวลาของทุกอย่าง โดยอ้างอิงจากค่า WPM
def calculate_timings(current_wpm):
    dot = int(1200 / current_wpm)
    dash = 3 * dot
    letter_gap = 3 * dot
    answer_submit_gap = 5 * dot 
    return dot, dash, letter_gap, answer_submit_gap

DOT_LENGTH, DASH_LENGTH, INTER_LETTER_GAP, ANSWER_SUBMIT_GAP = calculate_timings(WPM)
# ----> รหัสมอร์สที่โปรแกรมสามารถเล่นได้
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9', '..--..': '?', '-..-.': '/'
}

REVERSE_MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}
CHARACTER_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?/"

def play_morse_sequence(sequence):
    for symbol in sequence:
        duration = DOT_LENGTH if symbol == '.' else DASH_LENGTH
        music.pitch(700, -1, pin=SPEAKER_PIN, wait=False)
        sleep(duration)
        music.stop()
        sleep(DOT_LENGTH)

# --- ตัวแปรสำหรับจัดการสถานะและเกม ---
current_sequence = ""
last_event_time = utime.ticks_ms()
paddle_mode_enabled = False
game_state = "GENERATE_QUESTION"
correct_answer_char = ""

# --- โปรแกรมหลัก ---
display.show(Image.TARGET)

while True:
    current_time = utime.ticks_ms()

    # ---->เข้า/ออกโหมดตั้งค่า WPM <----
    if button_a.is_pressed() and button_b.is_pressed():
        if game_state == "SETTINGS":
            # ออกจากโหมดตั้งค่า
            game_state = "GENERATE_QUESTION"
            display.show(Image.HEART) # แสดงรูปหัวใจ
            sleep(500)
            # กลับไปแสดงไอคอนโหมด Input ปัจจุบัน
            display.show(Image.SQUARE_SMALL if paddle_mode_enabled else Image.TARGET)
        else:
            # เข้าสู่โหมดตั้งค่า
            game_state = "SETTINGS"
            display.show(Image.HEART) # แสดงรูปหัวใจ
            sleep(500)
        sleep(500)
        continue

    # --- ส่วนหลักของโปรแกรมที่ทำงานตามสถานะ ---
    if game_state == "GENERATE_QUESTION":
        display.show("?")
        sleep(1000)
        correct_answer_char = random.choice(CHARACTER_SET)
        morse_to_play = REVERSE_MORSE_DICT[correct_answer_char]
        play_morse_sequence(morse_to_play)
        last_event_time = utime.ticks_ms()
        game_state = "WAIT_FOR_ANSWER"

    elif game_state == "WAIT_FOR_ANSWER":
        accel_x, accel_y, accel_z = accelerometer.get_values()
        total_force_squared = accel_x**2 + accel_y**2 + accel_z**2
        if total_force_squared > SHAKE_THRESHOLD**2:
            paddle_mode_enabled = not paddle_mode_enabled
            display.show(Image.SQUARE_SMALL if paddle_mode_enabled else Image.TARGET)
            sleep(500)

       
        dit_event, dah_event = False, False
        if paddle_mode_enabled:
            if DIT_PIN.is_touched(): dit_event = True
            elif DAH_PIN.is_touched(): dah_event = True
        else:
            if button_a.was_pressed(): dit_event = True
            elif button_b.was_pressed(): dah_event = True

        if dit_event or dah_event:
            duration = DOT_LENGTH if dit_event else DASH_LENGTH
            symbol = "." if dit_event else "-"
            music.pitch(700, -1, pin=SPEAKER_PIN, wait=False)
            sleep(duration)
            music.stop()
            current_sequence += symbol
            last_event_time = current_time
            if paddle_mode_enabled: sleep(50)
        else:
            time_since_last_event = utime.ticks_diff(current_time, last_event_time)
            if current_sequence != "" and time_since_last_event > ANSWER_SUBMIT_GAP:
                player_answer_char = MORSE_CODE_DICT.get(current_sequence, "!")
                if player_answer_char == correct_answer_char:
                    display.show(Image.YES)
                else:
                    display.show(Image.NO)
                sleep(1000)
                display.scroll(correct_answer_char)
                current_sequence = ""
                game_state = "GENERATE_QUESTION"

    elif game_state == "SETTINGS":
        tilt_x = accelerometer.get_x()
        if tilt_x > 300 or tilt_x < -300:
            if tilt_x > 300: WPM += 1
            else: WPM -= 1
            if WPM < 5: WPM = 5
            DOT_LENGTH, DASH_LENGTH, INTER_LETTER_GAP, ANSWER_SUBMIT_GAP = calculate_timings(WPM)
            display.scroll("WPM:" + str(WPM), delay=80)
            sleep(300)