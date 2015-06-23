#encoding: utf-8
import nicoapi

n = nicoapi.nicoapi()

# 複数の動画を保存
opener = n.login_n("dxfsra1004@gmail.com","bigstone")
n.getFlvs(opener,["sm2688713","sm2815822","sm2668737"],"/home/user/flv/")