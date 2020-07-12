class CodeBuilder:
    indent_size = 2

    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = []
        self.build()

    def build(self):
        self.fields.append(f'class {self.root_name}')
        self.fields.append(f'  def __init__(self)')
        return self

    def add_field(self, type, name):
        indent = ' ' * (self.indent_size + 1)
        self.fields.append(f'{indent}self.{type} = {name}')
        return self

    def __str__(self):
        return '\n'.join(self.fields)


cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)
