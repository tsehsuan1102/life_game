import pygame as pg
import pygame.gfxdraw as gfxdraw
import math, random
import pygame.sprite as ps
import View.const as viewConst
import Model.const as modelConst
import sys


class Viewer():
    """docstring for Viewer"""
    def __init__(self, model):
        self.gameSurface = None
        self.model = model
        # init pygame modules
        pg.mixer.pre_init(44100, -16, 2, 2048)
        pg.init()

        # init game window
        pg.display.set_caption(viewConst.GameCaption)
        self.screen = pg.display.set_mode(viewConst.ScreenSize)
        self.renderSurface = pg.Surface(viewConst.ScreenSize)

        ####Font
        self.titleFont = pg.font.Font(viewConst.titleFont, viewConst.titleFontSize)
        self.titleSmallFont = pg.font.Font(viewConst.titleSmallFont, viewConst.titleSmallFontSize)
        self.teamNameFont = pg.font.Font(viewConst.teamNameFont, viewConst.teamNameFontSize)
        self.teamLengthFont = pg.font.Font(viewConst.teamLengthFont, viewConst.teamLengthFontSize)
        self.teamScoreFont = pg.font.Font(viewConst.teamScoreFont, viewConst.teamScoreFontSize)
        self.countDownFont = pg.font.Font(viewConst.countDownFont, viewConst.countDownFontSize)
        self.tmpScoreFont = pg.font.Font(viewConst.tmpScoreFont, viewConst.tmpScoreFontSize)

    def Update(self):
        # The main game loop
        self.draw_infomation()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit_game()

        # Redraw the background
        self.screen.fill(viewConst.Color_Silver)
        pg.display.flip()
        #self.screen.blit( (400,300))
        #pg.display.update()

    def draw_infomation(self):
        # Frame
        timer = 100
        while timer > 0:
            timer -= 1
            pg.draw.line(self.screen, viewConst.Color_Black, (0,0), (600,600), 50)
            pg.display.flip()
            pg.display.update()

            color = viewConst.Color_Gold
            pos = [[100,300], [300,300] ]
            Names = [self.model.player1.name, self.model.player2.name]
            HP = self.tmpScoreFont.render(str(self.model.player1.hp), True, color)
            self.renderSurface.blit(HP, pos[0])
            self.screen.blit(self.renderSurface, pos[0] )

'''
        for i, player in enumerate(self.model.player_list):
            color = viewConst.aliveTeamColor if player.is_alive else viewConst.deadTeamColor
            teamName = self.teamNameFont.render(player.name, True, color)
            self.renderSurface.blit(teamName, pos[i])
        # Team Scores
        pos = [(x, y + viewConst.GameSize[1] // 32) for x, y in pos]
        for i, player in enumerate(self.model.player_list):
            color = viewConst.Color_Black
            teamScore = self.teamScoreFont.render(str(self.model.score_list[player.index]), True, color)
            self.renderSurface.blit(teamScore, pos[i])

        for i in range(1, modelConst.PlayerNum):
            gfxdraw.hline(self.renderSurface, viewConst.GameSize[0],
                          viewConst.ScreenSize[0],
                          viewConst.GameSize[1] // modelConst.PlayerNum * i, viewConst.sbColor)
        # Team Names
        pos = [(viewConst.GameSize[0] + viewConst.GameSize[1] // modelConst.PlayerNum, viewConst.GameSize[1] // modelConst.PlayerNum * i + viewConst.GameSize[1] // (modelConst.PlayerNum * 8)) for i in range(modelConst.PlayerNum)]
        for i, player in enumerate(self.model.player_list):
            color = viewConst.aliveTeamColor if player.is_alive else viewConst.deadTeamColor
            teamName = self.teamNameFont.render(player.name, True, color)
            self.renderSurface.blit(teamName, pos[i])
        # Team Scores
        pos = [(x, y + viewConst.GameSize[1] // 32) for x, y in pos]
        for i, player in enumerate(self.model.player_list):
            color = viewConst.Color_Black
            teamScore = self.teamScoreFont.render(str(self.model.score_list[player.index]), True, color)
            self.renderSurface.blit(teamScore, pos[i])
        # Team Balls
        pos = [(viewConst.GameSize[0] + viewConst.GameSize[1] // (modelConst.PlayerNum * 2), viewConst.GameSize[1] // (modelConst.PlayerNum * 2) * i) for i in range(1, modelConst.PlayerNum * 2, 2)]
        radius = int(viewConst.GameSize[1] // (modelConst.PlayerNum * 2) * 0.7)
        for i, player in enumerate(self.model.player_list):
            if self.model.have_scoreboard[i]:
                ballPos = tuple([x + random.randint(-5, 5) for x in pos[i]]) if self.model.bombtimer[i] != -1 else pos[i]
                if self.model.bombtimer[i] == modelConst.bombtime - 1:
                    self.vibrationSound.play()
                gfxdraw.filled_circle(self.renderSurface, *ballPos, radius, player.color)
        # Team Player Lengths
        for i, player in enumerate(self.model.player_list):
            length = str(len(player.body_list)) if player.is_alive else '0'
            color = viewConst.teamLengthColor if self.model.have_scoreboard[i] else viewConst.Color_Black
            teamLength = self.teamLengthFont.render(length, True, color)
            self.blit_at_center(self.renderSurface, teamLength, pos[i])
'''










