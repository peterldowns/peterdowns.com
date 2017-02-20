// Saving node positions
var Dump = function() {};
Dump.prototype.print = function() {
    console.log('var saved =', JSON.stringify(this));
};
var Save = function(s) {
    var saved = new Dump();
    saved.camera = {
        x: s.camera.x,
        y: s.camera.y,
        ratio: s.camera.ratio,
    };
    saved.nodes = {}
    s.graph.nodes().forEach(function(node) {
        saved.nodes[node.id] = {
            x: node.x,
            y: node.y,
            size: node.size,
        };
    });
    return saved;
};
var Load = function(s, dump) {
    s.camera.x = dump.camera.x;
    s.camera.y = dump.camera.y;
    s.camera.ratio = dump.camera.ratio;
    s.graph.nodes().forEach(function(node) {
        var old = dump.nodes[node.id];
        node.x = old.x;
        node.y = old.y;
        node.size = old.size;
        node['read_cam0:size'] = old['read_cam0:size'];
        node['read_cam0:x'] = old['read_cam0:x'];
        node['read_cam0:y'] = old['read_cam0:y'];
    });
}
// Small zooms
var zout = function(s, x) {
    s.camera.ratio += (x || 0.05);
    s.refresh();
}
var zin = function(s, x) {
    s.camera.ratio -= (x || 0.05);
    s.refresh();
}
