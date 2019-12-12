import turtle
import random


def draw_limb(side, person_color):
    turtle.pendown()
    turtle.pencolor(person_color)
    if side == "right":
        turtle.left(45)
        turtle.forward(75)
        turtle.backward(75)
        turtle.right(45)
    if side == "left":
        turtle.right(45)
        turtle.forward(75)
        turtle.backward(75)
        turtle.left(45)


def set_again(another_one):
    if another_one == "yes":
        valid = False
    elif another_one == "no":
        valid = True
    else:
        valid = True
    return valid


def write_wrong_answers(incorrect_answers_array, person_color):
    #print wrong answers
    turtle.penup()
    turtle.goto(-300,300)
    turtle.setheading(0)
    turtle.pencolor("Khaki")
    turtle.write("Incorrect letters: ", font=("Arial", 24, "normal"))
    turtle.forward(200)
    for letter in incorrect_answers_array:
        #turtle.right(90)
        #turtle.forward(50)
        turtle.write(letter, font=("Arial", 30, "normal"))
        turtle.forward(25)
        #turtle.backward(90)
        #turtle.backward(50)
        #turtle.left(90)
        #turtle.forward(35)
    turtle.home()
    turtle.pendown()
    turtle.setheading(0)
    turtle.pencolor(person_color)
    turtle.pensize(10)


def write_correct_answers(correct_answers_array):
    #write correct answers
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(-300, -250)
    for letter in correct_answers_array:
        if letter != "" and letter != '' and letter is not None:
            turtle.forward(5)
            turtle.left(90)
            turtle.forward(10)
            #turtle.pencolor("Ghost White")
            turtle.pencolor("Light coral")
            turtle.write(letter, font=("Arial", 48, "normal"))
            turtle.backward(10)
            turtle.right(90)
            turtle.backward(5)
        turtle.penup()
        turtle.forward(75)


def write_dashes(word):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(-300, -250)
    turtle.pencolor("blue")
    for letter in word:
        turtle.write("_", font=("Arial", 48, "normal"))
        turtle.penup()
        turtle.forward(75)


def correct_letter(correct_answers_array, word, user_input):
    indexes = []
    # go through the word to look for where it is
    word_as_array = string_to_list(word)
    for elements in word_as_array:
        if elements == user_input:
            indexes.append(word_as_array.index(elements))
            word_as_array[word_as_array.index(elements)] = "/o\\"
    # set all the values to the correct positions
    for values in indexes:
        correct_answers_array[values] = user_input
    print("correct\n")
    return indexes


def string_to_list(string):
    wordList = []
    for letters in string:
        wordList.append(letters)
    return wordList


def draw_face(orientation):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(0)
    turtle.forward(25)
    turtle.pendown()
    #turtle.pencolor("white")
    #turtle.dot(20)
    turtle.pencolor("black")
    turtle.dot(5)
    turtle.penup()
    turtle.backward(50)
    turtle.pendown()
    #turtle.pencolor("white")
    #turtle.dot(20)
    turtle.pencolor("black")
    turtle.dot(5)
    turtle.penup()
    #mouth
    turtle.goto(0, 0)
    turtle.setheading(90)
    if orientation == "sad":
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(20)
        turtle.left(90)
    if orientation == "happy":
        turtle.forward(30)
        turtle.right(90)
        turtle.backward(20)
        turtle.right(90)
    turtle.pendown()
    turtle.pensize(3)
    turtle.circle(20, 180)


def draw_structure(color1, color2):
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(90)
    turtle.forward(100)
    turtle.pencolor(color1)
    turtle.pensize(10)
    turtle.pendown()
    i=0
    while(i<3):
        turtle.forward(25)
        turtle.dot(25)
        i = i + 1
    turtle.forward(50)
    turtle.pencolor(color2)
    turtle.right(90)
    turtle.pensize(20)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(40)
    turtle.backward(80)
    turtle.penup()
    turtle.goto(0,0)


def draw_ground():
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(-400, -250)
    turtle.setheading(0)
    turtle.pensize(150)
    turtle.pencolor("Wheat")
    turtle.pendown()
    turtle.forward(800)


def draw_sun():
    turtle.penup()
    turtle.goto(-300, 250)
    turtle.pencolor("Yellow")
    turtle.dot(75)
    for i in range(0,3):
        turtle.right(45)
        turtle.forward(75)
        turtle.backward(150)
        turtle.forward(75)
    turtle.penup()


def draw_grass(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pencolor("Green")
    turtle.setheading(90)
    i = 0
    turtle.pendown()
    turtle.pensize(3)
    while i < 50:
        turtle.left(0 + 0.1 * i)
        turtle.pensize(-0.008*((i-25)*(i-25))+5)
        turtle.forward(1)
        i = i + 1
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(90)
    i = 0
    while i < 50:
        turtle.pensize(-0.008 * ((i - 25) * (i - 25)) + 5)
        turtle.forward(1)
        i = i + 1
    turtle.penup()
    turtle.goto(x,y)
    i = 0
    turtle.pendown()
    while i < 50:
        turtle.right(0 + 0.1 * i)
        turtle.pensize(-0.008 * ((i - 25) * (i - 25)) + 5)
        turtle.forward(1)
        i = i + 1
    turtle.penup()


def draw_flower(x, y, color):
    turtle.colormode(255)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor("Green")
    turtle.setheading(90)
    i = 0
    turtle.pendown()
    turtle.pensize(3)
    while (i<50):
        turtle.left(0 + 0.05 * i)
        turtle.forward(1)
        i = i + 1
    #center = turtle.position()
    turtle.setheading(90)
    if isinstance(color, str):
        turtle.pencolor(color)
    else:
        turtle.pencolor((color[0],color[1],color[2]))
    turtle.forward(10)
    turtle.dot(20)
    turtle.backward(20)
    turtle.dot(20)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.dot(20)
    turtle.backward(20)
    turtle.dot(20)
    turtle.forward(10)
    turtle.pencolor("yellow")
    turtle.dot(10)
    turtle.penup()


def draw_cloud(cloud_color):
    turtle.pencolor(cloud_color)
    turtle.setheading(0)
    turtle.dot(40)
    turtle.forward(40)
    turtle.dot(50)
    turtle.forward(50)
    turtle.dot(75)
    turtle.forward(50)
    turtle.dot(50)
    turtle.forward(40)
    turtle.dot(40)
    turtle.forward(40)


def draw_x_eyes(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.left(45)
    turtle.pensize(4)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.forward(10)
    turtle.backward(20)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.backward(20)
    turtle.right(45)


def get_rgb_value():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = [r, g, b]
    return rgb


def check_valid_input(user_input):
    if user_input.lower().isalpha():
        return True
    else:
        return False


class HangmanGame:

    def __init__(self):
        self.start_game()

    #-----------------------------------------------------------------------------------
    def draw_background(self, background, cloud_color, make_sun, structure, flowers):
        turtle.speed(0)
        turtle.penup()
        turtle.home()
        turtle.pencolor(background)
        turtle.dot(1000)
        turtle.goto(75, 275)
        draw_cloud(cloud_color)
        turtle.goto(150, 150)
        draw_cloud(cloud_color)
        turtle.goto(-300,100)
        draw_cloud(cloud_color)
        if structure:
            draw_structure("Burlywood","Saddle Brown")
        draw_ground()
        i = 0
        while i < 5:
            j = 100 * i
            draw_grass(-250 + j, -190)
            i += 1
        i = 0
        while i < 10:
            j = 75 * i
            draw_grass(-300 + j, -300)
            i += 1
        i = 0
        while i < 10:
            j = 75 * i
            draw_grass(-325 + j, -325)
            i += 1
        #draw_grass(250,-275)
        #for x in range(10):
        #    draw_flower(random.randrange(-300, 300, 1), random.randrange(-300, -190, 1), get_rgb_value())
        if flowers:
            for x in range(10):
                #(-300,-250)
                draw_flower(random.randrange(-300, 300, 1), random.randrange(-275, -225, 1), get_rgb_value())
        if make_sun:
            draw_sun()
        turtle.end_fill()
        turtle.up()

    #-----------------------------------------------------------------------------------
    def draw_head(self, orientation, person_color):
        turtle.setheading(0)
        turtle.pendown()
        turtle.pensize(10)
        if orientation == "sad":
            turtle.pencolor("Burlywood")
        if orientation == "happy":
            turtle.pencolor(person_color)
        turtle.circle(50)
        turtle.penup()
        turtle.left(90)
        turtle.forward(50)
        turtle.pendown()
        turtle.pencolor(person_color)
        turtle.dot(99)
        #turtle.delay(25)
        turtle.penup()
        turtle.goto(0,0)
        turtle.left(90)
        draw_face(orientation)

    #-----------------------------------------------------------------------------------
    def draw_full_body(self, orientation, person_color):
        turtle.goto(0,0)
        self.draw_head(orientation,person_color)
        #body
        turtle.penup()
        turtle.goto(0,0)
        turtle.setheading(270)
        turtle.pendown()
        turtle.pencolor(person_color)
        turtle.pensize(10)
        turtle.forward(100)
        turtle.backward(80)
        draw_limb("right",person_color)
        draw_limb("left",person_color)
        # 2 stick legs
        turtle.forward(100)
        draw_limb("right",person_color)
        draw_limb("left",person_color)

                                    #MAIN FUNCTION CODE
    #-----------------------------------------------------------------------------------

    def hangman(self, word):
        count=0
        #offer the options to the user to change certain things about the gamem, background
        #turtle.shape("classic")
        turtle.clear()
        #person_color = "Misty Rose"
        #person_color = "Gold"
        #person_color = "Dark Slate Blue"
        #person_color = "Lemon Chiffon"
        person_color = "Yellow Green"
        #person_color = "Yellow"
        turtle.hideturtle()
        correct = 0
        correct_answers_array = []
        #get correct answers display
        for i in word:
            correct_answers_array.append("")
        incorrect_answers_array = []
        turtle.pencolor(person_color)
        #draw_background("Steel Blue")
        turtle.tracer(0,0)
        self.draw_background("Steel Blue","Gainsboro",False,True,False)
        turtle.update()
        write_dashes(word)
        while correct < len(word) and count < 6:
            #print("Correct answers so far: ")
            #print(correct_answers_array)
            #print("Inorrect answers so far: ")
            #print(incorrect_answers_array)
            user_input = turtle.textinput("User Input", "Input a letter: ")
            if check_valid_input(user_input):
                pass
            else:
                #turtle.clear()
                #turtle.write("This is an invalid input!", font=("Arial", 50, "normal"))
                user_input = turtle.textinput("Input a new answer", "Input a different letter: ")
                #quit("This is an invalid input")
            #check if repeat
            if (user_input in correct_answers_array) or (user_input in incorrect_answers_array):
                print("You already input this")
                user_input = turtle.textinput("Input a new answer", "Input a different letter: ")
                #break
            #user_input = input("Input a letter: ")
            #if the letter is in the word
            if user_input in word:
                indexes = correct_letter(correct_answers_array,word,user_input)
                write_correct_answers(correct_answers_array)
                j=0
                while j < len(indexes):
                    correct = correct + 1
                    j = j + 1
            else:
                incorrect_answers_array.append(user_input)
                write_wrong_answers(incorrect_answers_array,person_color)
                #print("incorrect")
                count = count + 1
                turtle.pendown()
                #Add a 5 second delay for each of the steps to draw the stick figure.
                #head - red line and filled with yellow
                if count == 1:
                    turtle.speed(6)
                    self.draw_head("sad",person_color)
                    #face
                    #back to origin
                    turtle.penup()
                    turtle.pencolor(person_color)
                    turtle.goto(0, -10)
                    turtle.pensize(10)
                    turtle.pendown()
                    turtle.update()
                #body
                if count == 2:
                    turtle.speed(6)
                    turtle.setheading(270)
                    turtle.forward(100)
                    turtle.backward(80)
                    turtle.update()
                #two stick arms
                if count == 3:
                    turtle.speed(6)
                    turtle.penup()
                    turtle.goto(0,-20)
                    turtle.setheading(270)
                    draw_limb("right",person_color)
                    turtle.update()
                if count == 4:
                    turtle.speed(6)
                    turtle.penup()
                    turtle.goto(0,-20)
                    turtle.setheading(270)
                    draw_limb("left",person_color)
                    turtle.update()
                #2 stick legs
                if count == 5:
                    turtle.speed(6)
                    turtle.setheading(270)
                    turtle.forward(120)
                    draw_limb("right",person_color)
                    turtle.update()
                if count == 6:
                    turtle.speed(6)
                    turtle.setheading(270)
                    turtle.forward(120)
                    draw_limb("left",person_color)
                    draw_x_eyes(-25,50)
                    draw_x_eyes(25,50)
                    turtle.penup()
                    turtle.goto(-150,-100)
                    print("GAME OVER")
                    turtle.pencolor("white")
                    turtle.write("GAME OVER", font=("Arial", 48, "normal"))
                    turtle.goto(40, -250)
                    #turtle.pencolor("grey")
                    #turtle.write("The word was:", font=("Arial", 30, "normal"))
                    turtle.goto(-300, -275)
                    correct_answers_array = [char for char in word]
                    write_correct_answers(correct_answers_array)
                    turtle.setheading(0)
                    #turtle.done()
                    turtle.update()
                    self.next_game()
        if correct == len(word):
            turtle.speed(6)
            turtle.penup()
            self.draw_background("Sky Blue","Snow",True,False,True)
            for x in range(4):
                draw_flower(random.randrange(-300,300,1),random.randrange(-300,-190,1),"pink")
                draw_flower(random.randrange(-300,300,1),random.randrange(-300,-190,1),"Light Sky Blue")
                draw_flower(random.randrange(-300,300,1),random.randrange(-300,-190,1),"gold")
                draw_flower(random.randrange(-300,300,1),random.randrange(-300,-190,1),"orange")
                #draw_flower(random.randrange(-300,-190,1),random.randrange(-300,300,1),get_rgb_value())
            turtle.goto(-300, 0)
            turtle.pencolor("Gold")
            turtle.write("YOU WIN!", font=("Arial", 48, "normal"))
            print("YOU WIN!")
            turtle.speed(8)
            self.draw_full_body("happy", "Gold")
            turtle.update()
            #turtle.done()
            self.next_game()
        #----------------------------------------------

    #hanging = hangman("turtle")
    #-----------------------------------------------------------------------------------
    def play(self,preference):
        if preference:
            player_word = turtle.textinput("Your word", "What word do you want to use?")
            #make the input word lowercase
            self.hangman(player_word)
        else:
            # get the first line if this is the one with the words words
            valid = True
            while valid:
                difficulty = turtle.textinput("Difficulty", "Input a difficulty?(easy/medium/hard)")
                if difficulty == "easy":
                    lines = open("easy_words.txt","r").read()
                    valid = False
                elif difficulty == "medium":
                    lines = open("medium_words.txt","r").read()
                    valid = False
                elif difficulty == "hard":
                    lines = open("hard_words.txt","r").read()
                    valid = False
                else:
                    valid = True
            #fix Miles' error because he doesn't want to listen
            #print(lines)
            #line = lines[0]
            words = lines.split("\n")
            #print(words)
            my_word = random.choice(words)
            #print(my_word)
            self.hangman(my_word)

    #-----------------------------------------------------------------------------------
    def start_game(self):
        turtle.speed(0)
        turtle.hideturtle()
        turtle.home()
        turtle.pencolor("Azure")
        turtle.dot(1000)
        self.draw_full_body("happy", "Pale green")
        turtle.penup()
        turtle.forward(150)
        turtle.pencolor("Black")
        turtle.write("Hangman", font=("Arial", 64, "normal"))

        valid = True
        while valid:
            user_input = turtle.textinput("Start", "Do you want to use your own word?(yes/no/quit)")
            if user_input == "yes":
                self.play(True)
                another_one = turtle.textinput("Next", "Do you want to play again?(yes/no/quit)")
                valid = set_again(another_one)
            elif user_input == "no":
                self.play(False)
                another_one = turtle.textinput("Next", "Do you want to play again?(yes/no/quit)")
                valid = set_again(another_one)
            elif user_input == "quit" or user_input == "q":
                quit()
            else:
                valid = True

    #-----------------------------------------------------------------------------------

    def next_game(self):
        user_input = turtle.textinput("Round 2", "Do you want to play again?(yes/no)")
        if user_input == "yes":
            self.start_game()
        else:
            quit()
#--------------------------------------------------------------------------------------------------------------
#draw_flower(0,0,"pink")
#for x in range(10):
#    r = random.randint(0, 255)
#    g = random.randint(0, 255)
#    b = random.randint(0, 255)
#    rgb = [r, g, b]
#    draw_flower(random.randrange(-300, 300, 1),random.randrange(-300, -190, 1),rgb)
#for x in range(10):
    #(-300,-250)
#    draw_flower(random.randrange(-300, 300, 1), random.randrange(-275, -225, 1), get_rgb_value())
#turtle.done()
#eyes
#-25.00,50.00)
#(25.00,50.00)

#Print the characters and where they go
#animate so it goes from the box to the position in the word

