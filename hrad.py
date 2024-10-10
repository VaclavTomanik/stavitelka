import stavitelka as st
from random import random

"""
def kvadr(d, h, v):
    for i in range(d):
        for j in range(v):
            for k in range(h):
                st.Hranol(i, j, k)
"""

def cimburi(px,py,pz):
    st.Hranol(px,py,pz, 4,1,4, 0,0,0, [random(),random(),random()]) #podstava
    st.Hranol(px-1.5,py+1,pz-1.5, 1,1,1, 0,0,0, [random(),random(),random()]) #kostky na tom
    st.Hranol(px-1.5,py+1,pz+0.5, 1,1,1, 0,0,0, [random(),random(),random()])
    st.Hranol(px-0.5,py+1,pz+1.5, 1,1,1, 0,0,0, [random(),random(),random()])
    st.Hranol(px+1.5,py+1,pz+1.5, 1,1,1, 0,0,0, [random(),random(),random()])
    st.Hranol(px+1.5,py+1,pz-0.5, 1,1,1, 0,0,0, [random(),random(),random()])
    st.Hranol(px+0.5,py+1,pz-1.5, 1,1,1, 0,0,0, [random(),random(),random()])

def vez(px,py,pz):
    st.Hranol(px,py,pz, 2,8,2, 0,0,0, [random(),random(),random()]) #sloup
    cimburi(px,py,pz)
    cimburi(px,py+4,pz)

def velkavez(px,py,pz):
    st.Hranol(px,py,pz, 6,15,6, 0,0,0, [random(),random(),random()])
    st.Hranol(px-2.5,py+8.5,pz-2.5, 1.5,2,1.5, 0,0,0, [random(),random(),random()])
    st.Hranol(px-2.5,py+8.5,pz+0.5, 1.5,2,1.5, 0,0,0, [random(),random(),random()])
    st.Hranol(px-0.5,py+8.5,pz+2.5, 1.5,2,1.5, 0,0,0, [random(),random(),random()])
    st.Hranol(px+2.5,py+8.5,pz+2.5, 1.5,2,1.5, 0,0,0, [random(),random(),random()])
    st.Hranol(px+2.5,py+8.5,pz-0.5, 1.5,2,1.5, 0,0,0, [random(),random(),random()])
    st.Hranol(px+0.5,py+8.5,pz-2.5, 1.5,2,1.5, 0,0,0, [random(),random(),random()])

st.Hranol(0,0,0, 16,4,16, 0,0,0, [random(),random(),random()])
vez(-6,5,-6)
vez(6,5,6)
vez(-6,5,6)
vez(6,5,-6)
velkavez(0,5,0)

st.ZobrazScenu()