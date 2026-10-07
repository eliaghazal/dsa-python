rivers = {'nile':'egypt', 'amazon':'brazil', 'yangtze':'china'}
for k, v in rivers.items():
  print(f"The {k.title()} runs through {v.title()}")
for k in rivers.keys():
  print(k)
for v in rivers.values():
  print(v)
