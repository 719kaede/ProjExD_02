import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    bom_img = pg.Surface((20, 20))
    bom_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bom_img, (255, 0, 0), (10, 10), 10)
    x=random.randint(0, WIDTH)
    y=random.randint(0, HEIGHT)
    bd_rct = bom_img.get_rect()
    bd_rct.center = x, y
    vx, vy = +5, +5
    delta = {pg.K_UP:(0, -5), pg.K_DOWN:(0, +5), pg.K_LEFT:(-5, 0), pg.K_RIGHT:(+5, 0),}
    clock = pg.time.Clock()
    tmr = 0

    def bom_bound(rect):
        yoko, tate = True, True
        if rect.left < 0 or WIDTH < rect.right:
            yoko = False
        if rect.top < 0 or HEIGHT < rect.bottom:
            tate = False
        return yoko, tate
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        key_lst = pg.key.get_pressed()#これでキーの情報取得
        #キー:Ture、False　の辞書っぽいものができていて、入力されると該当のアイテムがTrueになる

        for k, mv in delta.items():
            if key_lst[k]:
                print(key_lst[k])
                kk_rct.move_ip((mv))
        bd_rct.move_ip(vx, vy)


        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        screen.blit(bom_img, bd_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()