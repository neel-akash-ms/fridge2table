var add = document.getElementById("add");
var chosen = document.getElementById("chosen");
var hiddenchosen = document.getElementById("hiddenchosen");

if (hiddenchosen && chosen) {
    window.onload = () => {
        chosen.value = hiddenchosen.value;
    };
}

if (add) {
    add.addEventListener('click', () => {
        let checked = document.querySelectorAll('input[name=ings]:checked');
        let qstr = "";
        checked.forEach(c => {
            qstr += ("," + c.value);
        });
        if (hiddenchosen.value == null || hiddenchosen.value == "")
            qstr = qstr.slice(1);
        chosen.value += qstr;
        hiddenchosen.value += qstr;
    });
}