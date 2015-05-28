# coding:utf-8

import add
import sub
import multi
import div

if __name__ == "__main__":
	an_add = add.Add(3,5)
	an_add.cal_add()
	an_add.print_answer()

	an_sub = sub.Sub(5,2)
	an_sub.cal_sub()
	an_sub.print_answer()

	an_multi = multi.Multi(3,3)
	an_multi.cal_multi()
	an_multi.print_answer()

	an_div = div.Div(1,2)
	an_div.cal_div()
	an_div.print_answer()