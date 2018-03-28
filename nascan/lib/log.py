# coding:utf-8
import threading
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
mutex = threading.Lock()
def write(scan_type, host, port, info):
    mutex.acquire()
    port = int(port)
    try:
        log_str = ""
        time_str = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
        if scan_type == 'portscan':
            log_str = "[%s] %s:%d open" % (time_str, host, port)
        elif scan_type == 'server':
            log_str = "[%s] %s:%d is %s" % (time_str, host, port, str(info))
        elif scan_type == 'web':
            log_str = "[%s] %s:%d is web" % (time_str, host, port)
            log_str += "\n"
            log_str += "[%s] %s:%d web info %s" % (time_str, host, port, info)
        elif scan_type == 'active':
            log_str = "[%s] %s active" % (time_str, host)
        elif scan_type == 'info':
            log_str = "[%s] %s" % (time_str, info)

        print log_str
        with open("scan.log","a") as f:
            f.write(log_str+'\n')
    except Exception, e:
        print 'logerror',e
        pass
    mutex.release()
