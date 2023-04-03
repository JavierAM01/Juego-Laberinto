

"""dimensiones: NX = 50, NY = 50, DIM = 15 """

mapa1 = [[0, 0], [735, 735], [0, 30], [0, 45], [0, 60], [0, 75], [0, 105], [0, 120], [0, 135], [0, 150], [0, 165], [0, 180], [0, 195], [0, 210], [0, 90], [0, 225], [0, 240], [0, 450], [0, 465], [0, 480], [0, 495], [0, 510], [0, 525], [0, 540], [0, 555], [0, 570], [0, 585], [0, 600], [0, 615], [0, 630], [0, 645], [0, 660], [0, 675], [0, 705], [0, 690], [30, 735], [45, 735], [60, 735], [75, 735], [90, 735], [105, 735], [120, 735], [135, 735], [150, 735], [165, 735], [180, 735], [195, 735], [210, 735], [225, 735], [240, 735], [255, 735], [270, 735], [285, 735], [450, 735], [465, 735], [480, 735], [495, 735], [510, 735], [525, 735], [540, 735], [555, 735], [570, 735], [585, 735], [600, 735], [615, 735], [630, 735], [645, 735], [660, 735], [675, 735], [690, 735], [705, 735], [735, 705], [735, 690], [735, 675], [735, 660], [735, 645], [735, 630], [735, 615], [735, 600], [735, 585], [735, 570], [735, 555], [735, 540], [735, 495], [735, 480], [735, 510], [735, 525], [735, 465], [735, 450], [390, 735], [375, 735], [360, 735], [345, 735], [735, 390], [735, 375], [735, 360], [735, 345], [735, 285], [735, 270], [735, 255], [735, 240], [735, 225], [735, 210], [735, 195], [735, 180], [735, 165], [735, 150], [735, 135], [735, 120], [735, 105], [735, 90], [735, 75], [735, 60], [735, 45], [735, 30], [705, 0], [690, 0], [675, 0], [660, 0], [645, 0], [630, 0], [615, 0], [600, 0], [585, 0], [570, 0], [555, 0], [540, 0], [525, 0], [510, 0], [450, 0], [465, 0], [480, 0], [495, 0], [0, 375], [0, 360], [0, 345], [0, 390], [0, 285], [0, 270], [0, 255], [30, 0], [45, 0], [60, 0], [75, 0], [90, 0], [105, 0], [120, 0], [135, 0], [150, 0], [165, 0], [180, 0], [195, 0], [255, 0], [240, 0], [225, 0], [210, 0], [270, 0], [285, 0], [390, 0], [375, 0], [360, 0], [345, 0], [270, 255], [285, 255], [300, 255], [315, 255], [330, 255], [345, 255], [390, 255], [405, 255], [420, 255], [435, 255], [450, 255], [465, 255], [480, 255], [480, 270], [480, 285], [480, 300], [480, 315], [480, 330], [480, 345], [480, 390], [480, 405], [480, 420], [480, 435], [480, 450], [480, 465], [480, 480], [465, 480], [450, 480], [420, 480], [405, 480], [390, 480], [345, 480], [330, 480], [315, 480], [300, 480], [285, 480], [270, 480], [255, 480], [255, 465], [255, 450], [255, 435], [255, 420], [255, 405], [255, 390], [255, 345], [255, 330], [255, 315], [255, 300], [255, 285], [255, 270], [255, 255], [435, 480], [390, 405], [405, 390], [405, 345], [390, 330], [345, 330], [330, 345], [330, 390], [345, 405], [0, 720], [15, 735], [720, 735], [735, 720], [720, 0], [735, 15], [0, 15], [15, 0], [0, 735], [735, 0], [240, 690], [255, 690], [270, 690], [285, 690], [300, 690], [330, 690], [405, 690], [420, 690], [435, 690], [450, 690], [465, 690], [495, 690], [315, 690], [480, 690], [510, 690], [525, 690], [540, 690], [555, 690], [225, 690], [210, 690], [195, 690], [180, 690], [165, 690], [570, 690], [150, 690], [135, 690], [120, 690], [105, 690], [45, 690], [45, 675], [45, 660], [45, 645], [45, 630], [45, 615], [45, 600], [45, 585], [45, 570], [45, 555], [45, 540], [45, 525], [45, 510], [45, 495], [45, 480], [45, 465], [45, 450], [45, 435], [45, 420], [45, 405], [45, 330], [45, 315], [45, 300], [45, 285], [45, 270], [45, 255], [45, 240], [45, 225], [45, 210], [45, 195], [45, 180], [45, 165], [45, 150], [45, 135], [45, 120], [45, 105], [45, 45], [60, 45], [75, 45], [90, 45], [105, 45], [120, 45], [135, 45], [150, 45], [165, 45], [180, 45], [210, 45], [195, 45], [225, 45], [240, 45], [255, 45], [270, 45], [285, 45], [300, 45], [315, 45], [330, 45], [405, 45], [420, 45], [435, 45], [450, 45], [465, 45], [480, 45], [495, 45], [510, 45], [525, 45], [540, 45], [555, 45], [570, 45], [585, 45], [600, 45], [615, 45], [630, 45], [690, 45], [690, 60], [690, 75], [690, 90], [690, 105], [690, 120], [690, 135], [690, 150], [690, 165], [690, 180], [690, 195], [690, 210], [690, 225], [690, 240], [690, 255], [690, 270], [690, 285], [690, 300], [690, 315], [690, 330], [690, 405], [690, 420], [690, 435], [690, 450], [690, 465], [690, 480], [690, 495], [690, 510], [690, 525], [690, 540], [690, 555], [690, 570], [690, 585], [690, 600], [690, 615], [690, 630], [690, 690], [675, 690], [660, 690], [645, 690], [630, 690], [615, 690], [600, 690], [585, 690], [330, 330], [405, 330], [330, 405], [405, 405], [525, 315], [540, 315], [540, 330], [540, 345], [540, 360], [540, 375], [540, 390], [540, 405], [540, 420], [525, 420], [420, 525], [420, 540], [405, 540], [390, 540], [375, 540], [360, 540], [345, 540], [330, 540], [315, 540], [315, 525], [210, 420], [195, 420], [195, 405], [195, 390], [195, 375], [195, 360], [195, 345], [195, 330], [195, 315], [210, 315], [315, 195], [330, 195], [345, 195], [360, 195], [375, 195], [390, 195], [405, 195], [420, 195], [420, 210], [315, 210], [120, 285], [120, 270], [270, 120], [285, 120], [120, 255], [135, 255], [135, 240], [135, 225], [150, 225], [150, 210], [150, 195], [165, 195], [165, 180], [165, 165], [255, 135], [240, 135], [225, 135], [255, 120], [225, 150], [210, 150], [195, 150], [195, 165], [180, 165], [450, 120], [465, 120], [480, 120], [480, 135], [495, 135], [510, 135], [510, 150], [525, 150], [540, 150], [540, 165], [555, 165], [570, 165], [570, 180], [570, 195], [585, 195], [585, 210], [585, 225], [600, 225], [600, 240], [600, 255], [615, 255], [615, 270], [615, 285], [615, 450], [615, 465], [615, 480], [600, 480], [600, 495], [600, 510], [585, 510], [585, 525], [585, 540], [570, 540], [570, 555], [570, 570], [555, 570], [540, 570], [540, 585], [525, 585], [510, 585], [510, 600], [495, 600], [480, 600], [480, 615], [465, 615], [450, 615], [285, 615], [270, 615], [255, 615], [255, 600], [240, 600], [225, 600], [225, 585], [210, 585], [195, 585], [195, 570], [180, 570], [165, 570], [165, 555], [165, 540], [150, 540], [150, 525], [150, 510], [135, 510], [135, 495], [135, 480], [120, 480], [120, 465], [120, 450], [150, 360], [135, 360], [120, 360], [105, 360], [90, 360], [150, 375], [135, 375], [120, 375], [105, 375], [90, 375], [360, 150], [375, 150], [375, 135], [375, 120], [375, 105], [375, 90], [360, 90], [360, 105], [360, 120], [360, 135], [585, 360], [585, 375], [600, 375], [615, 375], [630, 375], [630, 360], [615, 360], [600, 360], [645, 360], [645, 375], [375, 585], [360, 585], [360, 600], [360, 615], [360, 630], [360, 645], [375, 645], [375, 630], [375, 615], [375, 600], [720, 285], [720, 450], [15, 285], [15, 450], [450, 15], [285, 15], [450, 720], [285, 720], [90, 225], [90, 180], [90, 135], [90, 90], [135, 90], [180, 90], [225, 90], [135, 135], [510, 90], [555, 90], [600, 90], [645, 90], [645, 135], [645, 180], [645, 225], [600, 135], [645, 510], [645, 555], [645, 600], [645, 645], [600, 645], [555, 645], [510, 645], [600, 600], [90, 510], [225, 645], [180, 645], [135, 645], [90, 555], [90, 600], [135, 600], [90, 645], [15, 360], [30, 360], [45, 360], [60, 360], [75, 360], [75, 375], [60, 375], [45, 375], [30, 375], [15, 375], [660, 360], [675, 360], [690, 360], [705, 360], [720, 360], [720, 375], [705, 375], [690, 375], [675, 375], [660, 375], [375, 570], [375, 555], [360, 555], [360, 570], [375, 180], [375, 165], [360, 165], [360, 180]]

c1_usuario = [330, 300]
c1_snake   = [330, 735]
c1_killer  = [735, 315]

def get_map(level=1):
    if level == 1:
        return mapa1, c1_usuario, c1_snake, c1_killer


mapa2 = [[0, 0], [735, 735], [0, 30], [0, 45], [0, 60], [0, 75], [0, 105], [0, 120], [0, 135], [0, 150], [0, 165], [0, 180], [0, 195], [0, 210], [0, 90], [0, 225], [0, 240], [0, 450], [0, 465], [0, 480], [0, 495], [0, 510], [0, 525], [0, 540], [0, 555], [0, 570], [0, 585], [0, 600], [0, 615], [0, 630], [0, 645], [0, 660], [0, 675], [0, 705], [0, 690], [30, 735], [45, 735], [60, 735], [75, 735], [90, 735], [105, 735], [120, 735], [135, 735], [150, 735], [165, 735], [180, 735], [195, 735], [210, 735], [225, 735], [240, 735], [255, 735], [270, 735], [285, 735], [450, 735], [465, 735], [480, 735], [495, 735], [510, 735], [525, 735], [540, 735], [555, 735], [570, 735], [585, 735], [600, 735], [615, 735], [630, 735], [645, 735], [660, 735], [675, 735], [690, 735], [705, 735], [735, 705], [735, 690], [735, 675], [735, 660], [735, 645], [735, 630], [735, 615], [735, 600], [735, 585], [735, 570], [735, 555], [735, 540], [735, 495], [735, 480], [735, 510], [735, 525], [735, 465], [735, 450], [390, 735], [375, 735], [360, 735], [345, 735], [735, 390], [735, 375], [735, 360], [735, 345], [735, 285], [735, 270], [735, 255], [735, 240], [735, 225], [735, 210], [735, 195], [735, 180], [735, 165], [735, 150], [735, 135], [735, 120], [735, 105], [735, 90], [735, 75], [735, 60], [735, 45], [735, 30], [705, 0], [690, 0], [675, 0], [660, 0], [645, 0], [630, 0], [615, 0], [600, 0], [585, 0], [570, 0], [555, 0], [540, 0], [525, 0], [510, 0], [450, 0], [465, 0], [480, 0], [495, 0], [0, 375], [0, 360], [0, 345], [0, 390], [0, 285], [0, 270], [0, 255], [30, 0], [45, 0], [60, 0], [75, 0], [90, 0], [105, 0], [120, 0], [135, 0], [150, 0], [165, 0], [180, 0], [195, 0], [255, 0], [240, 0], [225, 0], [210, 0], [270, 0], [285, 0], [390, 0], [375, 0], [360, 0], [345, 0], [270, 255], [285, 255], [300, 255], [315, 255], [330, 255], [345, 255], [390, 255], [405, 255], [420, 255], [435, 255], [450, 255], [465, 255], [480, 255], [480, 270], [480, 285], [480, 300], [480, 315], [480, 330], [480, 345], [480, 390], [480, 405], [480, 420], [480, 435], [480, 450], [480, 465], [480, 480], [465, 480], [450, 480], [420, 480], [405, 480], [390, 480], [345, 480], [330, 480], [315, 480], [300, 480], [285, 480], [270, 480], [255, 480], [255, 465], [255, 450], [255, 435], [255, 420], [255, 405], [255, 390], [255, 345], [255, 330], [255, 315], [255, 300], [255, 285], [255, 270], [255, 255], [435, 480], [390, 405], [405, 390], [405, 345], [390, 330], [345, 330], [330, 345], [330, 390], [345, 405], [0, 720], [15, 735], [720, 735], [735, 720], [720, 0], [735, 15], [0, 15], [15, 0], [0, 735], [735, 0], [240, 690], [255, 690], [270, 690], [285, 690], [300, 690], [330, 690], [405, 690], [420, 690], [435, 690], [450, 690], [465, 690], [495, 690], [315, 690], [480, 690], [510, 690], [525, 690], [540, 690], [555, 690], [225, 690], [210, 690], [195, 690], [180, 690], [165, 690], [570, 690], [150, 690], [135, 690], [120, 690], [105, 690], [45, 690], [45, 675], [45, 660], [45, 645], [45, 630], [45, 615], [45, 600], [45, 585], [45, 570], [45, 555], [45, 540], [45, 525], [45, 510], [45, 495], [45, 480], [45, 465], [45, 450], [45, 435], [45, 420], [45, 405], [45, 330], [45, 315], [45, 300], [45, 285], [45, 270], [45, 255], [45, 240], [45, 225], [45, 210], [45, 195], [45, 180], [45, 165], [45, 150], [45, 135], [45, 120], [45, 105], [45, 45], [60, 45], [75, 45], [90, 45], [105, 45], [120, 45], [135, 45], [150, 45], [165, 45], [180, 45], [210, 45], [195, 45], [225, 45], [240, 45], [255, 45], [270, 45], [285, 45], [300, 45], [315, 45], [330, 45], [405, 45], [420, 45], [435, 45], [450, 45], [465, 45], [480, 45], [495, 45], [510, 45], [525, 45], [540, 45], [555, 45], [570, 45], [585, 45], [600, 45], [615, 45], [630, 45], [690, 45], [690, 60], [690, 75], [690, 90], [690, 105], [690, 120], [690, 135], [690, 150], [690, 165], [690, 180], [690, 195], [690, 210], [690, 225], [690, 240], [690, 255], [690, 270], [690, 285], [690, 300], [690, 315], [690, 330], [690, 405], [690, 420], [690, 435], [690, 450], [690, 465], [690, 480], [690, 495], [690, 510], [690, 525], [690, 540], [690, 555], [690, 570], [690, 585], [690, 600], [690, 615], [690, 630], [690, 690], [675, 690], [660, 690], [645, 690], [630, 690], [615, 690], [600, 690], [585, 690], [330, 330], [405, 330], [330, 405], [405, 405], [525, 315], [540, 315], [540, 330], [540, 345], [540, 360], [540, 375], [540, 390], [540, 405], [540, 420], [525, 420], [420, 525], [420, 540], [405, 540], [390, 540], [375, 540], [360, 540], [345, 540], [330, 540], [315, 540], [315, 525], [210, 420], [195, 420], [195, 405], [195, 390], [195, 375], [195, 360], [195, 345], [195, 330], [195, 315], [210, 315], [315, 195], [330, 195], [345, 195], [360, 195], [375, 195], [390, 195], [405, 195], [420, 195], [420, 210], [315, 210], [120, 285], [120, 270], [270, 120], [285, 120], [120, 255], [135, 255], [135, 240], [135, 225], [150, 225], [150, 210], [150, 195], [165, 195], [165, 180], [165, 165], [255, 135], [240, 135], [225, 135], [255, 120], [225, 150], [210, 150], [195, 150], [195, 165], [180, 165], [450, 120], [465, 120], [480, 120], [480, 135], [495, 135], [510, 135], [510, 150], [525, 150], [540, 150], [540, 165], [555, 165], [570, 165], [570, 180], [570, 195], [585, 195], [585, 210], [585, 225], [600, 225], [600, 240], [600, 255], [615, 255], [615, 270], [615, 285], [615, 450], [615, 465], [615, 480], [600, 480], [600, 495], [600, 510], [585, 510], [585, 525], [585, 540], [570, 540], [570, 555], [570, 570], [555, 570], [540, 570], [540, 585], [525, 585], [510, 585], [510, 600], [495, 600], [480, 600], [480, 615], [465, 615], [450, 615], [285, 615], [270, 615], [255, 615], [255, 600], [240, 600], [225, 600], [225, 585], [210, 585], [195, 585], [195, 570], [180, 570], [165, 570], [165, 555], [165, 540], [150, 540], [150, 525], [150, 510], [135, 510], [135, 495], [135, 480], [120, 480], [120, 465], [120, 450], [150, 360], [135, 360], [120, 360], [105, 360], [90, 360], [150, 375], [135, 375], [120, 375], [105, 375], [90, 375], [360, 150], [375, 150], [375, 135], [375, 120], [375, 105], [375, 90], [360, 90], [360, 105], [360, 120], [360, 135], [585, 360], [585, 375], [600, 375], [615, 375], [630, 375], [630, 360], [615, 360], [600, 360], [645, 360], [645, 375], [375, 585], [360, 585], [360, 600], [360, 615], [360, 630], [360, 645], [375, 645], [375, 630], [375, 615], [375, 600], [720, 285], [720, 450], [15, 285], [15, 450], [450, 15], [285, 15], [450, 720], [285, 720], [90, 225], [90, 180], [90, 135], [90, 90], [135, 90], [180, 90], [225, 90], [135, 135], [510, 90], [555, 90], [600, 90], [645, 90], [645, 135], [645, 180], [645, 225], [600, 135], [645, 510], [645, 555], [645, 600], [645, 645], [600, 645], [555, 645], [510, 645], [600, 600], [90, 510], [225, 645], [180, 645], [135, 645], [90, 555], [90, 600], [135, 600], [90, 645]]

"""
dimensiones: NX = 25, NY = 25, DIM = 30

usuario = P.Usuario([330, 300]) 
snake = P.Snake([330, 720])
killer = P.Killer([390, 720])
"""
mapa3 = [[0, 0], [0, 30], [0, 60], [0, 90], [0, 120], [0, 150], [0, 180], [0, 210], [0, 240], [0, 270], [0, 300], [0, 330], [0, 360], [0, 390], [0, 420], [0, 450], [0, 480], [0, 510], [0, 540], [0, 570], [0, 600], [0, 630], [0, 660], [0, 690], [0, 720], [30, 720], [60, 720], [90, 720], [120, 720], [150, 720], [180, 720], [210, 720], [240, 720], [270, 720], [720, 720], [690, 720], [660, 720], [630, 720], [600, 720], [570, 720], [540, 720], [510, 720], [480, 720], [450, 720], [300, 720], [720, 690], [720, 660], [720, 630], [720, 600], [720, 570], [720, 540], [720, 510], [720, 480], [720, 450], [720, 420], [720, 390], [720, 360], [720, 330], [720, 300], [720, 270], [720, 240], [720, 210], [720, 180], [720, 150], [720, 120], [720, 90], [720, 60], [720, 30], [720, 0], [690, 0], [660, 0], [630, 0], [600, 0], [570, 0], [540, 0], [510, 0], [480, 0], [450, 0], [420, 0], [390, 0], [360, 0], [330, 0], [300, 0], [270, 0], [240, 0], [210, 0], [180, 0], [150, 0], [120, 0], [90, 0], [60, 0], [30, 0], [270, 420], [270, 390], [270, 300], [270, 270], [270, 240], [300, 240], [480, 300], [480, 390], [420, 450], [270, 450], [450, 450], [240, 300], [210, 300], [180, 300], [150, 300], [510, 300], [540, 300], [570, 300], [510, 390], [540, 390], [570, 390], [150, 390], [210, 390], [240, 390], [180, 390], [330, 240], [360, 330], [360, 360], [390, 450], [300, 450], [450, 240], [420, 720], [450, 420], [450, 390], [450, 270], [450, 300], [420, 240], [90, 480], [90, 510], [90, 540], [120, 540], [120, 570], [150, 570], [180, 600], [210, 600], [210, 630], [150, 600], [90, 180], [120, 180], [120, 150], [150, 150], [180, 150], [180, 120], [210, 120], [210, 90], [240, 90], [450, 90], [480, 90], [510, 90], [540, 90], [540, 120], [570, 120], [570, 150], [600, 150], [600, 180], [630, 510], [600, 510], [600, 540], [570, 540], [570, 570], [540, 570], [510, 570], [510, 600], [330, 540], [390, 600], [330, 660], [300, 150], [330, 60], [390, 120]]


# mapa1 redimensionado a DIM = 30
mapa4 = [(0, 0), (1470, 1470), (0, 60), (0, 90), (0, 120), (0, 150), (0, 210), (0, 240), (0, 270), (0, 300), (0, 330), (0, 360), (0, 390), (0, 420), (0, 180), (0, 450), (0, 480), (0, 900), (0, 930), (0, 960), (0, 990), (0, 1020), (0, 1050), (0, 1080), (0, 1110), (0, 1140), (0, 1170), (0, 1200), (0, 1230), (0, 1260), (0, 1290), (0, 1320), (0, 1350), (0, 1410), (0, 1380), (60, 1470), (90, 1470), (120, 1470), (150, 1470), (180, 1470), (210, 1470), (240, 1470), (270, 1470), (300, 1470), (330, 1470), (360, 1470), (390, 1470), (420, 1470), (450, 1470), (480, 1470), (510, 1470), (540, 1470), (570, 1470), (900, 1470), (930, 1470), (960, 1470), (990, 1470), (1020, 1470), (1050, 1470), (1080, 1470), (1110, 1470), (1140, 1470), (1170, 1470), (1200, 1470), (1230, 1470), (1260, 1470), (1290, 1470), (1320, 1470), (1350, 1470), (1380, 1470), (1410, 1470), (1470, 1410), (1470, 1380), (1470, 1350), (1470, 1320), (1470, 1290), (1470, 1260), (1470, 1230), (1470, 1200), (1470, 1170), (1470, 1140), (1470, 1110), (1470, 1080), (1470, 990), (1470, 960), (1470, 1020), (1470, 1050), (1470, 930), (1470, 900), (780, 1470), (750, 1470), (720, 1470), (690, 1470), (1470, 780), (1470, 750), (1470, 720), (1470, 690), (1470, 570), (1470, 540), (1470, 510), (1470, 480), (1470, 450), (1470, 420), (1470, 390), (1470, 360), (1470, 330), (1470, 300), (1470, 270), (1470, 240), (1470, 210), (1470, 180), (1470, 150), (1470, 120), (1470, 90), (1470, 60), (1410, 0), (1380, 0), (1350, 0), (1320, 0), (1290, 0), (1260, 0), (1230, 0), (1200, 0), (1170, 0), (1140, 0), (1110, 0), (1080, 0), (1050, 0), (1020, 0), (900, 0), (930, 0), (960, 0), (990, 0), (0, 750), (0, 720), (0, 690), (0, 780), (0, 570), (0, 540), (0, 510), (60, 0), (90, 0), (120, 0), (150, 0), (180, 0), (210, 0), (240, 0), (270, 0), (300, 0), (330, 0), (360, 0), (390, 0), (510, 0), (480, 0), (450, 0), (420, 0), (540, 0), (570, 0), (780, 0), (750, 0), (720, 0), (690, 0), (540, 510), (570, 510), (600, 510), (630, 510), (660, 510), (690, 510), (780, 510), (810, 510), (840, 510), (870, 510), (900, 510), (930, 510), (960, 510), (960, 540), (960, 570), (960, 600), (960, 630), (960, 660), (960, 690), (960, 780), (960, 810), (960, 840), (960, 870), (960, 900), (960, 930), (960, 960), (930, 960), (900, 960), (840, 960), (810, 960), (780, 960), (690, 960), (660, 960), (630, 960), (600, 960), (570, 960), (540, 960), (510, 960), (510, 930), (510, 900), (510, 870), (510, 840), (510, 810), (510, 780), (510, 690), (510, 660), (510, 630), (510, 600), (510, 570), (510, 540), (510, 510), (870, 960), (780, 810), (810, 780), (810, 690), (780, 660), (690, 660), (660, 690), (660, 780), (690, 810), (0, 1440), (30, 1470), (1440, 1470), (1470, 1440), (1440, 0), (1470, 30), (0, 30), (30, 0), (0, 1470), (1470, 0), (480, 1380), (510, 1380), (540, 1380), (570, 1380), (600, 1380), (660, 1380), (810, 1380), (840, 1380), (870, 1380), (900, 1380), (930, 1380), (990, 1380), (630, 1380), (960, 1380), (1020, 1380), (1050, 1380), (1080, 1380), (1110, 1380), (450, 1380), (420, 1380), (390, 1380), (360, 1380), (330, 1380), (1140, 1380), (300, 1380), (270, 1380), (240, 1380), (210, 1380), (90, 1380), (90, 1350), (90, 1320), (90, 1290), (90, 1260), (90, 1230), (90, 1200), (90, 1170), (90, 1140), (90, 1110), (90, 1080), (90, 1050), (90, 1020), (90, 990), (90, 960), (90, 930), (90, 900), (90, 870), (90, 840), (90, 810), (90, 660), (90, 630), (90, 600), (90, 570), (90, 540), (90, 510), (90, 480), (90, 450), (90, 420), (90, 390), (90, 360), (90, 330), (90, 300), (90, 270), (90, 240), (90, 210), (90, 90), (120, 90), (150, 90), (180, 90), (210, 90), (240, 90), (270, 90), (300, 90), (330, 90), (360, 90), (420, 90), (390, 90), (450, 90), (480, 90), (510, 90), (540, 90), (570, 90), (600, 90), (630, 90), (660, 90), (810, 90), (840, 90), (870, 90), (900, 90), (930, 90), (960, 90), (990, 90), (1020, 90), (1050, 90), (1080, 90), (1110, 90), (1140, 90), (1170, 90), (1200, 90), (1230, 90), (1260, 90), (1380, 90), (1380, 120), (1380, 150), (1380, 180), (1380, 210), (1380, 240), (1380, 270), (1380, 300), (1380, 330), (1380, 360), (1380, 390), (1380, 420), (1380, 450), (1380, 480), (1380, 510), (1380, 540), (1380, 570), (1380, 600), (1380, 630), (1380, 660), (1380, 810), (1380, 840), (1380, 870), (1380, 900), (1380, 930), (1380, 960), (1380, 990), (1380, 1020), (1380, 1050), (1380, 1080), (1380, 1110), (1380, 1140), (1380, 1170), (1380, 1200), (1380, 1230), (1380, 1260), (1380, 1380), (1350, 1380), (1320, 1380), (1290, 1380), (1260, 1380), (1230, 1380), (1200, 1380), (1170, 1380), (660, 660), (810, 660), (660, 810), (810, 810), (1050, 630), (1080, 630), (1080, 660), (1080, 690), (1080, 720), (1080, 750), (1080, 780), (1080, 810), (1080, 840), (1050, 840), (840, 1050), (840, 1080), (810, 1080), (780, 1080), (750, 1080), (720, 1080), (690, 1080), (660, 1080), (630, 1080), (630, 1050), (420, 840), (390, 840), (390, 810), (390, 780), (390, 750), (390, 720), (390, 690), (390, 660), (390, 630), (420, 630), (630, 390), (660, 390), (690, 390), (720, 390), (750, 390), (780, 390), (810, 390), (840, 390), (840, 420), (630, 420), (240, 570), (240, 540), (540, 240), (570, 240), (240, 510), (270, 510), (270, 480), (270, 450), (300, 450), (300, 420), (300, 390), (330, 390), (330, 360), (330, 330), (510, 270), (480, 270), (450, 270), (510, 240), (450, 300), (420, 300), (390, 300), (390, 330), (360, 330), (900, 240), (930, 240), (960, 240), (960, 270), (990, 270), (1020, 270), (1020, 300), (1050, 300), (1080, 300), (1080, 330), (1110, 330), (1140, 330), (1140, 360), (1140, 390), (1170, 390), (1170, 420), (1170, 450), (1200, 450), (1200, 480), (1200, 510), (1230, 510), (1230, 540), (1230, 570), (1230, 900), (1230, 930), (1230, 960), (1200, 960), (1200, 990), (1200, 1020), (1170, 1020), (1170, 1050), (1170, 1080), (1140, 1080), (1140, 1110), (1140, 1140), (1110, 1140), (1080, 1140), (1080, 1170), (1050, 1170), (1020, 1170), (1020, 1200), (990, 1200), (960, 1200), (960, 1230), (930, 1230), (900, 1230), (570, 1230), (540, 1230), (510, 1230), (510, 1200), (480, 1200), (450, 1200), (450, 1170), (420, 1170), (390, 1170), (390, 1140), (360, 1140), (330, 1140), (330, 1110), (330, 1080), (300, 1080), (300, 1050), (300, 1020), (270, 1020), (270, 990), (270, 960), (240, 960), (240, 930), (240, 900), (300, 720), (270, 720), (240, 720), (210, 720), (180, 720), (300, 750), (270, 750), (240, 750), (210, 750), (180, 750), (720, 300), (750, 300), (750, 270), (750, 240), (750, 210), (750, 180), (720, 180), (720, 210), (720, 240), (720, 270), (1170, 720), (1170, 750), (1200, 750), (1230, 750), (1260, 750), (1260, 720), (1230, 720), (1200, 720), (1290, 720), (1290, 750), (750, 1170), (720, 1170), (720, 1200), (720, 1230), (720, 1260), (720, 1290), (750, 1290), (750, 1260), (750, 1230), (750, 1200), (1440, 570), (1440, 900), (30, 570), (30, 900), (900, 30), (570, 30), (900, 1440), (570, 1440), (180, 450), (180, 360), (180, 270), (180, 180), (270, 180), (360, 180), (450, 180), (270, 270), (1020, 180), (1110, 180), (1200, 180), (1290, 180), (1290, 270), (1290, 360), (1290, 450), (1200, 270), (1290, 1020), (1290, 1110), (1290, 1200), (1290, 1290), (1200, 1290), (1110, 1290), (1020, 1290), (1200, 1200), (180, 1020), (450, 1290), (360, 1290), (270, 1290), (180, 1110), (180, 1200), (270, 1200), (180, 1290), (30, 720), (60, 720), (90, 720), (120, 720), (150, 720), (150, 750), (120, 750), (90, 750), (60, 750), (30, 750), (1320, 720), (1350, 720), (1380, 720), (1410, 720), (1440, 720), (1440, 750), (1410, 750), (1380, 750), (1350, 750), (1320, 750), (750, 1140), (750, 1110), (720, 1110), (720, 1140), (750, 360), (750, 330), (720, 330), (720, 360)]

