导入课表到iOS日历


1.爬取课表信息
2.根据xlsx文件，填写课表（注意：1，2节课classTime为1，方便classTimeinfo.josn文件设置）
3.python -u excleReader.py 生成Classinfo.json
4.根据情况修改ClassTimeinfo.json
5.python -u main.py 生成ics文件
6.导入苹果设备即可
