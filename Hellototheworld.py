import random
import time

money,energy,income,brain_cell,work_energy= 0,0,0,0,0
mainloop,gain_brain_cell = 1,1
job = ""
job_id = ["0","1","2","3","4","999"]
max_energy = 100

#important comment
# ● ┌ ─ ┐ │ └ ┘ 

def start():
    while (len(name := input("Enter your name[must be 3 character or more]: "))) < 3:
        print()
    print(f"hi {name},")
    print("┌─────────────────────────────────────────────────┐")
    print("│ Welcome to the world! Say hello world!          │")
    print("│ This is a game of hello to the world            │")
    print("│ Type /command to check out what command we have │")
    print("└─────────────────────────────────────────────────┘")

def command():
    print("Here is a list of commands")
    print("┌─────────────────────────────────────────────────┐")
    print("│ /command to find out what are all the commands  │")
    print("│ /work to work for money                         │")
    print("│ /sleep to sleep and gain energy                 │")
    print("│ /study to study and gain brain cells            │")
    print("│ /stop to stop playing the game                  │")
    print("└─────────────────────────────────────────────────┘")

def work():
    global money,income,energy
    if job == "":
        print("get a job with /joblist")
        return
    elif energy < work_energy:
        return
    else:
        energy -= work_energy
        money += income
        print(f"You work as a {job}")
        print(f"You earned {income} dollar")
        print(f"You now have {money}$")

def joblist():
    print("Here is a list of jobs")
    print("┌─────────────────────────────────────────────────┐")
    print("│ Quit the job[id: 0]                             │")
    print("│ Farmer[id: 1]                                   │")
    print("│ Miner[id: 2]                                    │")
    print("│ Engineer[id: 3]                                 │")
    print("│ Scientist[id: 4]                                │")
    print("│ /jobchoose to choose the job                    │")
    print("└─────────────────────────────────────────────────┘")

def jobchoose():
    global job,job_id,income,work_energy
    while (job_choice := input("Enter the job id to get a job[Enter 999 to exit]: ")) not in job_id:
        print("Invalid id")
    if job_choice == "999":
        pass
    elif job_choice == "0":
        job = ""
        print("Job quited")
    elif job_choice == "1":
        job = "farmer"
        income = 20
        work_energy = 50
        print(f"You work as a {job}")
        print("┌─────────────────────────────────────────────────┐")
        print("│ Salary: 20$                                     │")
        print("│ Energy: 50                                      │")
        print("│ Brain cells required: 0                         │")
        print("│ Desc: Potato farming                            │")
        print("└─────────────────────────────────────────────────┘")
    elif job_choice == "2":
        if brain_cell < 1:
            print("You have not enough brain cells")
            return
        job = "miner"
        income = 40
        work_energy = 70
        print(f"You work as a {job}")
        print("┌─────────────────────────────────────────────────┐")
        print("│ Salary: 40$                                     │")
        print("│ Energy: 70                                      │")
        print("│ Brain cells required: 1                         │")
        print("│ Desc: Trying to get diamond                     │")
        print("└─────────────────────────────────────────────────┘")
    elif job_choice == "3":
        if brain_cell < 20:
            print("You have not enough brain cells")
            return
        job = "engineer"
        income = 100
        work_energy = 50
        print(f"You work as a {job}")
        print("┌─────────────────────────────────────────────────┐")
        print("│ Salary: 100$                                    │")
        print("│ Energy: 50                                      │")
        print("│ Brain cells required: 20                        │")
        print("│ Desc: I fix and make machine                    │")
        print("└─────────────────────────────────────────────────┘")
    elif job_choice == "4":
        if brain_cell < 20:
            print("You have not enough brain cells")
            return
        job = "scientist"
        income = 1000
        work_energy = 50
        print(f"You work as a {job}")
        print("┌─────────────────────────────────────────────────┐")
        print("│ Salary: 1000$                                   │")
        print("│ Energy: 50                                      │")
        print("│ Brain cells required: 100                       │")
        print("│ Desc: Doing for the greater good of humanity    │")
        print("└─────────────────────────────────────────────────┘")

def sleep():
    global energy
    energy = max_energy
    print(f"Energy restored. You now have {energy}/{max_energy}")

def study():
    global brain_cell
    brain_cell += gain_brain_cell
    print(f"You gain {gain_brain_cell} brain cell. You now have {brain_cell} brain cells")


def main():
    global mainloop
    while mainloop:
        commands = input("Type something here: ")
        if commands.lower() == "/command":
            command()
        elif commands.lower() == "/work":
            work()
        elif commands.lower() == "/sleep":
            sleep()
        elif commands.lower() == "/stop":
            mainloop = 0
        elif commands.lower() == "/joblist":
            joblist()
        elif commands.lower() == "/jobchoose":
            jobchoose()
        elif commands.lower() == "/study":
            study()
if __name__ == "__main__":
    try:
        start()
        main()
    except KeyboardInterrupt:
        print("\nThanks for playing\n")