import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1000, 600


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img1 = pg.transform.rotozoom(kk_img, 0, 2.0)#(-5, 0)
    kk_img2 = pg.transform.rotozoom(kk_img, 315, 2.0)#(-5, -5)
    kk_img3_k = pg.transform.flip(kk_img, True, False)
    kk_img3 = pg.transform.rotozoom(kk_img3_k, 90, 2.0)#(0, -5)
    kk_img4_k = pg.transform.flip(kk_img, True, False)#(5, -5)
    kk_img4 = pg.transform.rotozoom(kk_img4_k, 45, 2.0)
    kk_img5_k = pg.transform.flip(kk_img, True, False)
    kk_img5 = pg.transform.rotozoom(kk_img5_k, 0, 2.0)#(5, 0)
    kk_img6_k = pg.transform.flip(kk_img, True, False)
    kk_img6 = pg.transform.rotozoom(kk_img6_k, 315, 2.0)#(5, 5)
    kk_img7_k = pg.transform.flip(kk_img, True, False)
    kk_img7 = pg.transform.rotozoom(kk_img7_k, 270, 2.0)#(0, 5)
    kk_img8 = pg.transform.rotozoom(kk_img, 45, 2.0)#(-5, 5)
    kk_img_d = {(0, 0):kk_img1, 
                (-5, 0):kk_img1, 
                (-5, -5):kk_img2, 
                (0, -5):kk_img3, 
                (5, -5):kk_img4, 
                (5, 0):kk_img5, 
                (5, 5):kk_img6, 
                (0, 5):kk_img7, 
                (-5, 5):kk_img8}
    kk_img_owari = pg.image.load("ex02/fig/8.png")
    kk_img_owari = pg.transform.rotozoom(kk_img_owari, 0, 2.0)
    kk_rct = kk_img1.get_rect()
    kk_rct.center = 900, 400

    #ここから爆弾について
    bom_img = pg.Surface((20, 20))
    bom_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bom_img, (255, 0, 0), (10, 10), 10)
    x=random.randint(0, WIDTH)
    y=random.randint(0, HEIGHT)
    bd_rct = bom_img.get_rect()
    bd_rct.center = x, y
    vx, vy = +5, +5
    accs = [a for a in range(1, 11)]

    owari = True
    #sa_ve = [0, 0]
    
    
    delta = {pg.K_UP:(0, -5), 
             pg.K_DOWN:(0, +5), 
             pg.K_LEFT:(-5, 0), 
             pg.K_RIGHT:(+5, 0),}
    clock = pg.time.Clock()
    tmr = 0

    def tobidasi(rect):
        yoko, tate = True, True
        if rect.left < 0 or WIDTH < rect.right:
            yoko = False
        if rect.top < 0 or HEIGHT < rect.bottom:
            tate = False
        return yoko, tate
    
    #def seikika(a, b):
    #    sqrt(a**2+b**2)
    #    a/(a+b)
    #    b/(a+b)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        if owari:
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

            #sa_vx, sa_vy = seikika(kk_rct[0]-bd_rct[0], kk_rct[1]-bd_rct[1])
            avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)]
            bd_rct.move_ip(avx, avy)

            if tobidasi(bd_rct) == (False, True):
                print("tobi")
                vx *= -1
            elif tobidasi(bd_rct) == (True, False):
                print("tobi")
                vy *=-1

            tmr_o = tmr
            screen.blit(bg_img, [0, 0])
            screen.blit(kk_img_d[tuple(sum_mv)], kk_rct)
            screen.blit(bom_img, bd_rct)
            pg.display.update()

        if kk_rct.colliderect(bd_rct):
            screen.blit(bg_img, [0, 0])
            screen.blit(kk_img_owari, kk_rct)
            screen.blit(bom_img, bd_rct)
            pg.display.update()
            owari = False
        
        print(tmr_o-tmr)
        if tmr_o-tmr <= -150:
            return
        
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()