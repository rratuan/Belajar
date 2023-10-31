// // // const hero = {
// // //     nama: "Layla",
// // //     level: 5,
// // //     jenisHero: "Marksman"
// // // };

// // // console.log(JSON.stringify(hero));

// //menggunakan ajax
// // let ajax = new XMLHttpRequest()

// // ajax.onreadystatechange = function() {
// //     if(ajax.readyState === 4 && ajax.status === 200) {
// //         let hero = JSON.parse(this.responseText)
// //         console.log(hero)
// //     }
// // }

// // ajax.open('GET', 'hero.json', true);
// //     ajax.send();

// //menggunakan jQuery
// $.getJSON('hero.json', function(response) {
//     console.log(response)
// })


//latihan json
let xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if(this.readyState == 4 && this.status == 200) {
        // typical action to be performed when the document is ready
        let data = JSON.parse(xhttp.responseText);
        data.forEach(function(element) {
            document.getElementById('demo').innerHTML += "NIM:" + element.nim + "<br>Nama:" + element.nama + "<br>Alamat:" + element.alamat + "<br><br>";
        });
    }
};

xhttp.open('GET', 'latihan.json', true);
xhttp.send();