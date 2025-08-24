
class HtmlNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("HTML translation not implemented yet.")

    def props_to_html(self):
        if not self.props:
            return None
        props_string=" "
        for key, value in self.props.items():
            props_string += f'{key}="{value}" '
        return props_string

    def __repr__(self):
        return f'<tag={self.tag} value={self.value} children={self.children}, props={self.props_to_html()}>'

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Error: Leaf Node has no value")    
        if not self.tag:
            return value
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"     
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"    

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Error: Parent node must have tag")
        if not self.children:
            raise ValueError("Error: Parent node must have children")

    def to_html(self):
        html_string = f"<{self.tag}"
        if self.props:
            html_string += self.props_to_html
        html_string += ">"    
        for child in self.children:
            html_string += child.to_html()
        html_string += f"</{self.tag}>"    
        return html_string
