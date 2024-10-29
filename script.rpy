# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("แดดดี้")
define m = Character("มามี๊")
define s = Character("[name]")
define k = Character("คำอธิบาย")




label start:
    $ name = renpy.input ("โปรดใส่ชื่อตัวละคร")
    $ name = name.strip()

    scene 1010298

    s "เจี๊ยกกๆๆอุ๊ๆๆอ๊าาาๆๆๆ"

    scene 1034922
    show พ่อ
    with fade

    f "ดูสิแม่ ลูกเราร้องใหญ่เลย เกิดมาก็เสียงดีซะด้วย"

    scene 1034922
    show pngegg

    m  "ลูกแม่น่ารักม๊วกกกกก"

    menu:
        "นั่นแม่หรอ":
            jump นั่นแม่หรอ
        "ปวดเยี่ยวอ่ะ":
            jump เยี่ยวราด

    label นั่นแม่หรอ:
        m "ดูสิคุณ ลูกเกิดมาก็พูดได้เลย ดีนะไม่เดินได้7เก้า"

        scene 1034922
        show พ่อ

    f "ฮ่าๆ ลูกนี่ได้แม่มาเต็มๆเลยนะเนี่ย"
    jump ส่องกระจก


    return

    label เยี่ยวราด:
        m "ว๊ายยยยย ลู๊กกกก.."

        scene 1034922
        show พ่อ
    
    f "เยี่ยวแตกเลยหรอลูกกก"
    jump ส่องกระจก

    label ส่องกระจก:

        scene 1034922

    k "ทันทีที่สาวน้อยแรกเกิดตกใจ จึงรีบเดินไปส่องกระจกในห้องน้ำทันที"

    scene wp9518516
    with fade


    s "นะ...นี่มัน"

    s "B...BAKANA!!"

    show กล้าม

    s "...."

    s "แม๊!!!"

    scene wp9518516

    k "แม่ที่ได้ยินเสียงลูกคำรามจึงได้วิ่งเข้ามาดูด้วยความเป็นห่วง"

    show pngegg

    m "เป็นอะไรลูกร้องซะเสียงดังเชียว แม่ก็ว่าบ้านเราไม่มีกอลิล่านะ"

    scene wp9518516
    show กล้าม

    s "แต่ตอนนี้หนูก็ไม่ต่างอะไรกับกอลิล่าเลยนะแม่"


    m "อุ๊ย แม่ขอโทษจ๊ะ"

    s "แล้วทำไมหนูถึงเกิดมามีสภาพเป็นแบบนี้"
    s "ตอนคลานออกมามันลำบากนะแม่"

    scene wp9518516
    show pngegg

    m "สงสัยแม่คงจะทำเวย์โปรตีนหกลงในสมูทตี้น่ะจ๊ะ ลูกเลยออกมามีกล้ามที่ใหญ่โตขนาดนี้"

    scene wp9518516
    show กล้าม
    
    s "สาระนะแม่ ไม่เอาสาหร่าย"

    scene wp9518516
    show pngegg

    m "สาระจ๊ะลูก"
    
    scene wp9518516
    show กล้าม

    s "เคเลยแม่"

    scene wp9518516
    show pngegg

    m "ลูกหิวมั้ย เดี๋ยวแม่หาข้าวให้กิน"

    scene wp9518516
    show กล้าม

    s "จัดไปแม่ หนูขออกไก่ปั่น ข้าว150g ฟักทองต้มกับบล็อคโคลี่นะ"
    s "หนูต้องกินโปรตีน120g"

    scene wp9518516
    show pngegg

    m "ได้จ๊ะลูกแม่ กินเสร็จแล้วอย่าลืมคาร์ดิโอ19ชั่วโมงไม่พักนะ"

    scene wp9518516
    show กล้าม

    s "หนูขอ21ชั่วโมงได้มั้ย แค่19ยังไม่กินแรงหนูเลย"

    scene wp9518516
    show pngegg

    m "ได้จ๊ะลูกแม่ พักผ่อนให้เพียงพอด้วยนะ"

    scene wp9518516
    show กล้าม

    s "ค่ะแม่"

















     

    # This ends the game.

    return
