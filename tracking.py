import libcst as cst

def operator_to_text(operator):
    return cst.parse_module("").code_for_node(operator).replace(' ', '_')\
        .replace('>=', 'GreaterThanEquals')\
        .replace('<=', 'LesserThanEquals')\
        .replace('>', 'GreaterThan')\
        .replace('<', 'LesserThan')\
        .replace('<', 'LesserThan')\
        .replace('!=', 'NotEqual')\
        .replace('==', 'Equal')


class Tracking:
    def __init__(self, formula):
        self.tracking = None
        self.formula = formula
        self.map_conditionals = {}
        self.modified_code = None

    def transform(self):
        statements_list = cst.parse_module(self.formula)
        visitor = TypingTransformer()
        modified_code = statements_list.visit(visitor)
        self.modified_code = modified_code.code

        for structure in modified_code.body:
            if isinstance(structure, cst.If):
                replaced_spaces_sufix = operator_to_text(structure.test)
                self.map_conditionals[f"if_{replaced_spaces_sufix}"] = False
                if structure.orelse is not None:
                    if isinstance(structure.orelse, cst.Else):
                        self.map_conditionals[f"else_{replaced_spaces_sufix}"] = False
                    else:
                        replaced_spaces_sufix = operator_to_text(structure.orelse.test)
                        self.map_conditionals[f"if_{replaced_spaces_sufix}"] = False


class TypingTransformer(cst.CSTTransformer):

    def leave_If(self, original_node: cst.If, updated_node: cst.If) -> cst.If:
        replaced_spaces_sufix = operator_to_text(original_node.test)
        tracking_if_variable = cst.parse_statement(f"if_{replaced_spaces_sufix}=True")
        body_list = list(updated_node.body.body)
        body_list.append(tracking_if_variable)
        body_tuple = tuple(body_list)
        new_node = updated_node.body.with_changes(body=body_tuple)
        updated_node = updated_node.with_changes(body=new_node)
        if original_node.orelse is not None:
            tracking_else_variable = cst.parse_statement(f"else_{replaced_spaces_sufix}=True")
            body_else_list = list(updated_node.orelse.body.body)
            body_else_list.append(tracking_else_variable)
            new_node = updated_node.orelse.body.with_changes(body=body_else_list)
            updated_orelse_node = updated_node.orelse.with_changes(body=new_node)
            updated_node = updated_node.with_changes(orelse=updated_orelse_node)
        return updated_node
