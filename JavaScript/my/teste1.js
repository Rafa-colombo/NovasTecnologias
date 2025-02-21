/* 'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}
 */
/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function plusMinus(arr) {
    
    let tamanho = arr.length;
    let maior = 0;
    let menor = 0;
    let zero = 0;

    for(let i = 0; i<tamanho; i++){

        if(arr[i]>0){ maior++;}
        else if(arr[i] < 0){ menor++;}
        else {zero++; }

    }

    console.log((maior/tamanho).toFixed(6), (menor/tamanho).toFixed(6), (zero/tamanho).toFixed(6));


}

/* function main() {
    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    plusMinus(arr);
} */

plusMinus([1,2,8,-1,0]);