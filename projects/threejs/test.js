var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(
    75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

var renderer = new THREE.WebGLRenderer();
var autoResize = function() {
  var width = window.innerWidth;
  var height = window.innerHeight;
  renderer.setSize(width, height);
  camera.aspect = width / height;
  camera.updateProjectionMatrix();

};
autoResize();
window.addEventListener('resize', autoResize);

document.body.appendChild(renderer.domElement);

var coloredMesh = new THREE.MeshBasicMaterial({ color: 0xFFFFFF });
var joesFace = new THREE.MeshBasicMaterial({
  map: THREE.ImageUtils.loadTexture('./joesface.jpg'),
  overdraw: true
})
var britspears = new THREE.MeshBasicMaterial({
  map: THREE.ImageUtils.loadTexture('./brit.jpg'),
  overdraw: true
})
var treb = new THREE.MeshBasicMaterial({
  map: THREE.ImageUtils.loadTexture('./treb.jpg'),
  overdraw: true
})
var materials = [joesFace, treb, treb, coloredMesh, coloredMesh, joesFace];
var geometry = new THREE.BoxGeometry(1, 1, 1);
var faceMaterial = new THREE.MeshFaceMaterial(materials);
var cube = new THREE.Mesh(geometry, faceMaterial);
cube.position.x = 1;
scene.add(cube);


var rotationUnit = 1 / (2 * 2 * Math.PI);
var translationUnit = 0.1;
var zoomUnit = 0.05;
var keysDown = {}
var rotateCube = function() {
  cube.rotateY(-rotationUnit);
  for (var keyCode in keysDown) {
    if (!keysDown.hasOwnProperty(keyCode)) continue;
    if (!keysDown[keyCode]) continue;
    if (keyCode == 37) {
      console.log('left!');
      cube.rotateY(-rotationUnit);
    } else if (keyCode == 38) {
      console.log('up');
      cube.rotateX(rotationUnit);
    } else if (keyCode == 39) {
      console.log('right');
      cube.rotateY(rotationUnit);
    } else if (keyCode == 40) {
      console.log('down');
      cube.rotateX(-rotationUnit);
    } else if (keyCode == 87) {
      console.log('w');
      cube.position.y += translationUnit;
    } else if (keyCode == 83) {
      console.log('s');
      cube.position.y -= translationUnit;
    } else if (keyCode == 65 ) {
      console.log('a');
      cube.position.x -= translationUnit;
    } else if (keyCode == 68) {
      console.log('d');
      cube.position.x += translationUnit;
    } else if (keyCode == 69) {
      console.log('e');
      cube.position.z += zoomUnit;
    } else if (keyCode == 81) {
      console.log('q');
      cube.position.z -= zoomUnit;
    }
    console.log(keyCode);
  }
};
document.addEventListener('keydown', function(e) {
  keysDown[e.keyCode] = true;
});
document.addEventListener('keyup', function(e) {
  keysDown[e.keyCode] = undefined;
});
document.addEventListener('mousewheel', function(e) {
  cube.rotateZ(2 * rotationUnit * Math.sign(e.deltaY));
});

function render() {
  requestAnimationFrame(render);
  rotateCube();
  renderer.render(scene, camera);
}
render();
