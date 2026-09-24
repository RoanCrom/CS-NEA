import tkinter as tk
import Main


def submit_answer():
    answer = answer_entry.get()

    if answer.strip() == "":
        return

    is_correct = Main.check_answer(answer)

    if is_correct:
        result_label.config(text="Correct!")
    else:
        result_label.config(
            text=f"Incorrect! Answer: {Main.current_answer}"
        )

    score_label.config(
        text=f"Score: {Main.correct}/{Main.questions_asked}"
    )

    answer_entry.delete(0, tk.END)

    if Main.questions_asked >= Main.total_questions:
        question_label.config(
            text=f"Quiz finished!\nYou got {Main.correct}/{Main.total_questions}"
        )

        submit_button.config(state="disabled")
        answer_entry.config(state="disabled")

    else:
        next_question = Main.new_question()
        question_label.config(text=next_question)


window = tk.Tk()

window.title("A Level Computer Science Quiz")
window.geometry("600x350")


title_label = tk.Label(
    window,
    text="Computer Science Quiz",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=20)


question_label = tk.Label(
    window,
    text="",
    font=("Arial", 16),
    wraplength=500
)

question_label.pack(pady=20)


answer_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=35
)

answer_entry.pack(pady=10)


submit_button = tk.Button(
    window,
    text="Submit",
    font=("Arial", 14),
    command=submit_answer
)

submit_button.pack(pady=10)


result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12)
)

result_label.pack(pady=5)


score_label = tk.Label(
    window,
    text="Score: 0/0",
    font=("Arial", 12)
)

score_label.pack(pady=5)


question_label.config(text=Main.new_question())


window.bind(
    "<Return>",
    lambda event: submit_answer()
)


window.mainloop()
