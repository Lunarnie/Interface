import pygame, sys, os
from button import Button
import cv2

# Khởi tạo Pygame
pygame.init()

# Khởi tạo mô-đun sound
pygame.mixer.init()

SCREEN = pygame.display.set_mode((1920,1080))
# Thiết lập kích thước màn hình
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
#SCREEN = pygame.display.set_mode((960, 540))
#pygame.display.set_caption("Menu")
sound_button = pygame.mixer.Sound('display board/sound/button.mp3')

BG = pygame.image.load('display board/img/background.jpg')

pygame.display.flip()
def get_font(size):
    return pygame.font.Font("display board/img/koni.ttf", size)

selected_options = {}
selected_options['drink'] = []
selected_options['topping'] = []


toppings = {
    4: "Black Boba",
    5: "White Boba",
}

drink = {
    1: "Trà sữa",
    2: "Trà đào",
    3: "Trà tắc",
}


def change_selected_drink(selected_drink):
    drink_string = ",".join(str(x) for x in selected_drink)  # Convert list to string
    for i in range(1, 4):  # Loop through fruit indices (1, 2, 3)
        drink_string = drink_string.replace(str(i), drink[i])  # Replace using str.replace
    # No need to convert back to integers
        print(drink_string)
    return drink_string 

def change_selected_topping(selected_topping):
    topping_string = ",".join(str(x) for x in selected_topping)  # Convert list to string
    for i in range(4, 6):  # Loop through fruit indices (1, 2, 3)
        topping_string = topping_string.replace(str(i), toppings[i])  # Replace using str.replace
    # No need to convert back to integers
        print(topping_string)
    return topping_string


def main_menu():    
    while True:      
        SCREEN.blit(BG, (0, 0))
        

        MENU_MOUSE_POS = pygame.mouse.get_pos()      
        START_BUTTON = Button(image=None, pos=(935, 830), text_input="START", font=get_font(130), base_color="#d7fcd4", hovering_color="Black")
        #QUIT_BUTTON = Button(image=None, pos=(355, 500),text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="Black")

        #SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [START_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            
            if START_BUTTON.checkForInput(MENU_MOUSE_POS):
                sound_button.play()
                selected_options['drink'] = []
                selected_options['topping'] = []
                DRINK()

                '''    
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sound_button.play()
                    pygame.quit()
                    sys.exit()
                '''
        
        pygame.display.update()

def topping(selected_options_drink):
    global enlarged_image_rect4, enlarged_image_rect5
    enlarged_image_rect4, enlarged_image_rect5 = None, None
    while True:
        TOPPINGS_POS = pygame.mouse.get_pos()
        imgslide3 = pygame.image.load("display board/img/toppingss.jpg").convert()
        SCREEN.blit(imgslide3, (0, 0)) 

        #PLAY_TEXT1 = get_font(45).render("Select Toppings", True, "Black")
        #PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(355, 200))
        #SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)

        #PLAY_BACK2 = Button(image=None, pos=(250, 850),text_input="BACK", font=get_font(55), base_color="Black", hovering_color="Green")
        BLACK_BOBA = Button(image=pygame.transform.scale(pygame.image.load("display board/img/black.png"), (550, 550)), pos=(550, 630), 
                            text_input="", font=get_font(35), base_color="Black" if 4 not in selected_options['topping'] else "Green", hovering_color="Green")
        WHITE_BOBA = Button(image=pygame.transform.scale(pygame.image.load("display board/img/white.png"), (400, 400)), pos=(1250, 725), 
                            text_input="", font=get_font(35), base_color="Black" if 5 not in selected_options['topping'] else "Green", hovering_color="Green")  
        BUY = Button(image=None, pos=(1590, 950), 
                            text_input="BUY", font=get_font(55), base_color="Black" if len(selected_options['topping']) > 0 else "#808080", hovering_color="Green")
        
        for button in [ BLACK_BOBA, WHITE_BOBA, BUY]:
            button.changeColor(TOPPINGS_POS)
            button.update(SCREEN)

        if enlarged_image_rect4 is not None and 4 in selected_options['topping']:
            # Calculate the center position of the SELECT1 button
            center_x = BLACK_BOBA.rect.x + BLACK_BOBA.rect.width // 2
            center_y = WHITE_BOBA.rect.y + WHITE_BOBA.rect.height // 2

            # Position the enlarged image centered on the button
            enlarged_image_x = center_x - 460
            enlarged_image_y = center_y - 560
            SCREEN.blit(pygame.transform.scale(pygame.image.load("display board/img/black.png"), (800, 800)), (enlarged_image_x, enlarged_image_y))
        if enlarged_image_rect5 is not None and 5 in selected_options['topping']:
            # Calculate the center position of the SELECT1 button
            center_x = WHITE_BOBA.rect.x + WHITE_BOBA.rect.width // 2
            center_y = WHITE_BOBA.rect.y + WHITE_BOBA.rect.height // 2

            # Position the enlarged image centered on the button
            enlarged_image_x = center_x - 270
            enlarged_image_y = center_y - 300
            SCREEN.blit(pygame.transform.scale(pygame.image.load("display board/img/white.png"), (560, 560)), (enlarged_image_x, enlarged_image_y))
        if enlarged_image_rect4 is not None and enlarged_image_rect5 is not None and 4 in selected_options['topping'] and 5 in selected_options['topping']:
             # Calculate the center position of the SELECT1 button
            center_x = BLACK_BOBA.rect.x + BLACK_BOBA.rect.width // 2
            center_y = WHITE_BOBA.rect.y + WHITE_BOBA.rect.height // 2

            # Position the enlarged image centered on the button
            enlarged_image_x = center_x - 460
            enlarged_image_y = center_y - 560
            SCREEN.blit(pygame.transform.scale(pygame.image.load("display board/img/black.png"), (800, 800)), (enlarged_image_x, enlarged_image_y))
            # Calculate the center position of the SELECT1 button
            center_x = WHITE_BOBA.rect.x + WHITE_BOBA.rect.width // 2
            center_y = WHITE_BOBA.rect.y + WHITE_BOBA.rect.height // 2

            # Position the enlarged image centered on the button
            enlarged_image_x = center_x - 270
            enlarged_image_y = center_y - 300
            SCREEN.blit(pygame.transform.scale(pygame.image.load("display board/img/white.png"), (560, 560)), (enlarged_image_x, enlarged_image_y))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                '''
                if PLAY_BACK2.checkForInput(TOPPINGS_POS):
                    sound_button.play()
                    DRINK()
                    '''
                if BLACK_BOBA.checkForInput(TOPPINGS_POS):
                    sound_button.play()
                    if 4 not in selected_options['topping']:
                        selected_options['topping'].append(4)
                    else:
                        selected_options['topping'].remove(4)
                    enlarged_image_rect4 = BLACK_BOBA.rect.copy()
                elif WHITE_BOBA.checkForInput(TOPPINGS_POS):
                    sound_button.play()
                    if 5 not in selected_options['topping']:
                        selected_options['topping'].append(5)
                    else:
                        selected_options['topping'].remove(5)
                    enlarged_image_rect5 = WHITE_BOBA.rect.copy()
                elif BUY.checkForInput(TOPPINGS_POS) and len(selected_options['topping']) > 0:
                    sound_button.play()
                    print(selected_options['topping'])
                    Payment(selected_options['topping'])
                    
        pygame.display.update()      


def DRINK():
    global enlarged_image_rect1, enlarged_image_rect2, enlarged_image_rect3
    enlarged_image_rect1, enlarged_image_rect2, enlarged_image_rect3 = None, None, None
    
    # Khởi tạo biến để lưu lựa chọn của người dùng
    while True:
        DRINK_MOSE_POS = pygame.mouse.get_pos()
        imgslide1 = pygame.image.load("display board/img/drinks.jpg").convert()
        SCREEN.blit(imgslide1, (0,0))

        #PLAY_TEXT1 = get_font(45).render("Select Drink", True, "Black")
        #PLAY_RECT1 = PLAY_TEXT1.get_rect(center=(355, 200))
        #SCREEN.blit(PLAY_TEXT1, PLAY_RECT1)

        PLAY_BACK = Button(image=None, pos=(250, 950), 
                            text_input="BACK", font=get_font(55), base_color="Black", hovering_color="Green")
        SELECT1 = Button(image=pygame.transform.scale(pygame.image.load("display board/img/trà_sữa.png"), (300, 300)), pos=(420, 650), 
                            text_input="", font=get_font(35), base_color="Black" if 1 not in selected_options['drink'] else "Green", hovering_color="Green")
        SELECT2 = Button(image=pygame.transform.scale(pygame.image.load("display board/img/trà_đào.png"), (300, 300)), pos=(970, 650), 
                            text_input="", font=get_font(35), base_color="Black" if 2 not in selected_options['drink'] else "Green", hovering_color="Green")
        SELECT3 = Button(image=pygame.transform.scale(pygame.image.load("display board/img/trà_tắc.png"), (300, 300)), pos=(1480, 650), 
                            text_input="", font=get_font(35), base_color="Black" if 3 not in selected_options['drink'] else "Green", hovering_color="Green")
        NEXT = Button(image=None, pos=(1590, 950), 
                            text_input="NEXT", font=get_font(55), base_color="Black" if len(selected_options['drink']) > 0 else "#808080", hovering_color="Green")

        for button in [PLAY_BACK, SELECT1, SELECT2, SELECT3, NEXT]:
            button.changeColor(DRINK_MOSE_POS)
            button.update(SCREEN)
        
        if enlarged_image_rect1 is not None and 1 in selected_options['drink']:
            # Calculate the center position of the SELECT1 button
            center_x = SELECT1.rect.x + SELECT1.rect.width // 2
            center_y = SELECT1.rect.y + SELECT1.rect.height // 2

            # Position the enlarged image centered on the button
            enlarged_image_x = center_x - 305
            enlarged_image_y = center_y - 300
            SCREEN.blit(pygame.transform.scale(pygame.image.load("display board/img/trà_sữa.png"), (600, 600)), (enlarged_image_x, enlarged_image_y))
        elif enlarged_image_rect2 is not None and 2 in selected_options['drink']:
            center_x = SELECT2.rect.x + SELECT2.rect.width // 2
            center_y = SELECT2.rect.y + SELECT2.rect.height // 2
            enlarged_image_x2 = center_x - 270
            enlarged_image_y2 = center_y - 300
            SCREEN.blit(pygame.transform.scale(pygame.image.load("display board/img/trà_đào.png"), (600, 600)), (enlarged_image_x2, enlarged_image_y2))
        elif enlarged_image_rect3 is not None and 3 in selected_options['drink']:
            center_x = SELECT3.rect.x + SELECT3.rect.width // 2
            center_y = SELECT3.rect.y + SELECT3.rect.height // 2
            enlarged_image_x3 = center_x - 260
            enlarged_image_y3 = center_y - 300
            SCREEN.blit(pygame.transform.scale(pygame.image.load("display board/img/trà_tắc.png"), (600, 600)), (enlarged_image_x3, enlarged_image_y3))
        elif 1 in selected_options['drink']:
            SCREEN.blit(pygame.transform.scale(pygame.image.load("display board/img/trà_sữa.png"), (600, 600)), (SELECT1.rect.x, SELECT1.rect.y))
        elif 2 in selected_options['drink']:
            SCREEN.blit(pygame.transform.scale(pygame.image.load("display board/img/trà_đào.png"), (600, 600)), (SELECT2.rect.x, SELECT2.rect.y))
        elif 3 in selected_options['drink']:
            SCREEN.blit(pygame.transform.scale(pygame.image.load("display board/img/trà_tắc.png"), (600, 600)), (SELECT3.rect.x, SELECT3.rect.y))


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(DRINK_MOSE_POS):
                    sound_button.play()
                    main_menu()
                elif SELECT1.checkForInput(DRINK_MOSE_POS):
                    sound_button.play()
                    if 1 not in selected_options['drink']:
                        selected_options['drink'].append(1)
                    else:
                        selected_options['drink'].remove(1)
                    enlarged_image_rect1 = SELECT1.rect.copy()

                elif SELECT2.checkForInput(DRINK_MOSE_POS):
                    sound_button.play()
                    if 2 not in selected_options['drink']:
                        selected_options['drink'].append(2)
                    else:
                        selected_options['drink'].remove(2)
                    enlarged_image_rect2 = SELECT2.rect.copy()

                elif SELECT3.checkForInput(DRINK_MOSE_POS):
                    sound_button.play()
                    if 3 not in selected_options['drink']:
                        selected_options['drink'].append(3)
                    else:
                        selected_options['drink'].remove(3)
                    enlarged_image_rect3 = SELECT3.rect.copy()

                elif NEXT.checkForInput(DRINK_MOSE_POS) and len(selected_options['drink']) > 0:
                    sound_button.play()
                    print(selected_options['drink'])
                    topping(selected_options['drink'])
                  
        pygame.display.update()


def Payment(selected_options_topping):

    while True:
        PAY_MOUSE_POS = pygame.mouse.get_pos()
        slide_pay = pygame.image.load('display board/img/oder.jpg').convert()
        SCREEN.blit(slide_pay, (0, 0))    
        FRUIT_PAY = get_font(60).render(change_selected_drink(selected_options['drink']), True, "Black")
        ICE_PAY = get_font(60).render((change_selected_topping(selected_options['topping'])), True, "Black")
   
        FRUIT_PAY_RECT = FRUIT_PAY.get_rect(x=600, y=580)  # Use keyword arguments for position
        SCREEN.blit(FRUIT_PAY, FRUIT_PAY_RECT)

        ICE_PAY_RECT = ICE_PAY.get_rect(x=600, y=680)  # Use keyword arguments for position
        SCREEN.blit(ICE_PAY, ICE_PAY_RECT)


        #PLAY_BACK3 = Button(image=None, pos=(250, 850),text_input="BACK", font=get_font(55), base_color="Black", hovering_color="Green")

        NEXT3 = Button(image=None, pos=(1550, 930), 
                                text_input="MENU", font=get_font(55), base_color="Black", hovering_color="Green")


        for button in [NEXT3]:
                button.changeColor(PAY_MOUSE_POS)
                button.update(SCREEN)
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    '''
                    if PLAY_BACK3.checkForInput(PAY_MOUSE_POS):
                        sound_button.play()
                        topping(selected_options['topping'])
                    '''
                        

                    
                    if NEXT3.checkForInput(PAY_MOUSE_POS):
                        sound_button.play()
                        AI()
                        
        pygame.display.update()

def AI():
    while True:
        AI_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        PLAY_BACK_AI = Button(image=None, pos=(250, 850), 
                                text_input="BACK", font=get_font(55), base_color="Black", hovering_color="Green")

        START_AI = Button(image=None, pos=(850, 550), 
                                text_input="START", font=get_font(40), base_color="Black", hovering_color="Green")
        NEXT_AI = Button(image=None, pos=(850, 850), 
                        text_input="NEXT", font=get_font(55), base_color="Black" if len(selected_options['drink']) > 0 else "#808080", hovering_color="Green")


        for button in [PLAY_BACK_AI, START_AI, NEXT_AI]:
            button.changeColor(AI_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK_AI.checkForInput(AI_MOUSE_POS):
                    sound_button.play()
                    Payment()
                if START_AI.checkForInput(AI_MOUSE_POS):
                    sound_button.play()
                    os.system("python Output.py")
                if NEXT_AI.checkForInput(AI_MOUSE_POS):
                    sound_button.play()
                    main_menu()

        pygame.display.update()

main_menu()
