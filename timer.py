import time

def countdown(minutes, label):
    total_seconds = minutes * 60
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = f"{label} ⏱️ {mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print(f"\n✅ {label} session completed!\n")

def pomodoro_timer():
    work_minutes = 25
    break_minutes = 5
    sessions = int(input("🔁 How many Pomodoro sessions do you want to run? "))

    for i in range(1, sessions + 1):
        print(f"\n🍅 Pomodoro Session {i}")
        countdown(work_minutes, "Work")
        if i != sessions:
            countdown(break_minutes, "Break")
        else:
            print("🎉 All sessions completed! Great job!")

pomodoro_timer()
