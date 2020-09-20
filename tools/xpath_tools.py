# ^_^ coding:utf-8 ^_^
"""
-------------------------------------------------
   文件名：xpath_tools.py
   描述: web控件路径 适配模块
   作者: penglingsen
   创建日期: 2019/11/19
-------------------------------------------------
"""
import importlib,os,traceback

class XpathTools:

    def __init__(self,target_obj):
        self.__target_obj = target_obj

    def __auto_module(self,type, deviceType, deviceVersion, feature, className):
        '''
        命令行动态加载
        :param type: 测试平台类型[product,platform]
        :param deviceVersion: 设备C版本信息
        :param feature: 模块文件名称
        :param className: 类型
        :return: classObj
        '''
        if type == 'Platform':
            imp_module = "DAMA_AUTOTEST." + type + '.cmd.' + deviceVersion + '.' + feature
        else:
            if deviceVersion == None:
                imp_module = "Venus." + type + '.common.' + feature
            else:
                imp_module = "Venus." + type + '.' + deviceType + '.' + deviceVersion + '.' + feature


        imp_class = className

        # 加载动态模块中的类
        ip_module = importlib.import_module(imp_module)
        return getattr(ip_module, imp_class)  # 返回找到的类模块

    def __getTypeAndVersion(self):
        dev_type = self.__target_obj.get_dev_type()
        dev_ver = self.__target_obj.get_dev_version()
        return [dev_ver,dev_type]

    def get_xpath(self,feature, className, function, type='product'):
        '''
        获取command命令控制字
        :param feature: 模块文件名称
        :param className: 模块类名
        :param function: 命令行接口方法名称（cmd_特性方法名）
        :param type: 测试对象类型（平台/产品）
        :return: command特性命令行对应的类模块
        '''

        versionList = []
        # 支撑工程路径
        projectDir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # print("projectDir:",projectDir)
        # 设备类型和版本（类型默认为common，版本从设备获取）
        versionAndType = self.__getTypeAndVersion()

        file_list = os.listdir(projectDir + '/' + type+'/'+versionAndType[1])
        version_list = []
        for cur_file in file_list:
            if ('.' not in cur_file):
                version_list.append(cur_file)

        ClassName = []

        try:  # 当组网图中的版本没在versionList中时，不抛出异常，程序继续运行
            for i in range(version_list.index(versionAndType[0]), -1, -1):
                # print(versionAndType[1],version_list[i])
                curClassName = self.__auto_module(type, versionAndType[1],version_list[i], feature, className)

                if hasattr(curClassName(devType=versionAndType[1]), function):
                    ClassName.append(curClassName)
                    break
                else:
                    curClassName = self.__auto_module(type, version_list[i], feature, className)
                    if hasattr(curClassName(devType=versionAndType[1]), function):
                        ClassName.append(curClassName)
                        break
        except Exception:
            getCmdErr = traceback.format_exc()
            print(getCmdErr + '\n命令行提取错误')

        if ClassName == []:
            # 产品分类中找不到，寻找common
            curClassName = self.__auto_module(type,'common',None,feature,className)
            if hasattr(curClassName(devType=versionAndType[1]), function):
                ClassName.append(curClassName)
            else:
                AssertionError("未映射到相关操作，请检查")

        return ClassName[0](devType=versionAndType[1])