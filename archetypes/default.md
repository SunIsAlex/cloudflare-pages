---
weight : 1000
date : '{{ .Date }}'
draft : false
title : '{{ replace .File.ContentBaseName "-" " " | title }}'
---
