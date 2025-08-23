# CW-trainer
Morse code trainer project Micro:Bit , Raspberry Pi pico

-------------------------------------------------------------------------
## Micro:Bit ## ----> Microbit/MBit-morse-game .py
-------------------------------------------------------------------------
 "เกมทายรหัสมอร์ส"  
     (แนะนำให้ใช้งานกับ Micro:Bit V.2 ขึ้นไป) ขอให้สนุกกับเกมนะครับ!
      
      ### ## กติกาการเล่น 🎯
      เป้าหมายของเกมคือ **การฟังเสียงรหัสมอร์สและทายให้ถูกว่าเป็นตัวอักษรหรือตัวเลขอะไร**
      
      1.  **ฟังโจทย์:** เมื่อเกมเริ่ม หน้าจอจะแสดงเครื่องหมาย **?** จากนั้นโปรแกรมจะเล่นเสียงรหัสมอร์สของตัวอักษรปริศนา 1 ตัว
      2.  **ตอบคำถาม:** ให้คุณเคาะรหัสมอร์สที่คุณได้ยินโดยใช้วิธีการป้อนข้อมูล (Input) ที่เลือกไว้ (ดูในหัวข้อถัดไป)
      3.  **ตรวจคำตอบ:** เมื่อคุณเคาะจบ 1 ตัวอักษร (โดยการเว้นจังหวะเล็กน้อย) โปรแกรมจะตรวจคำตอบ
          * **ถ้าถูก:** หน้าจอจะแสดงเครื่องหมาย **✓**
          * **ถ้าผิด:** หน้าจอจะแสดงเครื่องหมาย **X**
      4.  **ดูเฉลย:** ไม่ว่าจะตอบถูกหรือผิด โปรแกรมจะเลื่อนแสดงตัวอักษรที่ถูกต้องบนหน้าจอเสมอ เพื่อเป็นการยืนยันและทบทวน
      5.  **เริ่มรอบใหม่:** หลังจากเฉลยจบ เกมจะเริ่มเล่นโจทย์ข้อต่อไปโดยอัตโนมัติ
      
      ---
      ### ## การควบคุมพื้นฐาน (การตอบคำถาม)
      คุณสามารถเลือกวิธีการป้อนข้อมูลได้ 2 โหมด โดยสลับโหมดได้ด้วยการ **เขย่าบอร์ด**
      
      #### **โหมดที่ 1: ใช้ปุ่มบนบอร์ด (ค่าเริ่มต้น)**
      * **สัญลักษณ์โหมด:** รูปเป้า (🎯) `Image.TARGET`
      * **การควบคุม:**
          * กด **ปุ่ม A** = Dit (เสียงสั้น)
          * กด **ปุ่ม B** = Dah (เสียงยาว)
      
      #### **โหมดที่ 2: ใช้ Key ภายนอก**
      * **สัญลักษณ์โหมด:** รูปสี่เหลี่ยมเล็ก (⏹️) `Image.SQUARE_SMALL`
      * **การควบคุม:**
          * เคาะ **Dit** (ที่ต่อกับ P1) = Dit
          * เคาะ **Dah** (ที่ต่อกับ P2) = Dah
      
      ---
      ### ## การตั้งค่าขั้นสูง
      
      #### **การสลับโหมด Input (เขย่าบอร์ด)**
      * หากต้องการสลับระหว่าง "โหมดปุ่ม" และ "โหมด Key" ให้ **เขย่าบอร์ดแรงๆ** (ค่าความแรงตั้งไว้ที่ 3500) หน้าจอจะแสดงสัญลักษณ์ของโหมดใหม่ที่คุณเพิ่งสลับไป
      
      #### **การปรับความเร็ว (WPM Settings Mode)**
      หากรู้สึกว่าเสียงโจทย์เร็วหรือช้าไป คุณสามารถปรับได้ตลอดเวลา
      1.  **เข้าสู่โหมดตั้งค่า:** กด **ปุ่ม A และ B พร้อมกัน**
          * เกมจะหยุดชั่วคราว และหน้าจอจะแสดง **รูปหัวใจ ❤️** เพื่อยืนยันว่าคุณได้เข้าสู่โหมดตั้งค่าแล้ว
      2.  **ปรับความเร็ว:**
          * **เอียงบอร์ดไปทางขวา** เพื่อ **เพิ่ม** WPM (เร็วขึ้น)
          * **เอียงบอร์ดไปทางซ้าย** เพื่อ **ลด** WPM (ช้าลง)
          * หน้าจอจะเลื่อนแสดงค่า WPM ใหม่ทุกครั้งที่มีการปรับ
      3.  **ออกจากโหมดตั้งค่า:** กด **ปุ่ม A และ B พร้อมกันอีกครั้ง**
          * หน้าจอจะแสดง **รูปหัวใจ ❤️** อีกครั้ง และโปรแกรมจะกลับไปเริ่มเกมรอบใหม่ด้วยความเร็วที่คุณเพิ่งตั้งค่าไว้
      
      ---
      ### ## การเชื่อมต่อ Key (ถ้ามี) 🔌
      หากคุณต้องการเล่นใน "โหมด Key" ให้เชื่อมต่ออุปกรณ์ดังนี้:
      
      * **สาย Dit:** ต่อเข้าที่ **Pin 1** และ **GND**
      * **สาย Dah:** ต่อเข้าที่ **Pin 2** และ **GND**
      * **ลำโพง:** ต่อเข้าที่ **Pin 0** และ **GND**
    -------------------------------------------------------------------------
## **User Guide & Rules: Morse Code Guessing Game**

  ### **Game Rules** 🎯
  The objective is to **listen to a Morse code sound and correctly guess the corresponding letter or number**.

    1.  **Listen for the Clue:** When a round starts, the screen will show a **?** symbol. The program will then play the Morse code sound for a random, secret character.
    2.  **Enter Your Answer:** Key in the Morse code you heard using your selected input method (onboard buttons or an external key).
    3.  **Check the Result:** After you finish keying in the character (by pausing briefly), the program will check your answer. A **✓** will appear for a correct answer, and an **X** will appear for an incorrect one.
    4.  **See the Answer:** Whether you were right or wrong, the game will always scroll the correct character across the screen to confirm the answer and help you learn.
    5.  **New Round:** After the answer is shown, the game will automatically start the next round.
    
    ---
    ### **Basic Controls (Answering)**
    You can choose between two input modes. Switch between them by **shaking the board**.
    
    #### **Mode 1: Onboard Buttons (Default)**
    * **Mode Icon:** Target (🎯) `Image.TARGET`
    * **Controls:**
        * Press **Button A** for Dit (short sound).
        * Press **Button B** for Dah (long sound).
    
    #### **Mode 2: External  Key**
    * **Mode Icon:** Small Square (⏹️) `Image.SQUARE_SMALL`
    * **Controls:**
        * Use the **Dit ** (connected to P1) for Dit.
        * Use the **Dah ** (connected to P2) for Dah.
    
    ---
    ### **Advanced Settings**
    
    #### **Switching Input Modes (Shake the Board)**
    To switch between "Button Mode" and " Key Mode," give the board a **firm shake**. The screen will display the icon for the new, active mode.
    
    #### **Adjusting Speed (WPM Settings Mode)**
    If the Morse code sounds are too fast or too slow, you can adjust the speed at any time.
    
    1.  **Enter Settings Mode:** Press **buttons A and B simultaneously**. The game will pause, and a **heart icon ❤️** will appear to confirm you are in settings mode.
    2.  **Adjust Speed:**
        * **Tilt the board right** to **increase** the WPM (faster).
        * **Tilt the board left** to **decrease** the WPM (slower).
        * The screen will scroll the new WPM value with each adjustment.
    3.  **Exit Settings Mode:** Press **buttons A and B simultaneously** again. A **heart icon ❤️** will appear, and the program will start a new game round with your newly set speed.
    
    ---
    ### **Connecting a Key (Optional)** 🔌
    If you wish to play in "Key Mode," connect your hardware as follows:
    
    * **Dit Cable:** Connect one wire to **Pin 1** and the other to **GND**.
    * **Dah Cable:** Connect one wire to **Pin 2** and the other to **GND**.
    * **Speaker:** Connect one wire to **Pin 0** and the other to **GND**.
    
    Enjoy the game!
-------------------------------------------------------------------------
