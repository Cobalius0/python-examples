"""main

"""

import ui

def main():
    """main

    """
    root = ui.Window()
    control = ui.ControlPage(root).get_instance()

    page4 = ui.ConfigPage(control)
    page3 = ui.ScorePage(control)
    page2 = ui.GamePage(control)
    page1 = ui.MainPage(control)

    root.mainloop()

    # logic.new_game()


if __name__ == '__main__':
    main()
