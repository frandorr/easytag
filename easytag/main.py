from easytag.models.RulesModel import RulesModel
from easytag.common import types

def rule_1(doc_tokens: types.Doc) -> bool:
    return "cefalea" in doc_tokens

def rule_2(doc_tokens: types.Doc) -> bool:
    return "migraña" in doc_tokens

label_rule_1 = types.LabelRules(label="label_1", rules=[rule_1])

label_rule_2 = types.LabelRules(label="label_2", rules=[rule_2])

rules_model = RulesModel(labels_rules=[label_rule_1,label_rule_2])

rules_model.apply_rules(['hola', 'malo','cefalea'])
rules_model.tag([['hola', 'malo','cefalea'],['hola', 'malo'],['hola', 'migraña','cefalea']])
