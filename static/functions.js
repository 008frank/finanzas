function clicker(x) {

    var conf = confirm("¿Desea editar este campo?");

    if (conf == true){
        document.getElementById('popUp').style.display = 'flex';
        var fechas = document.getElementById('fecha');
        var campos = document.getElementById('campo');

        // TAKE THE WINDOW TO THE TOP
        window.scrollTo(0, 0);
        document.body.style.overflow = 'hidden';


        // FATHER
        var elem = x;
        var n1 = elem.parentNode;
        var n2 = n1.parentNode;

        var father = n2.childNodes[1];


        // SON
        var elem = x;
        var chn1 = elem.childNodes[0];
        var son = chn1.textContent.toLowerCase();

        // GET DATA
        fechas.value = father.innerHTML;
        campos.value = son;

        fechas.disabled = true;
        campos.disabled = true;
    }
}


function clean_areas(){
    var fechas = document.getElementById('fecha');
    var campos = document.getElementById('campo');
    var cambios = document.getElementById('cambio');

    fechas.value = "";
    campos.value = "";
    cambios.value = "";

    document.getElementById('popUp').style.display = 'none';
    document.body.style.overflow = 'scroll';
}



// DATA CHARTS
const thisMap = new Map([
    ['Enero', [['Ingreso','Egreso'], [0,0]]]
]);
var barColors = [
    "rgb(0, 150, 255)",
    "rgb(211, 211, 211)"
];
  
  
const mainChart = new Chart("myChart1", {
type: "pie",
data: {
    labels: thisMap.get('Enero')[0],
    datasets: [{
    backgroundColor: barColors,
    data: thisMap.get('Enero')[1]
    }]
    },
    options: {
        title: {
        display: false,
        text: "Incomes"
        },
        
    }
});
// --------------------------------------------------------------------------------------
const thisMap2 = new Map([
    ['Enero', [['Ingreso','Egreso'], [0,0]]]
]);
var barColors = [
    "rgb(0, 150, 255)",
    "rgb(211, 211, 211)"
];


const mainChart2 = new Chart("myChart3", {
    type: "pie",
    data: {
        labels: thisMap.get('Enero')[0],
        datasets: [{
        backgroundColor: barColors,
        data: thisMap.get('Enero')[1]
        }]
    },
    options: {
        title: {
        display: false,
        text: "Incomes"
        }
    }
});