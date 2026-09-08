import datetime
import time
import pygame

def set_alarm(alarm_time):
    print(f"alarm set for {alarm_time}")
    sound_alarm = "14. alarm clock/my_alarm.mp3"

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Wake Up!!!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_alarm)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            break
        
        time.sleep(1)
        

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time: (HH:MM:SS): ")
    set_alarm(alarm_time)