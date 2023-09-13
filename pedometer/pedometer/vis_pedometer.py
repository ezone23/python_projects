import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

fig, ax1 = plt.subplots()

data_file = open(sys.argv[1], 'r').read()
result_file = open(sys.argv[2], 'r').read()

def getImage(path):
  return OffsetImage(plt.imread(path))

paths = ['standing.png', 'walking.png', 'running.png']

info = data_file.split('\n')
state = result_file.split('\n')

accel = []
for lines in info:
  if len(lines) > 0:
    accel.append(float(lines))

x = []
y = []
cnt = 0
for lines in state[3:]:
  if len(lines) > 0:
    xx = cnt
    parse = lines.split(': ')
    yy = int(parse[1])

    x.append((xx+1) * 25)
    y.append(yy)

    cnt+=1

ax1.plot(accel)
ax2 = ax1.twinx()
ax2.plot(x, y, color='black')


img_path = []
for y0 in y:
  img_path.append(paths[y0])

for x0, y0, path in zip(x, y, img_path):
  ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
  ax2.add_artist(ab)

ax2.set_ylim(0, 20)
#ax2.autoscale()

plt.show()