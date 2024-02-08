function $(query, list=false){
    var res = document.querySelectorAll(query);
    if (list) return res;
    return res.length == 1 ? res[0] : res;
}
function request(url, method, func) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            func(xmlhttp.responseText);
        }
    }
    xmlhttp.open(method, url, true);
    xmlhttp.send();
}
function choice(list){
    return list[Math.floor(Math.random()*list.length)];
}
var markdownOptions = {
    html: false,
    xhtmlOut: false,
    breaks: true,
    langPrefix: "",
    linkify: true,
    linkTarget: "_blank\" rel=\"noreferrer",
    doHighlight: false
};
var md = new Remarkable("full", markdownOptions);
var escape = Remarkable.utils.escapeHtml;
md.renderer.rules.image = function (tokens, idx, options) {
    var src = escape(tokens[idx].src);
    return `<a href="${src}" target="_blank" rel="noreferrer">` + src + "</a>";
};
var ids = [
    "2003496765", // rockn roll
    "1956534872", // flower tower
    "1496089152", // stay at your house
    "1332815073", // pill ibiza
    "26096272", // senbon zakura
];
$("#music").src=`https://music.163.com/outchain/player?type=2&id=${choice(ids)}&auto=1&height=66`;
request("/gettext", "GET", function(text){
    $("#text").innerHTML = md.render(text);
})