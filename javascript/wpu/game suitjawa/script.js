let ulang = true

while(ulang) {
// pilihan player
    let player = prompt('pilih : gajah,semut,atau manusia');

// pilihan computer 
    let computer = Math.random()

    if(computer <= 0.34) {
        computer = 'gajah';
    } else if(computer > 0.34 && computer <= 0.67) {
        computer = 'manusia';
    }else {
        computer = 'semut';
    }

// menentukan rules 
    let hasil = '';

    if(player == computer) {
        hasil = 'maka SERI!';
    } else if (player == 'gajah') {
        if (computer == 'semut') {
            hasil = 'maka kamu KALAH!';
        }else {
            hasil = 'maka kamu MENANG!';
        }
    } else if (player == 'semut') {
        if (computer == 'gajah') {
            hasil = 'maka kamu MENANG!';
        }else {
            hasil = 'maka kamu KALAH!';
        }
    }  else if (player == 'manusia') {
        if (computer == 'gajah') {
            hasil = 'maka kamu KALAH!';
        }else {
            hasil = 'maka kamu MENANG!';
        }
    }  else {
        hasil = 'masukkan pilihan yang benar!';
    }

// menampilkan hasil
    alert(`kamu memilih ${player} dan computer memilih ${computer}, ${hasil}`);

// ulang
    ulang = confirm('mau bermain lagi?');
};

alert('terimakasih sudah bermain!');

