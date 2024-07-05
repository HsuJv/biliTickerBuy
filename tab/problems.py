import gradio as gr

def problems_tab():
    gr.Markdown("""


## QA 合集：
> 下面是我们使用大数据（？）收集到的一些**不知名**问题。
1. Q: 我能用手机运行这个项目吗？  
A: 暂时不能。
2. Q: 设置配置的那一栏，我需要所有都填吗？  
A: 不需要，请直接二选一。
3. Q: “配置文件格式错误: Expecting value...” 是什么问题？  
A: 请您查看您上传的是否为**非空的** .json 文件。
4. Q: 为什么我的抢票页面无法访问了？  
A: 麻烦您看看您是不是打开网页后关闭了控制台（弹出来的那个黑框框），如果是，请重新开启程序。
5. Q: 为什么我无法获取 cookie 了？  
A: 原因**一般有**两个：一个是未使用 Edge 浏览器；另一个是新设备验证。  
对于前一个，请自行更换默认浏览器；后者，请单开一个浏览器并进入 [BiliBili](https://www.bilibili.com) 进行新设备验证后再获取 cookie .
6. Q: 如何多开？  
A: 复制一份程序**所在文件夹内所有文件**到不同的**文件目录**，再打开相应程序。
7. Q: 为什么我一打开程序就会闪退？  
A: 虽然**这个问题**不应该在这里才得到答案，但是您可以告诉问问题的人，让他们**右键**使用管理员模式打开程序。

## 迷惑行为大赏：
1. 拍屏不打码个人信息；
2. 不发日志就问问题；
3. 从非 Github 等官方渠道获取该项目 Release 的；
4. 打开网页后关闭控制台的；
5. 配置文件里上传 exe 文件的；
6. **到处张扬**这个项目或发 Bilibili 视频的**显眼包**。 

## 我该如何提问？
问得好！要想得到详细的答案，  
请带上您的**打码了敏感信息**的日志/截图，附上详细的问题、诚恳的态度，  
大多数人都会十分乐意解答您的问题。  

如果还是没得到答案，请接着提问 “我该如何做呢？”。

         
> [Tip]  
> 如果你是买来这个程序的话：恭喜你被骗了！   
> 另外，本项目已开启[爱发电](https://afdian.net/a/mikumifa)，如果你想支持本项目请点击上面的那个网址。

本项目免责声明详见项目地址的 readme.md.
""")