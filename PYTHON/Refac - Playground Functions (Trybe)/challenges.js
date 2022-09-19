// Desafio 1
console.log('exercicio 1')
function compareTrue(v1, v2) {
  // seu código aqui

  if (v1 == true && v2 == false) {
    return false
  } else if ((v1 && v2) == false) {
    return false
  } else {
    return true
  }
}

// Desafio 2
function calcArea(base, height) {
  let area = (base * height) / 2;
  return (area);
}

// Desafio 3
function splitSentence(string) {
  let splitting = string.split(' ');
  return (splitting);
}

// Desafio 4
function concatName() {
  let arr;
  let firstIndex = arr[0];
  let lastIndex = arr[arr.length - 1];
  let result = lastIndex + (', ') + firstIndex;
  return result;
}

// Desafio 5
function footballPoints(wins, ties) {
  let win = wins * 3;
  let tie = ties;
  let pontos = win + tie;

  return pontos;
}

// Desafio 6
function highestCount(numb) {
  let cont = 0;

  let max = Math.max(...numb);
  for (i = 0; i < numb.length; i += 1) {
    if (numb[i] === max) {
      cont += 1;
      // console.log(cont);
    }
  }
  return cont;
}

// Desafio 7
console.log('exercicio 7');
function catAndMouse(mouse, cat1, cat2) {
  let position1 = cat1 - mouse;
  let position2 = cat2 - mouse;
  if (position1 < 0) position1 *= -1;
  if (position2 < 0) position2 *= -1;
  if (position1 < position2) {
    return 'cat1';
  } if (position1 > position2) {
    return 'cat2';
  }
  return 'os gatos trombam e o rato foge';
}

// Desafio 8
function fizzBuzz(array) {
  // seu código aqui
  let result = [];
  for (let i in array) {
    if ((array[i] % 3) == 0 && (array[i] %5) == 0) {
      result.push('fizzBuzz');
    } else if (array[i] % 3 == 0) {
      result.push('fizz');
    } else if (array[i] % 5 == 0) {
      result.push('buzz');
    } else {
      result.push('bug!');
    }
  }
  return result
}
fizzBuzz()

// Desafio 9
console.log('exercicio 9')
let encript = 'hi there!'
function encode(string) {
  let code = string.replace(/a/gi, 1).replace(/e/gi, 2).replace(/i/gi, 3).replace(/o/gi, 4).replace(/u/gi, 5);
  return code;
}
console.log(encode('hi there!'));
let decript = encode(encript);

function decode(b) {
  let dec = b.replaceAll(1, "a").replaceAll(2, "e").replaceAll(3, "i").replaceAll(4, "o").replaceAll(5, "u");
  return dec;
}
console.log(decode(decript))

module.exports = {
  calcArea,
  catAndMouse,
  compareTrue,
  concatName,
  decode,
  encode,
  fizzBuzz,
  footballPoints,
  highestCount,
  splitSentence,
};