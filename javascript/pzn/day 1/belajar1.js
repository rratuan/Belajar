/*pendahuluan*/
document.writeln("Hello World");
document.writeln("</br>");

//tipe data number
document.writeln(100);
document.writeln("</br>");
document.writeln(1.2);
document.writeln("</br>");

//tipe data boolean
document.writeln(true);
document.writeln("</br>");
document.writeln(false);
document.writeln("</br>");

//tipe data string
document.writeln("Ratuayu Nurfajar");
document.writeln("");
document.writeln("</br>");

//menambah string
document.writeln("Nama: " + "Ratuayu" + " Nurfajar");
document.writeln("<br>");

//variable --- var

    //tanpa variable -- jika ada perubahan data maka harus dirubah satu per satu
    /*document.writeln("Ratuayu Nurfajar");
    document.writeln("<br>");
    document.writeln("Ratuayu Nurfajar");
    document.writeln("<br>");
    document.writeln("Ratuayu Nurfajar");
    document.writeln("<br>");
    document.writeln("Ratuayu Nurfajar");
    document.writeln("<br>");
    document.writeln("Ratuayu Nurfajar");
    document.writeln("<br>");*/

    //menggunakan variable -- membuat variable
    var fullName;
    var firstName;
    var middleName;
    var lastName;
    //menambahkan value pada variable
    /*fullName = "Ratuayu Nurfajar";
    firstName = "Ratuayu";
    lastName  = "Nurfajar";
    //ganti
    fullName = "Ardi Fajar Arifin";
    firstName = "Ardi";
    middleName = "Fajar";
    lastName = "Arifin";*/
    //data akan otomatis berubah sesuai perubahan data terakhir

    //variable dan value --- var nama_variable = "value"
    var firstName = "Ratuayu";
    var lastName = "Nurfajar";
    var fullName = "Ratuayu Nurfajar";

    //mengakses variable 
    document.writeln(firstName);
    document.writeln("</br>");
    document.writeln(lastName);
    document.writeln("</br>");
    document.writeln(fullName);
    document.writeln("</br>");
    //jika ada perubahan isi data,maka tinggal ganti di variablenya

//variable --- let (disarankan)

    let country = "Indonesia";
    document.writeln(country);
    document.writeln("</br>");

//variable --- const (disarankan)

    const application = "Belajar JavaScript Dasar";
    //data akan dirubah menjadi
    //const application = "gak mau belajar";
    //terjadi error karena variable const bersifat konstan atau tidak dapat dirubah nilainya
    document.writeln(application);
