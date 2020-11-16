# import paramiko
#
# ip = "47.107.86.238"  # 服务器ip
# port = 22  # 端口号
# username = "root"  # 用户名
# password = "18366034218Aa"  # 密码
#
#
# def uploadfiletoserver(local, remote):  # 上传文件到服务器.第一个参数是要上传文件的本地路径；第二个参数是上传到服务器的路径
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(ip, port, username, password)
#
#     sftp = ssh.open_sftp()
#     sftp.put(local, remote)
#     return remote
#
#
# 在客户端打开远端服务器上的文件或文件夹
# def openremotefile(filepath):  # filepath是服务器上要打开的文件的绝对路径
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect(ip, port, username, password, compress=True)
#     sftp_client = client.open_sftp()
#     remotefile = sftp_client.open(filepath)  # 文件路径
#     return remotefile
#
#
# def main():
#     uploadfiletoserver('D:/谷歌浏览器下载地址/22.png', '/www/wwwroot/python/')
#
#
# if __name__ == "__main__":
#     main()


# import os,time
# import pyautogui as pag
# try:
#     while True:
#             print("Press Ctrl-C to end")
#             x,y = pag.position() #返回鼠标的坐标
#             posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
#             print (posStr)#打印坐标
#             time.sleep(0.2)
#             #os.system('cls')#清楚屏幕
# except  KeyboardInterrupt:
#     print ('end....')

# d = {"北京大学":"北京", "中国人民大学":"北京","清华大学":"北京",\
# "北京航空航天大学":"北京","北京理工大学":"北京","中国农业大学":"北京",\
# "北京师范大学":"北京","中央民族大学":"北京","南开大学":"天津",\
# "天津大学":"天津","大连理工大学":"辽宁","吉林大学":"吉林",\
# "哈尔滨工业大学":"黑龙江","复旦大学":"上海", "同济大学":"上海",\
# "上海交通大学":"上海","华东师范大学":"上海", "南京大学":"江苏",\
# "东南大学":"江苏","浙江大学":"浙江","中国科学技术大学":"安徽",\
# "厦门大学":"福建","山东大学":"山东", "中国海洋大学":"山东",\
# "武汉大学":"湖北","华中科技大学":"湖北", "中南大学":"湖南",\
# "中山大学":"广东","华南理工大学":"广东", "四川大学":"四川",\
# "电子科技大学":"四川","重庆大学":"重庆","西安交通大学":"陕西",\
# "西北工业大学":"陕西","兰州大学":"甘肃", "国防科技大学":"湖南",\
# "东北大学":"辽宁","郑州大学":"河南", "湖南大学":"湖南", "云南大学":"云南", \
# "西北农林科技大学":"陕西", "新疆大学":"新疆"}
# lis=[]
# for i in d.values():
#     lis.append(i)
# print("\n北京:%d\n天津:%d\n辽宁:%d\n吉林:%d\n黑龙江:%d\n上海:%d\n江苏:%d\n浙江:%d\n安徽:%d\n福建:%d\n山东:%d\n湖北:%d\n湖南:%d\n广东:%d\n四川:%d\n重庆:%d\n陕西:%d\n甘肃:%d\n辽宁:%d\n河南:%d\n云南:%d\n新疆:%d"%(lis.count('北京'),lis.count('天津'),lis.count('辽宁'),lis.count('吉林'),lis.count('黑龙江'),lis.count('上海'),lis.count('江苏')  ,lis.count('浙江')  ,lis.count('安徽')  ,lis.count('福建')  ,lis.count('山东')  ,lis.count('湖北')  ,lis.count('湖南')  ,lis.count('广东')  ,lis.count('四川')  ,lis.count('重庆')  ,lis.count('陕西')  ,lis.count('甘肃')  ,lis.count('辽宁')  ,lis.count('河南')  ,lis.count('云南')  ,lis.count('新疆') ))