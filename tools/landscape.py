# Generates _includes/landscape.svg: level sets of a 2-D non-convex loss and a heavy-ball descent path.
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
W,H=640,420
def f(x,y):
    return (0.6*(x**2+0.6*y**2) - 2.2*np.exp(-((x-0.9)**2+(y+0.35)**2)/0.3)
            - 1.0*np.exp(-((x+1.0)**2+(y-0.6)**2)/0.35) + 0.25*np.sin(1.7*x)*np.cos(1.3*y))
xs=np.linspace(-2.6,2.6,400); ys=np.linspace(-1.7,1.7,300); X,Y=np.meshgrid(xs,ys); Z=f(X,Y)
cs=plt.contour(X,Y,Z,levels=np.linspace(Z.min()+0.05,Z.max()*0.75,16))
def tx(x): return (x+2.6)/5.2*W
def ty(y): return (1.7-y)/3.4*H
paths=[]
for segs in cs.allsegs:
    for seg in segs:
        if len(seg)<8: continue
        seg=seg[::5]
        d='M'+' L'.join(f'{tx(a):.1f},{ty(b):.1f}' for a,b in seg)
        paths.append(d)
# heavy-ball trajectory
def grad(x,y,e=1e-4):
    return ((f(x+e,y)-f(x-e,y))/(2*e),(f(x,y+e)-f(x,y-e))/(2*e))
p=np.array([2.35,-1.45]); v=np.zeros(2); traj=[p.copy()]
for t in range(200):
    g=np.array(grad(*p)); v=0.8*v-0.03*g; p=p+v; traj.append(p.copy())
traj=np.array(traj)
tdat='M'+' L'.join(f'{tx(a):.1f},{ty(b):.1f}' for a,b in traj)
end=traj[-1]
svg=[f'<svg class="landscape" viewBox="0 0 {W} {H}" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg">',
     '<g class="levels" fill="none">']+[f'<path d="{d}"/>' for d in paths]+['</g>',
     f'<path class="trajectory" d="{tdat}" fill="none" pathLength="1"/>',
     f'<circle class="start" cx="{tx(traj[0][0]):.1f}" cy="{ty(traj[0][1]):.1f}" r="4"/>',
     f'<circle class="end" cx="{tx(end[0]):.1f}" cy="{ty(end[1]):.1f}" r="5"/>','</svg>']
open('_includes/landscape.svg','w').write('\n'.join(svg))
print(len(paths), 'paths; end', end, 'size', sum(map(len,svg)))
