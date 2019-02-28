from typing import IO, Tuple, Dict, List

import yaml

class Buffer(object):

    def __init__(self) -> None:
        self.contents = ""

    def append(self, contents: str) -> None:
        self.contents = "{existing}{end}".format(existing=self.contents, end=contents)

    def empty(self) -> bool:
        return len(self.contents) == 0


def _load(stream: IO[str]) -> Tuple[Dict, str]:

    yml_contents = Buffer()
    md_contents = Buffer()
    current_buffer = md_contents

    for line in stream:
        if _is_yaml_start(line, yml_contents):
            current_buffer = yml_contents

        elif _is_yaml_end(line, yml_contents):
            current_buffer = md_contents
            # Skip the ending `---` and move on to the next line as markdown
            continue

        current_buffer.append(line)

    yml_dict = yaml.load(yml_contents.contents, Loader=yaml.FullLoader) # type: Dict
    return (yml_dict, md_contents.contents.strip("\n"))

def _is_yaml_start(line: str, yml_buffer: Buffer) -> bool:
    return line.strip("\n").endswith("---") and yml_buffer.empty()

def _is_yaml_end(line: str, yml_buffer: Buffer) -> bool:
    return line.strip("\n").endswith("---") and not yml_buffer.empty()

def _dump(yml: Dict, markdown: str, yamlfirst=True) -> str:

    yamlout = yaml.dump(yml, default_flow_style=False, indent=2) # type: str

    dump = ""
    if yamlfirst:
        dump = "---\n{yml}\n---\n{markdown}".format(yml=yamlout, markdown=markdown)
    else:
        dump = "{markdown}\n---\n{yml}\n---".format(markdown=markdown, yml=yamlout)

    return dump
