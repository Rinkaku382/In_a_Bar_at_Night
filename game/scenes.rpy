screen scenes:
    tag menu

    frame:
        pos (0, 0)
        grid 5 2:
            xalign 0.5 yalign 0.5
            spacing 30
         ## scene 1
            if renpy.seen_label("passage_1") and persistent.passage_1 == True:
                imagebutton idle "images/thumbnails/scene1.png" action Replay("passage_1")
            else:
                add "images/thumbnails/thumbnail_locked.png"
        ## scene 2
            if renpy.seen_label("passage_2") and persistent.passage_2 == True:
                imagebutton idle "images/thumbnails/scene2.png" action Replay("passage_2")
            else:
                add "images/thumbnails/thumbnail_locked.png"
        ## scene 3
            if renpy.seen_label("passage_3") and persistent.passage_3 == True:
               imagebutton idle "images/thumbnails/scene3.png" action Replay("passage_3")
            else:
                add "images/thumbnails/thumbnail_locked.png"
        ## scene 4
            if renpy.seen_label("passage_4") and persistent.passage_4 == True:
               imagebutton:
                   idle "images/thumbnails/scene4.png" action Replay("passage_4")
            else:
                add "images/thumbnails/thumbnail_locked.png"
        ## scene 5
            if renpy.seen_label("passage_5") and persistent.passage_5 == True:
               imagebutton idle "images/thumbnails/scene5.png" action Replay("passage_5")
            else:
                add "images/thumbnails/thumbnail_locked.png"

        ## scene 6
            if renpy.seen_label("passage_6") and persistent.passage_6 == True:
               imagebutton idle "images/thumbnails/scene6.png" action Replay("passage_6")
            else:
                add "images/thumbnails/thumbnail_locked.png"
        ## scene 6
            if renpy.seen_label("passage_7") and persistent.passage_7 == True:
               imagebutton idle "images/thumbnails/scene7.png" action Replay("passage_7")
            else:
                add "images/thumbnails/thumbnail_locked.png"
        ## scene 8
            if renpy.seen_label("passage_8") and persistent.passage_8 == True:
               imagebutton idle "images/thumbnails/scene8.png" action Replay("passage_8")
            else:
                add "images/thumbnails/thumbnail_locked.png"
        ## scene 9
            if renpy.seen_label("passage_9") and persistent.passage_9 == True:
               imagebutton idle "images/thumbnails/scene9.png" action Replay("passage_9")
            else:
                add "images/thumbnails/thumbnail_locked.png"
        ## scene 10
            if renpy.seen_label("passage_10") and persistent.passage_10 == True:
               imagebutton idle "images/thumbnails/scene10.png" action Replay("passage_10")
            else:
                add "images/thumbnails/thumbnail_locked.png"

 #return to main menu
        textbutton "Return" action Return() xalign 0.5 yalign 0.9
