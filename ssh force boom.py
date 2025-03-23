from pexpect import pxssh


def Login(server, username, password):
    try:
        s = pxssh.pxssh()
        # 此处login方法为pxssh类中的方法，借助ssh协议，使用提供的信息尝试登陆到远程服务器
        s.login(server, username, password)
        print("yes")
    except:
        print("no")


def main():
    Login("192.168.80.129", "root", "toor")

if __name__ == "__main__":
    main()
