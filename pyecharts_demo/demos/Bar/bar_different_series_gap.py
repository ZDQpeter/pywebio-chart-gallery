from pywebio.output import put_html
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), gap="0%")
    .add_yaxis("商家B", Faker.values(), gap="0%")
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-不同系列柱间距离"))
    
)

c.width = "100%"
put_html(c.render_notebook())
