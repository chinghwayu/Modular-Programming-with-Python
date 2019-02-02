from charter import Chart, generate_chart

mychart = Chart()
mychart.set_title("Wild Parrot Deaths per Year")
mychart.set_x_axis(["2009", "2010", "2011", "2012", "2013", "2014", "2015"])
mychart.set_y_axis(minimum=0, maximum=700, labels=[0, 100, 200, 300, 400, 500, 600, 700])
mychart.set_series([250, 270, 510, 420, 680, 580, 450])
mychart.set_series_type("bar")
generate_chart(mychart.chart, "chart.pdf")
