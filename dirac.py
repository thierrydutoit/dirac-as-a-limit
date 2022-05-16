import streamlit as st
from numpy import *
from matplotlib.pyplot import *
import matplotlib.patches as mpatches

st.title('The Dirac impulse seen as a limit')
a=st.slider('Factor a', 1.0, 10.0, 1.0)
shift=st.slider('Delta', -3.0, 3.0, 0.0)

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

col1, col2, col3 = st.columns(3)

with col1:
   st.latex('''a\ rect(a(t-\Delta))''')
   fig1,ax1 = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-10, 10)
   plot(t,rect_a)
   st.pyplot(fig1)


with col2:
   st.latex('''a\ tri(a(t-\Delta))''')
   fig2,ax2 = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-10, 10)
   plot(t,tri_a)
   st.pyplot(fig2)


with col3:
   st.latex('''a\ sinc(a(t-\Delta))''')
   fig3,ax3 = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-10, 10)
   plot(t,sinc_a)
   st.pyplot(fig3)

st.markdown('When _a_ grows, these functions, although not fully identical, tend to have the same effect _when used in an integral_: only their values very close to 0 contribute to the result, as shown in the example below.')


col1, col2, col3 = st.columns(3)

with col1:
   product=multiply(rect_a, cos(3*t))
   integral=sum(product)/fe

   st.latex('''f(t) \ a\ rect(at-\Delta) ''')
   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-10, 10)
   plot(t,product)
   ax.fill_between(t,0,product)
   plot(t,cos(3*t),'--')
   st.pyplot(fig)
   st.latex('''\int_{-\infty}^{\infty} f(t) \ a\ rect(at-\Delta) \,dt''')
   st.metric("",around(integral,3))

with col2:
   product=multiply(tri_a, cos(3*t))
   integral=sum(product)/fe

   st.latex('''f(t) \ a\ tri(at-\Delta) ''')
   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-10, 10)
   plot(t,product)
   ax.fill_between(t,0,product)
   plot(t,cos(3*t),'--')
   st.pyplot(fig)
   st.latex('''\int_{-\infty}^{\infty} f(t) \ a\ tri(at-\Delta) \,dt''')
   st.metric("",around(integral,3))

with col3:
   product=multiply(sinc_a, cos(3*t))
   integral=sum(product)/fe
   
   st.latex('''f(t) \ a\ sinc(at-\Delta) ''')
   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-10, 10)
   plot(t,product)
   ax.fill_between(t,0,product)
   plot(t,cos(3*t),'--')
   st.pyplot(fig)
   st.latex('''\int_{-\infty}^{\infty} f(t) \ a\ sinc(at-\Delta) \,dt''')
   st.metric("",around(integral,3))

st.markdown('When _a_ tends to infinity, these functions can no longer be plotted. They are therefore symbolically represented as an arrow, the amplitude of which is set to the integral of the function: 1, and termed as a _dirac impluse_.')

col1, col2, col3 = st.columns(3)

with col2:
   
   fig,ax = subplots(figsize=(3,3))
   xlim(-3,3); ylim(-1, 3)
   arrow = mpatches.Arrow(shift, 0, 0, 1)
   ax.add_patch(arrow)
   plot([-3,3],[0,0])
   plot(t,cos(3*t),'--')
   plot(shift,cos(3*shift),'yD')
   st.pyplot(fig)
   st.latex('''\int_{-\infty}^{\infty} f(t) \ \delta(t- \Delta) \,dt''')
   st.metric("",around(cos(3*shift),3))
   st.markdown("or more generally:")
   st.latex('''\int_{-\infty}^{\infty} f(t) \ \delta(t- \Delta) \,dt=f(\Delta)''')
   st.markdown("and in particular")
   st.latex('''\int_{-\infty}^{\infty} f(t) \ \delta(t) \,dt=f(0)''')
 
