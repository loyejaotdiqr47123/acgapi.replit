function setGrayScale() {
 document.body.style.filter = 'grayscale(100%)';
}

function resetGrayScale() {
 document.body.style.filter = 'none';
}

// 设置灰度
setTimeout(setGrayScale, new Date(2023, 11, 13).getTime() - new Date().getTime());

// 恢复原状
setTimeout(resetGrayScale, new Date(2023, 11, 13).getTime() + 24 * 60 * 60 * 1000 - new Date().getTime());
