$(function () {
    var myChart = Highcharts.chart('container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'TESTion'
        },
        xAxis: {
            categories: ['saaaaaa', 'dddddssss', 'ddds']
        },
        yAxis: {
            title: {
                text: 'Fruit dddddeaten'
            }
        },
        series: [{
            name: 'dddd',
            data: [1, 0, 4]
        }, {
            name: 'Johsssn',
            data: [5, 7, 3]
        }]
    });
});