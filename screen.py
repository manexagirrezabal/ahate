
from matplotlib import pyplot as plt
import skimage.io
import numpy as np
plt.ion()

#http://www.nikukyu.es/archivos/juego%20oca%202.jpg
board = skimage.io.imread("juegooca2.jpg")

positions={
1:(500,1700),2:(650,1700),3:(800,1700),4:(950,1700),5:(1100,1700),
6:(1220,1700),7:(1400,1700),8:(1550,1700),9:(1700,1600),10:(1700,1400),
11:(1700,1250),12:(1700,1100),13:(1700,950),14:(1700,800),15:(1700,650),
16:(1700,500),17:(1700,400),18:(1700,250),19:(1500,70),20:(1400,70),
21:(1220,70),22:(1100,70),23:(950,70),24:(800,70),25:(650,70),
26:(550,70),27:(400,70),28:(250,70),29:(100,250),30:(100,400),
31:(100,500),32:(100,650),33:(100,800),34:(100,950),35:(100,1100),
36:(100,1250),37:(220,1450),38:(400,1450),39:(550,1450),40:(700,1450),
41:(820,1450),42:(980,1450),43:(1100,1450),44:(1300,1450),45:(1450,1280),
46:(1450,1100),47:(1450,980),48:(1450,800),49:(1450,650),50:(1450,500),
51:(1250,320),52:(1100,320),53:(950,320),54:(800,320),55:(700,320),
56:(500,320),57:(300,500),58:(300,700),59:(300,820),60:(300,1000),
61:(500,1200),62:(650,1200),63:(900,900)
}

list_colors = ['r','b','g','c','m','y']



fig,ax = plt.subplots(figsize=(15,15))
sizeparam = np.mean(fig.get_size_inches())

plt.imshow(board,alpha=0.7);

plt.show()

def show_situation(list_positions):

    poss = [positions[val] for val in list_positions]
    plotted_elements = plt.scatter([el[0] for el in poss],[el[1] for el in poss],
               color=list_colors[:len(list_positions)],s=30*sizeparam)

    ax.xaxis.set_ticks_position('top') # the rest is the same
    plt.draw()
    return plotted_elements

def clean_plotted(elements):
	elements.remove()

#show_situation([5,8,25,56])