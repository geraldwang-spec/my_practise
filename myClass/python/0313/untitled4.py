import streamlit as st
import os
from PIL import Image  #匯入影像模組
st.title('圖片展示')

folder='aaa'  #要檢視的照片的目錄

files=os.listdir(folder)

#列表表達式
image_files=[f for f in files if f.endswith(('.jpg','.png','.jpeg'))]

#拉桿控制一排幾圖
col_num=st.slider('一排要顯示的張數??',2,6,2)
#拉桿控制要顯示的圖片尺寸
min_size=st.slider('過濾圖片尺寸(最小寬高)',50,800,200)

#一個橫排三張照片
cols=st.columns(col_num)

i=0
for f in image_files:
    path=os.path.join(folder,f)
    
    with cols[i % col_num]:
        #st.image(path,caption=f)
        
        #打開檔案看尺寸
        img=Image.open(path)
        w,h=img.size
        
        #過濾小圖片 
        if w>=min_size and h>=min_size:
            #秀圖片
            st.image(path,width=200)
            st.caption(f'{f} ({w}x{h})')
            i +=1 
        
