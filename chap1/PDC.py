import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import graphviz
import time
import multiprocessing
import threading

# ==============================
# ✅ Keyword Match Logic
# ==============================
def recognize_keyword(text, keyword, mode):
    text = text.lower()
    keyword = keyword.lower()
    if mode == "Starts With":
        return text.startswith(keyword)
    elif mode == "Ends With":
        return text.endswith(keyword)
    elif mode == "Contains":
        return keyword in text
    return False

# ==============================
# ✅ DFA DRAW FUNCTIONS
# ==============================
def draw_dfa_starts_with(keyword):
    f = graphviz.Digraph('DFA')
    size_x = max(8, len(keyword) * 1.2)
    f.attr(rankdir='LR', size=f'{size_x},3', splines='true')
    keyword = keyword.lower()

    alphabet = list(dict.fromkeys(keyword))
    f.node('', shape='none')
    f.edge('', 'q0')

    for i in range(len(keyword) + 1):
        shape = 'doublecircle' if i == len(keyword) else 'circle'
        f.node(f'q{i}', shape=shape, style='filled',
               fillcolor='lightgreen' if shape == 'doublecircle' else 'white')

    f.node('trap', shape='circle', style='filled,dotted', fillcolor='lightcoral')

    for i, char in enumerate(keyword):
        f.edge(f'q{i}', f'q{i+1}', label=char, color='green')
        wrong_inputs = [c for c in alphabet if c != char]
        if wrong_inputs:
            f.edge(f'q{i}', 'trap', label=', '.join(wrong_inputs), color='red')

    f.edge('trap', 'trap', label=', '.join(alphabet), style='dashed', color='black')
    final_state = f'q{len(keyword)}'
    f.edge(final_state, final_state, label=', '.join(alphabet), style='dashed', color='blue')
    return f


def draw_dfa_contains(keyword):
    f = graphviz.Digraph('DFA')
    size_x = max(30, len(keyword) * 4.0)
    f.attr(rankdir='LR', size=f'{size_x},8', splines='true')
    keyword = keyword.lower()
    alphabet = list(dict.fromkeys(keyword))
    pi = [0] * len(keyword)
    for i in range(1, len(keyword)):
        j = pi[i-1]
        while j > 0 and keyword[i] != keyword[j]:
            j = pi[j-1]
        if keyword[i] == keyword[j]:
            j += 1
        pi[i] = j

    for i in range(len(keyword) + 1):
        shape = 'doublecircle' if i == len(keyword) else 'circle'
        f.node(f'q{i}', shape=shape, style='filled',
               fillcolor='lightgreen' if shape == 'doublecircle' else 'white')

    f.node('', shape='none')
    f.edge('', 'q0')

    for state in range(len(keyword) + 1):
        for c in alphabet:
            if state == len(keyword):
                next_state = state
            else:
                if c == keyword[state]:
                    next_state = state + 1
                else:
                    j = pi[state - 1] if state > 0 else 0
                    while j > 0 and c != keyword[j]:
                        j = pi[j - 1]
                    if c == keyword[j]:
                        next_state = j + 1
                    else:
                        next_state = 0
            f.edge(f'q{state}', f'q{next_state}', label=c)
    return f


def draw_dfa_ends_with(keyword):
    f = graphviz.Digraph('DFA')
    size_x = max(30, len(keyword) * 4.0)
    f.attr(rankdir='LR', size=f'{size_x},8', splines='true')
    keyword = keyword.lower()
    alphabet = list(dict.fromkeys(keyword))
    pi = [0] * len(keyword)
    for i in range(1, len(keyword)):
        j = pi[i-1]
        while j > 0 and keyword[i] != keyword[j]:
            j = pi[j-1]
        if keyword[i] == keyword[j]:
            j += 1
        pi[i] = j

    for i in range(len(keyword) + 1):
        shape = 'doublecircle' if i == len(keyword) else 'circle'
        f.node(f'q{i}', shape=shape, style='filled',
               fillcolor='lightgreen' if shape == 'doublecircle' else 'white')

    f.node('', shape='none')
    f.edge('', 'q0')

    for state in range(len(keyword) + 1):
        for c in alphabet:
            if state < len(keyword) and c == keyword[state]:
                next_state = state + 1
            else:
                j = pi[state - 1] if state > 0 else 0
                while j > 0 and c != keyword[j]:
                    j = pi[j - 1]
                if c == keyword[j]:
                    next_state = j + 1
                else:
                    next_state = 0
            f.edge(f'q{state}', f'q{next_state}', label=c)
    return f


def draw_dfa_for_keyword(keyword, mode):
    if mode == "Starts With":
        return draw_dfa_starts_with(keyword)
    elif mode == "Ends With":
        return draw_dfa_ends_with(keyword)
    elif mode == "Contains":
        return draw_dfa_contains(keyword)
    return None

# ==============================
# ✅ Multiprocessing & Threading Test
# ==============================
def do_something(size):
    out_list = []
    for i in range(size):
        out_list.append(i * i)
    return out_list


def run_processing_test():
    size = 200000
    configs = [5, 10, 50]
    results = []

    for count in configs:
        # Multiprocessing
        start_time = time.time()
        processes = []
        for _ in range(count):
            p = multiprocessing.Process(target=do_something, args=(size,))
            p.start()
            processes.append(p)
        for p in processes:
            p.join()
        mp_time = time.time() - start_time

        # Multithreading
        start_time = time.time()
        threads = []
        for _ in range(count):
            t = threading.Thread(target=do_something, args=(size,))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        mt_time = time.time() - start_time

        results.append((count, mp_time, mt_time))

    return results

# ==============================
# ✅ GUI LOGIC
# ==============================
def display_image(path, zoom_level=1.0):
    global img_tk, current_zoom
    current_zoom = zoom_level
    img = Image.open(path)
    width, height = img.size
    new_size = (int(width * zoom_level), int(height * zoom_level))
    img = img.resize(new_size, Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    canvas.delete("all")
    canvas.create_window(0, 0, window=image_label, anchor='nw')
    canvas.config(scrollregion=canvas.bbox("all"))


def check_and_display():
    sentence = sentence_entry.get()
    keyword = keyword_entry.get()
    mode = match_mode.get()

    if not sentence or not keyword:
        messagebox.showwarning("Input Error", "Please enter both sentence and keyword.")
        return

    found = recognize_keyword(sentence, keyword, mode)
    result_label.config(text=f"Keyword Found: {'Yes ✅' if found else 'No ❌'}")

    if found:
        dfa = draw_dfa_for_keyword(keyword, mode)
        dfa.render('dfa_output', format='png', cleanup=True)
        display_image("dfa_output.png", current_zoom)

        # Run multiprocessing/multithreading tests
        results = run_processing_test()
        msg = "⚙️ Processing Performance Comparison:\n\n"
        for count, mp_time, mt_time in results:
            msg += f"Processes/Threads: {count}\n"
            msg += f"  🧠 Multiprocessing: {mp_time:.3f} sec\n"
            msg += f"  🧵 Multithreading:  {mt_time:.3f} sec\n\n"
        messagebox.showinfo("Performance Results", msg)

    else:
        image_label.config(image='')
        canvas.delete("all")


# ==============================
# ✅ GUI Setup
# ==============================
if __name__ == "__main__":
    multiprocessing.freeze_support()

    root = tk.Tk()
    root.title("Keyword DFA Recognizer + Processing Time Benchmark")
    root.geometry("900x700")
    root.config(bg="#f5f5f5")
    current_zoom = 1.0

    tk.Label(root, text="Enter Sentence:", font=("Arial", 12), bg="#f5f5f5").pack(pady=(20, 5))
    sentence_entry = tk.Entry(root, font=("Arial", 12), width=60)
    sentence_entry.pack(pady=5)

    tk.Label(root, text="Enter Keyword:", font=("Arial", 12), bg="#f5f5f5").pack(pady=(10, 5))
    keyword_entry = tk.Entry(root, font=("Arial", 12), width=30)
    keyword_entry.pack(pady=5)

    tk.Label(root, text="Match Mode:", font=("Arial", 12), bg="#f5f5f5").pack(pady=(10, 5))
    match_mode = tk.StringVar(value="Starts With")
    tk.OptionMenu(root, match_mode, "Starts With", "Ends With", "Contains").pack()

    tk.Button(root, text="Check & Generate DFA + Run Processing Benchmark",
              command=check_and_display, bg="#4caf50", fg="white", font=("Arial", 12)).pack(pady=15)

    result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f5f5f5")
    result_label.pack(pady=5)

    canvas_frame = tk.Frame(root, bg="#f5f5f5")
    canvas_frame.pack(pady=10, fill='both', expand=True)
    canvas = tk.Canvas(canvas_frame, bg="#f5f5f5")
    canvas.pack(fill='both', expand=True)
    image_label = tk.Label(canvas, bg="#f5f5f5")

    root.mainloop()
