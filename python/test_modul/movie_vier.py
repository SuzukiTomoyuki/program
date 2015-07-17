# -*- coding: utf-8 -*-
 
# 動画ファイルから、顔認識したものを取り出す
 
# 分類器をアニメ向けのもの使用
import cv2
import time
 
# 分類器へのパス
cascade_path = "./lbpcascade_animeface.xml"
 
# 動画パス
video_path = "movie/kancolle_op.mp4"
out_video_path = "movie/fece_op.avi"
 
# colorはBGRの順番?
color = (0, 187, 254) #黄
#カスケード分類器の特徴量を取得する
cascade = cv2.CascadeClassifier(cascade_path)
 
# 動画のエンコード　とりあえず、これで動く拡張子はm4vで
fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
# 動画ファイル読み込み
cap = cv2.VideoCapture(video_path)
 
out = cv2.VideoWriter(out_video_path, fourcc, 30.0, (1280,720))
 
frame_num = 0
img_cnt = 0
# フレームごとの処理
print ":"+str(out)
while(cap.isOpened()):
  ret, frame = cap.read()
  if (ret == False):
    break
  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  facerect = cascade.detectMultiScale(frame_gray,1.1,3)
 
  print("frame : %d" % frame_num)
  if len(facerect) != 0:
    #検出した顔を囲む矩形の作成
    for (x,y,w,h) in facerect:
      cv2.rectangle(frame, (x,y),(x+w,y+h), color, thickness=7)
      img_cnt += 1
  out.write(frame)
  frame_num += 1
 
cap.release()
cv2.destroyAllWindows()
out.release()