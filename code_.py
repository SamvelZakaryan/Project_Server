# import sounddevice as sd
# from tkinter import *
# import queue
# import soundfile as sf
# import threading
# from tkinter import messagebox
#
#
# voice_rec = Tk()
# voice_rec.geometry("360x200")
# voice_rec.title("Your Voice Recorder")
# voice_rec.config(bg="#107dc2")
# q = queue.Queue()
# recording = False
# file_exists = False
#
# def callback(indata, frames, time, status):
#     q.put(indata.copy())
#
# def threading_rec(x):
#     if x == 1:
#         t1 = threading.Thread(target=record_audio)
#         t1.start()
#     elif x == 2:
#         global recording
#         recording = False
#         messagebox.showinfo(message="Recording Finished")
#     elif x == 3:
#         if file_exists:
#             data, sf.read("trial.wav", dtype='float32')
#             sd.play(data, sf)
#
#
#             sd.wait()
#         else:
#             messagebox.showerror(message="Record something to play")



# import subprocess
#
# data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
# profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
# for i in profiles:
#     results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i,
#                                       'key=clear']).decode('utf-8').split('\n')
#     results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#     try:
#         print("{:<35}) {:<}".format(i, results[0]))
#     except IndexError:
#         print("{:<35}) {:<}".format(i, ""))
#

# from multiprocessing import Process, Pipe
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())   # prints "[42, None, 'hello']"
#     p.join()


# import instaloader
#
# a = instaloader.Instaloader()
#
# user = "syuz_ii__"
# username = '_.samo.__18'
# password = "SAMO2002"
#
#
# def instalod(username, password, user):
#
#     a.login(username, password)
#     a.download_profile(user)
#
# instalod(username, password, user)





