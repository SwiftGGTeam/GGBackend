# App 接口文档
- [通用请求返回格式](#通用请求返回格式)
- [文章](#文章)
    - [文章列表](#文章列表)
    - [文章详情](#文章详情)
- [商品](#商品)
    - [商品列表](#商品列表)
    - [商品详情](#商品详情)
- [活动](#活动)
    - [活动列表](#活动列表)

## 通用请求返回格式
```json
{
    "success": true,
    "message": "",
    "results": {
 
    }
}
```
## 文章
### 文章列表
| 参数名 | 是否可选 | 备注 |
| --- | --- | --- |
| page | 是 | 页数，默认为 1 |
| size | 是 | 分页大小，默认为 10 |

接口地址：`GET` `http://api.swift.gg/app/posts`

```json
{
    "success": true,
    "message": "",
    "results": {
        "pageBean": {
            "page": 1,
            "size": 10,
            "total": 262
        },
        "items": [
            {
                "id": 238,
                "title": "千呼万唤始出来：SwiftWebUI",
                "preface": "六月初，Apple 在 WWDC 2019 上发布了 SwiftUI。SwiftUI 是一个“跨平台的”、“声明式”框架，用于构建 tvOS、macOS、watchOS 和 iOS 上的用户界面。SwiftWebUI 则将它带到了 Web 平台上✔️。",
                "imageURL": "",
                "category": "The Always Right Institute",
                "publishDate": "2019-09-12"
            },
            {
                "id": 237,
                "title": "面向协议教程",
                "preface": "对于开发者来说，复杂性是最大的敌人，因此我会去了解那些可以帮助我管理混乱的新技术。Swift 中的“面向协议编程”（POP）是最近（至少自2015年以来）引起广泛关注的“热门”方法之一。在这里我们将使用 Swift 4。在我自己编写代码时，发现 POP 很有前途。更吸引人的是，Apple 宣称 “Swift 的核心是面对协议的”。我想在一个正式的报告中分享关于 POP 的经验，一篇关于这个新兴技术清晰而简洁的教程。我将解释关键概念，提供大量代码示例，无法避免的将 POP 和 OOP （面向对象编程）进行比较，并对面向流行编程（FOP?）的人群所声称的 POP 是解决所有问题的灵丹妙药这一说法进行泼冷水。面向协议编程是一个很棒的新工具，值得添加到你现有的编程工具库中，但是没有什么可以代替那些经久不衰的基本功，就像将大的函数拆分成若干个小函数，将大的代码文件拆分成若干个小的文件，使用有意义的变量名，在敲代码之前花时间设计架构，合理而一致的使用间距和缩进，将相关的属性和行为分配到类和结构体中 - 遵循这些常识可以让世界变得不同。如果你编写的代码无法被同事理解，那它就是无用的代码。学习和采用像 POP 这样的新技术并不需要绝对的唯一。POP 和 OOP 不仅可以共存，还可以互相协助。对于大多数开发者包括我自己，掌握 POP 需要时间和耐心。因为 POP 真的很重要，所以我将教程分成两篇文章。本文将主要介绍和解释 Swift 的协议和 POP。第二篇文章将深入研究 POP 的高级应用方式（比如从协议开始构建应用程序的功能），范型协议，从引用类型到值类型转变背后的动机，列举 POP 的利弊，列举 OOP 的利弊，比较 OOP 和 POP，阐述为什么“Swift 是面向协议的”，并且深入研究一个被称为 “局部推理” 的概念，它被认为是通过使用 POP 增强的。这次我们只会粗略涉及一些高级主题。  ",
                "imageURL": "",
                "category": "POP",
                "publishDate": "2019-09-05"
            },
            {
                "id": 236,
                "title": "Swift 关键字",
                "preface": "有句话之前我提过，今天还想再说一次。那就是打铁还需自身硬。对于自身能力的严格要求，可以帮助实现我们所有梦寐以求的东西。说起来可能有些消极，知识毕竟是永远学不完的。不论如何，今天 我们先来学习一下 Swift 中的每一个关键字（V3.0.1），在介绍每个关键字的时候，同时会附带一段代码加以说明。在这些关键字之中，会有你熟悉或者不熟悉的部分。但为了最好的阅读和学习体验，我把它们全部列出来了。文章篇幅有些长，你准备好了么？让我们现在就开始吧。",
                "imageURL": "",
                "category": "swiftjectivec",
                "publishDate": "2019-08-22"
            },
            {
                "id": 235,
                "title": "给 UIView 来点烟花",
                "preface": "",
                "imageURL": "",
                "category": "Tomasz Szulc",
                "publishDate": "2019-08-14"
            },
            {
                "id": 234,
                "title": "Bundles and Packages",
                "preface": "在这个给予的季节，让我们停下脚步，思考一个现代计算机系统赐予我们的最棒的礼物：抽象。在数百万 CPU 晶体管、SSD 扇区和 LCD 像素共同协作下，全球数十亿人能够日常使用计算机和移动设备而对此全然不知。这一切都应归功于像文件，目录，应用和文档这样的抽象。这周的 NSHipster，我们将讨论苹果平台上两个重要的抽象：包与包裹。🎁",
                "imageURL": "",
                "category": "Swift",
                "publishDate": "2019-07-19"
            },
            {
                "id": 233,
                "title": "Swift 中的集合（Set）",
                "preface": "集合（Set）是 Swift 集合类型（collection types）之一，集合用来存储类型相同且没有确定顺序唯一的值。你可以将集合想象成一盒台球：它们在颜色和数量上独一无二，但在盒内是无序的。",
                "imageURL": "https://swift.gg/img/articles/Sets-in-Swift/billiard.jpg1562643187.9223473",
                "category": "thomashanning",
                "publishDate": "2019-07-09"
            },
            {
                "id": 232,
                "title": "PhotoKit 的数据模型",
                "preface": "在 iOS 系统中，PhotoKit 框架 不仅被系统的照片 App 所使用，同时它也为开发人员访问设备的照片库提供了接口支持。而它的底层则是 Core Data 实现的。",
                "imageURL": "",
                "category": "PhotoKit",
                "publishDate": "2019-07-01"
            },
            {
                "id": 231,
                "title": "将 Swift 序列切分为头部和尾部",
                "preface": "函数式编程语言的一个常用范式是把一个列表切分为头部（第一个元素）和尾部（其余元素）。在 Haskell 中，x:xs 会匹配非空列表，将头部绑定给变量 x，尾部绑定给 xs。Swift 不是一门函数式编程语言。既没有内置的 List 类型，也没有集合的特定匹配语法。[1]",
                "imageURL": "",
                "category": "Ole Begemann",
                "publishDate": "2019-06-24"
            },
            {
                "id": 230,
                "title": "使用 Swift 实现基于堆的优先级队列",
                "preface": "在计算机科学中，有很多问题可以通过将底层数据结构用优先级队列实现来改善算法的时间复杂度。其中 Dijkstra 的最短路径算法便是一个例子，该算法使用了优先级队列来在图中搜索两个顶点间的最短路径。不幸的是，Swift 的标准库中并没有提供优先级队列的默认实现。所以我们将会研究如何自行实现基于堆的优先级队列。",
                "imageURL": "",
                "category": "AppCoda",
                "publishDate": "2019-05-06"
            },
            {
                "id": 229,
                "title": "Swift 5 字符串插值-简介",
                "preface": "StringInterpolation 协议最初的设计效率低下又不易扩展，为了在后续的版本中能够将其彻底重构，Swift 4 中将该协议标记为废弃。即将在 Swift 5 中亮相的 SE-0228 提案介绍了一种新的 StringInterpolation 设计，使得 String 有了更大的潜能。",
                "imageURL": "",
                "category": "Crunchy Development",
                "publishDate": "2019-04-22"
            }
        ]
    }
}
```

### 文章详情
接口地址：`GET` `http://api.swift.gg/app/post/[:id]`

例：http://api.swift.gg/app/post/486

```json
{
    "success": true,
    "message": "",
    "results": {
        "id": 486,
        "title": "Swift 关键字",
        "body": "xxx"
    }
}
```

## 商品
### 商品列表
接口地址：`GET` `http://api.swift.gg/app/products`

```json
{
    "success": true,
    "message": "",
    "results": {
        "banner": [
            {
                "id": 4,
                "name": "SwiftUI 与 Combine 编程（预售）",
                "price": 69.0,
                "preface": "通过实践快速上手 SwiftUI 及 Combine 响应式编程框架，掌握下一代客户端 UI 开发技术",
                "imageURL": "https://img.yzcdn.cn/upload_files/2019/06/12/FtHmxrlLZ5i-Scq1-_TcUDusLPj1.png?imageView2/2/w/580/h/580/q/75/format/png"
            },
            {
                "id": 1,
                "name": "Reveal 21",
                "price": 300.0,
                "preface": null,
                "imageURL": "https://img.yzcdn.cn/upload_files/2018/04/24/FoOuGqUaZk6yL8auDoejc3d77Z6y.png?imageView2/2/w/580/h/580/q/75/format/png"
            }
        ],
        "list": [
            {
                "id": 3,
                "name": "Anker PowerLine+ 2 可拉车苹果数据线二代 0.9米",
                "price": 148.0,
                "preface": "从 San Jose 亲手运送回来的 T 恤， 轻轻一闻，甚至还有加州阳光。 我在说什么?",
                "imageURL": "https://img.yzcdn.cn/upload_files/2018/08/02/FuuXxKLlb4BDwqOkClp0oYQGWjA2.jpg?imageView2/2/w/580/h/580/q/75/format/jpg"
            },
            {
                "id": 2,
                "name": "Design+Code",
                "price": 356.0,
                "preface": "购买前请先在浏览器打开 designcode.io 进行注册与试读，确认网络情况良好后再购买。",
                "imageURL": "https://img.yzcdn.cn/upload_files/2018/06/13/FoCU9cECbwXPZL3uXlHfWu1q2IpH.png?imageView2/2/w/580/h/580/q/75/format/png"
            }
        ]
    }
}
```

### 商品详情
接口地址：`GET` `http://api.swift.gg/app/product/4`

```json
{
    "success": true,
    "message": "",
    "results": {
        "id": 4,
        "name": "SwiftUI 与 Combine 编程（预售）",
        "price": 69.0,
        "originPrice": 99.0,
        "detail": "WWDC 2019 上 Apple 公布了声明式全新界面框架 SwiftUI，以及配套的响应式编程框架 Combine。对于 Apple 平台的开发者来说，这是一次全新的转变和挑战。本书通过几个具体的实战例子，由浅入深介绍了 SwiftUI 和 Combine 框架的使用方式及核心思想，帮助您顺利步入令人激动的 Apple 开发新时代。\r\n\r\n![](https://img.yzcdn.cn/upload_files/2019/06/12/FvXOyH6W9ifPV9ILwjGemNB9yp6l.png!730x0.jpg)",
        "purchaseURL": "https://detail.youzan.com/show/goods?alias=1ygghkmhvccf2"
    }
}
```

## 活动
### 活动列表
接口地址：`GET` `http://api.swift.gg/app/events`

```json
{
    "success": true,
    "message": "",
    "results": {
        "pageBean": {
            "page": 1,
            "size": 10,
            "total": 2
        },
        "items": [
            {
                "name": "2019 力扣杯全国秋季编程大赛",
                "state": "开放报名中",
                "date": "2019-09-24 ~ 2019-09-25",
                "place": "线上活动",
                "imageURL": "https://activity-static.segmentfault.com/265/003/265003973-5d76265be94cc_big",
                "registerURL": "https://leetcode-cn.com/contest/season/2019-fall/"
            },
            {
                "name": "DDD领域驱动设计峰会",
                "state": "开放报名中",
                "date": "2019-11-28 ~ 2019-11-30",
                "place": "北京市丽都皇冠假日酒店",
                "imageURL": "https://activity-static.segmentfault.com/341/320/3413202100-5d4299e9be6b7_big",
                "registerURL": "http://ddd-china.com"
            }
        ]
    }
}
```
