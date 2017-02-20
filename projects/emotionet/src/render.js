var DEBUG = false;

var SCALE = 1;
var WIDTH = 240;
var HEIGHT = 135;
var calculateScale = function() {
    SCALE = Math.min(
        (window.innerWidth * window.innerHeight) / (1920 * 1080), 1);
    WIDTH = SCALE * 240;
    HEIGHT = SCALE * 135;
};
window.onresize = calculateScale;
calculateScale();

sigma.utils.pkg('sigma.canvas.nodes');
sigma.canvas.nodes.image = (function() {
  var _cache = {},
      _loading = {},
      _callbacks = {};
  // Return the renderer itself:
  var renderer = function(node, context, settings) {
    var args = arguments,
        prefix = settings('prefix') || '',
        size = node[prefix + 'size'],
        color = node.color || '#FFF',
        url = node.url;
    if (_cache[url]) {
      context.save();
      // Draw the clipping disc:
      context.beginPath();
      context.arc(
        node[prefix + 'x'],
        node[prefix + 'y'],
        HEIGHT/2 + 0.2,
        0,
        Math.PI * 2,
        true
      );
      context.closePath();
      context.clip();
      // Draw the image
      context.save();
      if (HL_NEXT || HL_PREV) {
        if (should_hl_node(node)) {
          context.globalAlpha = 1.0;
        } else {
          context.globalAlpha = 0.3;
        }
      }
      context.drawImage(
        _cache[url],
        node[prefix + 'x'] - WIDTH / 2,
        node[prefix + 'y'] - HEIGHT / 2,
        WIDTH,
        HEIGHT
      );
      context.restore();
      // Quit the "clipping mode":
      context.restore();
      // Draw the border:
      context.beginPath();
      context.arc(
        node[prefix + 'x'],
        node[prefix + 'y'],
        HEIGHT/2 + 0.2,
        0,
        Math.PI * 2,
        true
      );
      if (should_hl_node(node)) {
        context.lineWidth = 1.4;
        context.strokeStyle = 'rgba(255, 255, 255, 2)';
      } else {
          context.strokeStyle = 'rgba(255, 255, 255, 0.3)';
          context.linewidth = 0.8;
      }
      context.stroke();
    } else {
      sigma.canvas.nodes.image.cache(url);
      sigma.canvas.nodes.def.apply(
        sigma.canvas.nodes,
        args
      );
    }
  };
  // Let's add a public method to cache images, to make it possible to
  // preload images before the initial rendering:
  renderer.cache = function(url, callback) {
    if (callback)
      _callbacks[url] = callback;
    if (_loading[url])
      return;
    var img = new Image();
    img.onload = function() {
      _loading[url] = false;
      _cache[url] = img;
      if (_callbacks[url]) {
        _callbacks[url].call(this, img);
        delete _callbacks[url];
      }
    };
    _loading[url] = true;
    img.src = url;
  };
  return renderer;
})();


sigma.utils.pkg('sigma.canvas.edges');
sigma.canvas.edges.t = function(edge, source, target, context, settings) {
    var prefix = settings('prefix') || '';
    if (should_hl_edge(edge)) {
        context.strokeStyle = 'rgba(255, 255, 255, 1)';
        context.lineWidth = 2;
    } else {
        context.lineWidth = 1;
        context.strokeStyle = 'rgba(88, 88, 88, 0.3)';
    }
    context.beginPath();
    context.moveTo(source[prefix + 'x'], source[prefix + 'y']);
    context.lineTo(target[prefix + 'x'], target[prefix + 'y']);
    context.stroke();
};

var i;
var s;
var g = {
  nodes: [],
  edges: []
};
var loaded = 0;
Object.keys(tagsByFile).forEach(function(filename) {
    g.nodes.push({
        id: filename,
        label: '',
        type: 'image',
        url: smallURL(filename),
        data: {highlighted: false},
        size: 400,
        x: Math.random(),
        y: Math.random(),
        color: "#FFFFFF",
    });
});
edges.forEach(function(edge, i) {
    g.edges.push({
        id: i,
        source: edge[0],
        target: edge[1],
        type: 't',
        color: 'rgba(88, 88, 88, 0.3)',
    });
});

var NODES;
var NODES_BY_ID;
var EDGES;
var EDGES_BY_NODE;
var EDGES_BY_SOURCE;
// Then, wait for all images to be loaded before instanciating sigma:

var WRAPPER = document.getElementById('wrapper');
var CONTAINER = document.getElementById('graph-container');
var LOAD_STATUS = document.getElementById('load-status');
var HL_NEXT = null;
var HL_PREV = null;
var HL_EDGE = null;

var should_hl_node = function(node) {
    return (HL_NEXT && node === HL_NEXT) || (HL_PREV && node === HL_PREV);
};
var should_hl_edge = function(edge) {
    return (HL_EDGE && edge === HL_EDGE);
}

LOAD_STATUS.innerHTML = '(loading)';
setTimeout(function() {
urls.forEach(function(url) {
    sigma.canvas.nodes.image.cache(
            url,
            function() {
                LOAD_STATUS.innerHTML = (
                        '(' + (loaded+1) + '/' + urls.length + ')');
                if (++loaded === urls.length) {
                    setTimeout(function() {
                        WRAPPER.className += ' loaded';

                        s = new sigma({
                            graph: g,
                            renderer: {
                                // IMPORTANT:
                                // This works only with the canvas renderer, so the
                                // renderer type set as "canvas" is necessary here.
                                container: CONTAINER,
                                type: sigma.renderers.canvas,
                            },
                            settings: {
                                clone: false,
                                drawLabels: false,
                                drawEdgeLabels: false,
                                // Debug settings
                                touchEnabled: DEBUG,
                                mouseEnabled: DEBUG,
                                mouseWheelEnabled: DEBUG,
                                doubleclickEnabled: DEBUG,
                            },
                        });

                        //s.graph.edges().forEach(function(e) { e.color='#EEE' });
                        Load(s, saved);
                        if (DEBUG) {
                            var dl = new sigma.plugins.dragNodes(s, s.renderers[0]);
                        }
                        s.refresh();
                        NODES = s.graph.nodes();
                        NODES_BY_ID = {};
                        NODES.forEach(function(node) {
                            NODES_BY_ID[node.id] = node;
                        });
                        EDGES = s.graph.edges();
                        EDGES_BY_NODE = {};
                        EDGES_BY_SOURCE = {};
                        EDGES.forEach(function(edge) {
                            [edge.source, edge.target].forEach(function(node) {
                                if (!EDGES_BY_NODE[node]) {
                                    EDGES_BY_NODE[node] = [];
                                }
                                EDGES_BY_NODE[node].push(edge);
                            });
                            EDGES_BY_SOURCE[edge.source] = (EDGES_BY_SOURCE[edge.source] || {});
                            EDGES_BY_SOURCE[edge.target] = (EDGES_BY_SOURCE[edge.target] || {});
                            EDGES_BY_SOURCE[edge.target][edge.source] = edge;
                            EDGES_BY_SOURCE[edge.source][edge.target] = edge;
                        });
                        setTimeout(function() {
                            WALK(s);
                        }, 5000 + pause);
                    }, 1000);
                }
            }
    );
});
}, 1000);
