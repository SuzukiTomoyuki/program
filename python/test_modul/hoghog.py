# -*- coding: utf-8 -*-
import cv2

if __name__ == '__main__':
    # 画像の読み込み
    im = cv2.imread("test.jpg")
    # HoG特徴量の計算
    hog = cv2.HOGDescriptor()
    # SVMによる人検出
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    hogParams = {'winStride': (8, 8), 'padding': (32, 32), 'scale': 1.05}
    # 人を検出した座標
    human, r = hog.detectMultiScale(im, **hogParams)
    # 長方形で人を囲う
    for (x, y, w, h) in human:
        cv2.rectangle(im, (x, y),(x+w, y+h),(0,50,255), 3)
    # 人を検出した座標
    cv2.imshow("Human detection",im)
    cv2.waitKey(0)
    # 画像保存
    cv2.imwrite('test2.jpg',im)
    cv2.destroyAllWindows()