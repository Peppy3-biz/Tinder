; This is your AutoHotKey script
; Use F1 to activate the sequence


; copyStarter
x := 1378
y := 300
y_distance := 14


F1::
Loop, 25 ; repeat 25 times
{
    ; copy response
    Sleep, 100
    MouseClick, left, x, y, 1, 0
    y := y + 14
}
