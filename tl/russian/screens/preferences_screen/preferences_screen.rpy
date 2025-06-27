## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    tag menu
    style_prefix "settings"

    default image_path = "gui/settings/"

    add "settings_background"

    imagebutton:
        idle "return_button_idle"
        hover "return_button_hover"
        action Return()

    frame:
        xysize (808, 815)
        pos (129, 185)
        padding (35, 35)

        vbox:
            spacing 25

            # Display
            hbox:
                xfill True

                text "Display" yalign 0.5

                hbox:
                    xalign 1.0
                    spacing 20

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        action Preference("display", "window")
                        padding (50, 20)

                        text "Window" align (0.5, 0.5)

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        action Preference("display", "fullscreen")
                        padding (40, 20)

                        text "Full Screen" align (0.5, 0.5)

            # Skip
            hbox:
                xfill True

                text "Skip" yalign 0.5

                hbox:
                    xalign 1.0
                    spacing 20

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        action Preference("skip", "toggle")
                        padding (30, 20)

                        text "Unseen Text" align (0.5, 0.5)

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        action Preference("after choices", "toggle")
                        padding (25, 20)

                        text "After Choices" align (0.5, 0.5)

        # Other Settings
        vbox:
            yalign 1.0
            spacing 10

            # CENSORSHIP POPUPS / SKIP NSFW SCENES
            hbox:
                xfill True

                text "Пропустить эротический контент" yalign 0.5

                hbox:
                    xalign 1.0
                    spacing 5

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        action SetVariable("is_censored", True)
                        xysize (137, 61)

                        text "On" align (0.5, 0.5)

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        action SetVariable("is_censored", False)
                        xysize (137, 61)

                        text "Off" align (0.5, 0.5)

            # SHOW REPUTATION
            hbox:
                xfill True

                text "Показывать репутацию" yalign 0.5

                hbox:
                    xalign 1.0
                    spacing 5

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        action SetVariable("show_reputation", True)
                        xysize (137, 61)

                        text "On" align (0.5, 0.5)

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        action SetVariable("show_reputation", False)
                        xysize (137, 61)

                        text "Off" align (0.5, 0.5)

            # REAL LIFE MODE
            hbox:
                xfill True

                text "Режим Реальной Жизни" yalign 0.5

                hbox:
                    xalign 1.0
                    spacing 5

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        selected (real_life_mode)
                        action [SetVariable("real_life_mode", True), SetVariable("config.rollback_enabled", False), SetVariable("show_reputation", False)]
                        xysize (137, 61)

                        text "On" align (0.5, 0.5)

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        selected (not real_life_mode)
                        action [SetVariable("real_life_mode", False), SetVariable("config.rollback_enabled", True)]
                        xysize (137, 61)

                        text "Off" align (0.5, 0.5)

            # TUTORIALS
            hbox:
                xfill True

                text "Обучение" yalign 0.5

                hbox:
                    xalign 1.0
                    spacing 5

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        action Function(set_dict_values, persistent.enabled_tutorials, True)
                        selected all(persistent.enabled_tutorials.values())
                        xysize (137, 61)

                        text "On" align (0.5, 0.5)

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        action Function(set_dict_values, persistent.enabled_tutorials, False)
                        selected not all(persistent.enabled_tutorials.values())
                        xysize (137, 61)

                        text "Off" align (0.5, 0.5)

            # Quick Menu
            hbox:
                xfill True

                text "Показывать быстрое меню" yalign 0.5

                hbox:
                    xalign 1.0
                    spacing 5

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        action SetVariable("quick_menu", True)
                        xysize (137, 61)

                        text "On" align (0.5, 0.5)

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        action SetVariable("quick_menu", False)
                        xysize (137, 61)

                        text "Off" align (0.5, 0.5)

            # DIAGNOSTIC DATA
            hbox:
                xfill True

                text "Сбор данных для диагностики" yalign 0.5

                hbox:
                    xalign 1.0
                    spacing 5

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        insensitive_background Transform("blue_button_idle", matrixcolor=SaturationMatrix(0))
                        action NullAction()
                        sensitive False
                        xysize (137, 61)

                        text "On" align (0.5, 0.5)

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        action NullAction()
                        selected True
                        xysize (137, 61)

                        text "Off" align (0.5, 0.5)

            # MARKETING DATA
            hbox:
                xfill True

                text "Сбор маркетинговых данных" yalign 0.5

                hbox:
                    xalign 1.0
                    spacing 5

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        insensitive_background Transform("blue_button_idle", matrixcolor=SaturationMatrix(0))
                        action NullAction()
                        sensitive False
                        xysize (137, 61)

                        text "On" align (0.5, 0.5)

                    button:
                        idle_background "blue_button_idle"
                        hover_background "blue_button_hover"
                        selected_background "blue_button_hover"
                        action NullAction()
                        selected True
                        xysize (137, 61)

                        text "Off" align (0.5, 0.5)


    frame:
        xysize (808, 324)
        pos (987, 185)
        padding (35, 35)

        has vbox
        spacing 25

        hbox:
            xfill True

            text "Скорость текста" yalign 0.5

            bar value Preference("text speed"):
                xalign 1.0
                xysize (375, 37)
                left_bar "settings_bar_left"
                right_bar "settings_bar_right"
                thumb "settings_bar_thumb"
                thumb_offset 20

        hbox:
            xfill True

            text "Автоматическая перемотка" yalign 0.5

            bar value Preference("auto-forward time"):
                xalign 1.0
                xysize (375, 37)
                left_bar "settings_bar_left"
                right_bar "settings_bar_right"
                thumb "settings_bar_thumb"
                thumb_offset 20

        hbox:
            xfill True

            text "Музыка" yalign 0.5

            bar value Preference("music volume"):
                xalign 1.0
                xysize (375, 37)
                left_bar "settings_bar_left"
                right_bar "settings_bar_right"
                thumb "settings_bar_thumb"
                thumb_offset 20

        hbox:
            xfill True

            text "Звук" yalign 0.5

            bar value Preference("sound volume"):
                xalign 1.0
                xysize (375, 37)
                left_bar "settings_bar_left"
                right_bar "settings_bar_right"
                thumb "settings_bar_thumb"
                thumb_offset 20


    vpgrid:
        cols 2
        pos (987, 550)
        spacing 20
        allow_underfull True

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            selected_background "blue_button_hover"
            action Show("_accessibility")
            padding (50, 25)

            text "Настройки спец возможностей" align (0.5, 0.5)

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            selected_background "blue_button_hover"
            insensitive_background Transform("blue_button_idle", matrixcolor=SaturationMatrix(0))
            action Show("translation_selector")
            padding (50, 25)

            text "Перевод" align (0.5, 0.5)

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            selected_background "blue_button_hover"
            insensitive_background Transform("blue_button_idle", matrixcolor=SaturationMatrix(0))
            action Call("change_name")
            padding (50, 25)

            text "Выбрать имя" align (0.5, 0.5)

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            selected_background "blue_button_hover"
            action [LovenseQRCodeDownload(), ShowMenu("connect_lovense")]
            padding (40, 25)

            text "Соединение Lovense" align (0.5, 0.5)

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            selected_background "blue_button_hover"
            action Show("clear_persistent")
            padding (40, 25)

            text "Очистить постоянные данные" align (0.5, 0.5)

        if _in_replay:
            button:
                idle_background "blue_button_idle"
                hover_background "blue_button_hover"
                selected_background "blue_button_hover"
                action EndReplay()
                padding (50, 25)

                text "End Replay" align (0.5, 0.5)
