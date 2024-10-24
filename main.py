import pgzrun
import random
from time import sleep
from pgzero import clock

WIDTH = 800
HEIGHT = 500
TITLE = "NamaClicker v1.0.0"

achievements_displayed = False
condition_met = False

ambient = random.randint(1,4)
if ambient == 1:
    sounds.ost1.play(-1)
elif ambient == 2:
    sounds.ost2.play(-1)
elif ambient == 3:
    sounds.ost3.play(-1)
elif ambient == 4:
    sounds.ost4.play(-1)

def random_tama():
    global tamas
    rare = [1,12,11,1,5,2,2,2,2,3,3,3,4,4,5,6,6,7,9,8,8,7,9,10]
    rare_choice = random.choice(rare)
    if rare_choice == 1:
        namatama.image = 'like'
        tamas.append('1')
    elif rare_choice == 2:
        namatama.image = 'bob'
        tamas.append('2')
    elif rare_choice == 3:
        namatama.image = 'vibe'
        tamas.append('3')
    elif rare_choice == 4:
        namatama.image = 'gun'
        tamas.append('4')
    elif rare_choice == 5:
        namatama.image = 'evil'
        tamas.append('5')
    elif rare_choice == 6:
        namatama.image = 'demon'
        tamas.append('6')
    elif rare_choice == 7:
        namatama.image = 'builder'
        tamas.append('7')
    elif rare_choice == 8:
        namatama.image = 'tea'
        tamas.append('8')
    elif rare_choice == 9:
        namatama.image = 'birthday'
        tamas.append('9')
    elif rare_choice == 10:
        namatama.image = 'kinger'
        tamas.append('10')
    elif rare_choice == 11:
        namatama.image = 'stone'
        tamas.append('11')
    elif rare_choice == 12:
        namatama.image = 'evil'
        tamas.append('12')

def hide_achi():
    global achievements_displayed
    achievements_displayed = True

namatama = Actor('classic', (400,150))

button_boost = Actor('button', (100,400))
button_menu = Actor('button', (100,465))
button_start = Actor('button', (400,250))
button_achi = Actor('button', (400,200))
button_credits = Actor('button', (400,300))
button_achi_back = Actor('button', (100,465))
button_credits_back = Actor('button', (100,456))
button_upd = Actor('button', (700,466))
button_upd_back = Actor('button', (100,465))

price = 250
boost = 1

frame1 = Actor('frame', (100, 50))
frame2 = Actor('frame', (400, 50))
frame3 = Actor('frame', (700, 50))
frame4 = Actor('frame', (100, 180))
frame5 = Actor('frame', (400, 180))
frame6 = Actor('frame', (700, 180))

mode = 'menu'
clicks = 0
tamas = []

def draw():
    global clicks, achievements_displayed, condition_met
    if mode == 'menu':
        screen.fill('#583E26')
        button_start.draw()
        button_achi.draw()
        button_credits.draw()
        screen.draw.text("Играть",center=(400,250))
        screen.draw.text("Ачивки",center=(400,200))
        screen.draw.text("Честь", center=(400,300))
        screen.draw.text("NamaClicker", center=(400,100), fontsize=(100))
        button_upd.draw()
        screen.draw.text("Обновления", center=(700,466))
    if mode == 'game':
        screen.fill('#A78B71')
        namatama.draw()
        button_boost.draw()
        screen.draw.text(f"Буст: + {boost} \n {price} Кликов", center=(100,402))
        button_menu.draw()
        screen.draw.text("Меню", center=(100,465))
        if clicks == 0:
            screen.draw.text("Каждые 10 кликов, появляется новое изображение", center=(400,280), color='black', fontsize=(29))
            screen.draw.text("Нажми на Намутаму, чтобы начать", center=(400,300), color='black', fontsize=(35))
        screen.draw.text(str(clicks), center=(400,410), fontsize=75, color='black')
        if '1' in tamas and '2' in tamas and '3' in tamas and '4' in tamas and '5' in tamas and '6' in tamas and '7' in tamas and '8' in tamas and '9' in tamas and '10' in tamas and '11' in tamas and '12' in tamas:
            if not achievements_displayed:
                sounds.new_achievement.play()
                achievements_displayed = True
                screen.draw.text("Новая очивка: Master", center=(400,280), color='black')
                clock.schedule_unique(hide_achi, 1)
                achievements_displayed = False
                condition_met = True
        if clicks == 1000:
            sounds.new_achievement.play()
            screen.draw.text("Новая очивка: Master Clicker", center=(400,280), color='black')
        elif clicks == 5000:
            sounds.new_achievement.play()
            screen.draw.text("Новая очивка: Super Master CLicker", center=(400,280), color='black')
        elif clicks == 10000:
            sounds.new_achievement.play()
            screen.draw.text("Новая очивка: BugUse", center=(400,280), color='black')
        elif clicks == 100000:
            sounds.new_achievement.play()
            screen.draw.text("Новая очивка: Legend", center=(400,280), color='black')
        elif clicks == 1000000:
            sounds.new_achievement.play()
            screen.draw.text("Новая очивка: God", center=(400,280), color='black')
    if mode == 'achievements':
        screen.fill('#9C4A1A')
        button_achi_back.draw()
        screen.draw.text("Назад", center=(100,465))
        if clicks >= 1000:
            frame1.draw()
            screen.draw.text('Master Clicker \nНаберите 1K кликов', center=(100,45), color='black')
        if clicks >= 5000:
            frame2.draw()
            screen.draw.text("Super Master Clicker \nНаберите 5K кликов", center=(400,45), color='black')
        if clicks >= 10000:
            frame3.draw()
            screen.draw.text("BugUse \nНаберите 10K кликов", center=(700,45), color='black')
        if clicks >= 100000:
            frame4.draw()
            screen.draw.text("Legend \nНаберите 100K кликов", center=(100, 175), color='black')
        if clicks >= 1000000:
            frame5.draw()
            screen.draw.text("God \nНаберите 1M кликов", center=(400,175), color='black')
        if '1' in tamas and '2' in tamas and '3' in tamas and '4' in tamas and '5' in tamas and '6' in tamas and '7' in tamas and '8' in tamas and '9' in tamas and '10' in tamas and '11' in tamas and '12' in tamas:
            frame6.draw()
            screen.draw.text("Master \nСоберите все виды", center=(700, 180), color='black')
        else:
            screen.draw.text("Ты пока не получил ни одного достижения =(", center=(400,250), color='black')
    if mode == 'credits':
        screen.fill('#EC9704')
        screen.draw.text('Спасибо за то, что играете в мою игру. \nРазработчик - timoxha \nТестер - timoxha \nХудожники - Embark Studios, Nexon Corp. \nВсе права принадлежат компании Embark Studios, и их продукту THE FINALS (C)', center=(400,250), fontsize=(28))
        button_credits_back.draw()
        screen.draw.text('Назад', center=(100,456))
    if mode == 'upd':
        screen.fill('#F7C815')
        screen.draw.text('Обновление 1.0.0 \n-Релиз', center=(400,250), color='black')
        button_upd_back.draw()
        screen.draw.text("Назад", center=(100,466))

def on_mouse_down(pos):
    global clicks, mode, boost, price
    if mode == 'game':
        if namatama.collidepoint(pos):
            clicks += 1 * boost
            sounds.click.play()
            if clicks % 10 == 0:
                random_tama()
        if button_menu.collidepoint(pos):
            mode = 'menu'
        if button_boost.collidepoint(pos):
            if clicks >= price:
                sounds.success.play()
                boost *= 2
                if boost == 10:
                    boost = 1
                clicks -= price 
                price *= 2
            else:
                sounds.denied.play()
    if mode == 'menu':
        if button_start.collidepoint(pos):
            mode = 'game'
        if button_achi.collidepoint(pos):
            mode = 'achievements'
        if button_credits.collidepoint(pos):
            mode = 'credits'
        if button_upd.collidepoint(pos):
            mode = 'upd'
    if mode == 'achievements':
        if button_achi_back.collidepoint(pos):
            mode = 'menu'
    if mode == 'credits':
        if button_credits_back.collidepoint(pos):
            mode = 'menu'
    if mode == 'upd':
        if button_upd_back.collidepoint(pos):
            mode = 'menu'
    

pgzrun.go()