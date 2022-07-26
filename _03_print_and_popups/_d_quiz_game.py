from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window=Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score=0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    player=simpledialog.askstring('title','How many runs did the Red Sox give up to the Blue Jays on July 22nd?')
    #      // 3.  Use an if statement to check if their answer is correct
    if player=="28":
        score=score+1
    #      // 4.  if the user's answer was correct, add one to their score 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above
    question2=simpledialog.askstring('title','What is Cody Bellingers Batting Average?')
    #      // Option: Subtract a point from their score for a wrong answer
    if question2==".204":
        score=score+1

    question3=simpledialog.askstring('title','Who is my favorite baseball player not on the Red Sox?')

    if question3=="Bo Bichette":
        score=score+1
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    score1=str(score)
    messagebox.showinfo('title',score1)
    # Run the window's .mainloop() method
    window.mainloop()






























