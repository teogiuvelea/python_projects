import cv2


with open('pics_title.txt') as f:
    data = f.readlines()

titles = [item.strip("\n") for item in data]
print(titles)  

# pic = 'Screenshot_20220829-084752.png'
# pics = ['Screenshot_20220829-091207.png', 'Screenshot_20220829-091216.png', 'Screenshot_20220829-091230.png', 'Screenshot_20220829-091248.png', 'Screenshot_20220829-091332.png', 'Screenshot_20220829-091341.png', 'Screenshot_20220829-091348.png', 'Screenshot_20220829-091354.png', 'Screenshot_20220829-091400.png', 'Screenshot_20220829-091406.png', 'Screenshot_20220829-091411.png', 'Screenshot_20220829-091417.png', 'Screenshot_20220829-091427.png', 'Screenshot_20220829-091432.png', 'Screenshot_20220829-091506.png', 'Screenshot_20220829-091511.png', 'Screenshot_20220829-091519.png', 'Screenshot_20220829-091524.png', 'Screenshot_20220829-091543.png', 'Screenshot_20220829-091548.png', 'Screenshot_20220829-091554.png', 'Screenshot_20220829-091559.png', 'Screenshot_20220829-091605.png', 'Screenshot_20220829-091610.png', 'Screenshot_20220829-091616.png', 'Screenshot_20220829-091621.png', 'Screenshot_20220829-091626.png', 'Screenshot_20220829-091631.png', 'Screenshot_20220829-091654.png', 'Screenshot_20220829-091659.png', 'Screenshot_20220829-091705.png', 'Screenshot_20220829-091711.png', 'Screenshot_20220829-091716.png', 'Screenshot_20220829-091721.png', 'Screenshot_20220829-091726.png', 'Screenshot_20220829-091732.png', 'Screenshot_20220829-091740.png', 'Screenshot_20220829-091748.png', 'Screenshot_20220829-091753.png', 'Screenshot_20220829-091807.png', 'Screenshot_20220829-091812.png', 'Screenshot_20220829-091823.png', 'Screenshot_20220829-091828.png', 'Screenshot_20220829-091833.png', 'Screenshot_20220829-091838.png', 'Screenshot_20220829-091842.png', 'Screenshot_20220829-091847.png']


for pic in titles:
    picture_url = f"img_dir/{pic}"
    image = cv2.imread(picture_url)
    (x,y,w,h) = cv2.selectROI(image)
    ROI = image[y:y+h, x:x+w]

    cv2.imshow("ROI", ROI)
    cv2.imwrite(f"cropped_img/{pic}", ROI)
    cv2.waitKey()
