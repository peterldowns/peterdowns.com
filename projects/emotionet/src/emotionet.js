var tags = [
    'hap', //py
    'mel', //ancholy
    'bor', //edom
    'pas', //sion
    'won', //der
    'env', //y
    'con', //tendedness
    'nos', //talgia
    'cur', //iosity
    'tir', //ed
];
var tagsByFile = {
    '2016-12-30 02.48.30.jpg'  : 'won env con',
    '2017-01-01 10.28.57.jpg'  : 'hap won con nos',
    '2017-01-01 11.00.41.jpg'  : 'mel won',
    '2017-01-03 05.18.30.jpg'  : 'hap won pas con',
    '2017-01-03 06.20.50-2.jpg': 'hap won nos',
    '2017-01-04 00.44.30.jpg'  : 'hap pas won tir',
    '2017-01-08 11.31.04.jpg'  : 'mel pas env',
    '2017-01-08 11.59.51.jpg'  : 'mel bor won',
    '2017-01-08 12.14.09.jpg'  : 'hap cur tir',
    '2017-01-09 09.57.19.jpg'  : 'bor won cur tir',
    '2017-01-10 07.07.55.jpg'  : 'hap con nos cur tir',
    '2017-01-10 07.44.14.jpg'  : 'hap mel pas won nos',
    '2017-01-17 09.39.42.jpg'  : 'mel pas cur env',
    '2017-01-18 01.59.01.jpg'  : 'won con',
    '2017-01-18 19.28.05.jpg'  : 'hap mel con nos tir',
    '2017-01-19 21.29.30.jpg'  : 'mel cur',
    '2017-01-19 22.35.13.jpg'  : 'mel pas won',
    '2017-01-20 00.15.45.jpg'  : 'hap won con tir',
    '2017-01-20 01.16.51.jpg'  : 'bor tir',
    '2017-01-20 20.48.38.jpg'  : 'hap won cur',
    '2017-01-21 19.18.37.jpg'  : 'hap pas env cur',
    '2017-01-22 20.27.07.jpg'  : 'pas nos',
    '2017-01-24 06.44.03.jpg'  : 'mel env tir',
    '2017-01-25 10.21.31.jpg'  : 'bor tir',
    '2017-01-28 00.12.08.jpg'  : 'bor cur',
    '2017-02-03 01.04.28.jpg'  : 'hap env cur',
    '2017-02-03 03.53.17.jpg'  : 'mel tir',
    '2017-02-03 03.59.58.jpg'  : 'won cur',
    '2017-02-03 07.35.13.jpg'  : 'env nos cur',
    '2017-02-03 09.51.26.jpg'  : 'bor tir',
    '2017-02-03 10.15.58.jpg'  : 'hap cur tir',
    '2017-02-03 10.17.48.jpg'  : 'mel pas won tir',
};


var smallURL = function(filename) {
    return './photos/small/' + encodeURIComponent(filename);
};
var largeURL = function(filename) {
    return './photos/large/' + encodeURIComponent(filename);
};
var urls = [];
Object.keys(tagsByFile).forEach(function(filename) {
    urls.push(smallURL(filename));
    urls.push(largeURL(filename));
});
var filesByTag = {};
Object.keys(tagsByFile).forEach(function(filename) {
    var tags = tagsByFile[filename];
    tags.split(' ').forEach(function(tag) {
        filesByTag[tag] = filesByTag[tag] || [];
        filesByTag[tag].push(filename);
    });
});
var edges = [];
var edgeKey = function(file1, file2) {
    var sorted = [file1, file2].sort();
    return sorted[0] + ' / ' + sorted[1];
}
var edgeFiles = function(key) {
    return key.split(' / ');
}
var _edgeDedup = {};
var edgesByNode = {};
Object.keys(filesByTag).forEach(function(tag) {
    if (tag.length === 0) return;
    var filenames = filesByTag[tag];
    for (var i = 0; i < filenames.length; i++) {
        var outer_file = filenames[i];
        for (var j = i + 1; j < filenames.length; j++) {
            var inner_file = filenames[j];
            if (inner_file === outer_file) {
                throw "BROKEN";
            }
            _edgeDedup[edgeKey(outer_file, inner_file)] = true;
        }
    }
});
Object.keys(_edgeDedup).forEach(function(edgeKey) {
    edges.push(edgeFiles(edgeKey));
});

EDGES_BY_NODE = {};
edges.forEach(function(edge) {
    [edge[0], edge[1]].forEach(function(node, i) {
        if (!EDGES_BY_NODE[node]) {
            EDGES_BY_NODE[node] = [];
        }
        EDGES_BY_NODE[node].push(edge[1-i]);
    });
});
console.log(EDGES_BY_NODE)
