    
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget

引入包含PyQt5基本组件的模块
    
    app = QApplication(sys.argv)
    
每个PyQt5应用都需要创建一个应用对象，sys.argv是一组命令行参数的列表，Python可以在shell里运行，该参数提供对脚本控制的功能

    w = QWidget()

QWidget控件是一个用户界面的基本控件，它提供了基本的应用构造器。默认情况下构造器没有父级，没有父级的构造器被称为窗口（window）

    w.resize()
    w.move()
    w.setWindowTitle('')

resize()用于改变控件大小(width, height)
move()用于修改控件位置，参数为屏幕坐标系，单位为像素
setWindowTitle()用于添加标题于标题栏

    w.show()

show函数用于让控件在桌面上显示出来

    sys.exit(app.exec_())

事件开始循环后，调用exit方法或销毁主控件时，主循环结束。sys.exit()能确保主循环安全退出。外部环境能通知主控件怎么结束
exec_()带有下划线因为exec是一个Python关键字