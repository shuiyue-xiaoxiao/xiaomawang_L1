print("-- -- -- 欢迎登录字符串医院分诊系统 -- -- --")

service = input("请选择需要的医疗服务\n1：字符串缝合\n2：字符串分割\n3：变身药剂\n4：清除感染细胞")
if service == "1":
    print("欢迎来到字符串缝合手术室")
    str_list = []
    str_num = input("请输入需要缝合的字符个数：")
    for i in range(int(str_num)):
        str_info = input("请输入需要缝合的字符：")
        str_list.append(str_info)
    print(str_list)
    custom_line = input("自定义缝合线：")
    result = custom_line.join(str_list)
    print("字符串" + result + "缝合成功！")
elif service == "2":
    print("欢迎来到字符串分割手术室")
    str_info = input("请输入需要分割的字符串：")
    custom_line = input("请输入自定义分割线：")
    result = str_info.split(custom_line)
    print("字符串" + str_info + "成功分割为" + str(result))
elif service == "3":
    print("欢迎来到字符串药剂科")
    str_info = input("请输入需要注射药剂的字符串：")
    medicament = input("请选择药剂的种类：\n1：变大药剂\n2：缩小药剂\n3：大头药剂\n4：反转药剂")
    if medicament == "1":
        result = str_info.upper()
    elif medicament == "2":
        result = str_info.lower()
    elif medicament == "3":
        result = str_info.capitalize()
    elif medicament == "4":
        result = str_info.swapcase()
    print("药剂生效" + str_info + "变为" + result)
elif service == "4":
    print("欢迎来到字符串感染治疗科")
    str_info = input("请输入需要治疗的字符串：")
    result = ""
    for i in str_info:
        if i.isnumeric():
            continue
        else:
            result += i
    print("治疗成功，" + str_info + "恢复成：" + result)












    
