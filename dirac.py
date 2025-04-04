import streamlit as st
from numpy import *
from matplotlib.pyplot import *
import matplotlib.patches as mpatches

st.title('Measuring time content')
st.markdown('''Suppose you are given a black box with some unknown signal $f(t)$ in it, and the only 
               thing you can do is to provide another signal $in(t)$ as input, in which case the black 
               box will ouput the scalar product between the two: $<f(t),in(t)>$. ''')
st.markdown('''What kind of input signal should you use to get the value of $f(\Delta)$? ''')

col1, col2 = st.columns(2)
with col1:
   a=st.slider('Amplification: a', 1.0, 20.0, 1.0)
with col2:
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
   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-2,2)
   plot(t,cos(3*t),'--')
   title(r'$f(t)= \ cos(3t)$')
   xlabel('Time (seconds)')   
   st.pyplot(fig)
   
   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-2, 2)
   plot(t,rect_a)
   title(r'$in(t)=a\ rect(a(t-\Delta))$')
   xlabel('Time (seconds)')   
   st.pyplot(fig)

   product=multiply(rect_a, cos(3*t))
   integral1=sum(product)/fe

   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-2, 2)
   plot(t,product)
   ax.fill_between(t,0,product)
   title(r'$f(t)\ in(t)$')
   text(-2.7,-1.5,'<f(t),in(t)>='+str(around(integral1,2)),fontsize='xx-large')
   xlabel('Time (seconds)')   
   st.pyplot(fig)

with col2:
   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-2,2)
   plot(t,cos(3*t),'--')
   title(r'$f(t)= \ cos(3t)$')
   xlabel('Time (seconds)')   
   st.pyplot(fig)

   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-2, 2)
   plot(t,tri_a)
   title(r'$in(t)=a\ tri(a(t-\Delta))$')
   xlabel('Time (seconds)')   
   st.pyplot(fig)

   product=multiply(tri_a, cos(3*t))
   integral2=sum(product)/fe

   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-2, 2)
   plot(t,product)
   ax.fill_between(t,0,product)
   title(r'$f(t)\ in(t)$')
   text(-2.7,-1.5,'<f(t),in(t)>='+str(around(integral2,2)),fontsize='xx-large')
   xlabel('Time (seconds)')   
   st.pyplot(fig)

with col3:
   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-2, 2)
   plot(t,cos(3*t),'--')
   title(r'$f(t)= \ cos(3t)$')

   xlabel('Time (seconds)')   
   st.pyplot(fig)
   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-2, 2)
   plot(t,sinc_a)
   title(r'$in(t)=a\ sinc(a(t-\Delta))$')
   xlabel('Time (seconds)')   
   st.pyplot(fig)

   product=multiply(sinc_a, cos(3*t))
   integral3=sum(product)/fe
   
   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-2, 2)
   plot(t,product)
   ax.fill_between(t,0,product)
   title(r'$f(t)\ in(t)$')
   text(-2.7,-1.5,'<f(t),in(t)>='+str(around(integral2,2)),fontsize='xx-large')
   xlabel('Time (seconds)')   
   st.pyplot(fig)

if a>19.5:
   with col4:
      fig,ax = subplots(figsize=(3,3))
      xlim(-3,3); ylim(-2, 2)
      plot(t,cos(3*t),'--')
      title(r'$f(t)=a\ cos(3t)$')
      xlabel('Time (seconds)')   
      st.pyplot(fig)
      
      fig,ax = subplots(figsize=(3,3))
      xlim(-3,3); ylim(-2, 2)
      arrow = mpatches.Arrow(shift, 0, 0, 1)
      ax.add_patch(arrow)
      plot([-3,3],[0,0])
      title(r'$in(t)=\delta(t-\Delta)$')
      xlabel('Time (seconds)')   
      st.pyplot(fig)

      fig,ax = subplots(figsize=(3,3))
      xlim(-3,3); ylim(-2, 2)
      arrow = mpatches.Arrow(shift, 0, 0, cos(3*shift))
      ax.add_patch(arrow)
      plot([-3,3],[0,0])
      plot(t,cos(3*t),'--')
      title(r'$f(t)\ in(t)$')
      text(-2.7,-1.5,'<f(t),in(t)>='+str(around(cos(3*shift),2)),fontsize='xx-large')
      xlabel('Time (seconds)')   
      st.pyplot(fig)
  
with st.expander("Open for comments"):
   st.markdown('''The three plots on the top left show the unknown function _f(t)=cos(3t)_.
               The next three plots show possible candidates for _in(t)_ : rectangle, triangle
               and sinc functions which can be modified using sliders _a_ and $\Delta$. 
               Notice that the integral of these three functions is always 1, whatever _a_.''')
   st.markdown('''In the three bottom left plots, we multiply our three functions _in(t)_ with 
               _f(t)_. Then we compute and print the scalar product as the integral of this product, 
               i.e. the area in blue (taken with signs). ''')
   st.latex('''<f(t),in(t-\Delta)>=\int_{-\infty}^{\infty} f(t) \ in(t-\Delta) \,dt''')
   st.markdown('''When _a_ grows, we see that our three functions, although not fully identical, 
               tend to have the same effect _when used in the integral_: only their values very 
               close to their maximum contribute to the result. ''')
   st.markdown('''When _a_ tends to infinity (here, to 20), these functions can no longer be plotted. 
               They are therefore termed as a _dirac impluse_ $\delta(t)$ and symbolically represented 
               on the right plots as an arrow, the amplitude of which is set to the integral of the 
               functions: 1 on the top plot and _f(Delta)_ on the bottom plot.''')
   st.markdown(''' As a matter of fact, we see that when
               $\Delta$ is set to 0, all integrals tends to $f(0)$:''')
   st.latex('''<f(t),\delta(t)>=\int_{-\infty}^{\infty} f(t) \ \delta(t) \,dt=f(0)''')
   st.markdown('''When $\Delta$ is modified, all integrals tend to $f(\Delta)$:''')
   st.latex('''<f(t),\delta(t-\Delta)>=\int_{-\infty}^{\infty} f(t) \ \delta(t-\Delta) \,dt=f(\Delta)''')
   st.markdown('''The ideal input function $in(t)$ is therefore $\delta(t-\Delta)$.''')
