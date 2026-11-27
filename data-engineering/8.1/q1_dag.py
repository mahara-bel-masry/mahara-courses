from graphlib import TopologicalSorter
DAG = {"load": {"transform"}, "transform": {"extract"}, "extract": set()}
print(list(TopologicalSorter(DAG).static_order()))
