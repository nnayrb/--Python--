import pygame

#Author Bryann Vianna
#
#
def main():
    #Definicições dos objetos
    pygame.init()
    tela = pygame.display.set_mode([800,600])
    pygame.display.set_caption("Galaxy Lab - OpenSource RJ v1.0")
    relogio = pygame.time.Clock()
    cor_branca = (255,255,255)
    cor_azul = (108,194,236)
    cor_verde = (152, 231,114)
    cor_vermelha = (248, 18, 58)
    cor_rosa = (209, 56, 179)
    sup = pygame.Surface((800,600))
    sup.fill(cor_azul)

    sup2 = pygame.Surface((250, 250))
    #sup2.fill(cor_verde)

    ret = pygame.Rect(10, 10, 45, 45)
    ret2 = pygame.Rect(307,101, 560,20)
    ret3 = pygame.Rect(0, 15, 700, 20)
    ret4 = pygame.Rect(130,101, 700,20)
    ret5 = pygame.Rect(0, 190, 700, 20)
    ret6 = pygame.Rect(130, 400, 700, 20)
    ret7 = pygame.Rect(0,700, 700,20)
    ret8 = pygame.Rect(130, 900, 700, 20)

    sair = False

    fundo = pygame.image.load("./img/galaxyas.jpg")


    pygame.font.init()

    font_padrao = pygame.font.get_default_font()
    fonte_lose = pygame.font.SysFont(font_padrao, 45)
    #fonte_ganhou = pygame.font.SysFont(font_padrao, 30)
    audio_explosao = pygame.mixer.Sound('./efeitos/sonoros/explosao.ogg')
    #audio_ganhou = pygame.mixer.Sound('./efeitos/sonoros/ganhou.ogg')

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(740,30)

            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_a:
                   #ret.move_ip(-10,0)
                #if event.key == pygame.K_d:
                   #ret.move_ip(10,0)
                #if event.key == pygame.K_w:
                   #ret.move_ip(0, -10)
                #if event.key == pygame.K_s:
                   # ret.move_ip(0, 10)
                #if event.key == pygame.K_e:
                   # ret.move_ip(10,10)
                #if event.key == pygame.K_q:
                    #ret.move_ip(-10,-10)


        relogio.tick(60)
        #tela.fill(cor_branca)
        tela.blit(sup, [0,0]) #retangulo    1
        tela.blit(fundo, [0,0])
        #tela.blit(sup2, [200, 200]) #retangulo 2

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width/2
        ret.top -= ret.height/2

        if ret.colliderect(ret2):
            text = fonte_lose.render('Bateu !! ai ta na Disney !!', 1, (255, 255,255))
            audio_explosao.play()
            audio_explosao.set_volume(0.020)
            tela.blit(text, (150,150))
            (ret.left, ret.top) = (xant, yant)

        if ret.colliderect(ret3):
            text = fonte_lose.render('Bateu !! ai ta na Disney !!', 1, (255, 255,255))
            audio_explosao.play()
            audio_explosao.set_volume(0.020)
            tela.blit(text, (150,150))
            (ret.left, ret.top) = (xant, yant)

        if ret.colliderect(ret4):
            text = fonte_lose.render('Bateu !! ai ta na Disney !!', 1, (255, 255,255))
            audio_explosao.play()
            audio_explosao.set_volume(0.020)
            tela.blit(text, (150,150))
            (ret.left, ret.top) = (xant, yant)

        if ret.colliderect(ret5):
            text = fonte_lose.render('Bateu !! ai ta na Disney !!', 1, (255, 255,255))
            audio_explosao.play()
            audio_explosao.set_volume(0.020)
            tela.blit(text, (150,150))
            (ret.left, ret.top) = (xant, yant)

        if ret.colliderect(ret6):
            text = fonte_lose.render('Bateu !! ai ta na Disney !!', 1, (255, 255,255))
            audio_explosao.play()
            audio_explosao.set_volume(0.020)
            tela.blit(text, (150,150))
            (ret.left, ret.top) = (xant, yant)

        if ret.colliderect(ret7):
            text = fonte_lose.render('Bateu !! ai ta na Disney !!', 1, (255, 255,255))
            audio_explosao.play()
            audio_explosao.set_volume(0.020)
            tela.blit(text, (150,150))
            (ret.left, ret.top) = (xant, yant)

        if ret.colliderect(ret8):
            text = fonte_lose.render('Bateu !! ai ta na Disney !!', 1, (255, 255,255))
            audio_explosao.play()
            audio_explosao.set_volume(0.020)
            tela.blit(text, (150,150))
            (ret.left, ret.top) = (xant, yant)


        pygame.draw.rect(tela, cor_vermelha, ret)
        pygame.draw.rect(tela, cor_rosa, ret2)
        pygame.draw.rect(tela, cor_rosa, ret3)
        pygame.draw.rect(tela, cor_rosa, ret4)
        pygame.draw.rect(tela, cor_rosa, ret5)
        pygame.draw.rect(tela, cor_rosa, ret6)
        pygame.draw.rect(tela, cor_rosa, ret7)
        pygame.draw.rect(tela, cor_rosa, ret8)
        pygame.display.update()
    pygame.quit()


main()
