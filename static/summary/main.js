$(document).ready(function() {
    console.log(labels);
    var ctx = document.getElementById('myChart');
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['brynn', 'engbers', 'lmao'],
            datasets: [{
                label:'price over time',
                data: priceSet
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        min:15,
                        max: 40
                    }
                }]
            }
        }
    })
});