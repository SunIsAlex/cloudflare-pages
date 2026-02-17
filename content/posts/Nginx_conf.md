---
date : '2026-02-05T10:47:08+08:00'
draft : false
title : 'Nginx安全配置'
categories : ['网站建设','网络','Linux命令']
Tags : ['Linux','nginx']
---

```shell
root@datacon-winterc:~/quickstart# cat /etc/nginx/nginx.conf | grep access_log
access_log /var/log/nginx/access.log; #nginx访问日志文件
```
```shell
grep wp-admin /var/log/nginx/access.log | cat -n
#查看日志中含wp-admin(wordpress后台)的内容
```
```
1  162.158.182.84 - - [05/Feb/2026:00:05:25 +0800] "GET /wordpress/wp-admin/setup-config.php HTTP/1.1" 404 134 "-" "https://alexsun.one/wordpress/wp-admin/setup-config.php"
......
73  172.71.184.188 - - [05/Feb/2026:10:49:11 +0800] "GET /wp-admin/setup-config.php HTTP/1.1" 444 0 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
```
我的站点上并没有安装WordPress，以上73条访问日志来自于***恶意扫描***[^1]
![IP信息](https://free.picui.cn/free/2026/02/05/69840e9e9cc7c.png)

用nginx的location可以配置路由，实现对恶意扫描的处理：
```
location [modifier] [URI] {

}
```
>下面下面是 Nginx 中 **location** 指令最常用的几种匹配方式（modifier）的语法总结，以表格形式呈现，便于对照和记忆。

| 优先级 | Modifier（修饰符） | 匹配类型 | 大小写敏感 | 说明 | 示例 | 典型使用场景 |
|--------|---------------------|-------------------|------------|----------------------------------------------------------------------|-------------------------------------------|---------------------------------------|
| 1 | = | 精确匹配 | 是 | 必须完全相等（包括结尾斜杠），一旦命中立即停止搜索其他 location | `location = /` <br>`location = /index.html` | favicon.ico、首页、特定静态文件 |
| 2 | ^~ | 前缀匹配（优先） | 是 | 前缀匹配，命中后**不再检查正则** location（最长前缀优先） | `location ^~ /wp-` <br>`location ^~ /images/` | 屏蔽扫描路径、静态资源目录 |
| 3 | ~ | 正则匹配 | 是（区分） | 正则表达式匹配，区分大小写，按配置文件出现顺序逐个尝试 | `location ~ \.php$` <br>`location ~ ^/admin` | 处理 .php 文件、特定路径规则 |
| 4 | ~* | 正则匹配（忽略大小写） | 否 | 正则表达式匹配，不区分大小写，按配置文件出现顺序逐个尝试 | `location ~* \.(jpg|png|gif)$` <br>`location ~* \.php$` | 图片、js/css 等不区分大小写的文件 |
| 5 | （无修饰符） | 前缀匹配（普通） | 是 | 普通前缀匹配，匹配最长前缀后继续尝试正则（除非被 ^~ 阻止） | `location /` <br>`location /blog/` | 默认根路径、子目录兜底 |
| 特殊 | @name | 命名 location | — | 内部跳转使用，不能直接被外部请求命中 | `location @fallback { ... }` | error_page 跳转、try_files 内部重定向 |

```
# 屏蔽常见的 WordPress 扫描路径（可放在 server {} 内或 include 到所有 server）
location ~* ^/(wp-admin|wp-login\.php|wp-config\.php|xmlrpc\.php|readme\.html|license\.txt|wp-signup\.php|setup-config\.php) {
    # return HTTP_RESPONSE_CODE
    # 或者用 return 403; 但 444 更省资源
    return 444;
}
```
关于HTTP状态码，详见[HTTP_RESPONSE_STATUS_CODE](https://www.alexsun.one/posts/http_response_status_code/)

更加简单粗暴的解决方案：
```
location ~ (php|aspx|git|python) {
   	return 444;
}
```
如果访问这些路径，服务器断开连接，则配置成功
```shell
root@datacon-winterc:~/quickstart# curl -i https://www.alexsun.one/index.php
curl: (52) Empty reply from server
```
[^1]:*自动化扫描行为（reconnaissance scanning）*，不是针对你个人的攻击，而是几乎所有*暴露在公网*的服务器都会遇到的“噪音”。
