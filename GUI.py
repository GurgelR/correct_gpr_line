"""
This file will be used to creating the GUI (Guided User Interface) of the program
so the user can visualize the original and corrected lines, invert the sense of 
lines or whatsoever within the main window.

It will call the functions created and implemented in "correct.py"
"""

import correct

class App:
    __slots__ = [
        # OPERATIONAL
        "main", "correctobj"
        # BUTTON

        # RADIOBUTTON

        # TEXT BOX

        # SIMPLE TEXT

    ]

    def __init__(self, main, correctobj) -> None:
        pass

if __name__ == "__main__":
    correctobj = correct.Correct()
    main = correct.Main(correctobj)
    App(main, correctobj)