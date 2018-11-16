page = 0 
x = 0
star_pos_x = 100
star_pos_y = 100
star_size_x = 50
star_size_y = 50
star_speed_x = 10
star_speed_y = 10


def setup():
    global sat_img
    global back_img
    
    sat_img = loadImage("alien.png")
    back_img = loadImage("Bigger_stars.jpg")
    back_img.resize(width, height)
    fullScreen()
    
def draw():
    global star_pos_x, star_pos_y
    global star_size_x, star_size_y, star_speed_x, star_speed_y
    
    if page == 0:
        background(back_img)
        image(sat_img, 210, 100, 200, 200)

        global x
    
        if x >= 640:
            x = 0
        x += 4
    

    elif page == 1:
        background(255, 255, 0)
    elif page == 2:
        background(255, 100, 3)

    s = createShape()
    s.beginShape();
    s.vertex(0, -50);
    s.vertex(14, -20);
    s.vertex(47, -15);
    s.vertex(23, 7);
    s.vertex(29, 40);
    s.vertex(0, 25);
    s.vertex(-29, 40);
    s.vertex(-23, 7);
    s.vertex(-47, -15);
    s.vertex(-14, -20);
    s.endShape(CLOSE)
    shape(s, star_pos_x, star_pos_y, star_size_x, star_size_y)
    star_pos_x += star_speed_x
    star_pos_y += star_speed_y
    print(star_pos_x, star_pos_y)
    if star_pos_x < star_size_x/2 or star_pos_x > width - star_size_x/2:
        star_speed_x *= -1
    elif star_pos_y < star_size_y/2 or star_pos_y > height - star_size_y/2:
        star_speed_y *= -1
        
def mousePressed():  # Triggers once per mouse-press
    global page
    page += 1
    if page == 3:
        page = 0

    
  
