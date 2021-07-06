from PIL import Image
import glob


if __name__== "__main__":
    folder='Buffan_falls'
    files=glob.glob('./'+folder+'/*.jpg')
    
    for file in files:
        file_name=file.split('/')[-1].split('.')[0]
        
        img = Image.open(file)
        new_img = img.resize((640,480))
        
        new_img.save('./'+folder+'/'+file_name+'_resize.jpg', "JPEG", optimize=False)