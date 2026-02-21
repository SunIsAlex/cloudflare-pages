---
weight: 1000
title: "蓝屏0xc000000e修复"
date: 2026-02-20
categories: ["系统修复", "Windows", "UEFI"]
tags: ["EFI分区", "引导修复", "bcdboot", "蓝屏0xc000000e", "winload.efi"]
draft: false
---

## 问题引入

误删 {{< star info="GPT磁盘上的独立启动分区，负责保存UEFI引导文件与BCD数据。" >}}EFI 分区{{< /star >}}或破坏 BCD 后，Windows 启动蓝屏：

- 错误码：0xc000000e 或 0xc0000225
- 提示：**winload.efi 文件缺失或包含错误**

系统分区中的 **`\Windows\System32\winload.efi`** 文件通常仍然存在。

这类报错的关键不是文件真的没了，而是：

> Windows Boot Manager 已经启动，但无法根据 BCD 正确定位系统分区。

---

## ⚠ 适用前提

- 磁盘为 **GPT**
- 启动模式为 **UEFI**
- Windows 以 UEFI 模式安装

验证：

```cmd
diskpart
list disk
```

可能输出：

```
  磁盘 ###  状态         大小     可用     动态  GPT
  --------  -----------  -------  -------  ------  ---
  磁盘 0    联机          476 GB      0 B        *
```

带 `*` 表示 GPT。

---

## 正确理解启动链条

UEFI 启动流程：

1. 主板 UEFI 固件
2. 读取 EFI 分区（FAT32）
3. 加载 **`\EFI\Microsoft\Boot\bootmgfw.efi`**
4. 读取 **`\EFI\Microsoft\Boot\BCD`**
5. 根据 BCD 中记录的分区 GUID，定位系统分区
6. 加载 **`\Windows\System32\winload.efi`**

在本问题中：

- 步骤 1~3 正常
- Windows Boot Manager 可以启动
- 但步骤 5 无法完成（BCD 记录失效或指向错误分区）
- 因此提示找不到 **`\Windows\System32\winload.efi`**

---

## 使用工具

| 工具       | 作用                      | 下载链接                            | 备注                  |
|------------|---------------------------|-------------------------------------|-----------------------|
| WEPE / FirPE | 进入 PE 修复环境          | https://www.wepe.com.cn            | 推荐微 PE            |
| DiskGenius | 创建 / 查看 EFI 分区      | https://www.diskgenius.cn          | 免费版够用           |
| bcdboot    | 重建启动文件              | 系统自带                            | 最稳定               |
| EasyUEFI   | 删除多余启动项            | https://www.easyuefi.com           | 可选                 |
| DISM++     | 图形化修复引导            | https://github.com/Chuyu-Team/Dism-Multi-language | 不如 bcdboot 稳 |

---

# 修复步骤

使用 U 盘启动进入 PE。

---

## 第一步：确认分区状态

```cmd
diskpart
list vol
```

可能输出：

```
  卷 ###  Ltr  标签           Fs     类型        大小     状态     信息
  ----------  ---  -----------  -----  ----------  -------  ---------  --------
  卷 0         D   Windows      NTFS   分区        200 GB   正常
  卷 1              System      FAT32  分区        100 MB   正常     隐藏
```

确认：

- NTFS 分区包含 Windows 文件夹
- 存在 FAT32 小分区（EFI）

如果 EFI 分区不存在，需要先重建（300MB FAT32，类型为 EFI 系统分区）。

---

## 给 EFI 分区分配盘符

```cmd
diskpart
select vol 1
assign letter=Z
exit
```

可能输出：

```
DiskPart successfully assigned the drive letter or mount point.
```

---

# 重建 BCD 与启动文件（核心步骤）

假设：

- Windows 在 D:
- EFI 在 Z:

执行：

```cmd
bcdboot D:\Windows /s Z: /f UEFI
```

正常输出：

```
Boot files successfully created.
```

该命令会：

- 重新生成 **`\EFI\Microsoft\Boot\bootmgfw.efi`**
- 重建 **`\EFI\Microsoft\Boot\BCD`**
- 写入正确的分区 GUID

---

# 如果 bcdboot 报错

可能输出：

```
Failure when attempting to copy boot files.
```

可执行：

```cmd
bootrec /fixboot
bootrec /scanos
bootrec /rebuildbcd
```

可能输出（/rebuildbcd 阶段）：

```
Successfully scanned Windows installations.
Total identified Windows installations: 1
Add installation to boot list? Yes(Y)/No(N)/All(A):
```

输入：

```
Y
```

然后再次执行：

```cmd
bcdboot D:\Windows /s Z: /f UEFI
```

---

# 移除临时盘符

```cmd
diskpart
select vol 1
remove letter=Z
exit
```

可能输出：

```
DiskPart successfully removed the drive letter or mount point.
```

关机 → 拔 U 盘 → 重启。

---

# 清理多余启动项（可选）

```cmd
bcdedit /enum firmware
```

删除无效项：

```cmd
bcdedit /delete {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}
```

---

# 总结

本问题的本质不是：

> winload.efi 文件真的丢失

而是：

> BCD 无法正确定位系统分区

只要系统分区仍在，执行：

```cmd
bcdboot X:\Windows /s Y: /f UEFI
```

即可重建启动链条。
