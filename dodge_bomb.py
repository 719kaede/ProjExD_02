import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1000, 600


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
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

    def tobidasi(rect):
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
            
        if kk_rct.colliderect(bd_rct):
            return
        key_lst = pg.key.get_pressed()#これでキーの情報取得
        #キー:Ture、False　の辞書っぽいものができていて、入力されると該当のアイテムがTrueになる

        sum_mv = [0, 0]
        for k, mv in delta.items():
            if key_lst[k]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)
        if tobidasi(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        print(sum_mv)

        bd_rct.move_ip(vx, vy)

        if tobidasi(bd_rct) == (False, True):
            vx *= -1
        elif tobidasi(bd_rct) == (True, False):
            vy *=-1


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