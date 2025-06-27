label change_name:
    scene black 

    $ name = renpy.input(_("Как тебя зовут?"), default=_("Алекс")).strip() or _("Алекс")
    $ pb_name_set = True
