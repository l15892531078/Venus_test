from global_veriable import *
import time
import telnetlib
import re

class AutoFilling:
    '''
    自动化灌装 TODO 添加异常判断
    '''
    def __init__(self):
        self.tn = telnetlib.Telnet(HOST, port=PORT, timeout=10)
        # self.tn.set_debuglevel(2)

    def command(self, flag='', str_="", func=None, read_all=False, write=False, read=False, timeout=None, **kwargs):
        if read_all:
            self.tn.write(str_.encode() + b"\n")
            time.sleep(2)
            data = self.tn.read_very_eager()
            data = data.decode('utf8')
            if func:
                manage_data = func(data, **kwargs)
                return manage_data
            return data
        elif write:
            self.tn.write(str_.encode()+b"\n")
        elif read:
            data = self.tn.read_very_eager()
            data = data.decode('utf8')
            return data
        else:
            data = str(self.tn.read_until(flag.encode(), timeout=timeout), encoding='utf8')
            self.tn.write(str_.encode()+b"\n")
            return data

    def select_disk(self, data):
        '''
        选择磁盘
        :param data:
        :return:
        '''
        disk = {}
        disk_str = data.split('\n')
        # 截取字符串
        for info in disk_str:
            if re.match(r'.*disk\[\d\].*', info):
                temp = info.split(':')
                disk_num = temp[0].strip()
                disk_size = temp[1].split('  ')
                disk_size = disk_size[-1].replace('\r', '').replace('(*)', '').strip()
                if disk_size.endswith('MB'):
                    disk_size = re.findall('\d*', disk_size)[0]
                    disk_size = str(int(disk_size)//1024) + 'GB'
                disk[disk_num] = disk_size
        #选择硬盘
        disk_list = []
        num = 0
        for disk_num, disk_size in disk.items():
            disk_size = re.findall('\d*', disk_size)[0]
            # 目前bootloader最大为8G
            if int(disk_size) > 8:
                disk_list.append(str(num))
            num += 1

        return disk_list

    def select_disk_format(self, data, format='EXT4'):
        format_str = data.split('\n')
        for info in format_str:
            temp = info.split('. ')
            num = temp[0].strip()
            disk_format = temp[-1].strip()
            if disk_format == format:
                return num

    def enter_bootloader(self):
        '''
        重启cs，进入bootloader
        :param data:
        :return:
        '''
        info = self.command(read_all=True)
        if 'Username' in info:
            self.command(str_='adm', write=True)
            self.command('Password', str_=CS_PASSWORD)
        time.sleep(1.5)
        verify = self.command(str_='reboot', read_all=True)
        if 'confirm' in verify:
            self.command(str_='y', write=True)
        self.command(flag='4 second', str_='\3\n')

    def format_disk(self, single_disk=False):
        '''
        格式化硬盘 单硬盘则不格盘
        :return:
        '''
        self.command()
        self.command('Please input your choice[1-6]: ')
        time.sleep(1)
        disk = self.command('Please input your choice[1-6]: ', 'f', func=self.select_disk, read_all=True)
        if len(disk) >= 1:
            format_num = self.command(str_=disk[0], func=self.select_disk_format, read_all=True)
            self.command(str_=format_num)
            self.command('will be formated, continue ? (y/n): ', 'y')
        else:
            self.command(str_='q', write=True)
            single_disk = True
        return single_disk

    def tftp_config(self):
        '''
        tftp配置
        :return:
        '''
        self.command()
        self.command(flag='Please input your choice[1-6]: ', str_='1')
        self.command(flag='Do you want to edit startup script - continue (y/n)? ', str_='y')
        self.command('Startup image', ENGINE_FILE)
        self.command('Startup local', ENGINE_IP)
        self.command('Startup mask')
        self.command('Startup interface', ENGINE_INTERFACE)
        self.command('Startup server', FTP_IP)
        self.command('Startup gateway', GATEWAY)
        self.command('Are you sure to store the parameters above - continue (y/n)?', 'y')

    def tansfer_file(self):
        '''
        传输引擎
        :return:
        '''
        self.command('Please input your choice[1-6]: ', '2')
        info = self.command(read=True)
        return info

    def reboot_cs(self):
        self.command()
        self.command('Please input your choice[1-6]: ', '6')

    def close(self):
        self.tn.close()

    def check(self, target_str, source_str):
        if target_str in source_str:
            return True
        else:
            return self.tn.close()

    def gb_operation(self):
        try:
            self.enter_bootloader()
            disk_res = False
            single_disk = self.format_disk()
            if not single_disk:
                info = self.command(flag='Writing superblocks and filesystem accounting information: done',
                                    timeout=1200)
                disk_res = self.check('done', info)
            if disk_res or single_disk:
                self.tftp_config()
                self.tansfer_file()
                info = self.command(flag='Finish to install version file!', timeout=600)
                res = self.check('Finish', info)
                if res:
                    self.reboot_cs()
                    self.close()
        except Exception as e:
            raise e



if __name__ == '__main__':
    gb = AutoFilling()
    gb.gb_operation()
