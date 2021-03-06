import tkinter as tk
import tools.modules.extra as ex
from tkinter.filedialog import askopenfile


def set_vid_size():
    if size.get() != '':
        ex.set_video_size(size.get())
    videosize.destroy()


def vid_window():
    global size, videosize
    green = '#00a99d'
    videosize = tk.Tk()
    videosize.resizable(0, 0)
    h = videosize.winfo_screenheight() // 2 - 50
    w = videosize.winfo_screenwidth() // 2 - 100
    videosize.geometry("200x100+%d+%d" % (w, h))
    videosize.title("Set Video Size")
    videosize.configure(bg=green)
    videosize.focus_force()
    videosize.attributes('-topmost', True)
    videosize.overrideredirect(1)
    info = tk.Label(text="Enter Video Size for uiCY: \n Default is 1024 \n Ex: 1080,1024,1366", master=videosize,
                    font=['Segoe UI Bold', 12], bg=green)
    info.pack()
    size = tk.Entry(width=10, master=videosize, font=["Segoe UI Bold Italic", 12])
    size.pack()
    size.place(x=5, y=70)
    print(size.get())
    button = ex.HoverButton(master=videosize, text='Set Size', command=set_vid_size)
    button.pack()
    button.place(x=120, y=70)
    videosize.mainloop()


def vlc_path():
    vlcpath = askopenfile(filetypes=[("VLC Application", "*.exe")])
    ex.set_vlc_path(vlcpath.name)
    txt = '''VLC Path set to
''' + vlcpath.name + '!'
    vlclabel = tk.Label(master=frame, text=txt, bg=black, fg='green', font=["Segoe UI Light Italic", 18],
                        justify='left')
    vlclabel.pack()
    vlclabel.place(x=200, y=420)


def fade_in():
    alpha = master.attributes("-alpha")
    if alpha <= 1:
        alpha += .1
        master.attributes("-alpha", alpha)
        master.after(50, fade_in)


def Page2():
    ex.set_dir('main')
    page1.destroy()
    global page2, black, master, frame
    black = '#202125'
    page2 = tk.Tk()
    page2.title("uiCY: Your Capture Card")
    h = page2.winfo_screenheight() // 2 - 300
    w = page2.winfo_screenwidth() // 2 - 400
    page2.geometry("800x600+%d+%d" % (w, h))
    page2.resizable(False, False)
    page2.overrideredirect(1)

    # FADE IN ANIMATION
    page2.attributes("-alpha", 0)
    master = page2
    fade_in()

    # UI
    frame = tk.LabelFrame(master=page2, height=600, width=800, bg=black)
    frame.pack()
    frame.place(x=0, y=0)

    logo_img = tk.PhotoImage(file=r'photos/uicy_t.png')
    logo_img = logo_img.subsample(2, 2)
    logo = tk.Label(master=frame, image=logo_img, bg=black)
    logo.pack()
    logo.place(x=200, y=0)

    intro = tk.Label(master=frame, text='Setup uiCY:', font=["Segoe UI Light Italic", 36], bg=black,
                     fg='white', justify='center')
    intro.pack()
    intro.place(x=20, y=220)

    set_vid_img = tk.PhotoImage(file=r'photos/setsize.png')
    set_vid_img = set_vid_img.subsample(2, 2)
    set_vid = ex.HoverButton(master=frame, image=set_vid_img, activebackground=black,
                             bg=black, relief='flat', command=vid_window)
    set_vid.pack()
    set_vid.place(x=60, y=300)

    vlcb = tk.PhotoImage(file=r'photos/choosevlc.png')
    vlcb = vlcb.subsample(2, 2)
    vlc_button = ex.HoverButton(master=frame, image=vlcb, command=vlc_path, relief='flat', activebackground=black,
                                bg=black)
    vlc_button.pack()
    vlc_button.place(x=60, y=410)
    nxt_img = tk.PhotoImage(file=r'photos/next.png')
    nxt_img = nxt_img.subsample(3, 3)
    nxt = tk.Button(master=frame, image=nxt_img, bg=black, relief='flat', activebackground=black, command=page2.destroy)
    nxt.pack()
    nxt.place(x=650, y=500)
    page2.mainloop()


def Page1():
    ex.set_dir('main')
    # INITIALIZING THE WINDOW
    global page1, black, master, frame
    black = '#202125'
    page1 = tk.Tk()
    page1.title("uiCY: Your Capture Card")
    h = page1.winfo_screenheight() // 2 - 300
    w = page1.winfo_screenwidth() // 2 - 400
    page1.geometry("800x600+%d+%d" % (w, h))
    page1.resizable(False, False)
    page1.overrideredirect(1)

    # FADE IN ANIMATION
    page1.attributes("-alpha", 0)
    master = page1
    fade_in()

    # UI
    frame = tk.LabelFrame(master=page1, height=600, width=800, bg=black)
    frame.pack()
    frame.place(x=0, y=0)

    logo_img = tk.PhotoImage(file=r'photos/uicy_t.png')
    logo_img = logo_img.subsample(2, 2)
    logo = tk.Label(master=frame, image=logo_img, bg=black)
    logo.pack()
    logo.place(x=200, y=0)
    intro = tk.Label(master=frame, text="Introduction to uiCY:", font=["Segoe UI Light Italic", 36], bg=black,
                     fg='white', justify='center')
    intro.pack()
    intro.place(x=20, y=210)
    intro_txt = '''
    uiCY is an Open-Source GUI program based on scrCPY(Genymobile) and sndCPY(rom1v).
    It can be used to mirror your phone screen + internal audio to your PC(Windows/Linux)
    through USB data cable. It was made keeping bugdet gamers and streamers in mind who
    cannot afford devices like Elgato™. Indeed this program cannot give as much quality
    as Elgato™ but still it serves the purpose i.e. you can easily stream/record at 480p.
    The following window will guide you to setup uiCY on your system....
    Click Next to continue setup...
    
    '''
    intro_label = tk.Label(master=frame, text=intro_txt, font=["Segoe UI Light", 14], bg=black, fg='white',
                           justify='left')
    intro_label.pack()
    intro_label.place(x=0, y=270)
    nxt_img = tk.PhotoImage(file=r'photos/next.png')
    nxt_img = nxt_img.subsample(3, 3)
    nxt = tk.Button(master=frame, image=nxt_img, bg=black, relief='flat', activebackground=black, command=Page2)
    nxt.pack()
    nxt.place(x=650, y=500)
    page1.mainloop()
