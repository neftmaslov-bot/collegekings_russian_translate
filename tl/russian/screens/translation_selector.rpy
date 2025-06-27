screen translation_selector():
    add "darker_80"

    button:
        action Hide()

    frame:
        modal True
        background Frame("gui/frame.webp")
        align (0.5, 0.5)
        xysize (900, 375)
        padding (50, 50)

        grid 2 1:
            spacing 100
            align (0.5, 0.5)

            textbutton "English" action Language(None)
            textbutton "Russian" action Language("russian")