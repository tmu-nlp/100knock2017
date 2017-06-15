#!usr/bin/python

from graphviz import Source
from Parser import KnockSoup


def get_with_idx(tag):
  return "{}:{}".format(tag["idx"], tag.text)


def extract_dependencies(xml_name, type="collapsed-dependencies"):
  soup = KnockSoup(xml_name)
  tag1, tag2 = "dependencies", "dep"

  deps_list = list()
  for dependencies in soup.find_all(tag1, type=type):
    deps = list()
    for dep in dependencies.find_all(tag2):
      deps.append((dep["type"], get_with_idx(dep.governor),
                   get_with_idx(dep.dependent)))
    deps_list.append(deps)

  return deps_list


def make_dot_lang(deps, graph_name="dep_graph", layout="dot"):
  script = "digraph {} {{\n  graph [ layout = {} ];\n"
  script = script.format(graph_name, layout)
  for dep in deps:
    script += '  "{1}" -> "{2}" [ label = "{0}" ];\n'.format(*dep)
  script += "}"
  return script


if __name__ == "__main__":
  xml_name = "head.txt.xml"
  deps_list = extract_dependencies(xml_name)
  for deps in deps_list:
    script = make_dot_lang(deps)
    src = Source(script)
    src.render(view=True)
    input("Do you want to display the next? [Enter / Ctrl-C]")
