class Personagem:
    # Colocando a arte ASCII fornecida na variável arte_normal
    arte_normal = """
                  ########                 
                ##@@@@@@@@##               
              ########@@@@@@##             
        @@++##++++++++........##    ####MM 
      ##++##  ################    ##++##-- 
      ####    ########----MM##    ####--MM#
          ::::####++--++MM::##    ##++@@##M
        ::      ####--##::##  ##--++++..MM 
        ::        --##++::######--##++..MM 
        @@--      ##--##mm--##  ----##..MM 
        @@##------::--::##--  ..@@    ##   
        @@--##------    ##----  ..    ##   
        ::----##--    ##++##----..  ##     
        ::------##  ##--..  ####----##     
        ::--------------##                 
          ##----    --  ##                 
          ##----  ----##                   
          ##----  ++--##                   
          ########mmmmmm##                 
          ##@@mmmmmmmmmmMM                 
          ##@@mmmmmmmmmmmm##               
        ::@@@@mmmm@@##@@mmmmmm##           
        ::@@@@mmmm##@@@@@@mmmmmm@@         
        ::@@@@@@mm##@@@@@@@@####           
        ::##@@@@############....@@         
          ##------      ##--    --         
          ##--            ----  --         
          ##--  ##        ##--  --         
        ::--..  ##        mm..  @@         
        ::--    ##        --    @@         
        ::--  ##          --  ##           
        ::--  ##          --  ##           
        ::##--##        ##..##             
        ##..##        ##++..##             
        ##..##        ##++..##             
        ##..##          ##..##             
        ##++##--          ##--  @@         
        ##########          ####@@         
    """
    
    arte_ataque = """
                               ..######                                 
                            ####@@@@@@##                               
                          ########@@@@@@##                             
                    ##--##++++++++........##                           
                  ##++MM  ################                             
                  ######  ########----MM##                             
                          ######--      mm::                           
                          ######----  ####                             
                      ####--####----##  ##                    ####     
                  ####  ------++########  ####MM      ++######--..##   
              ::::@@@@mm##..##  --      ..      ....::@@..--mmmm####   
              ++##++....##  ##  --      ------      --@@++++++@@--##   
              mm##++++..##--##  --    ++######--------++##########     
              MM--##++++######--------@@      ########MM               
              ++####  @@----  ------##                                 
                      @@----        ##                                 
                      ::----  ----##                                   
                      ::----  ::--##                                   
                      ::######@@mmmm##                                 
                      ::@@@@@@mmmmmmmm@@                               
                      ::@@@@@@mmmmmmmmMM                               
                      ##@@@@##@@mmmmmmmmmm##                           
                    ##@@@@@@@@##@@mmmmmmmmmm##                         
                    ##@@@@@@@@@@@@@@mmmmmm##  MM                       
                  ##@@@@@@MMMM############..  ::                       
                    ##------##      ##--      MM                       
                    ##..  ##        ##--    ##                         
                  ##--..  ##      ##--..  ##                           
                  ##--  ##      mmMMmm::++                             
                ##--  --      ..++++..@@                               
                ##--  --      ##++..##                                 
                ##----##    ##++..##                                   
              ++++++##        --++..##                                 
              @@++..##          ####--@@                               
              @@..##              ##  @@                               
              @@..##                ##@@                               
            ##++++##--..                                               
            ############                                               
    """
    
    def __init__(self, nome, x, y, lado):
        self.nome = nome
        self.x = x
        self.y = y
        self.lado = lado
        self.pontos = 0
        self.atacando = False

        # Calcular altura e largura da arte
        self.altura = len(self.arte_normal.splitlines())
        self.largura = max(len(line) for line in self.arte_normal.splitlines())

    def desenhar(self, horizontal_margin=0, vertical_margin=0, ring_width=80, ring_height=20):
        arte = self.arte_ataque if self.atacando else self.arte_normal
        lines = arte.splitlines()
        for i, line in enumerate(lines):
            y_pos = self.y + vertical_margin + i
            x_pos = self.x + horizontal_margin
            if 0 <= y_pos < ring_height + vertical_margin and 0 <= x_pos < ring_width + horizontal_margin:
                print(f"\033[{y_pos + 1};{x_pos + 1}H{line}")

    def mover(self, direcao, ring_width, ring_height):
        # Verifica as colisões, considerando a largura e altura do personagem
        if direcao == 'w' and self.y > 0:
            self.y -= 1
        elif direcao == 's' and self.y < ring_height - self.altura:
            self.y += 1
        elif direcao == 'a' and self.x > 0:
            self.x -= 1
        elif direcao == 'd' and self.x < ring_width - self.largura:
            self.x += 1

    def atacar(self, oponente, ring_width):
        self.atacando = True
        if self.lado == "esquerda" and oponente.x - self.x <= 7:
            oponente.receber_dano()
            self.pontos += 1
        elif self.lado == "direita" and self.x - oponente.x <= 7:
            oponente.receber_dano()
            self.pontos += 1
