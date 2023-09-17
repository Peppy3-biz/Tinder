; This is your AutoHotKey script
; Use F1 to activate the sequence

F1::
    MouseMove, 200, 20
    MouseClick, left, , , 1, 0

    MouseClick, left, 65, 222, 1, 0

    Sleep, 200

    ; Newest Match
    MouseClick, left, 340, 320, 1, 0

    ; Move the mouse cursor to the start position of the text (replace x1, y1 with the actual coordinates)
    MouseMove, 1410, 770

    ; Press the left mouse button down to start highlighting
    MouseClick, left, , , 1, 0, D

    ; Move the mouse cursor to the end position of the text to highlight it (replace x2, y2 with the actual coordinates)
    MouseMove, 1766, 1021 ; 0 after coordinates makes it an absolute move

    Sleep, 600

    ; Release the left mouse button to finish highlighting
    MouseClick, left, , , 1, 0, U

    ; Copy the highlighted text
    Send, ^c

    ; chatGPT tab
    MouseClick, left, 440, 20, 1, 0

    Sleep, 100

    ; text box
    MouseClick, left, 800, 960, 1, 0

    Send, ^v
    Send, {Enter}

    Sleep, 9000

; copyOpener
x := 1378
y := 300
y_distance := 14

Loop, 25 ; repeat 25 times
{
    ; copy response
    Sleep, 38
    MouseClick, left, x, y, 1, 0
    y := y + 14
}


    ; copy response selector 2