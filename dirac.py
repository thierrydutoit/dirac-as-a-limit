import streamlit as st
from numpy import *
from matplotlib.pyplot import *
import matplotlib.patches as mpatches

st.title('The Dirac impulse seen as a limit')
a=st.slider('Amplification: a', 1.0, 20.0, 1.0)
shift=st.slider('Time shift: Delta', -3.0, 3.0, 0.0)

fe=10000;
t=arange(-3,3,1/fe) 

def rect(x):
    return where(abs(x)<=0.5, 1, 0)
rect_a=rect(a*(t-shift))*a

def tri(x):
    return where(abs(x)<=1,1-abs(x),0)
tri_a=tri(a*(t-shift))*a

def sincard(x):
    return divide(sin(pi*x),(pi*x))
sinc_a=sincard(a*(t-shift))*a

col1, col2, col3, col4 = st.columns(4)

with col1:
   fig1,ax1 = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-10, 10)
   plot(t,rect_a)
   title(r'$a\ rect(a(t-\Delta))$')
   st.pyplot(fig1)

with col2:
   fig2,ax2 = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-10, 10)
   plot(t,tri_a)
   title(r'$a\ tri(a(t-\Delta))$')
   st.pyplot(fig2)

with col3:
   fig3,ax3 = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-10, 10)
   plot(t,sinc_a)
   title(r'$a\ sinc(a(t-\Delta))$')
   st.pyplot(fig3)

with col4:
   fig4,ax4 = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-2,2)
   arrow = mpatches.Arrow(shift, 0, 0, 1)
   ax4.add_patch(arrow)
   plot([-3,3],[0,0])
   title(r'$\delta(t-\Delta)$')
   st.pyplot(fig4)
   
col1, col2, col3, col4 = st.columns(4)

with col1:
   product=multiply(rect_a, 2*cos(3*t))
   integral1=sum(product)/fe

   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-10, 10)
   plot(t,product)
   ax.fill_between(t,0,product)
   plot(t,2*cos(3*t),'--')
   title(r'$f(t) \ a\ rect(a(t-\Delta)) $')
   text(-2.3,-9,'integral='+str(around(integral1,2)),fontsize='xx-large')
   st.pyplot(fig)

with col2:
   product=multiply(tri_a, 2*cos(3*t))
   integral2=sum(product)/fe

   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-10, 10)
   plot(t,product)
   ax.fill_between(t,0,product)
   plot(t,2*cos(3*t),'--')
   title(r'$f(t) \ a\ tri(a(t-\Delta)) $')
   text(-2.3,-9,'integral='+str(around(integral2,2)),fontsize='xx-large')
   st.pyplot(fig)

with col3:
   product=multiply(sinc_a, 2*cos(3*t))
   integral3=sum(product)/fe
   
   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-10, 10)
   plot(t,product)
   ax.fill_between(t,0,product)
   plot(t,2*cos(3*t),'--')
   title(r'$f(t) \ a\ sinc(a(t-\Delta)) $')
   text(-2.3,-9,'integral='+str(around(integral2,2)),fontsize='xx-large')
   st.pyplot(fig)

with col4:
   fig4,ax4 = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-2, 2)
   arrow = mpatches.Arrow(shift, 0, 0, 2*cos(3*shift))
   ax4.add_patch(arrow)
   plot([-3,3],[0,0])
   plot(t,2*cos(3*t),'--')
   title(r'$f(t)\ \delta((t-\Delta)) $')
   text(-2.3,-1.78,'integral='+str(around(2*cos(3*shift),2)),fontsize='xx-large')
   st.pyplot(fig4)
  
with st.expander("Open for comments"):
   st.markdown('''The three plots on the top left show rectangle, triangle and sinc functions which 
               can be modified using sliders _a_ and $\Delta$ . Notice that the integral of 
               these fucntions is always 1, whatever _a_.''')
   st.markdown('''When _a_ tends to infinity, these functions can no longer be plotted. 
               They are therefore symbolically represented in the bottom plotas an arrow, the 
               amplitude of which is set to the integral of the function: 1, and termed as 
               a _dirac impluse_ $\delta(t)$, shown on the right.''')
   st.markdown('''In the next four plots, we multiply our three functions with _f(t)=2cos(3t)_. 
               Then we compute the integral of this product. The integral is the area in blue
               (taken with signs). Multiplying the Dirac impulse by _2cos(3t)_ simply changes                the value of the impulse.''')
   st.markdown('''When _a_ grows, we see that our three functions, although not fully identical, 
               tend to have the same effect _when used in an integral_: only their values very 
               close to their maximum contribute to the result. As a matter of fact, when
               $\Delta$ is set to 0, all integrals tends to $f(0)$:''')
   st.latex('''\int_{-\infty}^{\infty} f(t) \ \delta(t) \,dt=f(0)''')
   st.markdown('''When $\Delta$ is modified, all integrals tend to $f(\Delta)$:''')
   st.latex('''\int_{-\infty}^{\infty} f(t) \ \delta(t-\Delta) \,dt=f(\Delta)''')
