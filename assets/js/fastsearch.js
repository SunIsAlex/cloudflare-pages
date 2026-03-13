import * as params from '@params';

// 将变量定义在外部，但在初始化时重新获取 DOM 节点
let fuse; 
let resList;
let sInput;
let first, last, current_elem = null;
let resultsAvailable = false;

// 1. 封装初始化函数
window.initPaperModSearch = function () {

    resList = document.getElementById('searchResults');
    sInput = document.getElementById('searchInput');

    if (!sInput || !resList) return;
    if (sInput.dataset.initialized) return; // 防止重复绑定
    sInput.dataset.initialized = "true";
    // --- 搜索索引加载逻辑 ---
    // 如果已经加载过 fuse，就不要重复获取 json 了
    if (!fuse) {
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                let data = JSON.parse(xhr.responseText);
                if (data) {
                    let options = {
                        distance: 100, threshold: 0.4, ignoreLocation: true,
                        keys: ['title', 'permalink', 'summary', 'content']
                    };
                    if (params.fuseOpts) {
                        options = {
                            isCaseSensitive: params.fuseOpts.iscasesensitive ?? false,
                            includeScore: params.fuseOpts.includescore ?? false,
                            includeMatches: params.fuseOpts.includematches ?? false,
                            minMatchCharLength: params.fuseOpts.minmatchcharlength ?? 1,
                            shouldSort: params.fuseOpts.shouldsort ?? true,
                            findAllMatches: params.fuseOpts.findallmatches ?? false,
                            keys: params.fuseOpts.keys ?? ['title', 'permalink', 'summary', 'content'],
                            location: params.fuseOpts.location ?? 0,
                            threshold: params.fuseOpts.threshold ?? 0.4,
                            distance: params.fuseOpts.distance ?? 100,
                            ignoreLocation: params.fuseOpts.ignorelocation ?? true
                        }
                    }
                    fuse = new Fuse(data, options);
                }
            }
        };
        xhr.open('GET', "../index.json");
        xhr.send();
    }

    // --- 输入监听逻辑 ---
    sInput.onkeyup = function (e) {
        if (fuse) {
            let results;
            if (params.fuseOpts) {
                results = fuse.search(this.value.trim(), { limit: params.fuseOpts.limit });
            } else {
                results = fuse.search(this.value.trim());
            }
            if (results.length !== 0) {
                let resultSet = '';
                for (let item in results) {
                    resultSet += `<li class="post-entry"><header class="entry-header">${results[item].item.title}&nbsp;»</header>` +
                        `<a href="${results[item].item.permalink}" aria-label="${results[item].item.title}"></a></li>`
                }
                resList.innerHTML = resultSet;
                resultsAvailable = true;
                first = resList.firstChild;
                last = resList.lastChild;
            } else {
                resultsAvailable = false;
                resList.innerHTML = '';
            }
        }
    }

    sInput.addEventListener('search', function (e) {
        if (!this.value) resetSearch();
    });

}

// 2. 抽离重置逻辑
function resetSearch() {
    resultsAvailable = false;
    if (resList) resList.innerHTML = '';
    if (sInput) {
        sInput.value = '';
        sInput.focus();
    }
}

function activeToggle(ae) {
    document.querySelectorAll('.focus').forEach((element) => element.classList.remove("focus"));
    if (ae) {
        ae.focus();
        current_elem = ae;
        ae.parentElement.classList.add("focus");
    }
}

// 3. 全局键盘绑定 (只需要绑定一次)
if (!window.searchKbBound) {
    document.onkeydown = function (e) {
        let key = e.key;
        let ae = document.activeElement;
        let searchBox = document.getElementById("searchbox");
        if (!searchBox) return;
        let inbox = searchBox.contains(ae);

        if (ae === sInput) {
            document.querySelectorAll('.focus').forEach(el => el.classList.remove('focus'));
        } else if (current_elem) {
            ae = current_elem;
        }

        if (key === "Escape") {
            resetSearch();
        } else if (!resultsAvailable || !inbox) {
            return;
        } else if (key === "ArrowDown") {
            e.preventDefault();
            if (ae == sInput) activeToggle(resList.firstChild.lastChild);
            else if (ae.parentElement != last) activeToggle(ae.parentElement.nextSibling.lastChild);
        } else if (key === "ArrowUp") {
            e.preventDefault();
            if (ae.parentElement == first) activeToggle(sInput);
            else if (ae != sInput) activeToggle(ae.parentElement.previousSibling.lastChild);
        } else if (key === "ArrowRight") {
            ae.click();
        }
    };
    window.searchKbBound = true;
}

// 4. 执行初始化
if (document.readyState === 'complete') {
    window.initPaperModSearch();
} else {
    window.addEventListener('DOMContentLoaded', window.initPaperModSearch);
}

