// tampilan awal
alert('tebak angka dari 1-10 \nkamu mempunyai 3 kesempatan');

// pemain masukkan angka
let angka = Math.floor(Math.random()* 10 )+ 1;
alert(angka)

let pemain = parseInt(prompt('masukkan angka tebakan!'));

// angka random

//rules permainan 
let tebak = false;
let kesempatan = 3;

while (!tebak && kesempatan > 0 ){
    if (angka === pemain){
        alert("kamu benar")
        tebak = true
    } else if ( pemain > angka){
        alert("angka terlalu tinggi",kesempatan)
        pemain = parseInt(prompt('masukkan angka tebakan!'));

        kesempatan--
    }  else if ( pemain < angka){
        alert("angka terlalu rendah",kesempatan)
        pemain = parseInt(prompt('masukkan angka tebakan!'));
        kesempatan--
    } 
    if (angka === pemain){
        alert("kamu benar")
        tebak = true
    } 
}
if (!tebak ) {
    alert('game over',kesempatan)
    kesempatan--
}