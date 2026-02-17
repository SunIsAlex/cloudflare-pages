---
date : '2026-02-02T16:36:28+08:00'
draft : false
title : '关于本站'
categories : ['网站建设','Linux命令']
tags : ["Nginx","Hugo","Linux"]
weight : 1
ShowToc : true
---

### 网站概况：

(通过JS请求[/api/neofetch]得到，每2秒更新)
<div class="highlight"><pre tabindex="0" style="color:#f8f8f2;background-color:#272822;-moz-tab-size:4;-o-tab-size:4;tab-size:4;-webkit-text-size-adjust:none;"><code id='stat' class="language"></code></pre></div>
<script>
    var stat = document.getElementById('stat');
    if(window.location.hostname=='github.alexsun.one'){
        stat.innerHTML = 'Github Pages<br>Repository:https://github.com/SunIsAlex/SunIsAlex.github.io';
    }else{
        let api_xhr = new XMLHttpRequest();
        neofetch = function(){
            if (api_xhr.readyState === XMLHttpRequest.DONE) {
                if (api_xhr.status === 0) {
                    console.log('请求被取消')
                } else if (api_xhr.status === 200) {
                    stat.innerText = api_xhr.response;
                } else {
                    console.error('请求失败:', api_xhr.status);
                }
            }
        }
        send_xhr = function(){
            api_xhr.open('GET','/api/neofetch');
            api_xhr.send();
        }
        api_xhr.onreadystatechange = neofetch;
        send_xhr();
        setInterval(send_xhr,2000);
    }
</script>

# 规划准备

此站于[清华附中](https://qhfz.edu.cn/)“极智”挑战期间(2026-01-31\~2026-02-06)搭建

笔者打算使用[*hugo*](https://www.alexsun.one/posts/hugo/)搭建静态博客网站，然后由nginx处理流量。

# 具体操作
1. 配置云服务器

    清华附中为学员提供了[阿里云ECS](https://www.aliyun.com/benefit/select/ecs)的服务器，这与笔者在初中时搭建的服务器类型相同。

    在Datacon注册及登录后，可以打开虚拟环境，查看ECS SSH的ip及密码，然后便可以通过SSH远程登录root账号（笔者使用了VSCode的OpenSSH插件）

    ```shell
    ssh -p 22 root@<your_ip>
    ```

    随后输入密码即可登录
2. 设置域名解析

    注册[Namesilo](https://www.namesilo.com/)的账号，并在Namesilo中购买一个域名（笔者购买了alexsun.one，花费24CNY），配置DNS记录，等待10分钟（TTL=3600）后即可全球生效
    | Type | Name | Text |
    | --- | --- | --- |
    | A | @ | <your_ip> |
    | A | www | <your_ip> |

    查看是否生效的方法：
    ```batch
    nslookup <host_name>
    ```
    如果正确返回<your_ip>，则DNS解析设置成功

3. 安装组件

    ## 安装nginx

    ```shell
    apt install nginx
    #安装nginx
    nginx
    ```
    然后访问http://host_name，若显示nginx欢迎页面，则成功
    
    ## 安装Hugo

    经笔者实测，Ubuntu上用apt安装的Hugo版本较老，与最新版本的ananke主题不兼容（这个浪费了笔者一晚上时间）

    ~~apt install hugo~~

    ```shell
    snap install --beta hugo
    hugo version
    ```
    > root@datacon-winterc:~/quickstart# hugo version
hugo v0.156.0-DEV-73641aeca107c26f53e9a0f76a141cdb43faf277+extended linux/amd64 BuildDate=2026-02-02T10:27:50Z VendorInfo=snap:0.155.2+git1.73641aeca

    这样就是安装成功Hugo了。

    ```shell
    hugo new site alexblog
    cd alexblog
    cd theme
    git clone https://github.com/theNewDynamic/gohugo-theme-ananke.git
    cd ..
    echo "theme = 'gohugo-theme-ananke'" >> hugo.toml
    hugo server
    ```
    alexblog目录结构如下：
    ```
    archetypes  assets  content  data  hugo.toml  i18n  layouts  public  resources  static  themes
    ```
    alexblog/public目录结构如下:
    ```404.html
    ananke
    asciinema
    assets
    book.min.cc2c524ed250aac81b23d1f4af87344917b325208841feca0968fe450f570575.css
    categories
    cdategories
    en.search-data.min.486891b2bf1f08818be2bdf8569fbadd5a4ca08de48415c4ca942d9353fe2404.json
    en.search-data.min.81946b14455debd3c2dab6f0ca6ba2c58dbc6e8bfbe6fddb06d433feb8340648.json
    en.search.min.28c0782592a93c540f59dfe0c5f5b4e0ccaa7a7e805178cd77913ca1169d5fae.js
    en.search.min.95caaac1812624d461b676a1695e701606990b8971b058a32d99aac655fa29c1.js
    favicon.png
    favicon.svg
    fuse.min.js
    icons
    images
    index.html
    index.json
    index.xml
    katex
    manifest.json
    mermaid.min.js
    page
    post
    posts
    search
    sitemap.xml
    tags
    test
    ```

    试着访问<host_name>:1313，未果。
    遂
    ```shell
    cp -r public/* /var/www/html
    #把Hugo生成的静态页面保存到nginx站点的目录下
    ```
    之后访问<host_name>，若正常看到Hugo站点，那么大功告成
    ## certbot
    我们使用certbot的standalone模式申请Let's Encrypt的免费证书（BTW:清华官网使用的也是Let's Encrypt的免费证书）

    Standalone是Certbot的一种工作模式，其会临时启动一个内置的Web服务器来处理Let's Encrypt的验证挑战
    ```shell
    apt install certbot
    systemctl stop nginx
    #避免nginx占用80端口
    certbot certonly --standalone -d www.alexsun.one
    ```
    一个证书也可以对应多个域名：
    ```shell
    certbot certonly --standalone -d www.alexsun.one -d alexsun.one -d cn.alexsun.one
    ```
    如果没有问题，你会获得公钥(fullchain.pem)和私钥(privkey.pem)
    在nginx配置文件/etc/nginx/sites-available/default中，把原有的server块再复制一份，并于新server块中加入
    ```shell
    ssl_certificate <path_to_fullchain.pem>
    ssl_certificate_key <path_to_privkey.pem>
    ```
    并把端口80改为443
    ```shell
    nginx -s reload
    #重启nginx
    ```
    之后https://<host_name>应该就可以正常访问了

4. 新增文章

    ```shell
    hugo new content posts/new_post.md
    ```
    新增的new_post.md内容如下
    ```markdown
    +++
    date = '2026-02-03T09:12:29+08:00'
    draft = true
    title = 'New_post'
    +++
    ```
    new_post.md的默认内容在quickstart/archetypes/default.md
    我根据自己的习惯，修改为
    ```markdown
    ---
    date : '{{ .Date }}'
    draft : true
    title : '{{ replace .File.ContentBaseName "-" " " | title }}'
    ---
    ```
    按照[markdown正常格式](posts/markdown/)书写文章即可（记得把draft = true改为draft = false）
    ```shell
    hugo
    cp -r public/* /var/www/html
    #更新站点
    ```
# 结语

到此为止，Hugo个人博客的搭建基本完成。进一步完善网站，如增加LaTex数学表达式支持，或设置menu，更换主题，美化网站等内容，可以参考[Hugo官方文档](https://gohugo.io/documentation/)
