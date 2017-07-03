from lxml import etree

markup = (
"""
<div class="content">
    內文
    <i> 備註解釋 1 </i>
    <span> 內文 2 </span>
    <i> 備註解釋 2 </i>
</div>
"""
)
page = etree.HTML(markup)
for item in page.xpath(u"//i"):
    item.getparent().remove(item)

for item in page.xpath(u"//text()"):
    print(item.strip())
