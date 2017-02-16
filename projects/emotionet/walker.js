var anim_length = 4 * 1000;
var disp_length = 20 * 1000;
var pause = 4 * 1000;

var hl_len = 4000;

var DISPLAY = document.getElementById('display');
DISPLAY.show = function(node, callback) {
    CONTAINER.className = 'off';
    setTimeout(function() {
        DISPLAY.style = 'background-image: url(' + largeURL(node.id) + ')';
        DISPLAY.className = 'on';
        setTimeout(callback || function() {}, anim_length);
    }, anim_length);
};
DISPLAY.hide = function(callback) {
    DISPLAY.className = 'off';
    setTimeout(function() {
        CONTAINER.className = 'on';
        setTimeout((callback || function() {}), anim_length);
    }, anim_length);
};


function highlight(s, node, cb) {
    HL_PREV = HL_NEXT;
    HL_EDGE = null;
    s.refresh();
    setTimeout(cb || function() {}, hl_len);
}

function showNode(s, node, cb) {
    DISPLAY.show(node,
        delay(true, disp_length, function() {
            DISPLAY.hide(cb);
        })
    )
}


var subtract = function(arr, x) {
    var out = [];
    arr.forEach(function(el) {
        if (el === x) {
            return;
        }
        out.push(el);
    });
    if (out.indexOf(x) !== -1) {
        throw "Failed to remove x";
    }
    return out;
};
var randomElement = function(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}
var delay = function(wrap, t, f) {
    var x = function() {
        return setTimeout(f, t);
    };
    if (wrap) {
        return x;
    } else {
        return x();
    }
}

var WALK = function(s) {
    var current = randomElement(subtract(NODES, current));
    HL_NEXT = current;
    s.refresh();
    var edge = null;

    var cycle = function() {
        highlight(s, current, function() {
            showNode(s, current, function() {
                setTimeout(function() {
                    edge = randomElement(
                            subtract(EDGES_BY_NODE[current.id], edge));
                    HL_EDGE = edge;
                    HL_PREV = current;
                    if (current === NODES_BY_ID[edge.target]) {
                        current = NODES_BY_ID[edge.source];
                    } else {
                        current = NODES_BY_ID[edge.target];
                    }
                    HL_NEXT = current;
                    s.refresh();
                    delay(false, hl_len, cycle);
                }, hl_len);
            });
        });
    };
    cycle();
};
