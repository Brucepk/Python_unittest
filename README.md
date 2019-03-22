# Python 中自带框架 unittest 详解

## 本代码文章首发于公众号「Python知识圈」，如需转载，请通过公众号联系作者pk哥，谢谢

![公众号](https://github.com/Brucepk/pk.github.io/blob/master/gzh.jpg)

### 也可以通过微信联系我。

![微信](https://github.com/Brucepk/pk.github.io/blob/master/pkwx.jpg)

之前给大家分享过用 RF 做自动化测试入门的系列文章，包括 Web 端和 App 端的自动化，大家可以点下面链接查看。

[自动化入门](https://mp.weixin.qq.com/s?__biz=MzU4NjUxMDk5Mg==&mid=2247484684&idx=1&sn=96d20a638faefa928d581e4e4609d781&chksm=fdfb62f3ca8cebe5fac62fc74f4a9818f1fb2ee27a95706b0afabb89ee6b6d56bf69fe5b8cfa&token=1313071969&lang=zh_CN#rd)
[Web 自动化测试](https://mp.weixin.qq.com/s?__biz=MzU4NjUxMDk5Mg==&mid=2247484702&idx=1&sn=ac18a91197a06587ea7cccab1203da86&chksm=fdfb62e1ca8cebf7c2b61f3258f3b0f0a4e15368d357db5d38423678133d2bf19dd988b095f1&token=1313071969&lang=zh_CN#rd)
[APP 自动化测试](https://mp.weixin.qq.com/s?__biz=MzU4NjUxMDk5Mg==&mid=2247484718&idx=1&sn=d4b6179ff1310b2271e15e68b9696e45&chksm=fdfb62d1ca8cebc741530ff7b99b58f4895e406f946b7e6fd75817d75527a4073c1b41821e34&token=1313071969&lang=zh_CN#rd)
[集成工具 Jenkins 搭建](https://mp.weixin.qq.com/s?__biz=MzU4NjUxMDk5Mg==&mid=2247484740&idx=1&sn=e83c346aa622c3cc94e618cf82990ed3&chksm=fdfb62bbca8cebaddf98d921527a88d31dfb8626b49e2883188e7ea0c6fbc199dd6c74438d7f&token=1313071969&lang=zh_CN#rd)
[集成工具 Jenkins 定时操作](https://mp.weixin.qq.com/s?__biz=MzU4NjUxMDk5Mg==&mid=2247484762&idx=1&sn=ceb4933c7f37b1df966e8e42112f0d59&chksm=fdfb62a5ca8cebb36c5141d29174fb6479f83d16b4422535265f3c30f598124d607a5c67c419&token=1313071969&lang=zh_CN#rd)

RF 的全称是 RobotFramework，它是第三方的框架，使用它必须先安装。RF 框架的优点在于对编程新手比较友好，支持关键字驱动。通常的适用场景是用一位有编程功力的自动化工程师搭建好框架，封装好常见的关键字，然后由不同的功能业务部门的测试人员调用关键字进行自动化测试脚本的编写。编写人员可以对编程没什么基础甚至零基础，因为调用的固定功能都已经封装好了。所以，对于编程新手而已，这个框架更像一个工具，我们往里面堆砌步骤就可以完成。

但是对于有编程基础的同学来说，一昧的调用关键字对我们的技术没有太大的提升，Python 入门了后，我们就要拿来用了，语言本来就是工具，多用用才能更加熟练。所以，今天我想分享的框架是 Python 自带的 unittest 框架，这个框架扩展性也比较强，可以做 Web 和 APP 的自动化，扩展性强。

