import lxml.etree as et

xml="""
<groceries>
  <fruit state="rotten">apple</fruit>
  <fruit state="fresh">pear</fruit>
  <punnet>
    <fruit state="rotten">strawberry</fruit>
    <fruit state="fresh">blueberry</fruit>
  </punnet>
  <fruit state="fresh">starfruit</fruit>
  <fruit state="rotten">mango</fruit>
  <fruit state="fresh">peach</fruit>
</groceries>
"""

tree=et.fromstring(xml)

for bad in tree.xpath("//fruit[@state='rotten']"):
    bad.getparent().remove(bad)

print(et.tostring(tree, pretty_print=True))
