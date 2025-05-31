let grid; 
let rows = 50;
let cols = 50;
let cellSize = 10;
let lastUpdate = 0;
const updateDelay = 700;
const SUSCEPTIBLE = 0; // Здорова
const INFECTED = 1;    // Інфікована
const RECOVERED = 2;   // Відновлена

function createGrid() {
    let newGrid = new Array(rows);
    for (let i = 0; i < rows; i++) {
        newGrid[i] = new Array(cols);
        for (let j = 0; j < cols; j++) {
            newGrid[i][j] = { state: SUSCEPTIBLE, time: 0 };
        }
    }
    return newGrid;
}

function initializeGrid() {
    let centerRow = Math.floor(rows / 2);
    let centerCol = Math.floor(cols / 2);
    grid[centerRow][centerCol].state = INFECTED;
    grid[centerRow][centerCol].time = 1;
}

function setup() {
    let canvas = createCanvas(cols * cellSize, rows * cellSize);
    canvas.parent('container');
    grid = createGrid();
    initializeGrid();
    const pInfectInput = document.getElementById('p_infect_input');
    const tRecoverInput = document.getElementById('t_recover_input');
    const pInfectValue = document.getElementById('p_infect_value');
    const tRecoverValue = document.getElementById('t_recover_value');
    pInfectInput.addEventListener('input', () => {  pInfectValue.textContent = pInfectInput.value;});
     tRecoverInput.addEventListener('input', () => { tRecoverValue.textContent = tRecoverInput.value; });
}


function updateGrid() {
    let p_infect = parseFloat(document.getElementById('p_infect_input').value);
    let t_recover = parseInt(document.getElementById('t_recover_input').value);
    
    let newGrid = [];
    for (let i = 0; i < rows; i++) {
        newGrid[i] = [];
        for (let j = 0; j < cols; j++) {
            newGrid[i][j] = { ...grid[i][j] };
        }
    }
    
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (grid[i][j].state === SUSCEPTIBLE) {
                let neighbors = [];
                for (let di = -1; di <= 1; di++) {
                    for (let dj = -1; dj <= 1; dj++) {
                        if (di === 0 && dj === 0) continue;
                        let ni = i + di;
                        let nj = j + dj;
                        if (ni >= 0 && ni < rows && nj >= 0 && nj < cols) {
                            neighbors.push(grid[ni][nj].state);
                        }
                    }
                }
                if (neighbors.includes(INFECTED) && Math.random() < p_infect) {
                    newGrid[i][j].state = INFECTED;
                    newGrid[i][j].time = 1;
                }
            } else if (grid[i][j].state === INFECTED) {
                newGrid[i][j].time++;
                if (newGrid[i][j].time > t_recover) {
                    newGrid[i][j].state = RECOVERED;
                }
            }
        }
    }
    grid = newGrid;
}

function drawGrid() {
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            let x = j * cellSize;
            let y = i * cellSize;
            let fillColor;
            
            if (grid[i][j].state === SUSCEPTIBLE) {
                fillColor = '#31d51e';
            } else if (grid[i][j].state === INFECTED) {
                fillColor = '#ad160e';
            } else if (grid[i][j].state === RECOVERED) {
                fillColor = '#084d8a';
            }
            fill(fillColor);
            rect(x, y, cellSize, cellSize);
        }
    }
}

function draw() {
    if (millis() - lastUpdate > updateDelay) {
        updateGrid();
        lastUpdate = millis();
    }
    background(255);
    drawGrid();
}