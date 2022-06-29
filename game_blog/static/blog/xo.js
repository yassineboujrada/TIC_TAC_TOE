// partie de jeu
const paragraphe = document.querySelector("p")
let jeu = true
let player = "X"
let Game = ["", "", "", "", "", "", "", "", ""]
let mini_cad=document.querySelectorAll(".min-cadre")
const cas_game_over = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
const gagne = () => `Congartulation ${player} you're WINER `
const egalite = () => "Egalité"
const noba = () => `le tour de ${player} player`
paragraphe.innerHTML = noba()
mini_cad.forEach(ele => ele.addEventListener("click", do_it))

function do_it(){
    const indexCase = parseInt(this.dataset.index-1)
    if(Game[indexCase] !== "" || !jeu){
        return
    }
    Game[indexCase] = player
    console.log("m",player)
    this.innerHTML = player
    if (Game[indexCase]==="O"){
        this.style.color="blue"
    }
    else{
        this.style.color="red"
    }
    verifGagne()
}

// pour verifier s'il y'a un cas pour win et pour change player
function verifGagne(){
    let tourverif = false
    for(let matrice of cas_game_over){
        let x1 = Game[matrice[0]]
        let x2 = Game[matrice[1]]
        let x3 = Game[matrice[2]]
        if(x1 === "" || x2 === "" || x3 === ""){
            continue
        }
        if(x1 === x2 && x2 === x3){
            tourverif = true
            break
        }
    }
    if(!Game.includes("")){
        paragraphe.innerHTML = "Egale"
        paragraphe.style.color="yellow"
        jeu = false
        return
    }

    if(tourverif){
        paragraphe.innerHTML = gagne()
        paragraphe.style.color="green"
        jeu = false
        return
    }
    
    player = player === "X" ? "O" : "X"
    paragraphe.innerHTML = noba()
}

// rejouer 
function newgame(){
    player = "X"
    jeu = true
    Game = ["", "", "", "", "", "", "", "", ""]
    paragraphe.innerHTML = noba()
    paragraphe.style.color="plum"
    mini_cad.forEach(ele => ele.innerHTML = "")
}

