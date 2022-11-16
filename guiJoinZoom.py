from tkinter import *
import time
from datetime import datetime
import pyautogui as auto
from tkinter import messagebox

timer = int()
first_timer = str()

window = Tk()
window.geometry('1920x1080')

main_label = Label(window, text='Zoom 2022', font=('arial', 30, 'bold')).pack()
main_subjects_label = Label(window, text='Main Subjects', font=('arial', 20), relief=RAISED, bd=5).pack()
main_subjects = Frame(window, bg='gold', relief=RAISED, bd=5)
main_subjects.pack()
subject = StringVar()
subject.set('None')


# --------------------------------------------------------------------------------------------------

def chinese():
    global subject
    subject.set('bc')


def bahasa():
    global subject
    subject.set('bm')


def english():
    global subject
    subject.set('eng')


def math():
    global subject
    subject.set('math')


def science():
    global subject
    subject.set('sci')


def geography():
    global subject
    subject.set('geo')


def history():
    global subject
    subject.set('his')


def art():
    global subject
    subject.set('art')


def computer():
    global subject
    subject.set('computer')


def sejarah():
    global subject
    subject.set('sej')


def moral():
    global subject
    subject.set('moral')


def steam():
    global subject
    subject.set('steam')


def british():
    global subject
    subject.set('british')


def chess():
    global subject
    subject.set('chess')


def badminton():
    global subject
    subject.set('bad')


def chesstuition():
    global subject
    subject.set('ct')
def physical():
    global subject
    subject.set('pe')

def telebort():
    global subject
    subject.set('telebort')
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
chinese = Button(main_subjects, text='Chinese', bg='grey', fg='black', width=10, height=5, command=chinese).pack(
    side=LEFT)
bahasa = Button(main_subjects, text='Bahasa', bg='grey', fg='black', width=10, height=5, command=bahasa).pack(side=LEFT)
english = Button(main_subjects, text='English', bg='grey', fg='black', width=10, height=5, command=english).pack(
    side=LEFT)
science = Button(main_subjects, text='Science', bg='grey', fg='black', width=10, height=5, command=science).pack(
    side=LEFT)
math = Button(main_subjects, text='Math', bg='grey', fg='black', width=10, height=5, command=math).pack(side=LEFT)
geography = Button(main_subjects, text='Geography', bg='grey', fg='black', width=10, height=5, command=geography).pack(
    side=LEFT)
history = Button(main_subjects, text='History', bg='grey', fg='black', width=10, height=5, command=history).pack(
    side=LEFT)
# --------------------------------------------------------------------------------------------------

side_subjects_label = Label(window, text='Side Subjects', font=('arial', 20), relief=RAISED, bd=5).pack()
side_subjects = Frame(window, bg='gold', relief=RAISED, bd=5)

# --------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------

art = Button(side_subjects, text='Art', bg='grey', fg='black', width=10, height=5, command=art).pack(side=LEFT)
pe = Button(side_subjects, text='PE', bg='grey', fg='black', width=10, height=5, command=physical).pack(side=LEFT)
computer = Button(side_subjects, text='Computer', bg='grey', fg='black', width=10, height=5, command=computer).pack(
    side=LEFT)
sejarah = Button(side_subjects, text='Sejarah', bg='grey', fg='black', width=10, height=5, command=sejarah).pack(
    side=LEFT)
moral = Button(side_subjects, text='Moral', bg='grey', fg='black', width=10, height=5, command=moral).pack(side=LEFT)
steam = Button(side_subjects, text='Steam', bg='grey', fg='black', width=10, height=5, command=steam).pack(side=LEFT)
british = Button(side_subjects, text='British', bg='grey', fg='black', width=10, height=5, command=british).pack(
    side=LEFT)

side_subjects.pack()

# --------------------------------------------------------------------------------------------------

co_curriculum_label = Label(window, text='Co-Curriculum and Tuition', font=('arial', 20), relief=RAISED, bd=5).pack()
co_curriculum = Frame(window, bg='gold', relief=RAISED, bd=5)

# --------------------------------------------------------------------------------------------------

chess = Button(co_curriculum, text='Han Chiang Chess Club', bg='grey', fg='black', width=20, height=5,
               command=chess).pack(side=LEFT)
badminton = Button(co_curriculum, text='Badminton Club', bg='grey', fg='black', width=15, height=5,
                   command=badminton).pack(side=LEFT)
chess_tuition = Button(co_curriculum, text='Chess tuition', bg='grey', fg='black', width=10, height=5,
                       command=chesstuition).pack(side=LEFT)
Button(co_curriculum, text='Telebort Data Analysis Class', bg='grey', fg='black', width=30, height=5,
                       command=telebort).pack(side=LEFT)

co_curriculum.pack()

num = IntVar()

timer_label = Label(window, text='How many minutes would you like to delay? ', font=('arial', 30), relief=RAISED, bd=10,
                    fg='green', bg='black').pack()
timer_scale = Scale(window, orient=HORIZONTAL, from_=0, to=60, length=300, width=25, tickinterval=10,
                    font=('cosmic sans', 10), troughcolor='light blue', variable=num)
timer_scale.set(0)
timer_scale.pack()

now = str(datetime.now())
current_time = now[11:19]
hour = str(current_time[0:2])
minutes = int(current_time[3:5])
seconds = current_time[6:]

hehehe = Label(window, text=f'Joining {hour}:{minutes}:{seconds} ', font=('arial', 10, 'bold'))
hehehe.pack()


def doSomething(var, indx, mode):
    now = str(datetime.now())
    current_time = now[11:19]
    hour = str(current_time[0:2])
    minutes = int(current_time[3:5])
    seconds = current_time[6:]
    minutes += num.get()

    if minutes > 59:
        minutes -= 60
        hour = int(hour)
        hour += 1
        if minutes < 10:
            hehehe.config(text=f'Joining {hour}:0{str(minutes)}:{seconds} ')
        else:
            hehehe.config(text=f'Joining {hour}:{str(minutes)}:{seconds}')


    else:
        if minutes < 10:
            hehehe.config(text=f'Joining {hour}:{str(minutes)}:{seconds}')

        else:
            hehehe.config(text=f'Joining {hour}:{str(minutes)}:{seconds}')


num.trace('w', doSomething)

current_selected_subject = Label(window,
                                 textvariable=subject).pack()  # Need to edit this to show "You have currently selected"
timer = int()


def go_join_class():
    global first_timer
    global timer
    global first_subject
    global subject
    first_timer = timer_scale.get()
    timer = first_timer

    first_subject = subject.get()
    subject = first_subject

    window.destroy()


go = Button(window, font=('comic sans', 15), relief=RAISED, bd=10, text='Start', bg='light green',
            command=go_join_class)

go.pack()

window.mainloop()

print(f'You chose : {subject}')

def time_to_join():
    now = str(datetime.now())
    current_time = now[11:19]
    hour = str(current_time[0:2])
    minutes = int(current_time[3:5])
    seconds = current_time[6:]
    minutes += timer

    if minutes > 59:
        minutes -= 60
        hour = int(hour)
        hour += 1

        if minutes < 10:
            print(f'Joining {hour}:0{str(minutes)}:{seconds} ')
        else:
            print(f'Joining {hour}:{str(minutes)}:{seconds}')
    else:

        if minutes < 10:
            print(f'Joining {hour}:0{str(minutes)}:{seconds} ')
        else:
            print(f'Joining {hour}:{str(minutes)}:{seconds}')


def join_class(id, password):
    auto.keyDown('win')
    auto.press('d')
    auto.keyUp('win')
    time.sleep(1)
    auto.rightClick(x=1840, y=892)
    time.sleep(5)
    auto.rightClick(974, 525, duration=0.5)
    time.sleep(4)
    auto.rightClick(x=856, y=473, duration=1)
    auto.write(str(id))
    auto.rightClick(x=974, y=775, duration=1)
    auto.rightClick(x=819, y=469, duration=4)
    auto.write(str(password))
    auto.rightClick(x=980, y=772, duration=1)


time_to_join()
if timer == 0:
    pass


elif timer > 0:
    print("Waiting...")
    for i in range(timer, 1 - 1, -1):
        if i == 1:
            print(f"{i} Minute left")
        else:
            print(f"{i} Minutes left")

        time.sleep(60)

    print('Done!')

if subject == 'bc':
    join_class('349 956 1370', '123456')

elif subject == "bm":
    join_class("894-137-5132", "Liew5331")

elif subject == 'math':
    join_class('981 426 3458', 'Math426')

elif subject == 'eng':
    join_class('565 565 1581', '25894')

elif subject == 'his':
    join_class("564-542-3013","682925")

elif subject == 'sci':
    join_class("630-395-2333","559030")

elif subject == 'art':
    join_class("330-775-8164","538967")

elif subject == 'geo':
    join_class("916-006-4844","84788")

elif subject == 'computer':
    join_class('654 617 9745', '150407')

elif subject == 'sej':
    join_class("208-983-0853","BC123456")

elif subject == 'moral':
    join_class('509 660 7976', '888999')

elif subject == 'steam':
    join_class("86944892680","HCSTEAM")

elif subject == 'british':
    join_class('898 8459 9957', 'HEed!7')

elif subject == 'bad':
    join_class('5185397946', '259146')

elif subject == 'chess':
    join_class('86905222436', '366447')

elif subject == "ct":
    join_class('772 7093 7386', 'chess2')
elif subject == 'pe':
    join_class('797-312-9568', '860364')
elif subject == 'telebort':
    join_class('817 6452 0485','838389')
else:
    messagebox.showerror(title='ERROR', message="Subject doesn't exist/you didn't choose a subject. Try again. ")
#TODO: Add a function where you can input a id and password and it will join for you
