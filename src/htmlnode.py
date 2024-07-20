class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented

    def props_to_html(self):
        properties = ""
        for prop in self.props:
            properties += f' {prop}="{self.props[prop]}"'
        return properties

    def __eq__(self, target):
        return(
            self.tag == target.tag
            and self.value == target.value
            and self.children == target.children
            and self.props == target.props
        )

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    