
// variaveis e constantes globais

var cnv = document.querySelector('canvas');
var ctx = cnv.getContext('2d');
const UP = 38, DOWN = 40, LEFT = 37, RIGHT = 39;

// objetos

var player = {
    px: 10,
    py: 10
};

// eventos

window.addEventListener("keydown",pressinarTecla);

// rodar

render();

// funções

function render(){

    ctx.clearRect(0,0,cnv.width,cnv.height);
    ctx.fillRect(player.px,player.py,50,50);

}

function pressinarTecla(e){
    var tecla =  e.keyCode;

    if(tecla == UP){
        player.py--;
    }
    if(tecla == DOWN){
        player.py++;
    }
    if(tecla == LEFT){
        player.px--;
    }
    if(tecla == RIGHT){
        player.px++;
    }
    render()

}